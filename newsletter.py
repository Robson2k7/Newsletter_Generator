import streamlit as st
from openai import OpenAI

client = OpenAI()

def generate_newsletter(link, graphic, title, text):
    """ Generuje HTML dla newslettera na podstawie podanych informacji. """

    # Tworzenie promptu dla OpenAi
    # Prompt można dowolnie rozszerzyć
    prompt = f"Sparafrazuj {text}."

    # Wysłanie zapytania do modelu gpt-4o (można wybrać inny)
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages =[{"role": "user", "content": prompt}],
        max_tokens=500
    )

    # Pobranie sparafrazowanego tekstu
    paraphrased_text = response.choices[0].message.content

    # Generowanie kodu HTML
    html_form = f"""
        <div align="center">
            <p><a href="{link}"><img src="{graphic}"></a></p>
    
            <p><font size="4"><b>{title}</b></font></p>

            <p align="justify"><font size="4">{paraphrased_text}</font></p>
    
        </div>
        """
    return html_form

# UI w Streamlit
st.title("Generator Newslettera 📩")
st.write("Wprowadź potrzebne informacje, a aplikacja wygeneruje kod HTML dla newslettera.")

# Fromularz
with st.form("newsletter_form"):
    link = st.text_input("🔗 Wklej link do książki lub promocji: ")
    graphic = st.text_input("🖼️ Wklej link do grafiki: ")
    title = st.text_input("📖 Wklej temat lub tytuł książki")
    text = st.text_input("✍️ Wklej tekst: ")

    # Przycisk do wygenerowania newslettera
    submit_button = st.form_submit_button("Generuj Newsletter")

# Jeśli przycisk został kliknięty, generuje się newsletter
if submit_button:
    if link and graphic and title and text:
        html_output = generate_newsletter(link, graphic, title, text)
        st.subheader("📄 Wygenerowany kod HTML:")
        st.code(html_output, language="html")
    else:
        st.error("❌ Wszystkie pola muszą być wypełnione!")