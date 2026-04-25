import streamlit as st
import pandas as pd
import numpy as np

dados = {
    'dia': [1,2,3,4,5],
    'vendas':[500,300,600,100,52]
}

df = pd.DataFrame(dados)
if st.button('Gerar Gráfico'):
    st.line_chart(df.set_index())

st.title('Isso é um teste')