from .text_decorator import TextDecorator
class UnderlineDecorator(TextDecorator):
    def __init__(self, inner):
        super().__init__(inner)
    
    def render(self):
        print("<u>", end="")
        self.inner.render()
        print("</u>", end="")