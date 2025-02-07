# Je n'ai pas créé de compte strealit cloud. Pour tester ce code, il va falloir le copi-colle dans votre vs-code et l'afficher dans votre navigateur.

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title = "Mon Application", layout = "wide")
if "authenticated" not in st.session_state :
    st.session_state.authenticated = False

def login():
    if st.session_state.username == "Blond" and st.session_state.password == "Pierre" :
        st.session_state.authenticated = True
    else:
        st.error("Tu t'es trompé !")

def logout() :
    st.session_state.authenticated = False
    st.experimental_rerun()

if not st.session_state.authenticated :
    st.title("Connexion")
    st.text_input("ID", key = "username")
    st.text_input("Mot de passe", type = "password", key = "password")
    st.button("Se connecter", on_click = login)
    st.stop()

with st.sidebar:
    st.button("Deconnexion", on_click = logout)
    st.markdown("Bienvenue")
    selected = option_menu(
        menu_title = "Menu",
        options = ["OMG", "Photos dossier"],
        icons = ["star","cat"],
        menu_icon = "cast",
        default_index = 0
)

if selected == "OMG" :
    st.title("Are you the famous Hackerman !!!")
    st.image("https://media.tenor.com/ykVAsEud6fwAAAAM/friends-matt-leblanc.gif")

elif selected == "Photos dossier":
    st.write("Images des plus grands dictateurs de l'humanité")
    col1, col2, col3 = st.columns(3)
    with col1 :
        st.image("https://www.woopets.fr/assets/img/031/962/1200x675/18-photos-de-chats-aussi-emouvantes-que-droles.jpg")
    with col2 :
        st.image("https://cdn.wamiz.fr/cdn-cgi/image/format=auto,quality=80,width=776,fit=contain/article/images/funny-perfectly-timed-cat-photo-50__605-7879.jpg")
    with col3 :
        st.image("https://img.leboncoin.fr/api/v1/lbcpb1/images/91/b6/d6/91b6d63a37323d92d07c834110d3a203c2ce87bc.jpg?rule=ad-large")

