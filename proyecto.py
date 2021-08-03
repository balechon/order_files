import os
import shutil
import re
from read_locations import config
import pandas as pd
import ast
def remove_duplicate_lists(my_list :list) -> list:
    return list(set(my_list))

def list_files(dir):
    os.chdir(dir)
    list_w_dir=remove_duplicate_lists(os.listdir())
    yield  list_w_dir


def move_to(file,directories):
    for folder in directories:
        is_ext=re.compile(r'{}'.format(folder['re']))
        dest=folder['route']
        if is_ext.match(file):
            shutil.move(file,dest)

def run():
    
    dest_folders=config()['destination']
    read_folders=config()['directories']
    names=remove_duplicate_lists([folder['name'] for folder in read_folders])
    unique=[str(a) for a in read_folders]
    uni_set=set(unique)
    unique=[ast.literal_eval(item) for item in uni_set]
    # unique=pd.DataFrame(read_folders).drop_duplicates().to_dict('records')
    print(unique)
    
    # for dest in read_folders:
    #     order_to_list = list_files(dest['route'])    
    #     for element in order_to_list:
    #         for name in element:
    #             move_to(name,dest_folders)

        
if __name__=="__main__":
    run()