import boto3

def translate_text(text, source_language, target_language):
    # Create an Amazon Translate client
    translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

    # Perform the translation
    result = translate.translate_text(Text=text,
                                      SourceLanguageCode=source_language,
                                      TargetLanguageCode=target_language)
    return result.get('TranslatedText')

if __name__ == "__main__":
    text_to_translate = "Aquí hay una solución para usar un IDE capaz de interactuar con recursos de AWS."
    source_language = "es"  # Spanish
    target_language = "en"  # English

    translated_text = translate_text(text_to_translate, source_language, target_language)
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {translated_text}")
