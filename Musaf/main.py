import streamlit as st 
import requests

st.set_page_config("Mushaf",page_icon="📖")

st.title("Best Mushaf App")
st.sidebar.title("Controls")
st.sidebar.write("Select a surah")

surah_list = requests.get("http://api.alquran.cloud/v1/surah").json()["data"]

surah_names= [f"{s['number']}.{s['englishName']}.{s['name']}" for s in surah_list]

selected_surah=st.sidebar.selectbox("choose a surah", surah_names)
select_surah_int=int(selected_surah.split(".")[0])

search_keyword=st.sidebar.text_input("Search An Ayah In Arabic")

show_tr=st.sidebar.checkbox("show Translation")
show_audio=st.sidebar.checkbox("Listen Recitation")

tr_choice=st.sidebar.selectbox("choose translation"
,["ur.maududi","ür.junagarhi", "ur jalandhry"])

recitation_url=f"http://api.alquran.cloud/v1/surah/{select_surah_int}/ar.alafasy"
rec_response=requests.get(recitation_url).json()
ayah_arabic=rec_response["data"]["ayahs"]
 
if show_tr:
     tr_url=f"http://api.alquran.cloud/v1/surah/{select_surah_int}/{tr_choice}"
     tr_response=requests.get(tr_url).json()
     ayah_tr=tr_response["data"]["ayahs"]
else:
    ayah_tr=[None]*len(ayah_arabic)
    
if search_keyword.strip():
        filter_ar=[]
        filter_tr=[]
        for i, ayah in enumerate(ayah_arabic):
            if search_keyword in ayah ["text"]:
                filter_ar.append(ayah)
                filter_tr.append(ayah_tr[i])
        ayah_arabic=filter_ar
        ayah_tr=filter_tr
st.subheader(selected_surah)
for i, ayah in enumarate(ayah_arabic):
        st.markdown(f"*{ayah["numberInSurah"]}* -{ayah["text"]}")
        if show_audio:
            if'audio' in ayah and ayah["audio"]:
                st.audio(ayah[äudio])
        if show_tr and ayah_tr[i]["text"]
        
        st.markdown("### Developed by SANA Kiran")
