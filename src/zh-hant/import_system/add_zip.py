'''
本節文章
https://learnscript.net/zh-hant/python-reference/import-system/module-search-path/set-module-search-path/ 如何設定 Python 模組搜尋路徑
'''

# 將命令列切換至該腳本所在目錄，然後使用 Python 執行該腳本
import os
import sys

# 取得壓縮檔案 plants.zip 的絕對路徑，並新增至模組搜尋路徑
zip_path = os.path.abspath('plants.zip')
sys.path.append(zip_path)

# 匯入 plants.zip 中的 tree 模組
import tree