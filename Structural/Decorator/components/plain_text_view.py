from .text_view import TextView
class PlainTextView(TextView):
    def __init__(self, text):
        self.text = text
    
    def render(self):
        print(self.text, end="")