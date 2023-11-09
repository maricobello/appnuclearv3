import streamlit as st
from datetime import datetime, timedelta
import time
import random

# Configuração do aplicativo
st.set_page_config(page_title="Sala de Comando da Usina Nuclear", page_icon="☢️", layout="centered")
st.title("Sala de Comando da Usina Nuclear")
st.image("https://media.tenor.com/ZN76SLfmQtwAAAAd/human-error.gif", use_column_width=True, width=400, height=400)

# Inicializa variáveis de sessão
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.now()
if 'senha_incorreta' not in st.session_state:
    st.session_state['senha_incorreta'] = False
if 'tentativas' not in st.session_state:
    st.session_state['tentativas'] = 0
if 'senha_correta' not in st.session_state:
    st.session_state['senha_correta'] = False
if 'erros' not in st.session_state:
    st.session_state['erros'] = []

# Senha correta
senha_correta = "senha123"

# Placeholder para o contador e para as mensagens de erro
placeholder_contador = st.empty()
placeholder_erros = st.empty()

# Exibe a quantidade de tentativas restantes e a descrição do painel de controle na barra lateral
sidebar = st.sidebar
sidebar.title("Painel de Controle")
sidebar.image("https://img.freepik.com/fotos-premium/closeup-do-painel-de-controle-de-botoes-e-interruptores-da-usina-nuclear_191555-6467.jpg", use_column_width=True)
sidebar.write("Este é o painel de controle da usina nuclear. Você precisa inserir a senha correta para evitar um desastre nuclear.")
tentativas_restantes = 5 - st.session_state.tentativas
sidebar.markdown(f"<h2 style='text-align: center; color: yellow;'>Tentativas restantes: {tentativas_restantes}</h2>", unsafe_allow_html=True)

# Função para adicionar mensagens de erro
def adicionar_mensagem_erro():
    erros = [
        "ALERTA: Flutuações inesperadas na saída de energia!",
        "CRÍTICO: Vazamento de água pesada detectado no sistema primário!",
        "PERIGO: Falha no sistema de controle de reatividade!",
        "ERRO: Perda de coolanteno circuito secundário!",
    ]
    # Adiciona uma mensagem aleatória à lista
    mensagem_erro = random.choice(erros)
    if len(st.session_state['erros']) >= 4:
        st.session_state['erros'].pop(0)  # Remove a mensagem mais antiga se já tiver 4 mensagens
    st.session_state['erros'].append(mensagem_erro)

# Loop para atualizar contador e mensagens de erro
while True:
    # Calcula o tempo restante
    tempo_passado = datetime.now() - st.session_state['start_time']
    tempo_restante = timedelta(minutes=10) - tempo_passado
    segundos_restantes = int(tempo_restante.total_seconds())

    # Atualiza o contador
    if segundos_restantes > 0 and not st.session_state['senha_correta']:
        placeholder_contador.markdown(f"<h1 style='text-align: center; color: red;'>{tempo_restante // timedelta(minutes=1)}:{tempo_restante.seconds % 60:02d}</h1>", unsafe_allow_html=True)

    # Verifica se deve adicionar uma mensagem de erro
    if tempo_passado.seconds % 4 == 0 and not st.session_state['senha_correta']:
        adicionar_mensagem_erro()
        # Exibe as mensagens de erro
        for erro in st.session_state['erros']:
            placeholder_erros.error(erro)  # Exibe a mensagem de erro

    # Verificação de senha
    senha_digitada = st.text_input("Digite a senha para resfriar o reator:", key="senha")
    if st.button("Enviar senha para o controle"):
        if senha_digitada == senha_correta:
            st.session_state['senha_correta'] = True
            st.empty()
            st.success("Processo de normalização concluído com sucesso!")
            st.image("https://nuclear-power.com/wp-content/uploads/2020/05/reactor-steady-min.gif", use_column_width=True)
            placeholder_erros.empty()  # Limpa as mensagens de erro
            break  # Sai do loop se a senha estiver correta
        else:
            st.session_state['tentativas'] += 1
            if st.session_state['tentativas'] >= 5:
                st.session_state['senha_incorreta'] = True
                st.error("Você perdeu, o reator explodiu")
                st.image("https://i.imgur.com/7Elna2p.gif", use_column_width=True)
                break  # Sai do loop se o número de tentativas se esgotar

    time.sleep(1)  # Espera 1 segundo antes da próxima atualização

    # Se todas as tentativas forem esgotadas ou o tempo acabar, exibir "Você perdeu"
    if st.session_state['senha_incorreta'] or segundos_restantes <= 0:
        st.session_state['end_game'] = True
        st.experimental_set_query_params(end_game="true")
        st.error("Tempo esgotado ou senha incorreta. O reator explodiu!")
        st.image("https://i.imgur.com/7Elna2p.gif", use_column_width=True)
        break

    # Atualiza o app para mostrar o contador em tempo real
    st.experimental_rerun()

# Botão para a próxima etapa após a normalização
if st.session_state.get['normalizacao_completa'] = True:
    if st.button("Próxima etapa", key="next_step"):
        st.markdown("<h1 style='text-align: center;'>MENSAGEM AQUI</h1>", unsafe_allow_html=True)