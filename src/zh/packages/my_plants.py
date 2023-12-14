'''
本节文章
https://learnscript.net/zh/python-reference/packages/ 什么是 Python 包，常规包，命名空间包？有何不同
'''

# 将命令行切换至该脚本所在目录，然后使用 Python 运行该脚本
import os
import sys

# 获取压缩文件 plants.zip 的绝对路径，并添加至模块搜索路径
zip_path = os.path.abspath('plants.zip')
sys.path.append(zip_path)

# 导入 plants.zip 中的 flowers 包
import flowers