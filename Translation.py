# T R A N S L A T I O N

from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate

# The target language
target = 'en'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=en)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))