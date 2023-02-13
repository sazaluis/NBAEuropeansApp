from googletrans import Translator

import urllib.parse

def translateText(text):
    translator = Translator()

    result = translator.translate(text)

    return result.text


