from enum import Enum
from dataclasses import dataclass
import time

class DungeonType(Enum):
    NORMAL = "普通"
    XIASHI = "侠士"

class DungeonName(Enum):
    JINCHANXIN = "金蟾心"
    DAOHAIJU = "蹈海去"
    MINGZHUHUAN = "明珠还"
    TAXIXING = "踏西行"

@dataclass
class DungeonConfig:
    name: DungeonName
    type: DungeonType
    level: int

class DungeonTask:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        
    def execute_jinchanxin_normal(self):
        """执行普通金蟾心副本"""
        print("开始执行普通金蟾心副本")
        # TODO: 实现具体逻辑
        
    def execute_daohaiju_normal(self):
        """执行普通蹈海去副本"""
        print("开始执行普通蹈海去副本")
        # TODO: 实现具体逻辑
        
    def execute_mingzhuhuan_normal(self):
        """执行普通明珠还副本"""
        print("开始执行普通明珠还副本")
        # TODO: 实现具体逻辑
        
    def execute_taxixing_xiashi(self):
        """执行侠士踏西行副本"""
        print("开始执行侠士踏西行副本")
        # TODO: 实现具体逻辑
        
    def execute_jinchanxin_xiashi(self):
        """执行侠士金蟾心副本"""
        print("开始执行侠士金蟾心副本")
        # TODO: 实现具体逻辑

    def execute_dungeon(self, config: DungeonConfig):
        """执行指定的副本任务"""
        if config.name == DungeonName.JINCHANXIN:
            if config.type == DungeonType.NORMAL:
                self.execute_jinchanxin_normal()
            else:
                self.execute_jinchanxin_xiashi()
        elif config.name == DungeonName.DAOHAIJU:
            self.execute_daohaiju_normal()
        elif config.name == DungeonName.MINGZHUHUAN:
            self.execute_mingzhuhuan_normal()
        elif config.name == DungeonName.TAXIXING:
            self.execute_taxixing_xiashi()

    def _find_and_click_zhongkui_task(self):
        """查找钟馗并点击抓鬼任务"""
        if location := self.game_controller.find_image("ghost_capture/zhongKui"):
            print("找到钟馗图标")
            self.game_controller.left_click(location)
            time.sleep(10)
            
            while True:  # 外层循环：整个抓鬼流程
                # 查找抓鬼任务按钮
                while True:  # 内层循环：查找抓鬼任务按钮
                    if location := self.game_controller.find_image("ghost_capture/zhuoGuiRenWu"):
                        print("找到抓鬼任务按钮")
                        self.game_controller.left_click(location)
                        time.sleep(2)
                        break
                    time.sleep(5)  # 每5秒检查一次抓鬼任务按钮
                
                # 查找抓鬼图标
                if location := self.game_controller.find_image("ghost_capture/ghost"):
                    print("找到抓鬼图标")
                    self.game_controller.left_click(location)
                    time.sleep(2)
                    
                    # 循环查找确定按钮
                    while True:
                        if location := self.game_controller.find_image("ghost_capture/queDing"):
                            print("找到确定按钮")
                            self.game_controller.left_click(location)
                            time.sleep(2)
                            break
                        time.sleep(30)  # 每30秒检查一次确定按钮
                    
                    time.sleep(10)  # 等待10秒后继续下一轮抓鬼
                    continue
            return True
        return False

    def execute_ghost_capture(self):
        """执行无限抓鬼任务"""
        print("开始执行无限抓鬼")
        while True:
            try:
                # 尝试查找第一个图标
                if location := self.game_controller.find_image("ghost_capture/ghost"):
                    print("找到第一个抓鬼任务图标")
                    self.game_controller.left_click(location)
                    time.sleep(2)
                    continue

                time.sleep(2)
                # 如果找不到第一个，尝试查找第二个图标
                if location := self.game_controller.find_image("ghost_capture/changAn"):
                    print("找到第二个抓鬼任务图标")
                    self.game_controller.left_click(location)
                    time.sleep(2)
                    
                    # 尝试查找钟馗
                    if self._find_and_click_zhongkui_task():
                        continue
                    else:
                        # 如果找不到钟馗，点击郑镖头
                        if location := self.game_controller.find_image("ghost_capture/zhengBiaoTou"):
                            print("找到郑镖头图标")
                            self.game_controller.left_click(location)
                            time.sleep(2)
                            
                            # 点击长安
                            if location := self.game_controller.find_image("ghost_capture/changAn"):
                                print("找到长安图标")
                                self.game_controller.left_click(location)
                                time.sleep(2)
                                
                                # 再次查找钟馗
                                self._find_and_click_zhongkui_task()
                        continue
                
                print("未找到任何抓鬼任务图标")
                break
                
            except Exception as e:
                print(f"抓鬼任务执行出错: {e}")
                break