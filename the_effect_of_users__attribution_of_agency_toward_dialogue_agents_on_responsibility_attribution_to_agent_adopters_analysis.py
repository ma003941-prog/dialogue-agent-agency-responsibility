# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from scipy import stats

# Spearman's rank correlation coefficient between responsibility attribution to AA and the change in perceived Agency
aa_responsibility = np.array([5, 6, 6, 6, 5, 7, 6, 5, 7, 6, 6, 6, 6, 3, 7, 2, 6, 7, 6, 7, 7, 5]) # Degree of responsibility attributed to AA
agency_diff = np.array([0.142857143, -0.285714286, 0.714285714, 0.142857143, 0.285714286, -0.857142857, -0.285714286, 0.142857143,
                    0, -0.142857143, -0.571428571, 0.142857143, 0.571428571, 2.857142857, -0.571428571, -0.428571429, -1.142857143,
                    -1.428571429, 1, 0.285714286, -0.857142857, 0.428571429]) # Difference in perceived Agency before and after the experiment

spearman_corr, p_value = stats.spearmanr(aa_responsibility, agency_diff)

print(f"Spearman's Rank Correlation Coefficient: {spearman_corr}")
print(f"P-value for testing non-correlation: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a correlation.")
else:
    print("Fail to reject the null hypothesis: There is no correlation.")

# Spearman's rank correlation coefficient between responsibility attribution to Sota and the change in perceived Agency
sota_responsibility = np.array([3, 4, 3, 1, 1, 3, 3, 3, 5, 3, 2, 5, 6, 2, 5, 5, 2, 1, 5, 2, 2, 2]) # Degree of responsibility attributed to Sota
# agency_diff is the same as defined above for AA, so it's not redefined here.

spearman_corr, p_value = stats.spearmanr(sota_responsibility, agency_diff)

print(f"Spearman's Rank Correlation Coefficient: {spearman_corr}")
print(f"P-value for testing non-correlation: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a correlation.")
else:
    print("Fail to reject the null hypothesis: There is no correlation.")


# Levene's test for the variance in the change in perceived Agency between utterance types

# Divide the change in perceived Agency into the two utterance types
typeA_agency_diff = agency_diff[:11]
typeB_agency_diff = agency_diff[11:]

# Perform Levene's test
levene_statistic, levene_p_value = stats.levene(
    typeA_agency_diff,
    typeB_agency_diff,
    center='mean'
)

# Display the results
print("Levene's Test Statistic:", levene_statistic)
print("P-value:", levene_p_value)


# Spearman's rank correlation coefficient between responsibility attribution to AA and the change in perceived Experience
# aa_responsibility is the same as defined above.
experience_diff = np.array([1.7, 0, 1.6, 0.3, 0.7, 1.2, -0.1, -0.9, -0.1, -0.3, -0.5, 0.1, 1, 2.3, 0, 0.7, 0.6, 0.1, 0.7, -0.1, -0.5, -0.5]) # Difference in perceived Experience before and after the experiment
spearman_corr, p_value = stats.spearmanr(aa_responsibility, experience_diff)

print(f"Spearman's Rank Correlation Coefficient: {spearman_corr}")
print(f"P-value for testing non-correlation: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a correlation.")
else:
    print("Fail to reject the null hypothesis: There is no correlation.")

# Spearman's rank correlation coefficient between responsibility attribution to Sota and the change in perceived Experience
# sota_responsibility is the same as defined above.
# experience_diff is the same as defined above for AA.
spearman_corr, p_value = stats.spearmanr(sota_responsibility, experience_diff)

print(f"Spearman's Rank Correlation Coefficient: {spearman_corr}")
print(f"P-value for testing non-correlation: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a correlation.")
else:
    print("Fail to reject the null hypothesis: There is no correlation.")

# Mann-Whitney U test for perceived Agency attribution to the agent between utterance types
from scipy.stats import mannwhitneyu

# Define the two matrices as numpy arrays for utterance types
utterance_typeA_agency = np.array([
    [7, 7, 3, 6, 6, 6, 6],
    [7, 5, 6, 5, 5, 6, 3],
    [7, 7, 6, 7, 7, 7, 6],
    [7, 7, 6, 7, 7, 7, 7],
    [7, 2, 5, 6, 6, 6, 6],
    [7, 7, 4, 5, 5, 7, 5],
    [6, 4, 5, 5, 6, 6, 3],
    [6, 3, 6, 7, 7, 6, 5],
    [7, 5, 4, 6, 7, 4, 6],
    [7, 5, 5, 7, 5, 6, 6],
    [7, 5, 3, 7, 7, 6, 3]
])

utterance_typeB_agency = np.array([
    [7, 3, 3, 6, 6, 7, 3],
    [7, 5, 6, 7, 6, 7, 5],
    [4, 7, 7, 7, 7, 7, 4],
    [2, 2, 2, 5, 2, 5, 4],
    [7, 6, 2, 7, 3, 3, 4],
    [6, 5, 2, 6, 6, 5, 2],
    [5, 4, 1, 6, 1, 4, 1],
    [6, 3, 5, 6, 5, 5, 7],
    [6, 3, 3, 6, 3, 5, 5],
    [4, 7, 7, 5, 5, 4, 3],
    [3, 5, 5, 5, 6, 6, 4]
])

# Calculate the mean for each array (row)
data1_means = np.mean(utterance_typeA_agency, axis=1)
data2_means = np.mean(utterance_typeB_agency, axis=1)

# Perform the Mann-Whitney U test on the means
result = mannwhitneyu(
    data1_means,
    data2_means,
    alternative='two-sided',
    method='asymptotic'
)

