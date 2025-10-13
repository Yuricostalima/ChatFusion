import streamlit as st

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


def main():
    pagina_chat()

if __name__ == "__main__":
    main()