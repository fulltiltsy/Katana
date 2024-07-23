from Katana import Callbacks
import logging


def wrenchWithRB(objectHash):
    from UI4.FormMaster.NodeActionDelegate import (BaseNodeActionDelegate, RegisterActionDelegate)
    from UI4.Manifest import QtWidgets


    class nodeDelegate(BaseNodeActionDelegate.BaseNodeActionDelegate):
        class _createAction(QtWidgets.QAction):
            def __init__(self, parent, node):
                QtWidgets.QAction.__init__(self, 'Action Script', parent)            

                if node:
                    self.triggered.connect(self.__triggered)
                
                # 0. When the specified node type meets the condition, it is enabled and disabled #
                try:
                    nodeTypes = ['Group','Merge']
                    for nodeType in nodeTypes:
                        if nodeType:
                            self.setEnabled(True)
                        else:
                            self.setEnabled(False)
                except:
                    self.setEnabled(False)


            # 1. Execution result #
            def __triggered(self, checked):
                print('Result')


        # 2. Add function button at mouse right button #
        def addToContextMenu(self, menu, node):
            menu.addAction(self._createAction(menu, node))


        # 3. Add function button at wrench panel #
        def addToWrenchMenu(self, menu, node, hints=None):
            menu.addAction(self._createAction(menu, node))


    # 4. Set log info #
    nodes = ['Group','Merge']
    global log
    for node in nodes:
        log.info('Adding new context menu to {}'.format(node))
        
        RegisterActionDelegate(node, nodeDelegate())




log = logging.getLogger('UIPlugins')
log.info('Registering context menu - NodeDelegate')

Callbacks.addCallback(Callbacks.Type.onStartupComplete, wrenchWithRB)