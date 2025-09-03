import streamlit as st
import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# carregar variaveis de ambiente
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"

# base e tabela
Base = declarative_base()

class SurveyData(Base):
    __tablename__ = 'survey_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    estado = Column(String(50))
    bibliotecas = Column(Text)
    area_atuacao = Column(String(50))
    horas_estudo = Column(String(20))
    conforto_dados = Column(String(50))
    experiencia_python = Column(Integer)
    experiencia_sql = Column(Integer)
    experiencia_cloud = Column(Integer)

def get_engine():
    try:
        engine = create_engine(DATABASE_URL)
        return engine
    except SQLAlchemyError as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela_se_nao_existir(engine):
    try:
        Base.metadata.create_all(engine)
    except SQLAlchemyError as e:
        st.error(f"Erro ao criar a tabela: {e}")

def salvar_dados_banco(session, dados):
    try:
        novo_dado = SurveyData(
            estado=dados["Estado"],
            bibliotecas=dados["Bibliotecas e ferramentas"],
            area_atuacao=dados["Área de Atuação"],
            horas_estudo=dados["Horas de Estudo"],
            conforto_dados=dados["Conforto com Dados"],
            experiencia_python=dados["Experiência de Python"],
            experiencia_sql=dados["Experiência de SQL"],
            experiencia_cloud=dados["Experiência de Cloud"],
        )
        session.add(novo_dado)
        session.commit()
    except SQLAlchemyError as e:
        st.error(f"Erro ao salvar os dados no banco: {e}")
        session.rollback()

engine = get_engine()
if engine is not None:
    criar_tabela_se_nao_existir(engine)

Session = sessionmaker(bind=engine)

estados = [
    "Acre", "Alagoas", "Amapa", "Amazonas", "Bahia", "Ceara",
    "Distrito Federal", "Espirito Santo", "Goias", "Maranhao",
    "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Para",
    "Paraiba", "Parana", "Pernambuco", "Piaui", "Rio de Janeiro",
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondonia", "Roraima",
    "Santa Catarina", "Sao Paulo", "Sergipe", "Tocantins"
]

areas_atuacao = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]

bibliotecas = [
    "Pandas", "Pydantic", "scikit-learn", "Git", "Pandera", "streamlit",
    "postgres", "databricks", "AWS", "Azure", "airflow", "dbt",
    "Pyspark", "Polars", "Kafka", "Duckdb", "PowerBI", "Excel",
    "Tableau", "storm"
]

horas_codando = ["Menos de 5", "5-10", "10-20", "Mais de 20"]

conforto_dados = ["Desconfortavel", "Neutro", "Confortavel", "Muito Confortavel"]

# formulario
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

    submit_button = st.form_submit_button("Enviar")

if submit_button:
    novo_dado = {
        "Estado": estado,
        "Bibliotecas e ferramentas": ", ".join(bibliotecas_selecionadas),
        "Área de Atuação": area_atuacao,
        "Horas de Estudo": horas_codando_select,
        "Conforto com Dados": conforto_dados_select,
        "Experiência de Python": experiencia_python,
        "Experiência de SQL": experiencia_sql,
        "Experiência de Cloud": experiencia_cloud,
    }
    session = Session()
    salvar_dados_banco(session, novo_dado)
    st.success("Dados enviados com sucesso!")

st.write("outside the form")
