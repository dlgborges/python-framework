import streamlit as st
import pandas as pd
from numpy import 

class Linguagem:
    def executar(self):
        return 'Executando código...'
    
class Python(Linguagem):
    def executar(self):
        return 'Executando linguagem Python...'

class Go(Linguagem):
    def executar(self):
        return 'Executando linguagem Go...'
    
class Javascript(Linguagem):
    def executar(self):
        return 'Executando linguagem Javascript...'

st.title('poo - Polimorfismo')
st.write('Escolha uma...')

opcao = st.selectbox(
    'escolha a linguagem para executar',
    ['Python', 'Go', 'JS']
)

match opcao:
    case 'Python':
        linguagem = Python()
    case 'Go':
        linguagem = Go()
    case _:
        linguagem = Javascript()

st.subheader('Resultado')
st.success(linguagem.executar())
st.balloons()

enable = st.checkbox('Enable Camera')
st.map()