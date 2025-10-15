import streamlit as st

TIPOS_ARQUIVOS_VALIDOS = ["Site","Youtube","Pdf","Csv","Txt"]

CONFIG_MODELOS = { "Groq": {"modelos": ["llama-3.1-70b-versatile","gemma2-9b-it", "mixtral-8x7b-32768"]},
                  "OpenIA": {"modelos": ["gpt-4o-mini","gpt-4o","ol-preview", "oi-mini"]}}

MENSAGENS_EXEMPLO = [
    ("user", "Olá, Oráculo!"),
    ("assistant", "Olá! Como posso ajudar você hoje?"),
    ("user", "Qual é a capital da França?"),
]

def pagina_chat():
    st.header("🤖 Bem-vindo ao Oráculo", divider=True)

    mensagens = st.session_state.get("mensagens", MENSAGENS_EXEMPLO)
    for mensagem in mensagens:
      chat = st.chat_message(mensagem[0])
      chat.markdown(mensagem[1])

    input_usuario = st.chat_input("Fale com oráculo")

    if input_usuario:
        mensagens.append(("user", input_usuario))    
        st.session_state["mensagens"] = mensagens
        st.rerun()


def sidebar():
    tabs = st.tabs(["Upload de Arquivos", "Seleção de Modelos"])

    with tabs[0]:
        tipo_arquivo = st.selectbox("Selecione o tipo de arquivo", TIPOS_ARQUIVOS_VALIDOS)
        if tipo_arquivo == 'Site':
            arquivo = st.text_input("Insira a URL do site")
        if tipo_arquivo == 'Youtube':
            arquivo = st.text_input("Insira a URL do vídeo")
        if tipo_arquivo == 'Pdf':
            arquivo = st.file_uploader("Faça o upload do arquivo PDF", type=[".pdf"])
        if tipo_arquivo == 'Csv':
            arquivo = st.file_uploader("Faça o upload do arquivo CSV", type=[".csv"])
        if tipo_arquivo == 'Txt':
            arquivo = st.file_uploader("Faça o upload do arquivo TXT", type=[".txt"])
    with tabs[1]:
        provedor = st.selectbox("Selecione o provedor de IA", CONFIG_MODELOS.keys())
        modelo = st.selectbox("Selecione o modelo", CONFIG_MODELOS[provedor]["modelos"])
        api_key = st.text_input(
            f"Insira a chave API do {provedor}", type="password", 
            value=st.session_state.get(f'api_key_{provedor}'))

        st.session_state[f'api_key_{provedor}'] = api_key

def main():
    pagina_chat()
    with st.sidebar:
        sidebar()

if __name__ == "__main__":
    main()