import math
from collections import Counter

# Data
scores = [
    88,45,53,86,33,86,85,30,89,53,41,96,56,38,62,
    71,51,86,68,29,28,47,33,37,25,36,33,94,73,46,
    42,34,79,72,88,99,82,62,57,42,28,55,67,62,60,
    96,61,57,75,93,34,75,53,32,28,73,51,69,91,35
]

n = len(scores)

# Sort data
scores_sorted = sorted(scores)

# Mean
mean = sum(scores) / n

# Median
if n % 2 == 0:
    median = (scores_sorted[n//2 - 1] + scores_sorted[n//2]) / 2
else:
    median = scores_sorted[n//2]

# Mode
freq = Counter(scores)
max_freq = max(freq.values())
mode = [k for k, v in freq.items() if v == max_freq][0]

# Variance and Standard Deviation (sample)
variance = sum((x - mean) ** 2 for x in scores) / (n - 1)
std_dev = math.sqrt(variance)

# Skewness
skewness = (n / ((n-1)*(n-2))) * sum(((x-mean)/std_dev)**3 for x in scores)

# Kurtosis
kurtosis = (
    (n*(n+1))/((n-1)*(n-2)*(n-3)) * sum(((x-mean)/std_dev)**4 for x in scores)
    - (3*(n-1)**2)/((n-2)*(n-3))
)

# Standard Errors
se_skew = math.sqrt(6/n)
se_kurt = math.sqrt(24/n)

# Percentile function
def percentile(data, p):
    k = (len(data)-1) * p/100
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data[int(k)]
    return data[f] + (k-f) * (data[c]-data[f])

Q1 = percentile(scores_sorted, 25)
Q2 = percentile(scores_sorted, 50)
Q3 = percentile(scores_sorted, 75)
D9 = percentile(scores_sorted, 90)
P95 = percentile(scores_sorted, 95)

# Display table
print("\nDescriptive Statistics")
print("-" * 37)
print(f"{'':>26}Score")  # Score header aligned above 60
print("-" * 37)

print(f"Valid                     {n}")
print("-" * 37)
print(f"Mode                      {mode:.3f}")
print("-" * 37)
print(f"Median                    {median:.3f}")
print("-" * 37)
print(f"Mean                      {mean:.3f}")
print("-" * 37)
print(f"Std. Deviation            {std_dev:.3f}")
print("-" * 37)
print(f"Variance                  {variance:.3f}")
print("-" * 37)
print(f"Skewness                  {skewness:.3f}")
print("-" * 37)
print(f"Std. Error of Skewness    {se_skew:.3f}")
print("-" * 37)
print(f"Kurtosis                  {kurtosis:.3f}")
print("-" * 37)
print(f"Std. Error of Kurtosis    {se_kurt:.3f}")
print("-" * 37)
print(f"Minimum                   {min(scores):.3f}")
print("-" * 37)
print(f"Maximum                   {max(scores):.3f}")
print("-" * 37)
print(f"25th percentile (Q1)      {Q1:.3f}")
print("-" * 37)
print(f"50th percentile (Q2)      {Q2:.3f}")
print("-" * 37)
print(f"75th percentile (Q3)      {Q3:.3f}")
print("-" * 37)
print(f"90th percentile (D9)      {D9:.3f}")
print("-" * 37)
print(f"95th percentile (P95)     {P95:.3f}")
print("-" * 37)

# Add the Score value aligned under the header
print(f"{'':>45}")
