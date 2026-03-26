import matplotlib.pyplot as plt
import numpy as np

Mischief = [3, 4, 5, 6, 4, 5, 3, 4, 5, 6, 5, 6, 7, 8, 6, 7, 5, 6, 7, 20] 
Cloak = ["Wearing Cloak"]*12 + ["Not Wearing Cloak"]*12

group_wearing = Mischief[:12]
group_not_wearing = Mischief[12:]

def get_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    outliers = [x if (x < lower or x > upper) else None for x in data]
    return outliers

outliers_wearing = get_outliers(group_wearing)
outliers_not_wearing = get_outliers(group_not_wearing)
# ---------------------------
plt.figure(figsize=(6,4))
plt.hist(Mischief, bins=8, color='#FFB6C1', edgecolor='black')
plt.title("Assumption 1: Continuous Dependent Variable")
plt.xlabel("Mischief Score")
plt.ylabel("Frequency")
plt.show()

# ---------------------------
# Assumption 2: Independent Groups
group_labels = ["Wearing Cloak", "Not Wearing Cloak"]
group_counts = [Cloak.count("Wearing Cloak"), Cloak.count("Not Wearing Cloak")]
plt.figure(figsize=(6,4))
plt.bar(group_labels, group_counts, color=['#FFB6C1', '#87CEFA'])
plt.title("Assumption 2: Independent Groups")
plt.xlabel("Cloak Status")
plt.ylabel("Number of Participants")
plt.show()
# ---------------------------
plt.figure(figsize=(8,4))

x_wearing = np.random.normal(0, 0.05, len(group_wearing))
x_not_wearing = np.random.normal(1, 0.05, len(group_not_wearing))

def get_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    outliers = [x if (x < lower or x > upper) else None for x in data]
    return outliers

outliers_wearing = get_outliers(group_wearing)
outliers_not_wearing = get_outliers(group_not_wearing)

plt.figure(figsize=(8,4))

x_wearing = np.random.normal(0, 0.05, len(group_wearing))
x_not_wearing = np.random.normal(1, 0.05, len(group_not_wearing))

plt.scatter(x_wearing, group_wearing, color='#FFB6C1', label='Wearing Cloak')
plt.scatter(x_not_wearing, group_not_wearing, color='#87CEFA', label='Not Wearing Cloak')

for i, y in enumerate(outliers_wearing):
    if y is not None:
        plt.hlines(y, x_wearing[i]-0.05, x_wearing[i]+0.05, color='red', linewidth=2, label='Outlier' if i==0 else "")
for i, y in enumerate(outliers_not_wearing):
    if y is not None:
        plt.hlines(y, x_not_wearing[i]-0.05, x_not_wearing[i]+0.05, color='red', linewidth=2, label='Outlier' if i==0 else "")

plt.xticks([0, 1], ['Wearing Cloak', 'Not Wearing Cloak'])
plt.title("Assumption 3: Observations with Outliers")
plt.xlabel("Cloak Status")
plt.ylabel("Mischief Score")

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

plt.tight_layout()
plt.show()
