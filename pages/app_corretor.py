import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# --- 1. ARQUIVOS DO MODELO ---
try:
    model = load_model("modelo_previsao_imoveis_final.keras")
    scaler = joblib.load("scaler_imoveis_final.pkl")

    # Bairros usados no treinamento
    BAIRROS_TREINAMENTO = [
        "Vila Nobre", "Jardim Sul", "Bairro Industrial", "Centro", "Zona Leste"
    ]

    # Ordem EXATA que o modelo espera
    COLUNAS_ESPERADAS = [
        "area_m2", "quartos", "banheiros", "garagem", "idade_do_imovel",
        "latitude", "longitude", "seguranca",
        "bairro_Vila Nobre", "bairro_Jardim Sul",
        "bairro_Bairro Industrial", "bairro_Centro"
    ]

except Exception as e:
    st.error(f"Erro ao carregar modelo ou scaler: {e}")
    st.stop()


# --- 2. FUNÇÃO DE PREVISÃO ---
def prever_preco(dados_entrada):

    df = pd.DataFrame([dados_entrada])

    # Criar todas as colunas OHE
    for bairro in BAIRROS_TREINAMENTO:
        df[f"bairro_{bairro}"] = 0

    # Marca o bairro selecionado
    df[f"bairro_{dados_entrada['bairro']}"] = 1

    # Remover a coluna original
    df = df.drop(columns=["bairro"])

    # Remover "bairro_Zona Leste" para evitar multicolinearidade
    if "bairro_Zona Leste" in df.columns:
        df = df.drop(columns=["bairro_Zona Leste"])

    # Garante todas as colunas esperadas
    for col in COLUNAS_ESPERADAS:
        if col not in df.columns:
            df[col] = 0

    # Reordenar colunas na ordem exata
    df = df[COLUNAS_ESPERADAS]

    # Escalonar SOMENTE as 8 numéricas
    col_num = [
        "area_m2", "quartos", "banheiros", "garagem",
        "idade_do_imovel", "latitude", "longitude", "seguranca"
    ]

    df[col_num] = scaler.transform(df[col_num])

    # Prever
    pred = model.predict(df)[0][0]

    return float(pred)


# --- 3. INTERFACE ---
st.set_page_config(page_title="Previsão Imobiliária IA", layout="wide")

st.title("🏡 Sistema Inteligente de Precificação Imobiliária")

with st.sidebar:
    st.header("Características do Imóvel")

    bairro_input = st.selectbox("Bairro:", BAIRROS_TREINAMENTO)
    seguranca_input = st.slider("Segurança (1–3):", 1, 3, 2)

    lat_input = st.number_input("Latitude:", value=-23.6, format="%.6f")
    lon_input = st.number_input("Longitude:", value=-46.6, format="%.6f")

st.subheader("Dados Estruturais")
col1, col2, col3 = st.columns(3)

with col1:
    area_input = st.number_input("Área m²:", 10.0, 500.0, 90.0)
    quartos_input = st.number_input("Quartos:", 1, 6, 3)

with col2:
    banheiros_input = st.number_input("Banheiros:", 1, 5, 2)
    garagem_input = st.number_input("Vagas Garagem:", 0, 5, 1)

with col3:
    idade_input = st.number_input("Idade (anos):", 0, 100, 5)

if st.button("CALCULAR PREÇO ESTIMADO"):

    dados = {
        "area_m2": area_input,
        "quartos": quartos_input,
        "banheiros": banheiros_input,
        "garagem": garagem_input,
        "idade_do_imovel": idade_input,
        "latitude": lat_input,
        "longitude": lon_input,
        "seguranca": seguranca_input,
        "bairro": bairro_input
    }

    preco = prever_preco(dados)

    st.header("💰 Resultado")
    st.metric("Preço Estimado", f"R$ {preco:,.2f}")
