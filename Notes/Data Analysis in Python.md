This is an excerpt of the project I did in the course *Statistical Methods for Data Science*. It focuses on the exploratory data analysis of one data set I used in this project.
## Data Preprocessing, Descriptive Statistics and Visualization

```python
# Loading .csv files
df_ds1 = pd.read_csv("Mental_Health_Dataset.csv", sep=",")

# Choosing relevant variables
df_ds1 = df_ds1[["Country", "Occupation", "treatment", "Growing_Stress", "Mood_Swings", "Coping_Struggles", "Social_Weakness"]]
df_ds1
```

```python
# Check for null values
null_values = df_ds1.isnull().sum()
print(null_values)
```

```python
# Check for datatype and possible values
columns = ['Country', 'Occupation', 'treatment', 'Growing_Stress', 'Mood_Swings', 'Coping_Struggles', 'Social_Weakness']
for column in columns:
	dtype = df_ds1[column].dtype
	unique_values = df_ds1[column].unique()
	print(f"Data type for {column}:", dtype)
	print(f"Unique values for {column}:", unique_values)
```

```python
# Replacing non-student occupations with the label 'Non-Student'
df_ds1['Occupation'] = df_ds1['Occupation'].apply(lambda x: 'Student' if x == 'Student' else 'Non-Student')
```

Because I only care about the distinction between students and non-students, I group the data accordingly to make data analysis easier.

```python
# Create new column region for better comparability
western_countries = [
'United States', 'Poland', 'Australia', 'Canada', 'United Kingdom',
'Sweden', 'New Zealand', 'Netherlands', 'Belgium', 'Ireland', 'France',
'Portugal', 'Germany', 'Switzerland', 'Finland', 'Italy',
'Bosnia and Herzegovina', 'Croatia', 'Denmark', 'Greece',
'Georgia', 'Czech Republic', 'Moldova'
]

non_western_countries = [
'South Africa', 'India', 'Brazil', 'Costa Rica', 'Russia',
'Israel', 'Singapore', 'Nigeria', 'Thailand', 'Philippines', 'Mexico', 'Colombia'
]
# Define a function to assign regions
def assign_region(country):
if country in western_countries:
	return 'Western'
elif country in non_western_countries:
	return 'Non-Western'
else:
	return 'Unknown'
# Apply the function to create the 'Region' column
df_ds1['Region'] = df_ds1['Country'].apply(assign_region)
```

To make comparison easier und to better align this dataset with the other two datasets I create a new column called `Region`. This column can either be 'Western' or 'Non-Western'. I define 'Western' as including european, north-american and oceanic countries.

```python
# Get frequencies of each label
columns = ['Region', 'Occupation', 'treatment', 'Growing_Stress', 'Mood_Swings', 'Coping_Struggles', 'Social_Weakness']
# Create subplots
fig, axs = plt.subplots(2, 4, figsize=(10, 7))
axs = axs.flatten() # Flatten the 2x3 array for easier iteration

# Plot histograms for each column
for i, column in enumerate(columns):
	value_counts = df_ds1[column].value_counts()
	axs[i].bar(value_counts.index, value_counts.values)
	axs[i].set_title(column)
	axs[i].set_ylabel('Frequency')
	axs[i].tick_params(axis='x', rotation=45) # Rotate x-axis labels if needed

# Hide any unused subplots
for j in range(len(columns), len(axs)):
	fig.delaxes(axs[j])
	plt.tight_layout()
	plt.show()
```

![[Pasted image 20250123100819.png|400]]

To get a better understanding of how the answer are distributed, I look at bar charts for each of the columns. For the x-axis I always have the possible values in the columns and for the y-axis I have the frequency.

```python
# List of columns to compare with Occupation
columns = ['treatment', 'Growing_Stress', 'Mood_Swings', 'Coping_Struggles', 'Social_Weakness']

# Create subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs = axs.flatten() # Flatten the array for easier indexing

# Plot heat maps
for i, column in enumerate(columns):

# Create crosstab
heatmap_data = pd.crosstab(df_ds1['Occupation'], df_ds1[column])

# Plot heat map
sns.heatmap(heatmap_data, annot=True, cmap='Blues', fmt='d', ax=axs[i])
axs[i].set_title(f'Occupation vs {column}')
axs[i].set_xlabel(column)
axs[i].set_ylabel('Occupation')

# Hide any unused subplots
for j in range(len(columns), len(axs)):
	fig.delaxes(axs[j])
	plt.tight_layout()
	plt.show()
```

  ![[Pasted image 20250123100946.png|400]]

Because I am especially interested in how the answer are distributed between students and non-students participants, I plot these distributions in a heat map. For the x-axis I have again the possible answer of the specific column and for the y-axis I have the distinction between students and non-students.

```python
# Define the mapping dictionary
value_mapping = {
'Yes': 2,
'No': 0,
'Maybe': 1,
'Low': 0,
'Medium': 1,
'High': 2
}

columns_to_map = ['Growing_Stress', 'Mood_Swings', 'Coping_Struggles', 'Social_Weakness']

# Apply the mapping to the specific columns
df_ds1[columns_to_map] = df_ds1[columns_to_map].map(value_mapping.get)

# Add a new column that sums the mapped columns
df_ds1['mental_health_score'] = df_ds1[columns_to_map].sum(axis=1)

# Scale the data
scaler = MinMaxScaler()
df_ds1['mental_health_score'] = scaler.fit_transform(df_ds1[['mental_health_score']])
```

```python
# Look at the descriptive statistics of the mental health score
print(df_ds1["mental_health_score"].describe())
```

```python
plt.figure(figsize=(8, 5))
sns.histplot(df_ds1['mental_health_score'], bins=5, kde=False, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribution of Mental Health Score among Students')
plt.xlabel('Normalized Mental Health Score')
plt.ylabel('Frequency')
plt.grid()
plt.tight_layout()
plt.show()
```

![[Pasted image 20250123101106.png|400]]

To get a better understanding of the mental health score I use the `describe()` function to look at the basic descriptive statistic and a bar chart to look at the distribution.
## Conclusion
In the case of DS1 I mainly have categorical (both ordinal and nominal) data. When generally looking at the descriptive statistics of categorical data, we want to mainly look at the frequency of each category and the composition of each variable. Additionally in this particular case we want to look at the composition of each variable compared to the occupation ("student" vs. "non-student").
To do this, I first looked at all the possible values for each column. Then I choose a bar chart to properly visualize the frequency of each label in each column. Lastly, I looked at the heatmap of each variable compared to the occupation.

The first interesting thing to note about the frequency is that about half the questioned people seem to have some mental health struggles. In the columns `treatment`, `Growing_Stress`, `Mood_Swings`, `Coping_Struggles`, and `Social_Weakness` we can see evenly distributed answers. It is also worth noting that of the questioned people only about 20% were students and only about 5% were participants originating from non-western countries.
Secondly, when looking at the graphs, we can see a clear tendency for students to be more stressed and have more mental health struggles. We can also see that about 50% of students seek treatment for a mental health condition.

Lastly I prepare the dataset for further statistical analysis. I want a metric that is easily interpretable and easily comparable with the other two datasets. I do this by mapping the values to numbers, calculating the mental health score of each participant and scaling this score to be between 0 and 1. For the mental health score I take the columns `Growing_Stress`, `Mood_Swings`, `Coping_Struggles`, and `Social_Weakness`into account.

Unlike the original columns of DS1, the mental health score is continuous numerical. This means that I am interested in different descriptive statistics (mean, std, quantile, ...). Especially interesting in this case, is that the mental health score seems to be almost normally distributed, as shown in the graph.
