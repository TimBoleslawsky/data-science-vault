Data encoding is the process of converting categorical or textual data into a numerical format so that it can be used by machine learning algorithms, which typically require numerical input.
## One-hot Encoding
This encoding technique works by creating new columns per unique values within a category feature. Each of these column corresponds to one category and therefore each data point has zeros in all of these column except one.

| ... | Color | Red | Green | Blue |
| --- | ----- | --- | ----- | ---- |
| ... | red   | 1   | 0     | 0    |
| ... | green | 0   | 1     | 0    |
| ... | blue  | 0   | 0     |      |

There exist multiple ways to do one-hot encoding. Two popular ways are described below:

**DictVectorizer**
This one-hot encoder works by taking in a list of dictionaries and automatically detecting categorical features. These are encoded using one-hot encoding, numerical features are left as-is. This is a very simple approach, but doesn't integrate easily with DataFrames. Here is an example: 

``` python
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier

# Convert DataFrame to list of dicts
dict_data = df.to_dict('records')

# One-hot encode
dv = DictVectorizer(sparse=False)
X_encoded = dv.fit_transform(dict_data)
```

**ColumnTransformer**
Here we take a pandas DataFrame (or NumPy array) and explicitly apply one-hot encoding to specified columns (using the ColumnTransformer). This gives us a more robust framework that allows us to have full control over which columns to encode, handle unknown categories during inference, work better with mixed data types, ...  but it is slightly more code. Here is an example:

``` python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier

# Define columns
categorical = ['Color', 'Size']
numerical = ['Price']

# ColumnTransformer applies OneHotEncoder to categorical columns
column_transformer = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical),
        ('num', 'passthrough', numerical)
    ]
)

# Fit and transform
X_encoded = column_transformer.fit_transform(df)

# Get feature names
ohe = column_transformer.named_transformers_['cat']
cat_features = ohe.get_feature_names_out(categorical)
all_features = list(cat_features) + numerical

print("Feature names:", all_features)
print("Encoded data:\n", X_encoded)
```