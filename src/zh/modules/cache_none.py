'''
本节文章
https://learnscript.net/zh/python-reference/modules/module-cache/ 什么是 Python 模块缓存
'''

import sys

# 模块 car 的完全限定名为 car，这里提前将其缓存设置为 None
sys.modules['car'] = None

# 导入模块 car 将导致异常
import car
