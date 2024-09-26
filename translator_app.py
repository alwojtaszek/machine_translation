import streamlit as st

from gpt_translation import TranslationException, translate_text
from languages import languages


st.title('🦜🔗 Multilingual Translation App')

st.write("Enter the text you want to translate, select the source and target languages, and click 'Translate' to see "
         "the result.")

# Input for the user to provide the text to the translation
text = st.text_area('Enter your text:')

# Select source and destination languages
source_lg = st.selectbox('Source Language:', list(languages.keys()))
dest_lg = st.selectbox('Translate to Language:', list(languages.keys()))

# Button to trigger the translation process
if st.button('Translate'):
    if text.strip() == "":
        st.warning("Please enter some text to translate.")
    elif source_lg == dest_lg:
        st.warning("Please select different languages for translation.")
    else:
        try:
            with st.spinner("Translating..."):
                answer = translate_text(text=text, from_lg=languages[source_lg], to_lg=languages[dest_lg])
            st.markdown(f"**Translated Text:** {answer}")
        except TranslationException as e:
            st.error("An error occurred during the translation process. "
                     "Please check your input or try again later. Error: {}".format(e))