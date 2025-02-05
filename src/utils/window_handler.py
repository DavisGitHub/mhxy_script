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
            # 检查窗口是否最小化
            import win32con
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
            if style & win32con.WS_MINIMIZE:
                print("游戏窗口已最小化，请先恢复窗口")
                return None
                
            # 获取窗口的客户区域坐标
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            print(f"获取到窗口坐标：左={left}, 上={top}, 右={right}, 下={bottom}")
            return left, top, right, bottom
        except Exception as e:
            print(f"获取窗口坐标失败: {e}")
            return None