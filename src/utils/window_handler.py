import win32gui
import win32con

class WindowHandler:
    def find_window(self, window_title):
        """查找指定标题的窗口"""
        return win32gui.FindWindow(None, window_title)
        
    def activate_window(self, hwnd):
        """激活指定的窗口"""
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        
    def get_window_rect(self, hwnd):
        """获取窗口的位置和大小"""
        try:
            # 获取窗口的客户区域坐标
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            print(f"获取到窗口坐标：左={left}, 上={top}, 右={right}, 下={bottom}")
            return left, top, right, bottom
        except Exception as e:
            print(f"获取窗口坐标失败: {e}")
            return None