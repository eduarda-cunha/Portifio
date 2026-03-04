import streamlit as st
import importlib


def show_page(page_name):
    modules = {
        "Início": "inicio",
        "Projetos": "projetos",
        "Vídeos": "videos",
        "Dashboards": "dashboards",
        "Contatos": "contato"
    }

    module_name = modules.get(page_name)

    if module_name:
        try:
            module = importlib.import_module(module_name)

            # Verifica se o módulo possui função run()
            if hasattr(module, "run"):
                module.run()
            else:
                st.write("O módulo não possui uma função 'run()' para exibir conteúdo.")

        except ModuleNotFoundError:
            st.write("Erro: módulo não encontrado.")
    else:
        st.write("Página não encontrada.")



# Selecbox

page = st.sidebar.selectbox(
    "Navegação",
    ['Início', 'Projetos', 'Conclusão']
)




# Streamlit Apresentação - Teste

if page == "Início":
    st.title('Apresentações')

    st.write("""
            
            Sou estudante da área de Analise e Desenvolvimento de Software,
            com grande interesse em desenvolvimento de sistemas e modelagem de codigos que possam auxilixar em atividades cotiadianas,
            mas com maior foco de estudos nas materias de analise e programação para dados.

            Tenho buscado aprimorar meus conhecimentos em programação, lógica computacional e ferramentas de desenvolvimento,
            além de estudar conceitos de Engenharia de Software, UML, SQL, Python, CSS, HTMI.
            Contando com projetos do curso, contando com exercicios de logica e desenvolvimento de curiosidasdes com Python.

            Sou determinada a evolução nas etapas dos meus estudos na facudade e encursos partculares.
            Almejando um aprendizado contínuo e crescimento na area de desenvolvedora,
            contribuindo com soluções eficientes e aprendendo cada vez mais com a prática.
            
            """)
else:
    show_page(page)