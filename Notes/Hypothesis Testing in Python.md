This is an excerpt of the project I did for the course *Statistical Methods for Data Science*. This part focuses on formulating and investigating hypotheses, after the exploratory data analysis is done. 
## Formulating Hypotheses
From analyzing the datasets, I gained valuable insight in some of the interesting questions regarding mental health struggles with students. These insights I now want to distill into four hypotheses. For that I look at the conclusion I gained from investigating each dataset and look for interesting commonalities or disparities to further analyze and prove.

This leads me to the following hypotheses:
- Hypothesis 1: Students experience more stress and mental health struggles than non-students.
- Hypothesis 2: More than 60% of students are diagnosed with mental health problems or seek treatment.
- Hypothesis 3: Students in higher-income countries report higher mental health scores than students in lower-income countries.
- Hypothesis 4: About 30% of students struggle with severe stress or mental health problems.
## Investigate Hypotheses
In this step I want to test the hypotheses I formulated in the previous step. To do this, I will need to define them as proper statistical hypotheses and perform statistical analysis. I will go through the steps necessary for each hypothesis individually.

For the definitions I will use this schema:
- The first step will be to define a **default statement**. This default statement is a general and "boring" statement that I aim to reject with the hypothesis test.
- The second step would be to design the experiment itself. I do not need to worry about this step in this project, because the experiment is already done.
- Now I want to describe the **data** generated from the experiment, the corresponding **random variables**, and the **parameter of interest** and their **estimates**.
- Next I translate the default statement into a statistical hypothesis (a proposed distribution) and call it the **null hypothesis $H_0$**.
- The **alternative hypothesis $H_A$** is a complement to the null hypothesis and determines, if the test will be a one-tailed or two-tailed test.
- For the **test statistic** $s$, I am interested in the expression or formula, which describes this test statistic.
- Lastly I will need to choose the **significance level** $\alpha$.

