'''
本節文章
https://learnscript.net/zh-hant/python-reference/import-system/module-search-path/directories-in-module-search-path/ Python 模組搜尋路徑中的目錄有哪些
'''

# 顯示 sys.path 的第一個元素，他是 __main__.py 所在 zip 檔案的路徑
import sys
print(f'__main__.py 位於：{sys.path[0]}')