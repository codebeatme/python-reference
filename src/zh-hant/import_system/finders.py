import sys

path_finder = None

# 嘗試找到名稱包含 PathFinder 的尋找器
for finder in sys.meta_path:
    if 'PathFinder' in str(finder):
        path_finder = finder
        break

# 將找到的尋找器刪除
if path_finder:
    sys.meta_path.remove(path_finder)

# 匯入 apple 模組
import apple