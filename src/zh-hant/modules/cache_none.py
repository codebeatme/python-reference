'''
本節文章
https://learnscript.net/zh-hant/python-reference/modules/module-cache/ 什麽是 Python 模組緩存
'''

import sys

# 模組 car 的完整名稱為 car，這裏提前將其緩存設定為 None
sys.modules['car'] = None

# 匯入模組 car 將導致例外狀況
import car
