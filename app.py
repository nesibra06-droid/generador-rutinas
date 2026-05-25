
import os


from groq import Groq
import streamlit as st
from groq import Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
def generar_rutina(objetivo, dias, nivel, feeling, nombre):
    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content":f"Eres un entrenador personal experto en {objetivo}, te caracterizas por saber dar los mejores resultados adaptandote a {feeling} como estado de animo. Usa un tono directo pero seguro y audaz. Empieza SIEMPRE tu respuesta con una frase corta que demuestre confianza, como un entrenador real haría. Siempre dirijete a la persona como {nombre}"},
            {"role": "user", "content": f"Crea una rutina de {objetivo} para {dias} días a la semana, nivel {nivel} y con estado de animo {feeling}"}

        ]
    )
    st.write(respuesta.choices[0].message.content)
st.set_page_config(page_title="Generador de rutinas", page_icon="💪")
st.title("Generador de rutinas con IA")
nombre = st.text_input("¿Cómo te llamas?")

if nombre:
    st.write(f"Hola {nombre}, vamos a trabajar.")
st.write("Tu entrenador personal con IA. Genera una rutina personalizada en segundos.")
objetivo = st.selectbox("¿Cuál es tu objetivo?", ["fuerza", "cardio", "estudio"])
dias = st.slider("¿Cuántos días a la semana?", 1, 7)
nivel = st.selectbox("¿Cuál es tu nivel?", ["principiante", "intermedio", "avanzado"])
feeling= st.selectbox("¿Cómo te sientes hoy?",["Con toda la energía", "Normal", "Cansado", "Sin motivación"])
if st.button("Generar rutina"):
    if feeling == "Cansado" or feeling == "Sin motivación":
        st.info("Hoy es difícil, pero estás aquí. Eso ya es ganar.")
    with st.spinner("Generando tu rutina..."):
        generar_rutina(objetivo, dias, nivel, feeling, nombre)
        