statistic = result.statistic
p_value = result.pvalue

# Sample sizes
n1 = len(data1_means)
n2 = len(data2_means)
N = n1 + n2

# Calculate the tie correction term
all_data = np.concatenate([data1_means, data2_means])
_, tie_counts = np.unique(all_data, return_counts=True)
tie_term = np.sum(tie_counts**3 - tie_counts)

# Calculate the expected value and standard deviation of U
mean_U = n1 * n2 / 2
std_U = np.sqrt(
    n1 * n2 / 12
    * ((N + 1) - tie_term / (N * (N - 1)))
)

# Calculate Z-value with continuity correction
if statistic > mean_U:
    z_value = (statistic - mean_U - 0.5) / std_U
else:
    z_value = (statistic - mean_U + 0.5) / std_U

# Calculate effect size r
effect_size_r = abs(z_value) / np.sqrt(N)

# Display the results
print("Mann-Whitney U Test Statistic (on means):", statistic)
print("P-value (on means):", p_value)
print("Z-value (on means):", z_value)
print("Effect size (r) (on means):", effect_size_r)



# Mann-Whitney U test for responsibility attribution to AA between utterance types
# Define the two arrays
typeA_aa_responsibility = np.array([5, 6, 6, 6, 5, 7, 6, 5, 7, 6, 6])
typeB_aa_responsibility = np.array([6, 6, 3, 7, 2, 6, 7, 6, 7, 7, 5])

# Perform the Mann-Whitney U test
statistic, p_value = mannwhitneyu(typeA_aa_responsibility, typeB_aa_responsibility, alternative='two-sided')

# Display the results
print("Mann-Whitney U Test Statistic:", statistic)
print("P-value:", p_value)

# Wilcoxon signed-rank test for the pre-post difference in likability towards the dialogue agent (Sota)
from scipy.stats import wilcoxon

# Define the data
sota_likability_pre = [4, 4.8, 4.6, 4.4, 3.8, 3.8, 3.6, 3.6, 4.2, 4.6, 3.4, 3.4, 2.6, 3.8, 3.2, 4.4, 4.6, 2.8, 3.2, 3.4, 5, 3.6]
sota_likability_post = [4.6, 4.8, 4.8, 4.8, 2.6, 2.6, 3.8, 4.2, 3.2, 4.8, 3.6, 3.8, 3.6, 5, 4.4, 4.6, 4.8, 3.6, 3.4, 4, 4.4, 4.6]

# Perform the Wilcoxon signed-rank test
result = wilcoxon(
    sota_likability_pre,
    sota_likability_post,
    alternative='two-sided',
    method='approx'
)

statistic = result.statistic
p_value = result.pvalue
z_value = result.zstatistic

# Sample size
N = len(sota_likability_pre)

# Calculate effect size r
effect_size_r = abs(z_value) / np.sqrt(N)

# Output results
print("Wilcoxon Statistic W:", statistic)
print("P-value:", p_value)
print("Z-value:", z_value)
print("Effect size r:", effect_size_r)

if p_value < 0.05:
    print("Reject the null hypothesis: The medians of the two groups are different.")
else:
    print("Fail to reject the null hypothesis: The medians of the two groups are the same.")

# Wilcoxon signed-rank test for the pre-post difference in likability towards AA
# Define the data
aa_likability_pre = [4.461538462, 4, 5.153846154, 3.384615385, 4.461538462, 3.461538462, 4, 5.384615385,
               3.230769231, 2.846153846, 3.076923077, 3.307692308, 5.461538462, 5.230769231, 3.076923077,
               4.538461538, 4.384615385, 1.923076923, 4.307692308, 3.923076923, 4.153846154, 4.307692308]

aa_likability_post = [4.538461538, 3.461538462, 4, 2.076923077, 3.307692308, 1.538461538, 3.384615385, 4.230769231,
              2.153846154, 1.769230769, 1.846153846, 3.846153846, 2.153846154, 5.769230769, 1.923076923,
              3.307692308, 3.846153846, 1.230769231, 4, 2.846153846, 3.153846154, 3.384615385]

# Perform the Wilcoxon signed-rank test
result = wilcoxon(
    aa_likability_pre,
    aa_likability_post,
    alternative='two-sided',
    method='approx'
)

statistic = result.statistic
p_value = result.pvalue
z_value = result.zstatistic

# Sample size
N = len(aa_likability_pre)

# Calculate effect size r
effect_size_r = abs(z_value) / np.sqrt(N)

# Output results
print("Wilcoxon Statistic W:", statistic)
print("P-value:", p_value)
print("Z-value:", z_value)
print("Effect size r:", effect_size_r)

if p_value < 0.05:
    print("Reject the null hypothesis: The medians of the two groups are different.")
else:
    print("Fail to reject the null hypothesis: The medians of the two groups are the same.")


# Mann-Whitney U test for responsibility attribution to AA between participants with increased and decreased/unchanged Agency attribution

# Divide participants into two groups based on the change in perceived Agency
increased_group = aa_responsibility[agency_diff > 0]
decreased_unchanged_group = aa_responsibility[agency_diff <= 0]

# Perform the Mann-Whitney U test
statistic, p_value = mannwhitneyu(
    increased_group,
    decreased_unchanged_group,
    alternative='two-sided'
)

# Sample sizes
n1 = len(increased_group)
n2 = len(decreased_unchanged_group)

# Calculate rank-biserial correlation
rank_biserial = 1 - (2 * statistic) / (n1 * n2)

# Display the results
print("Mann-Whitney U Test Statistic:", statistic)
print("P-value:", p_value)
print("Rank-biserial correlation:", rank_biserial)