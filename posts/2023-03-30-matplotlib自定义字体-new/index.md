# Matplotlib自定义全局字体


> Matplotlib如果想使用非系统字体就很麻烦，记录一下<!--more-->

## 自定义字体

一个简单的例子如下，只需要把`font_path`改成字体.tff文件的路径即可。
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = 'J:/MR.ttf'  # 此处改为自己字体的路径
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['font.family'] = prop.get_name()
plt.rcParams['mathtext.fontset'] = 'cm'  # 'cm' (Computer Modern)

x = np.linspace(0, 6, 50)
plt.plot(x, np.sin(x), label = r"正弦函数 Sine $\sin(\theta)$")
plt.title(r'中文测试 Sine Function $\alpha_i \leq \beta_j$')
plt.xlabel(r'$\theta_i$')
plt.ylabel(u'ab$^{12}$', fontsize=20)
plt.legend(fontsize = 'small', borderpad=1.5, labelspacing=0.2)
plt.show()
```
## 合并字体
如果需要使用不同的中英文字体，比如英文想用Times new romans，中文想用宋体，那么可以用一个简单的工具[Warcraft Font Merger](https://github.com/nowar-fonts/Warcraft-Font-Merger)对两个字体进行中英文合并，用法见网页。

