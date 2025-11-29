from components.text_view import TextView
class TextDecorator(TextView):
    def __init__(self, inner):
        self.inner = inner