class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("Will be overridden by the child classes")
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        temp_string = ""
        for key, value in self.props.items():
            temp_string += f' {key}="{value}"'

        return temp_string
    
    def __repr__(self):
        #str_output = f"HTMLNode(     Tag: {self.tag})\n"
        #str_output += f"        (   Value: {self.value})\n"
        #str_output += f"        (Children: {self.children})\n"
        #str_output += f"        (   Props: {self.props})"
        #return str_output
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"