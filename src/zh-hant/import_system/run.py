'''
本節文章
https://learnscript.net/zh-hant/python-reference/import-system/module-search-path/directories-in-module-search-path/ Python 模組搜尋路徑中的目錄有哪些
'''

# 顯示 sys.path 的第一個元素，他是該腳本檔案所在的目錄
import sys
print(f'腳本位於：{sys.path[0]}')