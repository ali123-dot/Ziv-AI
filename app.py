import streamlit as st

def içerik_önerici(konu):
    başlık = f"{konu} hakkında bilmen gerekenler!"
    açıklama = f"Bu videoda {konu} konusunu detaylıca inceliyoruz. İzlemeyi unutma!"
    etiketler = [f"#{konu.replace(' ', '')}", "#youtube", "#keşfet", "#video"]
    return başlık, açıklama, etiketler

st.title("YouTube İçerik Önerici")

konu = st.text_input("İçerik konusunu yazınız:")

if konu:
    başlık, açıklama, etiketler = içerik_önerici(konu)
    st.subheader("Başlık Önerisi")
    st.write(başlık)

    st.subheader("Açıklama Önerisi")
    st.write(açıklama)

    st.subheader("Etiketler")
    st.write(" ".join(etiketler))
