# Credit: Josh Hemann

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_methods = 4

accuracy = (73.36, 73.36, 71.68, 55.81)

f_score = (74.81, 74.81, 73.13, 71.61)

# time = (10, 40, 90, 5)

fig, ax = plt.subplots()

index = np.arange(n_methods)
bar_width = 0.2

opacity = 0.5

rects1 = ax.bar(index, accuracy, bar_width,
                alpha=opacity, color='b',
                label='Accuracy')

rects2 = ax.bar(index + bar_width, f_score, bar_width,
                alpha=opacity, color='r',
                label='F_Score')

# rects3 = ax.bar(index + 2*bar_width, time, bar_width,
#                 alpha=opacity, color='g',
#                 label='Time')

ax.set_xlabel('Learning Algorithm')
ax.set_ylabel('Metric Percentage')
# ax.set_title('Algorithm accuracy and f_score')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Decision Tree', 'Random Forest', 'KNN', 'Naive Bayes'))
ax.legend()

fig.tight_layout()

plt.grid(axis='y')
plt.ylim(50, 80)
plt.gray()
plt.show()