__commandName__ = 'OpenContainingFolder'
__commandDisplayName__ = 'Open Containing Folder'

def execute():
    import os, subprocess, platform

    dir_path, _ = os.path.split(GlobalMap.getMapName())

    # https://stackoverflow.com/a/435669
    if platform.system() == 'Darwin':
        subprocess.call(('open', dir_path))
    elif platform.system() == 'Windows':
        os.startfile(dir_path)
    else:
        subprocess.call(('xdg-open', dir_path))

if __executeCommand__:
    execute()
