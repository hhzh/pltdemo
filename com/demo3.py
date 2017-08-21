import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ good$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))

l1, = plt.plot(x, y1, label='down')

# plt.figure(num=3, figsize=(8, 5))
l2, = plt.plot(x, y2, label='up')
# plt.plot(x, y1, color='red', linewidth=2.0, linestyle='--')
plt.legend(handles=[l1, l2, ], labels=['aaa', 'bbb'], loc='upper right')

plt.show()
