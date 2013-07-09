from i3pystatus import Module


class DefaultPlugin:

    def test(self):
        return True

    def on_leftclick(self):
        pass

    def on_rightclick(self):
        pass

    def run(self):
        return {
            "full_text": "",
            "color": "#FFFFFF"
        }


class PluginModuleBase:

    settings = (
        ("plugin", "The object that really implements this module."),
    )

    required = ("plugin",)

    def test(self):
        return self.plugin.test()

    def on_leftclick(self):
        self.plugin.on_leftclick()

    def on_rightclick(self):
        self.plugin.on_rightclick()

    def run(self):
        self.output = self.plugin.run()


class PluginModule(PluginModuleBase, Module):
    pass
