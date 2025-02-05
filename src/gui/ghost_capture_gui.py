import tkinter as tk
from tkinter import ttk
from core.ghost_capture import GhostLevel, InstanceType, GhostCapture

class GhostCaptureGui:
    def __init__(self, root, game_controller):
        self.root = root
        self.ghost_capture = GhostCapture(game_controller)
        
        # 创建主框架
        self.frame = ttk.LabelFrame(root, text="副本抓鬼", padding="10")
        self.frame.pack(fill="x", padx=5, pady=5)
        
        # 创建选项和按钮
        self._create_widgets()

    def _create_widgets(self):
        # 创建任务类型选择
        self.task_type = tk.StringVar(value="副本")
        task_frame = ttk.LabelFrame(self.frame, text="任务类型", padding="5")
        task_frame.pack(fill="x", pady=5)
        
        ttk.Radiobutton(task_frame, text="副本", value="副本", variable=self.task_type, command=self._on_task_change).pack(fill="x", pady=2)
        ttk.Radiobutton(task_frame, text="抓鬼", value="抓鬼", variable=self.task_type, command=self._on_task_change).pack(fill="x", pady=2)

        # 创建副本类型选择
        self.dungeon_type = tk.StringVar(value="普通副本")
        self.dungeon_frame = ttk.LabelFrame(self.frame, text="副本类型", padding="5")
        self.dungeon_frame.pack(fill="x", pady=5)
        
        ttk.Radiobutton(self.dungeon_frame, text="普通副本", value="普通副本", variable=self.dungeon_type).pack(fill="x", pady=2)
        ttk.Radiobutton(self.dungeon_frame, text="侠士副本", value="侠士副本", variable=self.dungeon_type).pack(fill="x", pady=2)

        # 创建等级选择
        self.level_type = tk.StringVar(value="69级")
        self.level_frame = ttk.LabelFrame(self.frame, text="等级选择", padding="5")
        self.level_frame.pack(fill="x", pady=5)
        
        ttk.Radiobutton(self.level_frame, text="69级", value="69级", variable=self.level_type).pack(fill="x", pady=2)
        ttk.Radiobutton(self.level_frame, text="89级", value="89级", variable=self.level_type).pack(fill="x", pady=2)

        # 创建副本次数选择（仅用于副本任务）
        self.instance_count = tk.StringVar(value="双本")
        self.instance_frame = ttk.LabelFrame(self.frame, text="副本次数", padding="5")
        
        ttk.Radiobutton(self.instance_frame, text="双本", value="双本", variable=self.instance_count).pack(fill="x", pady=2)
        ttk.Radiobutton(self.instance_frame, text="三本", value="三本", variable=self.instance_count).pack(fill="x", pady=2)
        
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
        
        # 创建执行按钮
        self.start_button = ttk.Button(
            self.frame,
            text="开始执行",
            command=self._start_task
        )
        self.start_button.pack(fill="x", pady=10)

    def _start_task(self):
        """开始执行任务"""
        selected_option = self.dungeon_var.get()
        ghost_enabled = self.ghost_enabled.get()
        
        print(f"选择的副本: {selected_option}")
        print(f"是否抓鬼: {ghost_enabled}")
        # TODO: 实现具体任务逻辑
        task_type = self.task_type.get()
        level = self.level_type.get()
        
        if task_type == "副本":
            dungeon_type = self.dungeon_type.get()
            instance_count = self.instance_count.get()
            print(f"开始执行{level}{dungeon_type}{instance_count}")
            # TODO: 实现副本任务逻辑
        else:
            print(f"开始执行{level}抓鬼")
            # TODO: 实现抓鬼任务逻辑