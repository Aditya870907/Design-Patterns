from .text_decorator import TextDecorator
class ItalicDecorator(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)
    
    def render(self):
        print("<i>", end="")
        self.inner.render()
        print("</i>", end="")