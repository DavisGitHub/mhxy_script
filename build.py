import os
import PyInstaller.__main__

def build():
    PyInstaller.__main__.run([
        'src/main.py',                      # 主程序入口
        '--name=梦幻西游自动化工具',         # 生成的exe名称
        '--windowed',                       # 使用GUI模式
        '--onefile',                        # 打包成单个文件
        '--clean',                          # 清理临时文件
        '--add-data=src/assets;assets',     # 注意这里使用分号
        '--icon=src/assets/icon.ico',       # Windows图标
        '--noconfirm',                      # 不确认覆盖
        '--distpath=dist',                  # 输出目录
        '--workpath=build',                 # 工作目录
    ])

if __name__ == "__main__":
    build()