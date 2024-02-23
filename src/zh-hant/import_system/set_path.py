'''
本節文章
https://learnscript.net/zh-hant/python-reference/import-system/module-search-path/set-module-search-path/ 如何設定 Python 模組搜尋路徑
'''

# 取得資料夾 plants 的絕對路徑
import os
import sys
plants_path = os.path.abspath('plants')

# 將資料夾 plants 的絕對路徑新增至模組搜尋路徑
sys.path.append(plants_path)

# 直接匯入 plants 中的 tree 模組
import tree