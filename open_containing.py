"""
Open the folder containing this map in a file browser.
"""

__commandName__ = 'OpenContainingFolder'
__commandDisplayName__ = '(File) Open Containing Folder'

def execute():
    import os, subprocess, platform

    dir_path, _ = os.path.split(GlobalMap.getMapName())

    print("Open folder:", dir_path)
    # https://stackoverflow.com/a/435669
    if platform.system() == 'Windows':
        os.startfile(dir_path)
    elif platform.system() == 'Darwin':
        subprocess.call(('open', dir_path))
    else:
        subprocess.call(('xdg-open', dir_path))

if __executeCommand__:
    execute()
