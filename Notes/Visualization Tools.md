Visualization is a big part of what data science is. We aim to answer real-world problems, and the audience of these answers is, in most cases, another human. Therefore, it is crucial that we are not only able to answer the questions but also present them in a manner that is understandable for our audience. 

When it comes to visualization, we want to take into account what data type we are looking at, categorical or numerical. Independent of that we usually care about the **distribution** (or composition) or **dependence** (or relationship) of the data we want to visualize. That's why we will categorize the different graphs by these two categories. 
## Categorical Data
For the distribution of categorical data, we tend to use *bar charts*, *pie charts*, or *dot plots*, and for the dependence *mosaic plots*. 

**Bar Chart**
Bar charts are useful for comparing counts or proportions across categories. Bar charts can be stacked or grouped. These are useful for displaying subcategories within each main category.

**Pie Chart**
Pie charts are good at showing the proportions of categories in relation to the whole. However, pie charts become difficult to interpret with too many categories or with categories of similar sizes.

**Dot Plots** 
Dot plots are basically bar charts that only represent the largest value in each bar. Dot plots can be useful when we want to interpolate our categorical data to represent a continuous variable. 

**Mosaic Plot**
As said above, mosaic plots are good at displaying relationships between two or more categorical variables. The height and width represent the proportion of the corresponding category. 
## Numerical Data
For the distribution of numerical data, we tend to use *line plots*, *histograms*, or *box plots*, and for the dependence *scatter plots* or *heat maps*. 

**Line Plot**
A line plot is the simplest form to see the distribution of numerical data and is best used to view changes over time.

**Box Plot**
When we also plot the uncertainty with line plots or dot plots, we speak of box plots (or whisker plots). One way to plot the uncertainty is to additionally to the median, also plot quantiles and the outliers to more honestly represent the data. 

**Histogram**
The idea of a histogram is very simple. Divide the range of the sample into equally sized bins. Count how many data points lie inside each bin. Then plot the count (y-axis) and the bin values (x-axis). The difficulty is to determine the right number of bins $b$. One estimate could be: $b = n/25$
A **normalized histogram** is just a histogram but the area is normalized to 1. This equates roughly to the PDF of the underlying distribution and can be transformed into the same by using the **Kernel density estimator**. The KDE is the smoothed normalized histogram. The KDE is computed as follows: $f_{KDE}(x) = {1 \over nh}  \sum_{i=1}^{n} K({x_i - x \over h})$, with $x$ being the bin, $h$ being the bandwidth and $K()$ being the kernel function. 

**Scatter Plot**
The scatter plot is best used for analyzing the covariance/correlation. It makes it easy to identify the relationship between two variables and identify possible clusters. 

**Heat Map**
A heat map can be useful if we want to analyze the covariance/correlation of more than two variables. 
