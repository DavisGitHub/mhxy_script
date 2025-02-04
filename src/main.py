import os
import sys
import tkinter as tk
from core.game_controller import GameController
from gui.ghost_capture_gui import GhostCaptureGui

def get_resource_path(relative_path):
    """获取资源文件的绝对路径"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def main():
    # 创建主窗口
    root = tk.Tk()
    root.title("梦幻西游自动化工具")
    
    # 设置窗口图标（如果有的话）
    # icon_path = get_resource_path(os.path.join("assets", "icon.ico"))
    # if os.path.exists(icon_path):
    #     root.iconbitmap(icon_path)
    
    # 初始化游戏控制器
    game_controller = GameController()
    
    # 创建抓鬼界面
    ghost_capture_gui = GhostCaptureGui(root, game_controller)
    
    # 启动主循环
    root.mainloop()

if __name__ == "__main__":
    main()