'''
本节文章
https://learnscript.net/zh/python-reference/import-system/module-search-path/set-module-search-path/ 如何设置 Python 模块搜索路径
'''

# 将命令行切换至该脚本所在目录，然后使用 Python 运行该脚本
import os
import sys

# 获取文件夹 plants 的绝对路径，并添加至模块搜索路径
plants_path = os.path.abspath('plants')
sys.path.append(plants_path)

# 直接导入 plants 中的 tree 模块
import tree