"""
Make a CSG room where all but the interior faces are textured with Caulk.
"""

__commandName__ = 'CSGRoomCaulk'
__commandDisplayName__ = '(Brush) Make Room With Caulk'

def execute():
    import darkradiant as dr

    caulk = 'textures/common/caulk'
    default_shader = caulk

    class FindShaderSelectionVisitor(dr.SelectionVisitor):
        def visit(self, s):
            nonlocal default_shader
            brush = s.getBrush()
            if not brush.isNull():
                for f in range(brush.getNumFaces()):
                    shader = brush.getFace(f).getShader()
                    if shader != caulk:
                        default_shader = shader
                        return 0

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
                interior = brush.getFace(brush.getNumFaces() - 1)
                if interior.getShader() == caulk:
                    interior.setShader(default_shader)

    GlobalSelectionSystem.foreachSelected(FindShaderSelectionVisitor())
    GlobalCommandSystem.execute('CSGRoom')
    GlobalSelectionSystem.foreachSelected(RoomSelectionVisitor())

if __executeCommand__:
    execute()
