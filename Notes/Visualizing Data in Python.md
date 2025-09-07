## Using Matplotlib
### Basic Plotting
**plt.plot**
The basic plotting is done with the command `plt.plot` which gives us a basic line diagram. We can do this with two different syntaxes. Either `plt.plot(df)`or `df.plot()`. The former is original to matplotlib and is better for complex plots that require some form of customization. The latter is actually built in pandas (although it also uses matplotlib in the background) and is better to creat quick and easy plots. This is a basic example with labels, a title, and a legend:

``` python
# 1. Approach
plt.plot(fraction_dependent, label="Dependent population")
plt.plot(fraction_children, label="Fraction of children")
plt.plot(fraction_elderly, label="Fraction of elderly")


plt.xlabel("Year")
plt.ylabel("Per overall population")
plt.title("Dependent population, children and elderly")
plt.legend(loc="lower right")

# 2. Approach
emissions_wide.plot()
# In this case we can also manually determine wich columns we want to plot in the x and y axis.
emissions_wide.plot(x='year',y=['Cement', 'Coal'])

plt.xlabel("Year")
plt.ylabel("Emissions")
plt.title("Emissions by commodity per year")
# This will automatically display a legend were the labels are the column names of the data frame.
```

![[Pasted image 20240921154549.png|400]]

**plt.subplot**
We can plot several subplots in an x,y matrix with the function `plt.subplot`. The `plt.subplot` function creates a figure and several axes objects. For better visual clarity the function `fig.tight_layout()`can be helpful. For iterating over the axes the `enumerate`function can be helpful. 

``` Python
y1 = df_adelie_train['body_mass_g']

fig, axs = plt.subplots(2,2,figsize=(10,7))

axs[0,0].set_xlabel("Price")
axs[0,0].set_ylabel("Frequency")
axs[0,0].set_title("Histogram of Prices (unadjusted)")
# Turn the ticklabels from 1*e^6 to 100000
axs[0,0].ticklabel_format(style='plain')

# ...

fig.tight_layout()
```

### Categorical Data
Here are some useful graphs for visualizing categorical data. We usually want to visualize distribution or dependence.
#### Distribution
**Bar Plot**
Let's say we have a data set where all the Roman emperors are listed with the cause of the death and the killer. Now we want to visualize what killed the assassinated emperors. 

``` Python
emperors_assassinated = emperors.query('cause == "Assassination"')

# Get unique killers and their counts
killer_counts = emperors_assassinated['killer'].value_counts()

# Plot the bar chart
plt.bar(killer_counts.index, killer_counts.values, color='red')
plt.xticks(rotation=90)  # Rotate the x-axis labels if necessary
plt.xlabel('Killer')
plt.ylabel('Number of Emperors Assassinated')
plt.title('Number of Roman Emperors Assassinated by Each Killer')
plt.show()
```

![[Pasted image 20240928092341.png|400]]

**Stacked Column Chart**
A stacked column chart nicely shows us some categorical data's distribution and composition. To plot a stacked column chart, we first need to format the data in a certain way. 

``` Python
# Data preparation. We need a variable `data` of shape:
Class Male Female  
1     122  94 
2     108  76 
3     347  144

# Plotting the stacked column chart
ax = data.plot(kind='bar', stacked=True, figsize=(10, 6))
```

