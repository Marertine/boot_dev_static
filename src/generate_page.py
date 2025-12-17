import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):    
    #open the file
    with open(markdown, mode='r') as f:    
        #str_content = f.read()
        #alternatively, for line in f: f.readline() and test for the relevant content...
        for line in f.readline():
            if line[0] == "#":
                # pull the h1 and return it
                return line[1:].strip()

        raise Exception("No H1 segment found")
    
    #don't forget to close the file
    if not f.closed:
        f.close()



def generate_page(from_path, template_path, dest_path):    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(template_path, mode='r') as template_file:                
        str_template = template_file.read()
        if not template_file.closed:
            template_file.close()
    
    
    with open(from_path, mode='r') as f:
        md_content = f.read()
        if not f.closed:
                f.close()

        html_node = markdown_to_html_node(md_content)
        html_content = html_node.to_html()
        str_title = extract_title(from_path)
        html_output = str_template.replace("{{ Title }}", str_title)
        html_output = html_output.replace("{{ Content }}", html_content)

        dir_output = os.path.dirname(dest_path)
        if not os.path.exists(dir_output):
            os.makedirs(dir_output)

        with open(dest_path, mode='w') as file_output:
            file_output.write(html_output)
        
