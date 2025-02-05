import time
import pyautogui
from utils.window_handler import WindowHandler

class GameController:
    def __init__(self):
        self.window_handler = WindowHandler()
        self.game_window = None
        # 设置 pyautogui 的安全边距为0，这样可以移动到屏幕边缘
        pyautogui.FAILSAFE = True
        
    def find_image(self, image_name):
        """
        在屏幕上查找指定图片
        :param image_name: 图片名称（相对于assets目录）
        :return: 如果找到返回位置坐标(x, y)，否则返回None
        """
        try:
            # 构建完整的图片路径（使用 Windows 路径格式）
            image_path = f".\\src\\assets\\{image_name}.png"
            # 在屏幕上查找图片
            location = pyautogui.locateCenterOnScreen(image_path)
            return location
        except Exception as e:
            print(f"查找图片失败: {e}")
            return None
            
    def left_click(self, location):
        """
        在指定位置执行左键点击
        :param location: 位置坐标(x, y)
        """
        if location:
            pyautogui.click(location.x, location.y)
    
    def find_game_window(self):
        """查找梦幻西游游戏窗口"""
        self.game_window = self.window_handler.find_window("梦幻西游：时空")
        return self.game_window is not None
    
    def start_automation(self):
        """开始自动化任务"""
        if not self.game_window:
            raise Exception("游戏窗口未找到")
        
        # 激活游戏窗口
        self.window_handler.activate_window(self.game_window)
        time.sleep(1)  # 等待窗口激活
        
        # TODO: 实现具体的自动化任务逻辑