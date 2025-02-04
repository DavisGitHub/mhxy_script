from enum import Enum
from dataclasses import dataclass

class GhostLevel(Enum):
    LEVEL_69 = "69级"
    LEVEL_89 = "89级"

class InstanceType(Enum):
    DOUBLE = "双本"
    TRIPLE = "三本"

@dataclass
class GhostCaptureConfig:
    level: GhostLevel
    instance_type: InstanceType

class GhostCapture:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        self.config = None

    def start_capture(self, level: GhostLevel, instance_type: InstanceType):
        """开始抓鬼任务"""
        self.config = GhostCaptureConfig(level, instance_type)
        print(f"开始 {level.value}{instance_type.value} 抓鬼")
        
        # TODO: 实现具体的抓鬼逻辑
        self._prepare_capture()
        self._execute_capture()

    def _prepare_capture(self):
        """准备抓鬼前的操作"""
        # TODO: 实现进入副本前的准备工作
        pass

    def _execute_capture(self):
        """执行抓鬼流程"""
        # TODO: 实现具体的抓鬼流程
        pass