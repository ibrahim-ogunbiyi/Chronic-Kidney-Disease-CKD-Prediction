import pickle
import streamlit as st
st.title("Chronic Kidney Disease (CKD) Prediction")
st.sidebar.header("CKD Features")
sugar = st.sidebar.selectbox(label= "Sugar Level", options = (0, 1, 2, 3, 4, 5))
albumen = st.sidebar.select_slider(label="Choose Your Albumen Level", options= (0, 1, 2, 3, 4, 5))
bacteria = st.sidebar.radio("Bacteria", ("Present", "Not Present"))
red_blood_count = st.sidebar.number_input("Red Blood Count", min_value=0.0, max_value=10.0, step=0.1)
pus_cell_clump = st.sidebar.selectbox("Pus Cell Clumps", ("Present", "Not Present"))
red_blood_cell = st.sidebar.radio("Red Blood Cell", ("Normal", "Abnormal"))

## Middle container
age = st.number_input(label="Enter your Age", min_value=1, max_value=200, step=1, value=1)
blood_pressure = st.slider("Blood Pressure", min_value=10, max_value=150, step=10)
specifity = st.select_slider(label="Choose your Specifity Gravity", options=(1.005, 1.010, 1.015, 1.020, 1.025))
haemoglobin = st.number_input(label="Haemoglobin Level", min_value=0.0, max_value=100.0, step=0.1)
pus_cell = st.selectbox("Pus Cell", ("Normal", "Abnormal"))
white_blood_count = st.number_input("White Blood Count", min_value=2000, max_value=10000, step=1)
hypertension = st.selectbox("Hypertension", ("No", "Yes"))
serum_creatine = st.slider("Serum Creatine", min_value=0.0, max_value=10.0, step=0.01)
blood_gluscose_random = st.number_input("Blood Glucose", min_value=0, max_value=2000, step=1) 
blood_urea = st.number_input("Blood Urea", min_value=0, max_value=1000, step=1)
sodium = st.number_input("Sodium Level", min_value=100, max_value=200, step=1)
pottasium = st.number_input("Pottasium Level", min_value=0.0, max_value=10.0, step=0.1)
packed_cell_volume = st.sidebar.number_input("Packed Cell Volume", min_value=0, max_value=100, step=1)
diabetes = st.select_slider("Diabetes", ("No", "Yes"))
coronary_artery_disease = st.selectbox("Coronary Artery Disease", ("No", "Yes"))
appetite = st.select_slider("Appetite", ("No", "Yes"))
anemia = st.select_slider("Anemia", ("No", "Yes"))
pedal_edema = st.selectbox("Pedal Edema", ("No", "Yes"))


if specifity == 1.015:
    new_specifity = 0
elif specifity == 1.025:
    new_specifity = 1
elif specifity == 1.01:
    new_specifity = 2
elif specifity == 1.02:
    new_specifity = 3
elif specifity == 1.005:
    new_specifity = 4



# Red Blood Cell
if red_blood_cell  == "Normal":
    new_red_blood_cell = 1
else:
    new_red_blood_cell = 0

# Pus Cell
if pus_cell =="Normal":
    new_pus_cell = 1
else:
    new_pus_cell = 0

# Pus cell clump
if pus_cell_clump == "Present":
    new_pus_cell_clump = 1
else:
    new_pus_cell_clump = 0

 ## bacteria   
if bacteria == "Present":
    new_bacteria = 1
else:
    new_bacteria = 0


#Hypertension
#hypeterntion
if hypertension == "Yes":
    new_hyper = 1
else:
    new_hyper = 0


#Diabetes
if diabetes == "Yes":
    new_diabetes = 1
else:
    new_diabetes = 0

# CAD
if  coronary_artery_disease == "Yes":
    new_cad = 1
else:
    new_cad = 0

# Appetite
if appetite == "Yes":
    new_appetite = 1
else:
    new_appetite = 0

# Pedal edma
if pedal_edema == "Yes":
    new_pedal_edma = 1
else:
    new_pedal_edma = 0


# Anemia
if anemia == "Yes":
    new_anemia = 1
else:
    new_anemia = 0


container = ([age, blood_pressure, new_specifity, albumen, sugar, new_red_blood_cell, new_pus_cell,
            new_pus_cell_clump, new_bacteria, blood_gluscose_random, blood_urea, serum_creatine, 
            sodium, pottasium, haemoglobin, packed_cell_volume, white_blood_count, red_blood_count,
            new_hyper, new_diabetes, new_cad, new_appetite, new_pedal_edma, new_anemia
])


    
if st.button("Predict"):
    with open("Model.pkl", "rb") as f:
        model = pickle.load(f)

    preds = model.predict([container])
    if preds == 0:
        st.success("This Patient does not have a Kidney Disease")
    else:
        st.warning("This Patient has a Kidney Disease")
