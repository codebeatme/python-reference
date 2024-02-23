# 尝试找到名称包含 PathFinder 的查找器
import sys
path_finder = None

for finder in sys.meta_path:
	if 'PathFinder' in str(finder):
		path_finder = finder
		break

# 将找到的 PathFinder 查找器删除
if path_finder:
	sys.meta_path.remove(path_finder)

# 导入 apple 模块
import apple