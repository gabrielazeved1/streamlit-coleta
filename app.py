import streamlit as st

# Título da aplicação
st.title("Meu Primeiro App com Streamlit")

# Adiciona um cabeçalho
st.header("Introdução ao Streamlit")

# Adiciona um texto
st.text("Streamlit facilita a criação de aplicações web interativas com Python!")

# Widgets de entrada
nome = st.text_input("Digite seu nome")
idade = st.slider("Selecione sua idade", 0, 100, 25)

# Exibe os dados de entrada
st.write(f"Nome: {nome}")
st.write(f"Idade: {idade}")

# Adiciona um gráfico simples
st.line_chart([1, 2, 3, 4, 5])