import shutil
import os

shutil.unpack_archive('/Users/polinapugacheva/Downloads/main', '/Users/polinapugacheva/Desktop')
folders = []
for current_dir, dirs, files in os.walk('/Users/polinapugacheva/Downloads/main'):
    for i in files:
        if i[-2:] == 'py' and current_dir not in folders:
            folders.append(current_dir)
print(sorted(folders, key=str.lower))