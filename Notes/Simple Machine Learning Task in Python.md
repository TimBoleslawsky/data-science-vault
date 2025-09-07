This is an excerpt of the project I did for the course *Statistical Methods for Data Science*. This part focuses on a small machine learning task.
## Defining the Task
The task i want to take on is the following: Predicting students risk of mental Health struggles based on academic and social factors. This will involve that I develop a machine learning model to predict the likelihood that a student will experience mental health issues (such as stress, anxiety, or depression) based on a selection of features. I will select these features based on a logistic regression analysis.

Why I believe this is an important task, is because by leveraging machine learning models, universities and institutions could potentially identify students at risk early on and provide targeted interventions (e.g., counseling, stress management programs). Therefore this task has the potential to reduce mental health challenges among students by enabling preventive measures, helping to improve student well-being and academic success. From a technical perspective, this task is interesting to me, because it requires both classification (predicting the risk) and regression (understanding which factors most influence mental health) approaches

Research questions:
- “Can machine learning models be used to predict the likelihood of mental health struggles among students based on academic performance, social factors, and lifestyle habits?”
- "What machine learning model is best suited for this task?"
- "What variables have the most influence over the mental health of students?"

```python
# Preprocess Data
# Loading .csv files
df_ds3_ml = pd.read_csv("02_Student_Mental_Health_2021-10-10.csv", sep=",")

# Calculating mental health
df_ds3_ml["mental_health_score"] = df_ds3_ml.iloc[:, 96:117].sum(axis=1)

# Assign mental health class based on mental health score
range_width = (84 - 21) / 3
low_threshold = 21 + range_width
high_threshold = 84 - range_width

def classify(score):
	if score <= low_threshold:
		return 'low'
	elif score <= high_threshold:
		return 'middle'
	else:
		return 'high'

df_ds3_ml['mental_health_class'] = df_ds3_ml['mental_health_score'].apply(classify)

# Select relevant columns
df_ds3_ml = df_ds3_ml.iloc[:1192, [4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,38,39,40,52,148]]
```

Because for this task only data from DS3 is relevant, I loaded it into a separate data frame. I again calculated the mental health score again but this time assigned classes based on the range of the mental health score. This will allow me to use a classification model. For the lowest third I assigned the class "low", for the middle third I assigned the class "middle", and for the highest third I assigned the class "high".

I then selected all the columns that could theoretically influence the mental health score to prepare for the logistic regression analysis.

```python
# Split features and target
X = df_ds3_ml.drop("mental_health_class", axis=1)
y = df_ds3_ml["mental_health_class"]

numerical_feature_list = ["Age", "Strenous exercise", "Moderate exercise", "Mild exercise", "Hours_sleep"]

categorical_feature_list = ["Ethnicity", "Sex", "Gender", "Year_credits", "Year_calendar", "Program", "Part_time", "Degree", "Disability", "Living", "Province", "International", "Employment", "Volunteering", "Plans"]

# Encode categorical variables
encoder = OneHotEncoder(drop=None, sparse_output=False)
categorical_features = X[categorical_feature_list]
encoded_categorical = encoder.fit_transform(categorical_features)

# Standardize numerical features
scaler = StandardScaler()
numerical_features = X[numerical_feature_list]
scaled_numerical = scaler.fit_transform(numerical_features)

# Combine preprocessed features
X_processed = np.hstack((scaled_numerical, encoded_categorical))

# Encode target variable
y_encoded = y.map({"low": 0, "middle": 1, "high": 2})

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_processed, y_encoded, test_size=0.2, random_state=42)
```

```python
# Train multinomial logistic regression
model = LogisticRegression(multi_class="multinomial", max_iter=1000)
model.fit(X_train, y_train)

# Get coefficients for all features
coefficients = np.abs(model.coef_)
feature_names = (
	numerical_feature_list
	+ encoder.get_feature_names_out(categorical_feature_list).tolist()
	)

# Aggregate influence across all classes
feature_influence = coefficients.sum(axis=0)

# Create a DataFrame to sort and display results
influence_df = pd.DataFrame({
	"Feature": feature_names,
	"Influence": feature_influence
	}).sort_values(by="Influence", ascending=False)

print("Feature Influence Ranking:")
print(influence_df.head(10))
```

As I said, I first wanted to analyze the features based on influence over the target variable. For this, a regression analysis is more appropriate than a simple correlation analysis. This is because regression evaluates the relationship between predictors and the target variable while accounting for interactions and other variables, while correlation analysis only measures the linear relationship between two variables.

From the analysis we can see that the columns: `Province`, `Year_calendar`, `Disability`, `Plans`, `Degree`, `Employment`, and `Sex` have the most influence over the target variable. It is important to note, that we don't know whether these features have a positive or a negative influence over the target variable. Just that they have a large one. Let's break down what we see:
- For the province, the answers 10 and 9 mean Nova Scotia and Prince Edward Island respectively. I don't know canadian geography, and therefore can make no reasonable guess at to what these answers could mean.
- For the calendar year, the answers 6, 7, and 8, mean exactly that, students in their 6th, 7th, and 8th year. I guess that this means that students in their later years experience more mental health issues. This is not too surprising as studies tend to get more stressful towards the end of the degree.
- For the disability, the answer 2 means that these students have no disabilities. This leads me to believe that students with disabilities experience a lot more mental health issues than students without.
- For the plans, the answer 4 means that the student means to enter a trade. I can make no educated guess on to why or how this influences the mental health score.
- For the degree, the answer 1 means that this student is in their first university program. I will guess, that that means that students in their first degree experience a lot more stress than students in their second, third, and so on.
- For the sex, the answer 1 means that this student is male. I would say this probably means that male students experience less stress than female students.
## Develop the Models
To develop the models I will take the features that have the most influence on the target variable from the previous step and train a logistic regression model, a k-nearest neighbor model, and a naive Bayes model.

