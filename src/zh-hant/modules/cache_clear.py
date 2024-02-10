'''
本節文章
https://learnscript.net/zh-hant/python-reference/modules/module-cache/ 什麽是 Python 模組快取
'''

import sys

# 匯入模組 car
import car

module1 = sys.modules['car']
car1 = car.Car()

# 清除模組 car 的快取
del sys.modules['car']

# 再次匯入模組 car
import car

# 顯然，module2 將是一個新的 ModuleType 物件
module2 = sys.modules['car']
# car2 和 car1 將是不同的型別
car2 = car.Car()

print(f'module1 == module2 能成立？{module1 == module2}')
print(f'car1 與 car2 的型別相同？{type(car1) == type(car2)}')