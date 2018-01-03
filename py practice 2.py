_author_='pzy.muhoushaonian'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def func(x):
    return 2*(x**3)
def Func(x):
    return 1/2*(x**4)
a = int(input("a: "))  #down limit
b = int(input("b: "))  #up limit

for i in range(1,50): #range()函数遍历数字序列
    np.random.seed()  #随机数函数seed
    x = np.random.random(i*10) * (b-a) +a #生成一个随机x值
    y = func(x)
    equation = (b-a) * np.sum(y)/len(x) #蒙特卡洛法计算定积分
    print(equation)

x=np.linspace(0,10)

y=func(x)

x2=np.linspace(0,10)

y2=Func(x2)

fig,ax = plt.subplots()

plt.plot(x,y,'red')

plt.plot(x2,y2,'green')

plt.ylim(ymin=0)

plt.figtext(0.9,0.05,'$x$')

plt.figtext(0.1,0.9,'$y$')

ax.spines['right'].set_visible(False)

ax.spines['top'].set_visible(False)

ax.xaxis.set_major_locator(ticker.IndexLocator(base=1, offset=1))

plt.show()
