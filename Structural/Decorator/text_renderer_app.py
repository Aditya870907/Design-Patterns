from components.plain_text_view import PlainTextView
from decorators.bold_decorator import BoldDecorator
from decorators.italic_decorator import ItalicDecorator
from decorators.underline_decorator import UnderlineDecorator
class TextRendererApp:
    @staticmethod
    def main():
        text = PlainTextView("Hello, World!")

        print("Plain: ", end="")
        text.render()
        print()

        print("Bold: ", end="")
        bold_text = BoldDecorator(text)
        bold_text.render()
        print()

        print("Italic + Underline: ", end="")
        italic_underline_text = ItalicDecorator(UnderlineDecorator(text))
        italic_underline_text.render()
        print()

        print("Bold + Italic + Underline: ", end="")
        all_styles_text = BoldDecorator(ItalicDecorator(UnderlineDecorator(text)))
        all_styles_text.render()
        print()

if __name__ == "__main__":
    TextRendererApp.main()