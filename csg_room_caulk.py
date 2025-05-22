__commandName__ = 'CSGRoomCaulk'
__commandDisplayName__ = 'Make Room With Caulk'

def execute():
    import darkradiant as dr

    caulk = 'textures/common/caulk'

    class SelectionVisitorTest(dr.SelectionVisitor):
        def visit(self, s):
            brush = s.getBrush()
            if not brush.isNull():
                for f in range(brush.getNumFaces() - 1):
                    brush.getFace(f).setShader(caulk)

    GlobalCommandSystem.execute('CSGRoom')
    GlobalSelectionSystem.foreachSelected(SelectionVisitorTest())

if __executeCommand__:
    execute()
