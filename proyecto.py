import os
import shutil
import re
from read_locations import config
import ast

def remove_duplicate_lists(my_list :list) -> list:
    return list(set(my_list))

def remove_duplicate(my_list:list) -> list:
    str_list=[str(a) for a in my_list]
    uni_set=set(str_list)
    uni_list=[ast.literal_eval(item) for item in uni_set]
    return uni_list

def list_files(dir):
    try:
        os.chdir(dir)
        list_w_dir=remove_duplicate_lists(os.listdir())
        yield  list_w_dir
    except OSError as err:
        print(err)
        print('The location is not valid')

def move_to(file,directories):
    for folder in directories:
        is_ext=re.compile(r'{}'.format(folder['re']))
        dest=folder['route']
        if is_ext.match(file):
            try:
                shutil.move(file,dest)
                print(f'the file {file} was move to {dest}')
            except shutil.Error() as er:
                print(er)
                print('the location to move is not valid')


def run():
    print("starting program")
    dest_folders=config()['destination']
    read_folders=config()['directories']
    
    uni_dest_folders=remove_duplicate(dest_folders)
    uni_read_folders=remove_duplicate(read_folders)
    
    
    for folder in uni_read_folders:
        print(f"reading files in {folder['route']}")
        files_to_move=list_files(folder['route'])
        for element in files_to_move:
            for name in element:
                move_to(name, uni_dest_folders)
        
if __name__=="__main__":
    run()