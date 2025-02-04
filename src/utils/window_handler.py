import win32gui
import win32con

class WindowHandler:
    @staticmethod
    def find_window(window_name):
        """查找指定名称的窗口"""
        return win32gui.FindWindow(None, window_name)
    
    @staticmethod
    def activate_window(hwnd):
        """激活指定窗口"""
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
    
    @staticmethod
    def get_window_rect(hwnd):
        """获取窗口位置和大小"""
        return win32gui.GetWindowRect(hwnd)