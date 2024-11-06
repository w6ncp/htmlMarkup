class HTMLNode:
    def __init__(self, tag=None, value=None, childern=None, props=None):
        self.tag = tag
        self.value = value
        self.children = childern
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})" 
    
    # def __eq__(self, value):
    #     if self.tag != value.tag:
    #         return False
    #     if self.value != value.value:
    #         return False
    #     if self.children != value.children:
    #         return False
    #     if self.props != value.props:
    #         return False
    #     return True
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None or self.props == {}:
            return ""
        out = ""
        for name, value in self.props.items():
            out += f" {name}=\"{value}\""
        return out

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.tag == None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Invalid HTML: no tag")
        if self.children == None or self.children == {}:
            raise ValueError("Invalid HTML: no children")
        out = ""
        for child in self.children:
            out += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{out}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

