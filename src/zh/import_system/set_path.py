'''
本节文章
https://learnscript.net/zh/python-reference/import-system/module-search-path/set-module-search-path/ 如何设置 Python 模块搜索路径
'''

# 获取文件夹 plants 的绝对路径
import os
import sys
plants_path = os.path.abspath('plants')

# 将文件夹 plants 的绝对路径添加至模块搜索路径
sys.path.append(plants_path)

# 直接导入 plants 中的 tree 模块
import tree