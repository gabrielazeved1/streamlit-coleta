import streamlit as st
import pandas as pd
import os


#garantir que a pasta exista
os.makedirs("data", exist_ok=True)

# nome do arquivo CSV onde os dados serão armazenados
data_file = os.path.join("survey_data.csv")



# opcoes de estados
estados = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
    "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
    "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará",
    "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima",
    "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]

# opcoes de áreas de atuação
areas_atuacao = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]

# opcoes de bibliotecas
bibliotecas = [
    "Pandas", "Pydantic", "scikit-learn", "Git", "Pandera", "streamlit",
    "postgres", "databricks", "AWS", "Azure", "airflow", "dbt",
    "Pyspark", "Polars", "Kafka", "Duckdb", "PowerBI", "Excel", "Tableau", "storm"
]

# opcoes de horas codando
horas_codando = ["Menos de 5", "5-10", "10-20", "Mais de 20"]

# opcoes de conforto com dados
conforto_dados = ["Desconfortável", "Neutro", "Confortável", "Muito Confortável"]

# criacao do formulário
with st.form("dados_enquete"):
    estado = st.selectbox("Estado", estados)
    area_atuacao = st.selectbox("Área de Atuação", areas_atuacao)
    bibliotecas_selecionadas = st.multiselect("Bibliotecas e ferramentas mais utilizadas", bibliotecas)
    horas_codando = st.selectbox("Horas Codando ao longo da semana", horas_codando)
    conforto_dados = st.selectbox("Conforto ao programar e trabalhar com dados", conforto_dados)
    experiencia_python = st.slider("Experiência de Python", 0, 10)
    experiencia_sql = st.slider("Experiência de SQL", 0, 10)
    experiencia_cloud = st.slider("Experiência em Cloud", 0, 10)

    # botao para submeter o formulário
    submit_button = st.form_submit_button("Enviar")

# se o botao foi clicado, salvar os dados no DataFrame e no CSV
if submit_button:
    novo_dado = {
        "Estado": estado,
        "Bibliotecas e ferramentas": ", ".join(bibliotecas_selecionadas),
        "Área de Atuação": area_atuacao,
        "Horas de Estudo": horas_codando,
        "Conforto com Dados": conforto_dados,
        "Experiência de Python": experiencia_python,
        "Experiência de SQL": experiencia_sql,
        "Experiência em Cloud": experiencia_cloud,
    }
    new_data = pd.DataFrame([novo_dado])

    # verificar se o arquivo existe antes de tentar ler
    if os.path.exists(data_file):
        existing_data = pd.read_csv(data_file)
        updated_data = existing_data.append(new_data, ignore_index=True)
    else:
        updated_data = new_data
    
    # salvar os dados no arquivo CSV
    updated_data.to_csv(data_file, index=False)
    st.success("Dados enviados com sucesso!")

st.write("Outside the form")