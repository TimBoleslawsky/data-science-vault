import time
import argparse
from pyspark.sql import SparkSession
from pyspark.sql import functions as F # needed to import this!!
from pyspark.sql.functions import udf, col
from pyspark.sql.types import IntegerType, StructType, StructField, StringType, DoubleType # needed to add this!!
import pandas as pd
import sys

@udf(returnType=IntegerType())
def jdn(dt):
    """
    Computes the Julian date number for a given date.
    Parameters:
    - dt, datetime : the Gregorian date for which to compute the number

    Return value: an integer denoting the number of days since January 1, 
    4714 BC in the proleptic Julian calendar.
    """
    y = dt.year
    m = dt.month
    d = dt.day
    if m < 3:
        y -= 1
        m += 12
    a = y//100
    b = a//4
    c = 2-a+b
    e = int(365.25*(y+4716))
    f = int(30.6001*(m+1))
    jd = c+d+e+f-1524
    return jd

    
# you probably want to use a function with this signature for computing the
# simple linear regression with least squares using applyInPandas()
# key is the group key, df is a Pandas dataframe
# should return a Pandas dataframe
def lsq(key,df):
    """
    df: Pandas dataframe with columns 'TAVG' and 'date_jdn'
    key: group key (e.g. STATION code/name) is not used directly here

    Returns: pandas.DataFrame with columns 'STATION', 'STATION_NAME', 'BETA'
    """
    x = df['DATE_JDN'].to_numpy()
    y = df['TAVG'].to_numpy()

    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = sum((xi - mean_x) ** 2 for xi in x)

    beta = numerator / denominator

    return pd.DataFrame({
        'STATION': [df['STATION'].iloc[0]],
        'NAME': [df['NAME'].iloc[0]],
        'BETA': [beta]
    })


if __name__ == '__main__':
    # do not change the interface
    parser = argparse.ArgumentParser(description = \
                                    'Compute climate data.')
    parser.add_argument('-w','--num-workers',default=1,type=int,
                            help = 'Number of workers')
    parser.add_argument('filename',type=str,help='Input filename')
    args = parser.parse_args()
    start = time.time()

    # this bit is important: by default, Spark only allocates 1 GiB of memory 
    # which will likely cause an out of memory exception with the full data
    spark = SparkSession.builder \
            .master(f'local[{args.num_workers}]') \
            .config("spark.driver.memory", "16g") \
            .getOrCreate()
    
    # read the CSV file into a pyspark.sql dataframe and compute the things you need
    df = spark.read.csv(args.filename, header=True, inferSchema=True)

    start_computation = time.time()

    df = df.withColumn("DATE_JDN", jdn(df["DATE"]))
    df = df.withColumn("TAVG", (col("TMIN") + col("TMAX")) / 2)

    schema = StructType([
        StructField("STATION", StringType()),
        StructField("NAME", StringType()),
        StructField("BETA", DoubleType()),
    ])

    regression_results = df.groupBy("STATION", "NAME").applyInPandas(
        lsq, schema
    )

    top_5 = regression_results.orderBy(col("BETA").desc()).limit(5)

    positive_count = regression_results.filter(col("BETA") > 0).count()
    total_count = regression_results.count()
    fraction_positive = positive_count / total_count if total_count > 0 else float('nan')

    # top 5 slopes are printed here
    # replace None with your dataframe, list, or an appropriate expression
    # replace STATIONCODE, STATIONNAME, and BETA with appropriate expressions
    print('Top 5 coefficients:')
    for row in top_5.collect():
        print(f'{row["STATION"]} at {row["NAME"]} BETA={row["BETA"]} °F/d') # Change decimals!!
    print("")

    # replace None with an appropriate expression
    print('Fraction of positive coefficients:')
    print(fraction_positive)
    print("")

    # Five-number summary of slopes, replace with appropriate expressions
    print('Five-number summary of BETA values:')
    beta_min, beta_q1, beta_median, beta_q3, beta_max = regression_results.approxQuantile("BETA", [0.0, 0.25, 0.5, 0.75, 1.0], 0.01)
    print(f'beta_min {beta_min:0.3e}')
    print(f'beta_q1 {beta_q1:0.3e}')
    print(f'beta_median {beta_median:0.3e}')
    print(f'beta_q3 {beta_q3:0.3e}')
    print(f'beta_max {beta_max:0.3e}')
    print("")

    # Here you will need to implement computing the decadewise differences 
    # between the average temperatures of 1910s and 2010s

    # There should probably be an if statement to check if any such values were 
    # computed (no suitable stations in the tiny dataset!)

    # Note that values should be printed in celsius

    df = df.withColumn("YEAR", col("DATE").substr(1, 4)) 
    df = df.withColumn("DECADE", (col("YEAR") / 10).cast("int") * 10)
    df_decades = df.filter(col("DECADE").isin([1910, 2010]))

    decade_avg = (
        df_decades
        .groupBy("STATION", "NAME", "DECADE")
        .agg(F.avg("TAVG").alias("TAVGAVG"))
    )

    decade_pivot = (
        decade_avg
        .groupBy("STATION", "NAME")
        .pivot("DECADE", [1910, 2010])
        .agg(F.first("TAVGAVG"))  # Using first() since each group has just one value
    )

    both_decades = decade_pivot.filter(col("1910").isNotNull() & col("2010").isNotNull())

    if both_decades.count() == 0:
        sys.exit("No stations with both 1910s and 2010s data found.")
    else:
        result = both_decades.withColumn(
            "TAVGDIFF",
            ((col("2010") - 32) * 5 / 9) - ((col("1910") - 32) * 5 / 9)
        )

    top_5 = result.orderBy(col("TAVGDIFF").desc()).limit(5)

    positive_count = result.filter(col("TAVGDIFF") > 0).count()
    total_count = result.count()
    fraction_positive = positive_count / total_count if total_count > 0 else float('nan')
    
    # Replace None with an appropriate expression
    # Replace STATION, STATIONNAME, and TAVGDIFF with appropriate expressions
    print('Top 5 differences:')
    for row in top_5.collect():
        print(f'{row["STATION"]} at {row["NAME"]} difference {row["TAVGDIFF"]} °C)') # Change decimals!!
    print("")

    # replace None with an appropriate expression
    print('Fraction of positive differences:')
    print(fraction_positive)
    print("")

    # Five-number summary of temperature differences, replace with appropriate expressions
    print('Five-number summary of decade average difference values:')
    tdiff_min, tdiff_q1, tdiff_median, tdiff_q3, tdiff_max = result.approxQuantile("TAVGDIFF", [0.0, 0.25, 0.5, 0.75, 1.0], 0.01)
    print(f'tdiff_min {tdiff_min:0.1f} °C')
    print(f'tdiff_q1 {tdiff_q1:0.1f} °C')
    print(f'tdiff_median {tdiff_median:0.1f} °C')
    print(f'tdiff_q3 {tdiff_q3:0.1f} °C')
    print(f'tdiff_max {tdiff_max:0.1f} °C')
    print("")

    end = time.time()

    # Add your time measurements here
    # It may be interesting to also record more fine-grained times (e.g., how 
    # much time was spent computing vs. reading data)
    print(f'num workers: {args.num_workers}')
    print(f'total time: {end - start:.2f} s')
    print(f'reading time: {start_computation - start:.2f} s')
    print(f'computation time: {end - start_computation:.2f} s')
