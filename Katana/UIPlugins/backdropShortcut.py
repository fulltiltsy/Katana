from Katana import Callbacks, NodegraphAPI
import logging


def backdropShortcut(objectHash):
    import UI4
    from UI4.Manifest import QtWidgets

    
    def fitBackdrop(*args):
        if len(NodegraphAPI.GetAllSelectedNodes()) == 0:
            rootNode = NodegraphAPI.GetRootNode()
            backdrop = NodegraphAPI.CreateNode('Backdrop', rootNode)
            ngt.floatNodes([backdrop])
        else:
            execute = args[1]
            execute.trigger()
        
    ngt = UI4.App.Tabs.FindTopTab('Node Graph')
    if ngt:
        ngmb = ngt.getMenuBar()
        text = 'Fit Backdrop Node to Selected Nodes'
        actions = ngmb.findChildren(QtWidgets.QAction)

        for action in actions:
            if action.text() == text:
                action.setText(text + '\tB')
                backdropID = UI4.App.KeyboardShortcutManager.GenerateActionID('Backdrop')
                ngt.registerKeyboardShortcut(backdropID, 'Fit Backdrop To Selected Nodes', 'B', fitBackdrop, None, action)




log = logging.getLogger('UIPlugins')
log.info('Registering backdrop node shorcut')
Callbacks.addCallback(Callbacks.Type.onStartupComplete, backdropShortcut)