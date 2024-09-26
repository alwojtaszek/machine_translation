import openai
from langchain_text_splitters import RecursiveCharacterTextSplitter


def translate_text(text, from_lg, to_lg):
    """
    Translate a query using the OpenAI GPT-4 model.

    Returns:
        str: The translated text from source language.

    This method uses the OpenAI GPT-4 model to translate a query.
    """

    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=8192,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False,
            separators=["\n\n", "\n", " ", ""]
        )
        texts = text_splitter.create_documents([text])

        translations = []

        for chunk in texts:
            response = openai.chat.completions.create(
                temperature=0,
                model="gpt-4",
                messages=[
                    {'role': 'user',
                     'content': f"Translate the following text from {from_lg} to {to_lg}: {chunk.page_content}"}
                ]
            )
            print(response)
            translations.append(response.choices[0].message.content)

        return ' '.join(translations)

    except Exception as e:
        raise TranslationException(f"Translation failed: {str(e)}")


class TranslationException(Exception):
    def __init__(self, message):
        super(TranslationException, self).__init__(message)
