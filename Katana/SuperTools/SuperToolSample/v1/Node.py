from Katana import NodegraphAPI


# --- Default base set in Katana Node --- #
class SuperToolSampleNode(NodegraphAPI.SuperTool):
    def __init__(self):

		# 0. Node shape attributes #
        nodeAttrs = {
            'basicDisplay': 1, 'iconName': 'ImageRead',
            'colorr': 0.12, 'colorg': 0.31, 'colorb': 0.42
        }
        NodegraphAPI.SetNodeShapeNodeAttrs(self, nodeAttrs)


		# 1. Connect Sendport and Returnport
        self.addInputPort('in')
        self.addOutputPort('out')
        self.getReturnPort('out').connect(self.getSendPort('in'))
        self.getParameters().createChildNumber('version', 1)


		# 2. Katana Widget Parameter Samples #
        getParam = self.getParameters()
        groupParam = getParam.createChildGroup('Group')
        childParam = groupParam.createChildString('child', 'value')


		# 3. Set Parameter HintString #
        hint = {'labal':'Child'}
        childParam.setHintString(repr(hint))
