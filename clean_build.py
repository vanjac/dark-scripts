__commandName__ = 'CleanBuildFiles'
__commandDisplayName__ = 'Clean Build Files'

def execute():
    import os
    import glob

    def remove_glob(s):
        for f in glob.glob(s):
            print('  Remove file:', f)
            os.remove(f)

    print('Cleaning build files...')
    map_path = GlobalMap.getMapName()
    map_path_noext, _ = os.path.splitext(map_path)
    remove_glob(map_path_noext + '.proc')
    remove_glob(map_path_noext + '.cm')
    remove_glob(map_path_noext + '.aas*')
    print('Done')

if __executeCommand__:
    execute()
