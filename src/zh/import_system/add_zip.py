'''
本节文章
https://learnscript.net/zh/python-reference/import-system/module-search-path/set-module-search-path/ 如何设置 Python 模块搜索路径
'''

# 将命令行切换至该脚本所在目录，然后使用 Python 运行该脚本
import os
import sys

# 获取压缩文件 plants.zip 的绝对路径，并添加至模块搜索路径
zip_path = os.path.abspath('plants.zip')
sys.path.append(zip_path)

# 导入 plants.zip 中的 tree 模块
import tree