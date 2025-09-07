Exploratory data analysis is the search for patterns and trends in a given data set before actually doing any Data Science. We want to answer the question: What does our data really look like? Getting a handle on what you are dealing with is the first step of any serious analysis. 

When confronting a new data set, the following tasks should be done:
1. Answer the basic questions:
	- Who constructed this data set, when, and why?
	- How big is it? 
	- What do the fields mean?
2. Look for familiar or interpretable records:
	- The idea is to get familiar with a few records so we can put them in context and evaluate the soundness of the data you have on it. 
3. Look at the basic statistics of each column:
	- For numerical columns, a good place to start is the *Five-point summary*. The Five-point summary consists of the maximum value, the 1st quartile (25%), the median (50%), the 3rd quartile (75%) and the maximum value.
	- For categorical fields, like occupation, the analogous summary would be a report on how many different label types appear in the column, and what the three most popular categories are.
4. Pairwise correlations:
	- A matrix of correlation coefficients between all pairs of columns (or at least the columns against the dependent variables of interest)
5. Class breakdowns:
	- Are there interesting ways to break things down by major categorical variables, like gender or location?
6. Plots of interesting characteristics:
	- Use plots to look at the distribution, the class, ... to better visualize how the data set looks.