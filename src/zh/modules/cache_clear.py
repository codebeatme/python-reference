'''
本节文章
https://learnscript.net/zh/python-reference/modules/module-cache/ 什么是 Python 模块缓存
'''

import sys

# 首次导入模块 car，并创建 Car 对象
import car
module1 = sys.modules['car']
car1 = car.Car()

# 清除模块 car 的缓存
del sys.modules['car']

# 再次导入模块 car，并创建 Car 对象
import car
module2 = sys.modules['car']
car2 = car.Car()

print(f'module1 == module2 能成立？{module1 == module2}')
print(f'car1 与 car2 的类型相同？{type(car1) == type(car2)}')