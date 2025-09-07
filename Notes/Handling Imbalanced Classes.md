Having imbalanced classes occurs in datasets with a disproportionate ratio of observations in each class. This means that standard accuracy no longer reliably measures performance, which makes model training much trickier. Here are some methods to deal with imbalanced classes:
## Up-sample Minority Class
Up-sampling is the process of randomly duplicating observations from the minority class in order to reinforce its signal. There are several heuristics for doing so, but the most common way is to simply resample with replacement. Here is an example:

``` python
from sklearn.utils import resample

# Separate majority and minority classes
df_majority = df[df.balance==0]
df_minority = df[df.balance==1]

# Upsample minority class
df_minority_upsampled = resample(df_minority,
                                 replace=True,     # sample with replacement
                                 n_samples=576,    # to match majority class
                                 random_state=123) # reproducible results

# Combine majority class with upsampled minority class
df_upsampled = pd.concat([df_majority, df_minority_upsampled])
```

## Down-sample Majority Class
Down-sampling involves randomly removing observations from the majority class to prevent its signal from dominating the learning algorithm. The most common heuristic for doing so is resampling without replacement. Here is an example:

``` python
# Separate majority and minority classes
df_majority = df[df.balance==0]
df_minority = df[df.balance==1]

# Downsample majority class
df_majority_downsampled = resample(df_majority,
                                 replace=False,     # sample without replacement
                                 n_samples=49,    # to match minortiy class
                                 random_state=123) # reproducible results

# Combine majority class with upsampled minority class
df_upsampled = pd.concat([df_majority_downsampled, df_minority])
```

## SMOTE & ENN
Both SMOTE and ENN are predefined algorithms we can access through the `imbalanced-learn`library. They build upon the ideas of down-sampling and up-sampling but to this in a more sophisticated way. 

ENN is an down-sampling technique that works by removing instances from the majority class that are misclassified by their nearest neighbors. It removes instances from the majority class that are incorrectly classified by their nearest neighbors, thus reducing the noise.

SMOTE is an up-sampling technique that creates synthetic samples by selecting two or more similar instances (neighbors) and creating a new synthetic instance along the line between them. Unlike random oversampling (which duplicates instances), SMOTE adds new, **unique samples** that can help improve the generalization of the model.

=> Usually these methods are used in tandem and are then called SMOTE-ENN!