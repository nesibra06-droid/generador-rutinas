from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).parent / ".env")

import streamlit as st
from groq import Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
def generar_rutina(objetivo, dias, nivel):
    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content":f"Eres un entrenador personal experto en {objetivo}, te caracterizas por saber dar los mejores resultados adaptandote a cualquier circunstancia. Usa un tono directo pero seguro y audaz. Empieza SIEMPRE tu respuesta con una frase corta que demuestre confianza, como un entrenador real haría."},
            {"role": "user", "content": f"Crea una rutina de {objetivo} para {dias} días a la semana, nivel {nivel}"}
        ]
    )
    st.write(respuesta.choices[0].message.content)
st.set_page_config(page_title="Generador de rutinas", page_icon="💪")
st.title("Generador de rutinas con IA")
st.write("Tu entrenador personal con IA. Genera una rutina personalizada en segundos.")
objetivo = st.selectbox("¿Cuál es tu objetivo?", ["fuerza", "cardio", "estudio"])
dias = st.slider("¿Cuántos días a la semana?", 1, 7)
nivel = st.selectbox("¿Cuál es tu nivel?", ["principiante", "intermedio", "avanzado"])

if st.button("Generar rutina"):
    with st.spinner("Generando tu rutina..."):
        generar_rutina(objetivo, dias, nivel)

