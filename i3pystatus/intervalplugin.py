from i3pystatus import IntervalModule
from i3pystatus.plugin import PluginModuleBase


class IntervalPluginModule(PluginModuleBase, IntervalModule):

    settings = PluginModuleBase.settings + (
        ("interval", "The plugin interval"),
    )
