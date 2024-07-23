from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from Katana import UI4

class connectionTab(UI4.Tabs.BaseTab):
    def __init__(self, parent=None):
        super(connectionTab, self).__init__(parent)

        self.setUI()


    def setUI(self):
        self.LO = QtWidgets.QVBoxLayout(self)
        self.slider = QtWidgets.QSlider(Qt.Horizontal)                
        self.slider.setObjectName('slider')
        self.LO.addWidget(self.slider)

        self.__valueUpdate()
        self.slider.valueChanged.connect(self.__valueChanged)


    # 0. Changing the value of a widget with the same object name in all tabs panels #
    def _connectionTab__valueChanged(self, value):
        if self.sender() == self.slider:
            for tab in UI4.App.Tabs.GetTabsByType('Connection Tab'):
                findAllSlider = tab.findChildren(QtWidgets.QSlider)
                for slider in findAllSlider:
                    if str(slider.objectName()) == 'slider':
                        slider.setValue(value)


    # 1. When invoking a new tab, value it if it exists # 
    def _connectionTab__valueUpdate(self):
        if len(UI4.App.Tabs.GetTabsByType('Connection Tab')) >= 0:
            for tab in UI4.App.Tabs.GetTabsByType('Connection Tab'):
                findAllSlider = tab.findChildren(QtWidgets.QSlider)
                for slider in findAllSlider:
                    if str(slider.objectName()) == 'slider':
                        value = slider.value() 
                        self.slider.setValue(value)


PluginRegistry = [('KatanaPanel', 2, 'Connection Tab', connectionTab)]