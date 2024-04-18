import os

def change_name(new_name_file):
    files = os.listdir('ex/test')
    index = 0
    for file in files:
        ext = file.split('.')[1]
        os.rename(f'ex/test/{file}',f'ex/test/{new_name_file}_{index}.{ext}')
        index += 1
