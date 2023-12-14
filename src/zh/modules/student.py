'''
本节文章
https://learnscript.net/zh/python-reference/modules/module-fully-qualified-names/ 什么是 Python 模块的完全限定名
'''

# 运行 student.py 可以正常导入 teacher，因为 student.py 所在的目录将被添加至搜索路径
import teacher

# homework 包也可以被正常导入
import homework