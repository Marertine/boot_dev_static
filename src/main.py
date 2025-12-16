from textnode import TextNode
from textnode import TextType
import os
import shutil
#from os import path, listdir, mkdir
#from shutil import copy, rmtree
from copystatic import copy_files_recursive

def main():
#    str_destpath = "public/"
#    str_src_path = "static/"
#    if os.path.exists(str_destpath):
#        shutil.rmtree(str_destpath)
#    if not os.path.exists(str_destpath):
#        os.mkdir(str_destpath)
#    fn_copy_files(str_src_path, str_destpath)
    dir_path_static = "./static"
    dir_path_public = "./public"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)



#def fn_copy_files(str_src_path, str_destpath):
    #for item in os.listdir(str_src_path):
    #    print(f"Item: {item}")
    #    if os.path.isdir(path.join(str_src_path, item)):
    #        print(f"MkDir: {path.join(str_destpath, item)}")
    #        if not path.exists(path.join(str_destpath, item)):
    #            mkdir(path.join(str_destpath, item))
    #        fn_copy_files(path.join(str_src_path, item), path.join(str_destpath, item))    
    #    if path.isfile(path.join(str_src_path, item)):
    #        print(f"CopyFile: {path.join(str_destpath, item)}")
    #        copy(path.join(str_src_path, item), path.join(str_destpath, item))




main()