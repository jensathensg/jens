import matplotlib.pyplot as plt

group0 = [3, 4, 5, 6, 4, 5, 3, 4, 5, 6]
group1 = [5, 6, 7, 8, 6, 7, 5, 6, 7, 8]

plt.hist(group0, alpha=0.6, color="#FFC0CB", label="Without Cloak") 
plt.hist(group1, alpha=0.6, color="#ADD8E6", label="With Cloak")    

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=10)

plt.title("Histogram (Test Data)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
