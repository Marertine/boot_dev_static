import os
import shutil
import sys
from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive

def main():    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]  # 1 because 0 = python3.exe
    else:
        basepath = "./"

    dir_path_static = "./static"
    #dir_path_public = "./public"    
    dir_path_docs = "./docs"
    

    #print("Deleting public directory...")
    #if os.path.exists(dir_path_public):
    #    shutil.rmtree(dir_path_public)

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    #copy_files_recursive(dir_path_static, dir_path_public)
    copy_files_recursive(dir_path_static, dir_path_docs)

    #generate_page("./content/index.md", "./template.html", "./public/index.html")
    #generate_pages_recursive("./content/", "./template.html", "./public")
    #generate_pages_recursive("./content", "./template.html", "./public", basepath)
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)


main()