![[Pasted image 20241119091506.png|400]]
### Numerical Data
Here are some useful graphs for visualizing numerical data. We usually want to visualize distribution or dependence.
#### Distribution
**Line Plot**
For an example using a line plot see the example described in the chapter [[Visualizing Data in Python#Basic plotting]]

**Histogram**
The important part of plotting a histogram is the `bins`-attribute. Here we specify the number of bins we should use. Another important note is that outliers can heavily affect the histogram. Always check for outliers before plotting a histogram. 

``` Python
fig, axs = plt.subplots(1,1,figsize=(10,7), squeeze=False)

axs[0,0].hist(filtered_prices[1], bins=30, color='skyblue', edgecolor='black')
axs[0,0].set_xlabel("Price")
axs[0,0].set_ylabel("Frequency")
axs[0,0].set_title("Histogram of Prices (filtered)")
axs[0,0].ticklabel_format(style='plain')
```

![[Pasted image 20241118104245.png|400]]
#### Dependence
**Scatter Plot**
In this example, we are using a pandas series for input data. We can also use two different lists of x and y values, as shown in the next `plt.scatter` example: 

``` Python
x = [1, 2, 3, 4] 
y = [10, 20, 25, 30]

plt.scatter(x, y, s=100, c='red', alpha=0.5, label='Data Points') 
```

![[Pasted image 20240921154530.png|400]]
## Using Seaborn
### Basic Plotting
**Inserting Seaborn plots into Matplotlib subplots**
To insert a Seaborn plot into Matplotlib subplots we can simply add the attribute `ax=axs[0,0]`to the Seaborn statement. 

``` Python
fig, axs = plt.subplots(1,1,figsize=(10,7), squeeze=False)

sns.countplot(x='Embarked', data = df, color='blue', ax=axs[0,0])
axs[0,0].set_xlabel("Value")
axs[0,0].set_ylabel("Frequency")
axs[0,0].set_title("Histogram of 'Embarked'")

# Continue for the other axis with either seaborn or matplotlib.
```

### Categorical Data
Here are some useful graphs for visualizing categorical data. We usually want to visualize distribution or dependence.
#### Distribution
**Count Plot**
The count plot is a great way to quickly show the distribution of data points in a few categories. The basic idea is to plot a histogram for the count of data points in a given category.  

``` Python
fig, axs = plt.subplots(1,1,figsize=(10,7), squeeze=False)

sns.countplot(x='Embarked', data = df, color='blue', ax=axs[0,0])
axs[0,0].set_xlabel("Value")
axs[0,0].set_ylabel("Frequency")
axs[0,0].set_title("Histogram of 'Embarked'")
```

![[Pasted image 20241118110852.png|400]]

**Strip Plot**
A strip plot is great for comparing a categorical and a numerical variable. It shows us how the values in each category are distributed in regards to a specific numerical variable. 

``` Python
plt.figure(figsize=(10,6))

sns.stripplot(data=df, x ="Embarked", y = "Fare")

plt.title("Fare price for diffrent embarked ports")
plt.xlabel("Port where they embarked from")
plt.ylabel("Price of the ticket")
```

![[Pasted image 20241119091441.png|400]]

**Violin Plot**
The violin plot is great for analyzing the distribution of categorical data based on two different variables, one numerical and one categorical. 

``` Python
titanic = pd.read_csv("titanic_train.csv")

# Draw a nested violinplot and split the violins for easier comparison
sns.violinplot(data=titanic, x="Embarked", y="Age", hue="Sex",
split=True, inner="quart", fill=False,
palette={"male": "g", "female": ".35"})

plt.show()
```

![[Pasted image 20241119091739.png|400]]
### Numerical Data
Here are some useful graphs for visualizing numerical data. We usually want to visualize distribution or dependence.
#### Distribution
**Kde Plot**
The Kde plot makes use of the kernel density estimator explained [[Visualization Tools|here]] to visualize the distribution of numerical data. 

``` Python
fig, axs = plt.subplots(1,1,figsize=(10,7), squeeze=False)

sns.kdeplot(df['Fare'], color='blue', ax=axs[0,0])
axs[0,0].set_xlabel("Value")
axs[0,0].set_ylabel("Frequency")
axs[0,0].set_title("Density Plot of 'Fare'")
```

![[Pasted image 20241118111139.png|400]]
#### Dependence
**Advanced Scatter Plot**
Let's say we want to create a scatter plot that shows the relationship between two numerical values, colored by the species of penguin. We want to give it a title, label the axes appropriately, and add a legend. Now the 'complex' part is that we want to automatically see which points in the scatter plot belong to which species.

Doing this with matplotlib:

``` Python
# Plot each category separately to color them
species = penguins['species'].unique()
for s in species:
    subset = penguins[penguins['species'] == s]
    plt.scatter(subset['flipper_length_mm'], subset['body_mass_g'], label=s)

# Add labels, legend, and show the plot
plt.xlabel('Flipper length')
plt.ylabel('Body mass')
plt.legend(title='Species')
plt.title('Correlation of flipper length and body mass')
plt.show()
```

Doing this with seaborn:

``` Python
import seaborn as sns
sp = sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species')
sp.set(xlabel ="Flipper length", ylabel = "Body mass", title ='Correlation of flipper length and body mass')
```