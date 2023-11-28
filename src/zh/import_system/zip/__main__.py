'''
本节文章
https://learnscript.net/zh/python-reference/import-system/module-search-path/directories-in-module-search-path/ Python 模块搜索路径中的目录有哪些
'''

# 显示 sys.path 的第一个元素，他是 __main__.py 所在 zip 文件的路径
import sys
print(f'__main__.py 位于：{sys.path[0]}')