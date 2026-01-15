import streamlit as st
from streamlit_extras.colored_header import colored_header

# ----------- CONFIGURAÇÃO DA PÁGINA -----------
st.set_page_config(
    page_title="Precificação Inteligente de Imóveis",
    page_icon="🏡",
    layout="wide"
)

# ----------- ESTILOS PERSONALIZADOS -----------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 50%, #f48fb1 100%);
    background-attachment: fixed;
}

.big-title {
    font-size: 3.2rem;
    font-weight: 700;
    margin-bottom: -10px;
    background: -webkit-linear-gradient(#d81b60, #880e4f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sub-title {
    font-size: 1.3rem;
    color: #4a4a4a;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.10);
    transition: 0.3s ease-in-out;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 28px rgba(0,0,0,0.18);
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: #333;
    opacity: 0.7;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)


# ----------- TÍTULO PRINCIPAL -----------
st.markdown("<h1 class='big-title'>🏡 Precificação Inteligente de Imóveis</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Use inteligência artificial para prever valores imobiliários com mais precisão e confiança.</p>", unsafe_allow_html=True)

st.write("")
st.write("")

# ----------- SEÇÃO DE DESTAQUES -----------
colored_header(
    label="Por que usar nossa plataforma?",
    description="Benefícios para corretores, imobiliárias e investidores.",
    color_name="violet-70"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>⚡ Previsões instantâneas</h3>
        <p>Obtenha valores estimados em segundos usando modelos avançados de Machine Learning.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📊 Análises detalhadas</h3>
        <p>Explore faixas de preço, métricas de qualidade e indicadores personalizados.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🌎 Imóveis em qualquer região</h3>
        <p>Nosso modelo permite adicionar novas localidades de forma dinâmica.</p>
    </div>
    """, unsafe_allow_html=True)


# ----------- CHAMADA PARA AÇÃO -----------
st.write("")
st.write("")
colored_header(
    label="Comece agora",
    description="Faça uma previsão de preço em poucos cliques.",
    color_name="violet-50"
)

colA, colB, colC = st.columns([1, 1, 1])

with colB:
    if st.button("🚀 Ir para o Calculador de Preço", use_container_width=True):
        st.switch_page("pages/app_corretor.py")  # Ajuste para o nome do seu arquivo de previsão


# ----------- FOOTER -----------

st.write("")
st.markdown("""
<div class='footer'>
    Desenvolvido com ❤️ usando Python, TensorFlow e Streamlit.
</div>
""", unsafe_allow_html=True)
