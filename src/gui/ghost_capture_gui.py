import tkinter as tk
from tkinter import ttk
from core.ghost_capture import GhostLevel, InstanceType, GhostCapture
from core.dungeon_tasks import DungeonTask, DungeonConfig, DungeonName, DungeonType

class GhostCaptureGui:
    def __init__(self, root, game_controller):
        self.root = root
        self.dungeon_task = DungeonTask(game_controller)
        
    def _start_task(self):
        """开始执行任务"""
        selected_option = self.dungeon_var.get()
        ghost_enabled = self.ghost_enabled.get()
        
        # 执行选择的副本任务
        print(f"开始执行副本任务：{selected_option}")
        if selected_option == "69级普通2本":
            self._execute_69_normal_2()
        elif selected_option == "69级3本(2普通+1侠士)":
            self._execute_69_mixed_3()
        elif selected_option == "89级普通3本":
            self._execute_89_normal_3()
        elif selected_option == "89级5本(3普通+2侠士)":
            self._execute_89_mixed_5()
        
        # 如果启用了抓鬼任务
        if ghost_enabled:
            self.dungeon_task.execute_ghost_capture()

    def _execute_69_normal_2(self):
        """执行69级2个普通副本"""
        configs = [
            DungeonConfig(DungeonName.JINCHANXIN, DungeonType.NORMAL, 69),
            DungeonConfig(DungeonName.DAOHAIJU, DungeonType.NORMAL, 69)
        ]
        for config in configs:
            self.dungeon_task.execute_dungeon(config)

    def _execute_69_mixed_3(self):
        """执行69级2个普通副本和1个侠士副本"""
        configs = [
            DungeonConfig(DungeonName.JINCHANXIN, DungeonType.NORMAL, 69),
            DungeonConfig(DungeonName.DAOHAIJU, DungeonType.NORMAL, 69),
            DungeonConfig(DungeonName.JINCHANXIN, DungeonType.XIASHI, 69)  # 修改为金蟾心侠士
        ]
        for config in configs:
            self.dungeon_task.execute_dungeon(config)

    def _execute_89_normal_3(self):
        """执行89级3个普通副本"""
        configs = [
            DungeonConfig(DungeonName.JINCHANXIN, DungeonType.NORMAL, 89),
            DungeonConfig(DungeonName.DAOHAIJU, DungeonType.NORMAL, 89),
            DungeonConfig(DungeonName.MINGZHUHUAN, DungeonType.NORMAL, 89)
        ]
        for config in configs:
            self.dungeon_task.execute_dungeon(config)

    def _execute_89_mixed_5(self):
        """执行89级3个普通副本和2个侠士副本"""
        configs = [
            DungeonConfig(DungeonName.JINCHANXIN, DungeonType.NORMAL, 89),
            DungeonConfig(DungeonName.DAOHAIJU, DungeonType.NORMAL, 89),
            DungeonConfig(DungeonName.MINGZHUHUAN, DungeonType.NORMAL, 89),
            DungeonConfig(DungeonName.TAXIXING, DungeonType.XIASHI, 89),
            DungeonConfig(DungeonName.JINCHANXIN, DungeonType.XIASHI, 89)
        ]
        for config in configs:
            self.dungeon_task.execute_dungeon(config)
