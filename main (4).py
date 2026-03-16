import numpy as np
import math

females = [11,10,11,10,11,12,12,10,9,9,
           9,10,8,7,12,9,7,8,9,8,
           7,7,9,9,12,10,9,13,9,9,
           10,9,6,12,8,11,8,8,11,12,
           9,10,11,14,12,7,11,10,9,11]

males = [12,7,7,10,8,10,11,9,9,13,
         4,9,12,11,9,9,7,12,10,13,
         11,10,6,12,11,9,10,12,8,9,
         13,10,9,7,10,7,10,8,11,10,
         11,7,15,8,9,9,11,13,10,13]

data = females + males

def describe(arr):
    arr = np.array(arr)
    
    mean = np.mean(arr)
    median = np.median(arr)
    std = np.std(arr, ddof=1)
    var = np.var(arr, ddof=1)
    minimum = np.min(arr)
    maximum = np.max(arr)
    n = len(arr)

    quartiles = np.percentile(arr,[25,50,75])
    deciles = np.percentile(arr,[10,20,30,40,50,60,70,80,90])

    skew = ((np.mean((arr-mean)**3))/(std**3))
    kurt = ((np.mean((arr-mean)**4))/(std**4))-3

    t = 1.984
    margin = t * std / math.sqrt(n)
    ci_low = mean - margin
    ci_high = mean + margin

    return [n,mean,median,std,var,minimum,maximum,skew,kurt,quartiles,deciles,ci_low,ci_high]


overall = describe(data)
male_stats = describe(males)
female_stats = describe(females)

print("{:^65}".format("DESCRIPTIVE STATISTICS SUMMARY"))
print("-"*65)
print("{:<15}{:<15}{:<15}{:<15}".format("Statistic","Overall","Males","Females"))
print("-"*65)

labels = ["Sample Size",
          "Mean",
          "Median",
          "Std Dev",
          "Variance",
          "Minimum",
          "Maximum",
          "Skewness",
          "Kurtosis"]

for i,label in enumerate(labels):
    print("{:<15}{:<15.2f}{:<15.2f}{:<15.2f}".format(
        label,
        overall[i],
        male_stats[i],
        female_stats[i]
    ))

print("-"*65)

print("\nQuartiles (Overall):", overall[9])
print("Deciles (Overall):", overall[10])

print("\n95% Confidence Interval (Overall):",
      round(overall[11],2),"to",round(overall[12],2))

print("95% Confidence Interval (Males):",
      round(male_stats[11],2),"to",round(male_stats[12],2))

print("95% Confidence Interval (Females):",
      round(female_stats[11],2),"to",round(female_stats[12],2))