Apache Spark is a general-purpose engine for large-scale data processing, primarily used to implement [[Parallel Programming in Python|parallel programming]]. Unlike MapReduce it is not a programming paradigm but Spark also includes the MapReduce idea. The advantages of Spark are:
- Speed, ease of use, flexibility across many workloads  
- The programming model allows for cached computations, flexible operations, and iteration  
- Parallelization can be done automatically by the engine (like with MapReduce)  
- APIs available for Python, Java, Scala, R, ..

When comparing Spark to MapReduce implementations it becomes apparent, why in practice most people use Spark:

| **Characteristic**    | **MapReduce**                                  | **Spark**                                      |
| --------------------- | ---------------------------------------------- | ---------------------------------------------- |
| **Execution Model**   | Disk-based (reads/writes to disk each step)    | In-memory (keeps data in RAM for faster speed) |
| **Programming Model** | Low-level (manual map/reduce functions)        | High-level APIs (e.g., DataFrames, RDDs)       |
| **Iterative Support** | No native support (manual job chaining needed) | Built-in support for iterative algorithms      |
| **Use Cases**         | Batch processing only                          | Batch processing, real-time streaming, ML, SQL |

For an example of how to implement Spark in Python look at these two: 
- [[High Level Spark.py]] uses DataFrames and a Spark session.
- [[Low Level Spark.py]] uses RDDs and Spark context.
## Core Concepts of Spark
First we need to talk about the difference between RDDs and DataFrames. **RDDs** are low-level, immutable distributed collections of objects. You manipulate them using functional operations like map(), flatMap(), reduceByKey(), etc. We want to use them if there is no structured schema, meaning each line needs to be manually parsed and we need fine grained control over raw data. RDDs use Spark context for example like this:

``` python
sc = SparkContext(master=f'local[{args.num_workers}]')
lines = sc.textFile(args.filename)  # returns RDD
```

**DataFrames** are high-level APIs representing **structured** tabular data (like SQL tables). They support schema, columns, and optimized execution using Catalyst and Tungsten (Spark’s optimizer and memory manager). If we have structured data and want to run SQL-style operations we want to use DataFrames. They use the newer Spark session as an entry point like this:

``` python
spark = SparkSession.builder \
	.master(f'local[{args.num_workers}]') \
	.config("spark.driver.memory", "16g") \
	.getOrCreate()


df = spark.read.csv(args.filename, header=True, inferSchema=True)
```

**Driver programs** contain the main application that we write and run. It defines the RDDs or DataFrames, specifies transformations and actions, and orchestrates task execution across the cluster. The driver program runs on the driver node in the Spark cluster.

**Transformations** are lazy operations (meaning they are deferred until an action is called) that define a new RDD or DataFrame from an existing one. Examples are:
- RDDs: .map(), .filter(), .flatMap(), .reduceByKey()
- DataFrames: .select(), .filter(), .groupBy(), .join()

**Actions** trigger the execution of the transformations. Some examples are:
- RDDs: .collect(), .count(), .reduce(), .saveAsTextFile()
- DataFrames: .show(), .count(), .write(), .collect()

**Shared Variables** are used to share state between tasks running in different nodes (since each task runs independently). There are two types of shared variables:
- **Broadcast Variables**
	- Send read-only data (e.g. lookup tables) to all worker nodes efficiently.
	- Prevents sending large data redundantly with each task.
- **Accumulators**
	- Write-only variables used for **aggregating values** (e.g., counters, sums) across tasks.
	- Updated by tasks, read by the driver only.