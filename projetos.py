import streamlit as st

def run():
    st.set_page_config(layout="wide")

    st.markdown(
        "<h2 style='text-align: center;'>PROJETO DE EXTENSÃO - Github e Trello</h2>",
        unsafe_allow_html=True
    )

    st.title("📌 Projeto Comunidade Segura")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🟦 Backlog")
        st.markdown("""
        - Cadastro de usuários
        - Sistema de alertas
        - Mapa interativo
        """)

    with col2:
        st.subheader("🟨 Em Desenvolvimento")
        st.markdown("""
        - Página de login
        - Formulário de denúncia
        """)

    with col3:
        st.subheader("🟩 Concluído")
        st.markdown("""
        - Estrutura inicial
        - Conexão com banco
        """)

if __name__ == "__main__":
    run()