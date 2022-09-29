!pip install streamlit
import streamlit as st
import pickle


# load the model from disk
model_filename = '/content/drive/MyDrive/TFM - Palladium/Streamlit/rf.pkl'
loaded_model = pickle.load(open(model_filename, 'rb'))
# load the scaler from disk
scaler_filename = 'model_filename'
loaded_scaler = pickle.load(open(model_filename, 'rb'))

st.title("Palladium")
st.write("""
         Modelo de predicción de cancelaciones de reservas según datos de Palladium
         """)

NOCHES = st.text_input("Número de noches")
ADR = st.slider("ADR", 1, 2708, 1)
PAX = st.selectbox("PAX", options=['1', '2', '3', '4', '5', '6'])
LEAD_TIME = st.slider("LEAD_TIME", 1, 1000, 1)
#FIDELIDAD_Palladium Rewards = st.selectbox("FIDELIDAD_Palladium Rewards", options = (1, 0))
#FIDELIDAD_Palladium Connect = st.selectbox("FIDELIDAD_Palladium Connect", options=['1','0'])
MES = st.selectbox("MES LLEGADA", options=["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"])
DÍA_SEMANA = st.selectbox("WEEKDAY_LLEGADA", options=["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"])
SEMANA_DEL_AÑO = st.slider("WEEK_LLEGADA", 1, 48, 1)
TIPO_CLIENTE_1 = st.selectbox("TIPO_CLIENTE_1", options=['1', '0'])
TIPO_CLIENTE_2 = st.selectbox("TIPO_CLIENTE_2", options=['1', '0'])
TIPO_CLIENTE_3 = st.selectbox("TIPO_CLIENTE_3", options=['1', '0'])
TIPO_CLIENTE_9 = st.selectbox("TIPO_CLIENTE_9", options=['1', '0'])

HOTEL = st.selectbox("ID_HOTEL", options=['15', '30', '94'])
