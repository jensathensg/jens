A_pass, A_fail = 72, 17
B_pass, B_fail = 64, 23

total = A_pass + A_fail + B_pass + B_fail
rowA = A_pass + A_fail
rowB = B_pass + B_fail
colPass = A_pass + B_pass
colFail = A_fail + B_fail

E_A_pass = rowA * colPass / total
E_A_fail = rowA * colFail / total
E_B_pass = rowB * colPass / total
E_B_fail = rowB * colFail / total

chi_no_yates = (
    (A_pass - E_A_pass)**2 / E_A_pass +
    (A_fail - E_A_fail)**2 / E_A_fail +
    (B_pass - E_B_pass)**2 / E_B_pass +
    (B_fail - E_B_fail)**2 / E_B_fail
)

chi_yates = (
    (abs(A_pass - E_A_pass) - 0.5)**2 / E_A_pass +
    (abs(A_fail - E_A_fail) - 0.5)**2 / E_A_fail +
    (abs(B_pass - E_B_pass) - 0.5)**2 / E_B_pass +
    (abs(B_fail - E_B_fail) - 0.5)**2 / E_B_fail
)

crit_005 = 3.841
crit_001 = 6.635

print("Chi-square (Without Yates):", chi_no_yates)
print("Chi-square (With Yates):", chi_yates)


print("\nDecision at 0.05:")
print("---------------------------------")
print("Without Yates:", "Reject H0" if chi_no_yates > crit_005 else "Fail to reject H0")
print("With Yates:", "Reject H0" if chi_yates > crit_005 else "Fail to reject H0")

print("---------------------------------")
print("\nDecision at 0.01:")
print("---------------------------------")
print("Without Yates:", "Reject H0" if chi_no_yates > crit_001 else "Fail to reject H0")
print("With Yates:", "Reject H0" if chi_yates > crit_001 else "Fail to reject H0")
print("---------------------------------")