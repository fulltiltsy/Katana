from Katana import LayeredMenuAPI


# 0. Create layered menu #
def dataCallback(layeredMenu):
    for n in range(10):
        layeredMenu.addEntry(str(n), text=str(n)+'New function', color=(n*.01, 0.1, 0.2))


# 1. Script action #
def actionCallback(value):
    print(value)
    return value


# 2. Callback and register menu #
newLayeredMenu = LayeredMenuAPI.LayeredMenu(
    dataCallback,
    actionCallback,
    'T',
    alwaysPopulate=True,
    onlyMatchWordStart=False
)




LayeredMenuAPI.RegisterLayeredMenu(newLayeredMenu, 'newLayeredMenu')