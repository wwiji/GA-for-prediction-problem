import matplotlib.pyplot as plt
from GAs import *

plt.plot(losses[:200], c='green')
plt.xlabel('Generations')
plt.ylabel('losses')
plt.show()



