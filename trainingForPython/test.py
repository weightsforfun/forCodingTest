import matplotlib.pyplot as plt

t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]

plt.figure(figsize=(10, 6))

plt.xlim(0, 8)
plt.ylim(0, 10)


plt.plot(t, y, marker='o', markersize=15, color='red', linewidth=6)




plt.show()