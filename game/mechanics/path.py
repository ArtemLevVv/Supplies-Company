import os

def path(folder_name, file_name):
    return os.path.abspath(__file__+ f'/../../images/{folder_name}/{file_name}')
