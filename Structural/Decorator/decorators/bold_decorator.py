from .text_decorator import TextDecorator
class BoldDecorator(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)
    
    def render(self):
        print("<b>", end="")
        self.inner.render()
        print("</b>", end="")