from os import path, walk, listdir
import shutil

project_name = 'my_project_new'

try :
    for root, dirs, files in walk(project_name):
        if 'templates' in dirs and root != project_name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry), path.join(project_name, 'templates', entry))
except FileExistsError:
    print('These templates are sorted already !')

