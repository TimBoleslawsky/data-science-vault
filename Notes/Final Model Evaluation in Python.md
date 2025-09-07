## Evaluating a Classifier Algorithm
This is an example of how we can use a simple classifier algorithm to create and evaluate this model against a baseline model.
### Train-test Split
To apply a train-test split we can use the `train_test_split`of the module `sklearn`.

``` Python
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('penguins_size.csv').dropna()

# This will produce a train-test split with 80% of the data being in the train set and 20% being the test set
df_train, df_test = train_test_split(df, train_size=800, test_size=200, random_state=1234)
```

### ROC and AUC
Let's say we have a simple classifier model that classifies penguins in their species by looking at their weight. 

``` Python
def simple_classifier(df, w):
	return df['body_mass_g'].apply(lambda x: 'Gentoo' if x > w else 'Adelie')
```

Now lets calculate the TPR and the FPR and plot the ROC.

``` Python
df_adel = df_train.query('species in ["Adelie","Gentoo"]')
ws = np.arange(df_adel['body_mass_g'].min()-1,df_adel['body_mass_g'].max()+1) 
tprs = list()
fprs = list()
p = np.sum(df_adeliegentoo['species'] == 'Gentoo')
n = np.sum(df_adeliegentoo['species'] == 'Adelie')
for w in ws:
    y = simple_classifier(df_adeliegentoo,w)
    tp = np.sum((y == 'Gentoo') & (df_adel['species'] == 'Gentoo'))
    fp = np.sum((y == 'Gentoo') & (df_adel['species'] == 'Adelie'))
    tn = np.sum((y == 'Adelie') & (df_adel['species'] == 'Adelie'))
    fn = np.sum((y == 'Adelie') & (df_adel['species'] == 'Gentoo'))
    tpr = tp / p
    fpr = fp / n
    tprs.append(tpr)
    fprs.append(fpr)
plt.plot(fprs,tprs)
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
```

![[Pasted image 20240927104030.png]]

This is a lot of effort. We can do this simply by using the `sklearn.metrics.roc_curve` function.

``` Python
fpr_skl, tpr_skl, thr_skl = roc_curve(df_adel['species'], df_adel['body_mass_g'], pos_label='Gentoo')

plt.plot(fpr_skl, tpr_skl)
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
```

![[Pasted image 20240927110620.png]]

Now we can use the `roc_auc_score`function to compute the AUC. 

``` Python
from sklearn.metrics import roc_auc_score
roc_auc_score(df_adel['species'], df_adel['body_mass_g'])
```

### Baseline Model and Metrics
To look at the metrics of a model we first need a baseline model to compare these metrics to. In this case, we just use the assumption that every penguin is of species *Adelie*: 

``` Python
df_train_adel = df_train.query('species in ["Adelie", "Gentoo"]')

def baseline(df):
	return df['body_mass_g'].apply(lambda _: 'Adelie')
```

Now we want to calculate the accuracy, precision, and recall of the baseline model. Lets again first do this the "hard" way.

``` Python
y = baseline(df_train_adel)
p = np.sum(df_train_adel['species'] == 'Gentoo')
n = np.sum(df_train_adel['species'] == 'Adelie')
pp = np.sum(y == 'Gentoo')
pn = np.sum(y == 'Adelie')
tp = np.sum((df_train_adel['species'] == 'Gentoo') & (y == 'Gentoo'))
fp = np.sum((df_train_adel['species'] == 'Adelie') & (y == 'Gentoo'))
tn = np.sum((df_train_adel['species'] == 'Adelie') & (y == 'Adelie'))
fn = np.sum((df_train_adel['species'] == 'Gentoo') & (y == 'Adelie'))

acc_dummy = np.sum(y == df_train_adel['species']) / df_train_adel.shape[0]
prec_dummy = tp/pp
rec_dummy = tp/p
acc_dummy, prec_dummy, rec_dummy
```

In this case, the output is:
- acc: 0.5846153846153846
- prec: nan (because we have no positive predictions)
- rec: 0.0 (because we have no positive predictions)

Again we can do this in a much simpler way by using the `sklearn.metrics` library. The functions `accuracy_score, precision_score, recall_score` give us exactly the same result.

``` Python
from sklearn.metrics import accuracy_score, precision_score, recall_score

accuracy_score(df_train_adel['species'],y), \
precision_score(df_train_adel['species'],y,pos_label='Gentoo'), \
recall_score(df_train_adel['species'],y,pos_label='Gentoo')
```

To compute these metrics for our proper classifier we first need to find the optimal threshold. We can easily to this by simply trying out every threshold available.

``` Python
ws = np.arange(np.amin(df_train['body_mass_g'])-1,np.amax(df_train['body_mass_g'])+1)
best_w = 0
best_acc = 0.0
for w in ws:
    y = simple_classifier(df_train,w)
    acc = accuracy_score(df_train['species'],y)
    if acc > best_acc:
        best_acc = acc
        best_w = w
best_w, best_acc
```

Now we can compute the metrics for our proper classifier.

``` Python
y = = simple_classifier(df_test_adeliegentoo,best_w)

accuracy_score(df_test['species'],y), \
precision_score(df_test['species'],y,pos_label='Gentoo'), \
recall_score(df_test['species'],y,pos_label='Gentoo')
```

This gives us the following values: 
- acc: 0.8923076923076924
- prec: 0.8125
- rec: 0.9629629629629629

By comparing the values we can conclude that the accuracy of our model is much higher!
## Evaluating a Linear Regression Model
Let's try to construct a simple linear model that predicts the body mass based on the culmen length, and compare that against a baseline model that uses simply the mean body mass. We'll use the mean squared error as the metric.

Baseline model:

``` Python
mean_gentoo_mass = df_train_gentoo['body_mass_g'].mean()
def dummy_regressor(df):
    return df['culmen_length_mm'].apply(lambda _: mean_gentoo_mass)
```

Now we want to evaluate the baseline model using the squared error, which is (actual value - predicted value)^2:

``` Python
df_test_gentoo = df_test.query('species == "Gentoo"')
y = dummy_regressor(df_test_gentoo)
mse_dummy = np.mean((df_test_gentoo['body_mass_g'] - y)**2)
# mse_dummy is in this case = 237683.05745044386
```

This can also be very easily done with the `sklearn.metrics` library and the function `mean_squared_error`.

``` Python
from sklearn.metrics import mean_squared_error
mean_squared_error(df_test_gentoo['body_mass_g'],y)
```

Now let's consider a proper linear model:

``` Python
from sklearn.linear_model import LinearRegression

# Create linear regression object
lr = LinearRegression()

# Train the model using the training sets
lr.fit(df_train_gentoo['culmen_length_mm'].to_numpy().reshape(-1,1),df_train_gentoo['body_mass_g'])

# Make predictions using the testing set
y = lr.predict(df_test_gentoo['culmen_length_mm'].to_numpy().reshape(-1,1))

mse_linear = mean_squared_error(df_test_gentoo['body_mass_g'],y)
# mse_linear is in this case = 155665.84530917704
```

Unsurprisingly, in this case, we can also see that our trained model works better!