import numpy as np
from scipy.stats import chi2_contingency

table = np.array([
    [49, 25],  
    [30, 96]  
])

chi2, p, dof, expected = chi2_contingency(table)

n = np.sum(table)

C = np.sqrt(chi2 / (chi2 + n))

print("Chi-square value:", chi2)
print("Coefficient of Contingency:", C)

k = min(table.shape)
C_max = np.sqrt((k - 1) / k)

print("Maximum Coefficient:", C_max)