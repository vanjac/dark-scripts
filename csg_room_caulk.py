"""
Make a CSG room where all but the interior faces are textured with Caulk.
"""

__commandName__ = 'CSGRoomCaulk'
__commandDisplayName__ = '(Brush) Make Room With Caulk'

def execute():
    import darkradiant as dr

    caulk = 'textures/common/caulk'

    class RoomSelectionVisitor(dr.SelectionVisitor):
        def visit(self, s):
            brush = s.getBrush()
            if not brush.isNull():
                # Set all but the last face to Caulk shader.
                # This relies on the last face always being the one facing the interior,
                # which is not documented behavior of CSGRoom and could easily break in the future!
                # See brush::algorithm::hollowBrush in radiantcore/brush/csg/CSG.cpp
                for f in range(brush.getNumFaces() - 1):
                    brush.getFace(f).setShader(caulk)

    GlobalCommandSystem.execute('CSGRoom')
    GlobalSelectionSystem.foreachSelected(RoomSelectionVisitor())

if __executeCommand__:
    execute()
