import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

greeting = "Good Morning Jupyter"

words = greeting.split(" ")

word_length = [len(w) for w in words]
plt.bar(words, word_length)
plt.show()