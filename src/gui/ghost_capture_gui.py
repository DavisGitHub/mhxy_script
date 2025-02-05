import tkinter as tk
from tkinter import ttk
from core.dungeon_tasks import DungeonTask, DungeonConfig, DungeonName, DungeonType

class GhostCaptureGui:
    def __init__(self, root, game_controller):
        self.root = root
        self.dungeon_task = DungeonTask(game_controller)
        
        # 创建主框架
        self.frame = ttk.LabelFrame(root, text="副本抓鬼", padding="10")
        self.frame.pack(fill="x", padx=5, pady=5)
        
        # 创建选项和按钮
        self._create_widgets()

    def _create_widgets(self):
        # 创建选项框架
        options_frame = ttk.Frame(self.frame)
        options_frame.pack(fill="x", pady=5)
        
        # 创建副本选项
        self.dungeon_var = tk.StringVar(value="69级普通2本")
        options = [
            "69级普通2本",
            "69级3本(2普通+1侠士)",
            "89级普通3本",
            "89级5本(3普通+2侠士)"
        ]
        
        for option in options:
            ttk.Radiobutton(
                options_frame,
                text=option,
                value=option,
                variable=self.dungeon_var
            ).pack(fill="x", pady=2)
        
        # 创建抓鬼选项
        self.ghost_enabled = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            options_frame,
            text="执行完副本后是否无限抓鬼",
            variable=self.ghost_enabled
        ).pack(fill="x", pady=5)
        
        # 创建按钮框架（放在主窗口而不是副本抓鬼框架中）
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=5, pady=5)
        
        # 创建开始和结束按钮
        self.start_button = ttk.Button(
            button_frame,
            text="开始执行",
            command=self._start_task
        )
        self.start_button.pack(side="left", fill="x", expand=True, padx=5)
        
        self.stop_button = ttk.Button(
            button_frame,
            text="结束执行",
            command=self._stop_task,
            state="disabled"  # 初始状态为禁用
        )
        self.stop_button.pack(side="left", fill="x", expand=True, padx=5)

    def _start_task(self):
        """开始执行任务"""
        # 先查找并激活游戏窗口
        if not self.dungeon_task.game_controller.find_game_window():
            print("无法找到游戏窗口，请确保游戏已启动")
            return
            
        # 禁用开始按钮，启用结束按钮
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        
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
    def _create_widgets(self):
        # 创建选项框架
        options_frame = ttk.Frame(self.frame)
        options_frame.pack(fill="x", pady=5)
        
        # 创建副本选项
        self.dungeon_var = tk.StringVar(value="69级普通2本")
        options = [
            "69级普通2本",
            "69级3本(2普通+1侠士)",
            "89级普通3本",
            "89级5本(3普通+2侠士)"
        ]
        
        for option in options:
            ttk.Radiobutton(
                options_frame,
                text=option,
                value=option,
                variable=self.dungeon_var
            ).pack(fill="x", pady=2)
        
        # 创建抓鬼选项
        self.ghost_enabled = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            options_frame,
            text="执行完副本后是否无限抓鬼",
            variable=self.ghost_enabled
        ).pack(fill="x", pady=5)
        
        # 创建按钮框架（放在主窗口而不是副本抓鬼框架中）
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=5, pady=5)
        
        # 创建开始和结束按钮
        self.start_button = ttk.Button(
            button_frame,
            text="开始执行",
            command=self._start_task
        )
        self.start_button.pack(side="left", fill="x", expand=True, padx=5)
        
        self.stop_button = ttk.Button(
            button_frame,
            text="结束执行",
            command=self._stop_task,
            state="disabled"  # 初始状态为禁用
        )
        self.stop_button.pack(side="left", fill="x", expand=True, padx=5)

    def _stop_task(self):
        """结束执行任务"""
        print("正在停止所有任务...")
        # TODO: 添加停止任务的逻辑
        
        # 启用开始按钮，禁用结束按钮
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
