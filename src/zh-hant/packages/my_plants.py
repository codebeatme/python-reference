'''
本節文章
https://learnscript.net/zh-hant/python-reference/packages/ 什麽是 Python 套件，常規套件，命名空間套件？有何不同
'''

# 將命令列切換至該腳本所在目錄，然後使用 Python 執行該腳本
import os
import sys

# 取得壓縮檔案 plants.zip 的絕對路徑，並添加至模組搜尋路徑
zip_path = os.path.abspath('plants.zip')
sys.path.append(zip_path)

# 匯入 plants.zip 中的 flowers 套件
import flowers