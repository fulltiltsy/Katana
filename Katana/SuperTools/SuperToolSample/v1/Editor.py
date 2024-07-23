from PyQt5 import QtWidgets
from Katana import UI4


class SuperToolSampleEditor(QtWidgets.QWidget):
    def __init__(self, parent, node):
        QtWidgets.QWidget.__init__(self, parent)
        self.__node = node

        # 0. Factory Set #
        factory = UI4.FormMaster.KatanaFactory.ParameterWidgetFactory


        # 1. Call Parameters From Node.py Files #
        policy = UI4.FormMaster.CreateParameterPolicy(None, self.__node.getParameter('Group'))
        widget = factory.buildWidget(self, policy)


        # 2. Set Widget #
        self.LO = QtWidgets.QVBoxLayout(self)
        self.LO.addWidget(widget)
  

    def node(self):
        return self.__node