```python
# Split features and target
X = df_ds3_ml.drop("mental_health_class", axis=1)
y = df_ds3_ml["mental_health_class"]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=55)

# Define preprocessing
features = ["Province", "Year_calendar", "Disability", "Plans", "Degree", "Employment", "Sex"]

preprocessor = ColumnTransformer(
	transformers=[("cat", OneHotEncoder(sparse_output=False), features)])

# Define classifiers
classifiers = {
	"Logistic Regression": LogisticRegression(random_state=55, max_iter=1000),
	"K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=4), # arrived at k=4 by manually testing k's 1 to 8 and taking the best result.
	"Naive Bayes": GaussianNB()
	}
```

## Evaluate the Models

```python
# Evaluate each classifier
predictions = []
false_positive_rates = []
true_positive_rates = []

for name, classifier in classifiers.items():

	# Create pipeline
	pipeline = Pipeline(steps=[
		("preprocessor", preprocessor),
		("classifier", classifier)
		])
		
	# Train model
	pipeline.fit(X_train, y_train)
	
	# Predict and evaluate
	y_pred = pipeline.predict(X_test)
	predictions.append(y_pred)
	accuracy = accuracy_score(y_test, y_pred)
	f_score = f1_score(y_test, y_pred, average='macro')
	print(f"{name}")
	print("accuracy:", accuracy)
	print("f-score:", f_score)
```

Logistic Regression
accuracy: 0.4435146443514644
f-score: 0.3304761904761905

K-Nearest Neighbors
accuracy: 0.4769874476987448
f-score: 0.36106078957686866

Naive Bayes
accuracy: 0.22594142259414227
f-score: 0.19834321061259852

```python
# Evaluate the statistical significance
# Create contingency tables for each pair
table_LK = pd.crosstab(pd.Series(predictions[0]), pd.Series(predictions[1]))
table_LN = pd.crosstab(pd.Series(predictions[0]), pd.Series(predictions[2]))
table_KN = pd.crosstab(pd.Series(predictions[1]), pd.Series(predictions[2]))

# Perform McNemar's test for each pair
result_LK = mcnemar(table_LK, exact=True)
result_LN = mcnemar(table_LN, exact=True)
result_KN = mcnemar(table_KN, exact=True)

# Print p-values for each test
print("p-value for McNemar's test between logistic regression and k-nearest neighbor:", result_LK.pvalue)
print("p-value for McNemar's test between logistic regression and naive Bayes:", result_LN.pvalue)
print("p-value for McNemar's test between k-nearest neighbor and naive Bayes:", result_KN.pvalue)
```

p-value for McNemar's test between logistic regression and k-nearest neighbor: 1.0
p-value for McNemar's test between logistic regression and naive Bayes: 5.048709793414476e-29
p-value for McNemar's test between k-nearest neighbor and naive Bayes: 2.195560136601449e-32

To evaluate the classifiers, I first fitted each classifier and tried to predicted on my test data. I then calculated the accuracy and the f-score for each classifier. I did not look at the roc-curve, because the libraries I could find, did not support multiclass roc-curves out of the box.

We unfortunately see that the accuracy and the f-score for all these classifiers is not great. The k-nearest neighbor model did the best with an accuracy of 0.48 and a f-score of 0.36. Second best was the k-nearest neighbor model with an accuracy of 0.44 and a f-score of 0.33. Last was the naive Bayes classifier with an accuracy of 0.23 and a f-score of 0.2.

Next, I applied the McNemar test to examine the significance of the misclassification patterns between the models. I do this because, if two models have nearly identical accuracy, F1-score, etc., the McNemar’s test can reveal if they are statistically equivalent or if one consistently outperforms the other. I use the McNemar test and not the paired-t test, because I want to test if there is a difference the binary outcomes of each classifier.

The p-values from McNemar’s tests are extremely small (much less than 0.05), when we compare each of the other classifiers to the naive Bayes classifier. This suggests that there are significant differences between these two classifiers (logistic regression and k-nearest neighbor) and the naive Bayes classifier. For these two comparisons, we can reject the null hypothesis that there is no statistically significant difference between the classifiers.

For the test between the logistic regression classifier and the k-nearest neighbor classifier, the McNemar test gives me a p value of 1. This means that, for the given dataset, these two classifiers have no significantly different misclassification patterns compared to one another.

As we saw unfortunately none of these classifiers seem to work great at predicting the mental health class on students based on the given features. If I had to choose one of the classifiers I would choose between the logistic regression classifier and the k-nearest neighbor classifier. The performance of these two is almost identical and the McNemar's test also did not find any significantly different misclassification patterns. the naive Bayes classifier performed extremely poorly compared to other models. One possible explanation for this is that its independence assumption may not hold in this context.