"""
Description: nonebot-plugin-cd-manager
"""

import contextlib
from nonebot import require
from .config import Config
from . import matcher


require("nonebot_plugin_alconna")


with contextlib.suppress(Exception):
    from nonebot.plugin import PluginMetadata

    __plugin_meta__ = PluginMetadata(
        name="nonebot-plugin-cd-manager",
        description="通用cd管理插件",
        usage="1.设置cd <命令:注意要加引号> <cd时间:单位s> [-g|--group <群号:或者 all>]",
        homepage="https://github.com/Cvandia/nonebot-plugin-cd-manager",
        config=Config,
        type="application",
        supported_adapters=None,
    )
