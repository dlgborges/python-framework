#view
import streamlit as st
import controller

st.title('Anotações')

nova_nota = st.text_input('Escreva algo: ')

def salvar_nota(nota):
    if st.button('Salvar'):
        if controller.adicionar_nota(nota):
            st.success('Salvo')
            return True
        else:
            st.write('Digite algo ')
            return False

salvar_nota(nova_nota)

st.subheader('dados: ')
if controller.listar_notas():
    for nota in controller.listar_notas():
        if nota:
            st.write(f'Nota: {nota}')
