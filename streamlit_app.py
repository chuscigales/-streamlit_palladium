!pip install streamlit
import streamlit as st
import pickle


# load the model from disk
model_filename = '/content/drive/MyDrive/Copia de rf.pkl'
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





#age = st.slider("Edad", 1, 100, 1)
#p_class = st.selectbox("Clase", options=['Primera clase', 'Segunda clase', 'Tercera clase'])

#sex = 0 if sex == 'Hombre' else 1

#f_class = 1 if p_class == 'Primera clase' else 0
#s_class = 1 if p_class == 'Segunda clase' else 0
#t_class = 1 if p_class == 'Tercera clase' else 0

#input_data = loaded_scaler.transform([[NOCHES, ADRE, PAX, LEAD_TIME, MES, DÍA_SEMANA, SEMANA_DEL_AÑO, TIPO_CLIENTE_1, TIPO_CLIENTE_2, TIPO_CLIENTE_3, TIPO_CLIENTE_9]])
#prediction = loaded_model.predict(input_data)
#predict_probability = loaded_model.predict_proba(input_data)

#if name != "":
    #if prediction[0] == 1:
        #st.write(f":+1: El pasajero {name} **SI** hubiera sobrevivido con una probabilidad \
        #de {round(predict_probability[0][1] * 100, 3)}%")
    #else:
        #st.write(f":cry: El pasajero {name} **NO** hubiera sobrevivido con una probabilidad \
        #de {round(predict_probability[0][0] * 100, 3)}%")
