## Linear Regression
Linear regression models attempt to draw a straight line that will best minimize the residual sum of squares between the observed responses in the dataset. We use the *sklearn* function `LinearRegression` to do this in Python.

1. Step: Preparing the data.

``` python
df = pd.read_csv('penguins_size.csv').dropna()
df_adelie = df.query('species == "Adelie"')
from sklearn.model_selection import train_test_split
df_adelie_train, df_adelie_test = train_test_split(df_adelie)
```

2. Step: Fitting the model. As we can see we could calculate all this manually but sklearn does this for us.

```Python
x = df_adelie_train['culmen_depth_mm'].to_numpy()
y = df_adelie_train['body_mass_g'].to_numpy()

# Fitting the model with sklearn
lr = LinearRegression().fit(x.reshape(-1,1),y)
lr.intercept_, lr.coef_

# Fitting the model manually
beta = ((x-x.mean())*(y-y.mean())).sum() / ((x-x.mean())**2).sum()
alpha = y.mean() - beta*x.mean()
alpha, beta
```

3. Step: Predicting with the model. This can also be done by computing it manually but sklearn again helps us out.

``` Python
# Predicting with the model with sklearn
lr.predict(x.reshape(-1,1))

# Predicting with the model manually
y_pred = alpha + beta * x
```

![[Pasted image 20241018081128.png|400]]
## Polynomial Regression
When we want to fit non-linear regression with regression tools, we speak of polynomial regression. In *sklearn* this can easily be done by using the familiar `LinearRegression`function.

1. Step: Preparing the data.

``` Python
n = 100 # number of data points
noise_variance = 0.1

x = np.linspace(-10, 10, n, dtype=np.float64)
y_true_model = np.sin(x)
noise = np.random.normal(loc=0.0, scale=noise_variance, size=n)
y_with_noise = y_true_model + noise
```

2. Step: Plotting the true data.

``` Python
plt.plot(x, y_true_model, label="True model", color="orange")
plt.scatter(x, y_with_noise, label="Noisy data")
plt.legend()
```

![[Pasted image 20241018071836.png|400]]

3. Step: Using the built-in function `PolynomialFeatures` to create some polynomial features. What might seem weird is that we need to do a fit (when calling function fit_transform) before we actually fit the regression model. The function `fit_transform` has two functions within it: 
	- fit: Learns the structure of the transformation from the input data (in this case, it determines how to expand the original feature(s) into polynomial terms).
	- transform: Actually applies the transformation, converting the input data into the polynomial features. 
	We can then use the usual `LinearRegression` function from sklearn to create the model.

``` Python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly = PolynomialFeatures(degree=10, include_bias=False)
poly_features = poly.fit_transform(x.reshape(-1, 1))
poly_reg_model = LinearRegression()
poly_reg_model.fit(poly_features, y_with_noise)
y_predicted = poly_reg_model.predict(poly_features)


plt.scatter(x, y_with_noise, label="Noisy Data")
plt.plot(x, y_predicted, label=f"Best {k}-degree polynomial", color="red")
plt.legend()

```

![[Pasted image 20241018071824.png|400]]
## Baseline Models
We might want to create a baseline model to evaluate our model against. This can be done with the sklearn function `DummyRegression`.

With some array *X* and some target *y* we can create a simple dummy regressor with a simple strategy (in this example *mean*, which means the dummy regressor should predict the exam score to be always exactly equal to the mean of all data points seen in the training data). 

``` Python
from sklearn.dummy import DummyRegressor

dummy = DummyRegressor(strategy="mean")
dummy.fit(X, y)
```