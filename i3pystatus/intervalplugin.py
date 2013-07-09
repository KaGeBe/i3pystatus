from plugin import PluginModuleBase
from i3pystatus import IntervalModule


class IntervalPluginModule(PluginModuleBase, IntervalModule):

    settings = PluginModuleBase.settings + (
        ("interval", "The plugin interval"),
    )
