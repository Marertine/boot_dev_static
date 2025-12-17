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
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.tag == "img":
            #img doesn't use tag and thus also not a closing tag
            return f"<{self.tag}{self.props_to_html()}>"

        else:
            if not self.value:                
                raise ValueError("All leaf nodes must have a value")
            
            if self.tag is None:
                return f"{self.value}"
            else:               
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        
        if self.children == []:
            raise ValueError("All parent nodes must have children, but an empty list was provided")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
