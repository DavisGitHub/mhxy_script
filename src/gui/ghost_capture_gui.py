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
        
        # 创建选项
        self._create_options()

    def _create_options(self):
        # 创建选项按钮
        options = [
            ("69双本", GhostLevel.LEVEL_69, InstanceType.DOUBLE),
            ("69三本", GhostLevel.LEVEL_69, InstanceType.TRIPLE),
            ("89双本", GhostLevel.LEVEL_89, InstanceType.DOUBLE),
            ("89三本", GhostLevel.LEVEL_89, InstanceType.TRIPLE)
        ]

        for text, level, instance_type in options:
            btn = ttk.Button(
                self.frame,
                text=text,
                command=lambda l=level, t=instance_type: self._start_capture(l, t)
            )
            btn.pack(fill="x", pady=2)

    def _start_capture(self, level, instance_type):
        """开始抓鬼任务"""
        self.ghost_capture.start_capture(level, instance_type)