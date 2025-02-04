import sys
from pathlib import Path

# 项目根目录
ROOT_DIR = Path(__file__).parent

# 需要打包的数据文件
datas = [
    # ('src/assets', 'assets'),  # 如果有资源文件，取消注释这行
]

# 需要排除的模块
excludes = []

# 额外的二进制文件
binaries = []