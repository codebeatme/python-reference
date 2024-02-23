'''
本节文章
https://learnscript.net/zh/python-reference/import-system/module-search-path/set-module-search-path/ 如何设置 Python 模块搜索路径
'''

# 获取压缩文件 plants.zip 的绝对路径
import os
import sys
zip_path = os.path.abspath('plants.zip')

# 将 plants.zip 的绝对路径添加至模块搜索路径
sys.path.append(zip_path)

# 导入 plants.zip 中的 tree 模块
import tree