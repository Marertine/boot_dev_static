from textnode import TextNode
from textnode import TextType
from os import path, listdir, mkdir
from shutil import copy, rmtree

def main():
    str_destpath = "public/"
    str_src_path = "static/"


    if path.exists(str_destpath):
        rmtree(str_destpath)

    if not path.exists(str_destpath):
        mkdir(str_destpath)

    fn_copy_files(str_src_path, str_destpath)


def fn_copy_files(str_src_path, str_destpath):
    for item in listdir(str_src_path):
        print(f"Item: {item}")

        if path.isdir(path.join(str_src_path, item)):
            print(f"MkDir: {path.join(str_destpath, item)}")
            if not path.exists(path.join(str_destpath, item)):
                mkdir(path.join(str_destpath, item))
            fn_copy_files(path.join(str_src_path, item), path.join(str_destpath, item))

    
        if path.isfile(path.join(str_src_path, item)):
            print(f"CopyFile: {path.join(str_destpath, item)}")
            copy(path.join(str_src_path, item), path.join(str_destpath, item))




main()