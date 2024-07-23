from Callbacks import Callbacks


def topMenubar(objectHash):
    from Katana import UI4
    import startupSample

    # 0. Get MainWindow and MenuBar #
    mainWindow = UI4.App.MainWindow.GetMainWindow()
    mainMenuBar = mainWindow.getMenuBar()
    
    # 1. Add extra menu widget #
    topMenu = mainMenuBar.addMenu('Top Menu')
    topChildMenu = topMenu.addMenu('Child Menu')

    # 2. Add action and connect action
    startupSampleAct = topChildMenu.addAction('Script Action'+'\tShift+0')
    startupSampleAct.triggered.connect(startupSample.startupSampleScript)

    # 3. Register keyboard shortcut event #
    STARTUP_ID = UI4.App.KeyboardShortcutManager.GenerateActionID('startupSampleID')
    UI4.App.KeyboardShortcutManager.UnregisterKeyEvent(STARTUP_ID)
    mainWindow.registerKeyboardShortcut(STARTUP_ID, 'startupSampleID', 'shift+0', startupSample.startupSampleScript)




# --- Type of callback data --- #
Callbacks.addCallback(Callbacks.Type.onStartupComplete, topMenubar)

# --- Find all callback types --- #
# print(dir(Callbacks.Type))

