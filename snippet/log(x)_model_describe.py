# below code shows the plot of x and y (log model?)
# I need to look for a package that returns a polynomial model explaining the input data
def bird(number):
    birds = mins = 0
    while number > birds:
        mins += 1
        birds += min(mins, number - birds)
        number -= birds
    return birds

x = range(1,1000000)
y = []

for i in x:
    y.append(bird(i))    

import matplotlib.pyplot as plt
plt.plot(x, y, 'ro')
plt.axis([0, 1000000, 0, 50000])
plt.show()
