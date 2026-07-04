from __future__ import annotations


class HTMLNode():
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None = None, 
        children: HTMLNode | None = None, 
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> None:
        raise NotImplementedError()

    def props_to_html(self) -> str | None:
        html = ""
        if self.props:
            for key in self.props:
                html += f' {key}="{self.props[key]}"'
        return html
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self, 
        tag: str | None, 
        value: str,
        props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError()
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: HTMLNode,
        props: dict[str, str] | None = None
    ) -> None:
        pass