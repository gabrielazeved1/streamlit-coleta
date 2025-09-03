import streamlit as st
import pandas as pd
import os

# criar pasta data se nao existir
if not os.path.exists("data"):
    os.makedirs("data")

# arquivo CSV
data_file = "data/survey_data.csv"

# opcoes de estados
estados = [
    "Acre", "Alagoas", "Amapa", "Amazonas", "Bahia", "Ceara",
    "Distrito Federal", "Espirito Santo", "Goias", "Maranhao",
    "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Para",
    "Paraiba", "Parana", "Pernambuco", "Piaui", "Rio de Janeiro",
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondonia", "Roraima",
    "Santa Catarina", "Sao Paulo", "Sergipe", "Tocantins"
]

# opcoes de areas de atuacao
areas_atuacao = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]

# opcoes de bibliotecas
bibliotecas = [
    "Pandas", "Pydantic", "scikit-learn", "Git", "Pandera", "streamlit",
    "postgres", "databricks", "AWS", "Azure", "airflow", "dbt",
    "Pyspark", "Polars", "Kafka", "Duckdb", "PowerBI", "Excel",
    "Tableau", "storm"
]

# opcoes de horas codando
horas_codando = ["Menos de 5", "5-10", "10-20", "Mais de 20"]

# opcoes de conforto com dados
conforto_dados = ["Desconfortavel", "Neutro", "Confortavel", "Muito Confortavel"]

# criar formulario
with st.form("dados_enquete"):
    estado = st.selectbox("Estado", estados)
    area_atuacao = st.selectbox("Area de Atuacao", areas_atuacao)
    bibliotecas_selecionadas = st.multiselect(
        "Bibliotecas e ferramentas mais utilizadas",
        bibliotecas
    )
    horas_codando_select = st.selectbox(
        "Horas Codando ao longo da semana", horas_codando
    )
    conforto_dados_select = st.selectbox(
        "Conforto ao programar e trabalhar com dados", conforto_dados
    )
    experiencia_python = st.slider("Experiencia de Python", 0, 10)
    experiencia_sql = st.slider("Experiencia de SQL", 0, 10)
    experiencia_cloud = st.slider("Experiencia em Cloud", 0, 10)

    # botao enviar
    submit_button = st.form_submit_button("Enviar")

    if submit_button:
        novo_dado = {
            "Estado": estado,
            "Bibliotecas e ferramentas": ", ".join(bibliotecas_selecionadas),
            "Area de Atuacao": area_atuacao,
            "Horas de Estudo": horas_codando_select,
            "Conforto com Dados": conforto_dados_select,
            "Experiencia de Python": experiencia_python,
            "Experiencia de SQL": experiencia_sql,
            "Experiencia em Cloud": experiencia_cloud,
        }
        new_data = pd.DataFrame([novo_dado])

        # concatenar com dados existentes
        if os.path.exists(data_file):
            existing_data = pd.read_csv(data_file)
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        else:
            updated_data = new_data

        # salvar csv
        updated_data.to_csv(data_file, index=False)
        st.success("Dados enviados com sucesso")

st.write("outside the form")
