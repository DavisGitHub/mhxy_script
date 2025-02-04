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
        # 创建选项框架
        options_frame = ttk.Frame(self.frame)
        options_frame.pack(fill="x", pady=5)
        
        # 创建单选按钮变量
        self.selected_option = tk.StringVar()
        
        # 创建选项
        options = [
            ("69双本", GhostLevel.LEVEL_69, InstanceType.DOUBLE),
            ("69三本", GhostLevel.LEVEL_69, InstanceType.TRIPLE),
            ("89双本", GhostLevel.LEVEL_89, InstanceType.DOUBLE),
            ("89三本", GhostLevel.LEVEL_89, InstanceType.TRIPLE)
        ]

        # 存储选项映射关系
        self.options_map = {}
        
        for text, level, instance_type in options:
            radio = ttk.Radiobutton(
                options_frame,
                text=text,
                value=text,
                variable=self.selected_option
            )
            radio.pack(fill="x", pady=2)
            self.options_map[text] = (level, instance_type)
        
        # 设置默认选项
        self.selected_option.set("69双本")
        
        # 创建执行按钮
        self.start_button = ttk.Button(
            self.frame,
            text="开始执行",
            command=self._start_capture
        )
        self.start_button.pack(fill="x", pady=10)

    def _start_capture(self):
        """开始抓鬼任务"""
        selected = self.selected_option.get()
        if selected in self.options_map:
            level, instance_type = self.options_map[selected]
            self.ghost_capture.start_capture(level, instance_type)