'''
本節文章
https://learnscript.net/zh-hant/python-reference/import-system/module-search-path/set-module-search-path/ 如何設定 Python 模組搜尋路徑
'''

# 取得壓縮檔案 plants.zip 的絕對路徑
import os
import sys
zip_path = os.path.abspath('plants.zip')

# 將 plants.zip 的絕對路徑新增至模組搜尋路徑
sys.path.append(zip_path)

# 匯入 plants.zip 中的 tree 模組
import tree