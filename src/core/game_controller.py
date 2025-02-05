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
            if not self.game_window:
                if not self.find_game_window():
                    return None
                self.start_automation()
                
            rect = self.window_handler.get_window_rect(self.game_window)
            if not rect:
                return None
                
            left, top, right, bottom = rect
            
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
                # 先尝试使用 confidence 参数
                try:
                    location = pyautogui.locateCenterOnScreen(
                        abs_path,
                        region=(left, top, right - left, bottom - top),
                        confidence=0.9
                    )
                except Exception as e:
                    print(f"使用 confidence 参数失败，尝试不使用容错率：{str(e)}")
                    # 如果失败，则不使用 confidence 参数重试
                    location = pyautogui.locateCenterOnScreen(
                        abs_path,
                        region=(left, top, right - left, bottom - top)
                    )
                
                if location:
                    print(f"找到图片，位置：x={location.x}, y={location.y}")
                else:
                    print(f"未找到图片")
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
            pyautogui.click(location.x, location.y)
    
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