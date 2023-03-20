import shutil


def shutil_demo():
    """
    for daily file and directory management tasks
    """
    shutil.copyfile('files/test.txt', 'files/backup.txt')
    shutil.move('files/backup.txt', 'stdlib')       # NOTE: 2nd arg = a dir
    os.remove('stdlib/backup.txt')
    print(dir(shutil))