Another important note. I will use z-tests and t-tests to investigate the hypothesis. These statistical hypothesis tests assume normality. In my case I have sufficiently large sample sizes so that I do not need to check for normality (central limit theorem).
### Hypothesis 1 (two-sample t-test/Welch's t-test)
#### Definitions
- Default statement: Students and non-students experience the same amount of stress and mental health struggles.
- Data: $x_i$, mental health score of students and non-students.
- Random variable: $X_i$, i.i.d.
- Parameter of interest: $μ_P$, the mean of the mental health score
- Parameter estimate: $\hat{μ}_P$, the sample mean.
- Null hypothesis $H_0$: $μ_S = μ_N$, meaning that the mean of student mental health score and non-student mental health score is equal. This also means that we have a two sample test, because we evaluate two parameter estimates.
- Alternative hypothesis $H_A$: $μ_S > μ_N$. This means that the mean of student mental health score is greater than the mean of the non-student mental health score, making this a one tailed test.
- Test statistic $s$: $s = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$.
- Significance level $\alpha$: 0.05.
#### Evaluate the Hypothesis
To evaluate this hypothesis, we want to use a two-sample t-test (Welch's t-test). We want to use this test because we do not know the population variance and have two sample groups of varying sizes (students and non-students). Unfortunately I can only use data from DS1 to evaluate this hypothesis. I don't want to cross reference the data for students from DS1 and DS2/DS3, because I feel like DS1 focuses more on stress related issues and minor health struggles while DS2/DS3 focus more on actual mental health problems. I believe comparing these two scores would not accurately represent the data.

Before I begin with the hypothesis testing though, I need to prepare the sample for hypothesis testing. I have a very large dataset (n=292364) and a very uneven distribution of 80/20 (non-students vs. students). To account for this I will randomly select 200 students and non-students to get a more appropriate sample for hypothesis testing.

```python
# Prepare sample for hypothesis testing
students_sample = df_ds1[df_ds1['Occupation'] == 'Student'].sample(n=200, random_state=50)
non_students_sample = df_ds1[df_ds1['Occupation'] == 'Non-Student'].sample(n=200, random_state=50)

scores_students = students_sample["mental_health_score"]
scores_non_students = non_students_sample["mental_health_score"]
```

```python
# Perform the two-sample t-test
alpha = 0.05
t_stat, p_value = ttest_ind(scores_students, scores_non_students, alternative='greater', equal_var=False) # Assuming non-equal variances

# Power analysis
mean_students = np.mean(scores_students)
mean_non_students = np.mean(scores_non_students)
std_students = np.std(scores_students, ddof=1)
std_non_students = np.std(scores_non_students, ddof=1)
n_students = len(scores_students)
n_non_students = len(scores_non_students)
pooled_std = np.sqrt((std_students**2 / n_students) + (std_non_students**2 / n_non_students))
effect_size = (mean_students - mean_non_students) / pooled_std

power_analysis = TTestIndPower()
power = power_analysis.solve_power(effect_size=effect_size,
	alpha=alpha,
	nobs1=n_students,
	ratio=n_non_students/n_students,
	alternative='larger')

# Output results
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

if p_value <= alpha:
	print(f"Reject the null hypothesis (p = {p_value}, α = {alpha}).")
else:
	print(f"Fail to reject the null hypothesis (p = {p_value}, α = {alpha}).")

print(f"Power of the test: {power:.4f}")

```

T-statistic: 4.192664780479965
P-value: 1.700231393404226e-05
Reject the null hypothesis (p = 1.700231393404226e-05, α = 0.05).
Power of the test: 1.0000

```python
# Show statistical significance
# Calculate degree of freedom
denominator = ((std_students**2 / n_students)**2 / (n_students - 1)) + ((std_non_students**2 / n_non_students)**2 / (n_non_students - 1))
df = pooled_std / denominator

# Critical values for one-tailed test
t_critical = t.ppf(1 - alpha, df)

# T-Distribution
x = np.linspace(-4, 5, 500)
y = t.pdf(x, df)

# Plot the observed values and null distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='t-Distribution')
plt.fill_between(x, 0, y, where=(x >= t_critical), color='red', alpha=0.3, label="Rejection Region")
plt.axvline(t_stat, color='blue' if t_stat < t_critical else 'orange', linestyle='--', linewidth=2, label=f'Observed t = {t_stat:.2f}')
plt.title('Statistical Significance: Hypothesis 1', fontsize=14)
plt.xlabel('T-Statistic', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

  ![[Pasted image 20250123102149.png|400]]

For hypothesis 1 we reject the null hypothesis, meaning, that we can generalize our hypothesis that students in fact experience more stress and mental health struggles than non-students to the population. In the graph I depict the statistical significance of the results. The line we can see is the null distribution, in this case the t-distribution. On the x-axis we can see the t-statistic and on the y-axis we can see the probability density. We can see that the test statistic sufficiently lies beyond the rejection region letting us reject the null hypothesis.

The power value of 1 means that the hypothesis test is guaranteed to correctly reject the null hypothesis. The power value of 1 also leads me to believe that the sample size might be too large for an effect of this magnitude.

This conclusion is not surprising to me. I would probably have guessed that students are more likely to articulate stress and mental health struggles. What is surprising to me is the magnitude of the difference.
### Hypothesis 2 (z-test on proportions)
#### Definitions
- Default statement: 60% of students are diagnosed with mental health problems or seek treatment.
- Data: $x$ successes out of $n$ trials. In our case a success is if the student is diagnosed with a mental health problem or seeks treatment and the trials are the students.
- Random variable: $X_i \sim \text{Binomial}(n, p)$
- Parameter of interest: $p$, the proportion of students in the population with a diagnosis of a mental health disorder.
- Parameter estimate: $\hat{p}$, the sample proportion.
- Null hypothesis $H_0$: $p = 0.6$, meaning that the proportion of students with a diagnosis of a mental health disorder is 60%. This also means that we have a one sample test, because we evaluate a parameter estimates against a constant.
- Alternative hypothesis $H_A : p > 0.6$. This means that the proportion of students with a diagnosis for a mental health disorder is larger than 0.6, making this a one tailed test.
- Test statistic $s$: $s = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0 (1 - p_0)}{n}}}$.
- Significance level $\alpha$: 0.05.
#### Evaluate the Hypothesis
To test this hypothesis, I want to perform a one-sample, one-sided z-test on proportions. We cannot test the proportions with the t-test, therefore I use the z-test. As I explained I have a one-sample and one-sided z-test in this case. To cross reference data from multiple sources, I will perform this test on DS1 and DS3. DS2 unfortunately has no valuable information for this hypothesis.

```python
alpha = 0.05
p_0 = 0.6
z_stats = []
p_values = []

# Perform z-test with DS1 (I use the students sample I prepared for hypothesis 1)
n = len(students_sample)
x = students_sample[students_sample["treatment"] == "Yes"].shape[0]

z_stat, p_value = proportions_ztest(count=x, nobs=n, value=p_0, alternative='larger')
z_stats.append(z_stat)
p_values.append(p_value)

print("DS1:")
print(f"Z-Statistic: {z_stat}")
print(f"P-Value: {p_value}")

if p_value <= alpha:
	print(f"Reject the null hypothesis (p = {p_value}, α = {alpha}).")
else:
	print(f"Fail to reject the null hypothesis (p = {p_value}, α = {alpha}).")
	
# Power analysis
p_observed = x/n
effect_size = 2 * (np.arcsin(np.sqrt(p_observed)) - np.arcsin(np.sqrt(p_0)))
power_analysis = NormalIndPower()
power = power_analysis.solve_power(effect_size=effect_size, alpha=alpha, nobs1=n, alternative='larger')

print(f"Power of the test: {power}")

# Perform z-test with DS3
n = len(df_ds3)
x = df_ds3[df_ds3["Diagnosis"] == 2].shape[0]

z_stat, p_value = proportions_ztest(count=x, nobs=n, value=p_0, alternative='larger')
z_stats.append(z_stat)
p_values.append(p_value)

print("DS3:")
print(f"Z-Statistic: {z_stat}")
print(f"P-Value: {p_value}")

if p_value <= alpha:
	print(f"Reject the null hypothesis (p = {p_value}, α = {alpha}).")
else:
	print(f"Fail to reject the null hypothesis (p = {p_value}, α = {alpha}).")
	
# Power analysis
p_observed = x/n
effect_size = 2 * (np.arcsin(np.sqrt(p_observed)) - np.arcsin(np.sqrt(p_0)))
power_analysis = NormalIndPower()
power = power_analysis.solve_power(effect_size=effect_size, alpha=alpha, nobs1=n, alternative='larger')

print(f"Power of the test: {power}")
```

DS1:
Z-Statistic: -1.983472456766744
P-Value: 0.9763426596548425
Fail to reject the null hypothesis (p = 0.9763426596548425, α = 0.05).
Power of the test: 0.0011138292967564907
DS3:
Z-Statistic: 3.1945413347807277
P-Value: 0.0007002661384657091
Reject the null hypothesis (p = 0.0007002661384657091, α = 0.05).
Power of the test: 0.7212036241570817

```python
# Show statistical significance
test_names = ["df_ds1", "df_ds3"]

# Calculate the critical values
z_critical = norm.ppf(1 - alpha)

# Z-Distribution (Normal Standard Distribution)
x = np.linspace(-4, 4, 500)
y = norm.pdf(x, 0, 1)

# Plot the observed values and null distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Standard Normal Curve')
plt.fill_between(x, y, where=(x > z_critical), color='red', alpha=0.2, label='Rejection Regions (α = 0.05)')
for z_stat, name in zip(z_stats, test_names):
	plt.axvline(z_stat, color='blue' if z_stat < z_critical else 'orange', linestyle='--', label=f'{name}: z = {z_stat:.3f}')
	plt.title('Statistical Significance: Hypothesis 2')
	plt.xlabel('Z-Statistic')	
	plt.ylabel('Probability Density')
	plt.legend()
	plt.grid(alpha=0.3)
	plt.tight_layout()
	plt.show()
```

  ![[Pasted image 20250123102704.png|400]]

For the second hypothesis I tested on three datasets. The results show that we can reject the null hypothesis in one case (DS3) and fail to reject the null hypothesis in the other (DS1). This is again visualized against the null distribution, in this case the standard normal distribution. I this time plotted the z-statistic in the x-axis and the probability density is again shown on the y-axis. Now for the hypothesis I am testing and for the tests I am carrying out, only the z-value of DS3 is statistically significant. But the results of DS1 obviously should make us cautious. When taking into account the power of the tests, we can see that only the test on DS3 holds any significant statistical power.

For an overall conclusion I can say:
- DS3 provides strong evidence to reject the null hypothesis.
- For DS1 we cannot confidently say whether the null hypothesis is true or false due to the low power of the tests. Additional data or improved test design may be needed to draw more reliable conclusions for these datasets.

This results leads to the question: Can we explain why the test on DS3 rejects the hypothesis while the test on DS1 fails to do so? One possible explanation might be that DS3 only has data from a developed western nation (Canada) while DS1 has data from all around the world, leading to the hypothesis: Students in developed western countries are more frequently diagnosed with mental health issues than students in non-western countries. In the following section I want to investigate this follow-up hypothesis.
### Hypothesis 2.5 (two-sample Z-test on proportions)
#### Definitions
- Default statement: Students in developed western countries are diagnosed with mental health issues the same amount of times as students in non-western countries.
- Data: $x_1,x_2$ successes out of $n_1,n_2$ trials. In our case a success is if the student is diagnosed with a mental health problem or seeks treatment and the trials are the students.
- Random variable: $X_{1} \sim \text{Binomial}(n_1, p_1)$, $X_{2} \sim \text{Binomial}(n_2, p_2)$
- Parameter of interest: $p_1$ and $p_2$, the proportion of students with a diagnosis of a mental health disorder for the population "students in western countries" and for the population "students in non-western countries".
- Parameter estimate: $\hat{p}_1$ and $\hat{p}_2$, the sample proportions.
- Null hypothesis $H_0$: $p_1 = p_2$, meaning that the proportion of students with a diagnosis of a mental health disorder is the same for both western and non-western countries. This also means that this is a two-sample test.
- Alternative hypothesis $H_A : p_1 \ne p_2$. This means that the proportion of students with a diagnosis for a mental health disorder is not the same for both western and non-western countries, making this a two-tailed test.
- Test statistic $s$: $s = \frac{(p_1 - p_2)}{\sqrt{p_{\text{pooled}} \cdot (1 - p_{\text{pooled}}) \cdot \left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$.
- Significance level $\alpha$: 0.05.
#### Evaluate the Hypothesis
To evaluate hypothesis 2.5 I am using a two-sample, two-tailed z-test. In this case I want to see, if two proportions are the same (null hypothesis). For that the two-sample z-test is most appropriate. Because I only have global data in DS1, I will only test this hypothesis on DS1.

As samples I will take 30 students from each region (western / non-western). I do this because I know that the proportion of western to non-western students in DS1 is very heavily skewed towards western students.

```python
# Prepare sample for hypothesis testing
df_ds1_countries = df_ds1[df_ds1['Occupation'] == 'Student']
western_students_sample = df_ds1_countries[df_ds1_countries['Region'] == 'Western'].sample(n=30, random_state=50)
non_western_students_sample = df_ds1_countries[df_ds1_countries['Region'] == 'Non-Western'].sample(n=30, random_state=50)
```

```python
alpha = 0.05

# Perform z-test
x1, n1 = western_students_sample[western_students_sample["treatment"] == "Yes"].shape[0], len(western_students_sample)

x2, n2 = non_western_students_sample[non_western_students_sample["treatment"] == "Yes"].shape[0], len(non_western_students_sample)

count = np.array([x1, x2])
nobs = np.array([n1, n2])

z_stat, p_value = proportions_ztest(count, nobs)

# Output results
print(f"Z-Statistic: {z_stat}")
print(f"P-Value: {p_value}")

if p_value < alpha:
	print(f"Reject the null hypothesis (p = {p_value:}, α = {alpha})")
else:
	print(f"Fail to reject the null hypothesis (p = {p_value}, α = {alpha})")
	
# Power analysis
p1 = x1 / n1
p2 = x2 / n2
p_pooled = (x1 + x2) / (n1 + n2)
effect_size = abs(p1 - p2) / np.sqrt(p_pooled * (1 - p_pooled))
power_analysis = NormalIndPower()
power = power_analysis.solve_power(effect_size=effect_size, alpha=alpha, nobs1=n1, ratio=n2/n1, alternative='two-sided')

# Output
print(f"Power of the test: {power}")
```

Z-Statistic: 3.214798318660919
P-Value: 0.0013053619995990055
Reject the null hypothesis (p = 0.0013053619995990055, α = 0.05)
Power of the test: 0.8952306611735535

```python
# Show statistical significance
# Calculate the critical values
z_critical = norm.ppf(1 - alpha /2)

# Z-Distribution (Normal Standard Distribution)
x = np.linspace(-4, 4, 500)
y = norm.pdf(x, 0, 1)

# Plot the observed values and null distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Standard Normal Curve')
plt.fill_between(x, y, where=(x > z_critical) | (-x > z_critical), color='red', alpha=0.2, label='Rejection Regions (α = 0.05)')
plt.axvline(z_stat, color='blue' if z_stat < z_critical else 'orange', linestyle='--', label=f'{name}: z = {z_stat:.3f}')
plt.title('Statistical Significance: Hypothesis 2.5')
plt.xlabel('Z-Statistic')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

![[Pasted image 20250123103125.png|400]]

The test on DS1 for hypothesis 2.5 was successful in rejecting the null hypothesis. This means we can generalize our hypothesis that students in western countries are more likely to be diagnosed with a mental health disorder than students in non-western countries to the population. We can also see that the power of the test and the statistical significance seem the support this decision.

One possible explanation for this could be that the topic of "mental health" is more accepted in western countries, leading to more visits to mental health experts and therefore likely also to more diagnoses.