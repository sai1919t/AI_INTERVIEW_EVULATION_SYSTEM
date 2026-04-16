import os 
import shutil
for root, dirs, files in os.walk('./'):
    for d in dirs:
        if d == '__uploads__':
            shutil.rmtree(os.path.join(root, d))
print("ALL_UPLOADS__ FOLDERS DELETED")