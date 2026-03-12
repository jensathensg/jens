import itertools
import matplotlib.pyplot as plt

pop = [9, 12, 15]

samples = list(itertools.product(pop, repeat=2))

means = []
for a, b in samples:
    means.append((a + b) / 2)

xbar = sorted(set(means))

prob = []
total = len(means)

for x in xbar:
    count = means.count(x)
    prob.append(count / total)

mu = 0
for i in range(len(xbar)):
    mu += xbar[i] * prob[i]

var = 0
for i in range(len(xbar)):
    var += (xbar[i] ** 2) * prob[i]
var = var - mu**2

print("xbar values:", xbar)
print("probabilities:", prob)
print("mean of xbar:", mu)
print("variance of xbar:", var)

plt.plot(xbar, prob, marker='o', color='red')
plt.xlabel("xbar")
plt.ylabel("Probability")
plt.title("Sampling Distribution of xbar (n = 2)")
plt.show()