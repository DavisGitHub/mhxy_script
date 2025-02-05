import time
import random
import win32api
import win32con
import pyautogui
from utils.window_handler import WindowHandler

class GameController:
    def __init__(self):
        self.window_handler = WindowHandler()
        self.game_window = None
        # 设置 pyautogui 的安全边距为0，这样可以移动到屏幕边缘
        pyautogui.FAILSAFE = True
        # 验证 OpenCV 版本
        print(f"OpenCV 版本: {cv2.__version__}")
        
    def find_image(self, image_name):
        try:
            if not self.game_window:
                if not self.find_game_window():
                    return None
                self.start_automation()
                
            # 获取游戏窗口的位置和大小
            rect = self.window_handler.get_window_rect(self.game_window)
            if not rect:
                return None
                
            left, top, right, bottom = rect
            width = right - left
            height = bottom - top
            
            print(f"获取到窗口坐标：左={left}, 上={top}, 右={right}, 下={bottom}")
            print(f"窗口大小：宽={width}, 高={height}")
            
            image_name = image_name.replace('/', '\\')
            image_path = f"..\\src\\assets\\{image_name}.png"
            print(f"正在查找图片：{image_path}")
            
            import os
            abs_path = os.path.abspath(image_path)
            print(f"图片绝对路径：{abs_path}")
            if not os.path.exists(abs_path):
                print(f"错误：图片文件不存在！")
                return None
            
            print(f"查找区域：左={left}, 上={top}, 宽={right-left}, 高={bottom-top}")
            
            try:
                # 保存当前区域的截图用于调试
                import mss
                import mss.tools
                
                with mss.mss() as sct:
                    # 截取当前查找区域的截图
                    monitor = {"left": left, "top": top, "width": width, "height": height}
                    screenshot = sct.grab(monitor)
                    mss.tools.to_png(screenshot.rgb, screenshot.size, output=f"debug_screenshot.png")
                    print(f"已保存当前区域截图到：debug_screenshot.png")
                
                # 直接查找图片，不使用容错率
                location = pyautogui.locateCenterOnScreen(
                    abs_path,
                    region=(left, top, width, height),
                    confidence=0.85
                )
                
                if location:
                    print(f"找到图片，位置：x={location.x}, y={location.y}")
                else:
                    print(f"未找到图片，可能的原因：")
                    print("1. 图片不在当前区域内")
                    print("2. 图片与目标不完全匹配（颜色、大小等）")
                    print("3. 窗口可能被遮挡或最小化")
                return location
                
            except Exception as e:
                print(f"图片匹配过程出错：{str(e)}")
                return None
                
        except Exception as e:
            print(f"查找图片失败: {e}")
            return None
            
    def left_click(self, location):
        """
        在指定位置执行左键点击
        :param location: 位置坐标(x, y)
        """
        if location:
            print(f"移动鼠标到位置：x={location.x}, y={location.y}")
            self.move_click(location.x, location.y)
            
    def move_click(self, x, y, t=0.1):
        """移动鼠标并点击左键"""
        win32api.SetCursorPos((x, y))
        time.sleep(0.1)
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP,
            x, y, 0, 0
        )
        time.sleep(t)
        return 0
        
    def click(self, x, y):
        """点击指定位置并将鼠标移动到窗口外"""
        self.move_click(x, y, 0.1)
        # 获取窗口大小
        rect = self.window_handler.get_window_rect(self.game_window)
        if rect:
            left, top, right, bottom = rect
            # 移动到窗口右下角外
            pyautogui.moveTo(x=right + 10, y=bottom + 10, duration=0.1)
            
    def left_click(self, location):
        """在指定位置执行左键点击"""
        if location:
            print(f"点击位置：x={location.x}, y={location.y}")
            self.click(location.x, location.y)
            
    def find_game_window(self):
        """查找梦幻西游游戏窗口"""
        print("开始查找游戏窗口...")
        try:
            # 尝试查找完整标题
            self.game_window = self.window_handler.find_window("梦幻西游：时空")
            if self.game_window:
                print("成功找到游戏窗口：梦幻西游：时空")
                return True
            
            # 如果找不到完整标题，尝试部分标题匹配
            self.game_window = self.window_handler.find_window("梦幻西游")
            if self.game_window:
                print("成功找到游戏窗口：梦幻西游")
                return True
                
            print("未找到游戏窗口，请确保游戏已启动且窗口标题正确")
            return False
            
        except Exception as e:
            print(f"查找游戏窗口时出错: {e}")
            return False
        return self.game_window is not None
    
    def start_automation(self):
        """开始自动化任务"""
        if not self.game_window:
            raise Exception("游戏窗口未找到")
        
        # 激活游戏窗口
        self.window_handler.activate_window(self.game_window)
        time.sleep(1)  # 等待窗口激活
        
        # TODO: 实现具体的自动化任务逻辑