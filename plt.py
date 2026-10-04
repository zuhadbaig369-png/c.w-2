import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [70, 85, 60, 90, 75]

plt.plot(days, scores)
plt.title('My Quiz Score tracker')
plt.xlabel('Days of the week')
plt.ylabel('Score')
plt.grid(True)
plt.ylim(0, 100)
plt.show()
plt.plot(days, scores, marker='o', linestyle='dashed', color='blue')
plt.title('My Quiz Score tracker')
plt.xlabel('Days of the week')
plt.ylabel('Score')
plt.grid(True)
plt.ylim(0, 100)
plt.show()
plt.bar(days, scores, color='orange')
plt.title('My Quiz Score tracker')
plt.xlabel('Days of the week')
plt.ylabel('Score')
plt.grid(True)
plt.ylim(0, 100)
plt.show()