import Katana
from . import v1 as SuperToolSample


if SuperToolSample:
    PluginRegistry = [
        ('SuperTool', 2, 'SuperToolSample',
            (SuperToolSample.SuperToolSampleNode,
                SuperToolSample.GetEditor)),
    ]
