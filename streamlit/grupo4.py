import streamlit as st 
import joblib

model = joblib.load("modelo_lgbm33c.pkl")

st.title("Grupo 4 viviendas")




# Construimos un diccionario con one-hot encoding simulado
datos = {}

# ============ Grupo 1: Exterior 1st ============
exterior_options = [
    "AsbShng", "AsphShn", "BrkComm", "BrkFace", "CBlock",
    "CemntBd", "HdBoard", "ImStucc", "MetalSd", "Plywood",
    "Stone", "Stucco", "VinylSd", "Wd Sdng", "WdShing"
]
exterior = st.radio("Exterior 1st", exterior_options)

# ============ Grupo 2: Condition 1 ============
condition_options = [
    "Artery", "Feedr", "Norm", "PosA", "PosN",
    "RRAe", "RRAn", "RRNe", "RRNn"
]
condition = st.radio("Condition 1", condition_options)

# ============ Grupo 3: Neighborhood ============
neigh_options = [
    "Blmngtn", "Blueste", "BrDale", "BrkSide", "ClearCr", "CollgCr",
    "Crawfor", "Edwards", "Gilbert", "Greens", "GrnHill", "IDOTRR",
    "Landmrk", "MeadowV", "Mitchel", "NAmes", "NPkVill", "NWAmes",
    "NoRidge", "NridgHt", "OldTown", "SWISU", "Sawyer", "SawyerW",
    "Somerst", "StoneBr", "Timber", "Veenker"
]
neigh = st.radio("Neighborhood", neigh_options)

# ============ Grupo 4: Sale Condition ============
sale_cond_options = [
    "Abnorml", "AdjLand", "Alloca", "Family", "Normal", "Partial"
]
sale_cond = st.radio("Sale Condition", sale_cond_options)

# ============ Grupo 5: Land Contour ============
landcontour_options = [
    "Low", "Lvl", "Bnk", "HLS"
]
landcontour = st.radio("Land Contour", landcontour_options)

# ============ Grupo 6: Functional ============
Func_options = [
    "Min1", "Typ", "Sev", "Maj1", "Maj2", "Min2", "Sal", "Mod"
]
Func = st.radio("Functional", Func_options)






# ============ Otros valores numéricos ============
datos["Gr Liv Area"] = st.number_input("Gr Liv Area ",min_value=334, max_value=5642, value=1500)
datos["Year Built"] = st.number_input("Year Built",min_value=1827,max_value =2010, value=2000, step=1)
datos["Garage Cars"] = st.number_input("Garage Cars",min_value=0, max_value=5, value=2, step=1)

# Codificamos Functional
for op in Func_options:
    datos[f"Functional_{op}"] = 1.0 if Func == op else 0.0

# Codificamos land contour
for op in landcontour_options:
    datos[f"Land Contour_{op}"] = 1.0 if landcontour == op else 0.0

# Codificamos exterior
for op in exterior_options:
    datos[f"Exterior 1st_{op}"] = 1.0 if exterior == op else 0.0

# Codificamos condition
for op in condition_options:
    datos[f"Condition 1_{op}"] = 1.0 if condition == op else 0.0

# Codificamos neighborhood
for op in neigh_options:
    datos[f"Neighborhood_{op}"] = 1.0 if neigh == op else 0.0

# Codificamos sale condition
for op in sale_cond_options:
    datos[f"Sale Condition_{op}"] = 1.0 if sale_cond == op else 0.0


# Campos numéricos directos
datos["Overall Qual"] = st.number_input("Overall Quality (1-10)", value=5)
datos["Overall Cond"] = st.number_input("Overall Condition (1-10)", value=5)
datos["Open Porch SF"] = st.number_input("Open Porch SF", value=0)


datos["Year Remod/Add"] = st.number_input("Year Remod/Add", value=2000, step=1)
datos["Garage Area"]= st.number_input("Garage Area", value=400.0)
datos["Lot Frontage"]= st.number_input("Lot Frontage", value=60)
datos["Lot Area"]= st.number_input("Lot Area", value=60)
datos["1nd Flr SF"]= st.number_input("1nd Floor SF", value=0)
datos["2nd Flr SF"]= st.number_input("2nd Floor SF", value=0)
datos["Mas Vnr Area"]= st.number_input("Masonry Veneer Area", value=0)
datos["Screen Porch"]= st.number_input("Screen Porch SF", value=0)
datos["Mo Sold"]= st.number_input("Month Sold (1-12)", min_value=1, max_value=12, value=6)
datos["Full Bath"]= st.number_input("Full Baths", value=1)
datos["Wood Deck SF"]= st.number_input("Wood Deck SF", value=0)
datos["Fireplaces"]= st.number_input("Number of Fireplaces",min_value=0, value=1)
datos["Half Bath"]= st.number_input("Half Baths", min_value=0, value=0)
datos["TotRms AbvGrd"]= st.number_input("Total Rooms Above Ground", value=6)

#Cocina
datos["Kitchen Qual"] = st.selectbox("Kitchen Quality", options=[1, 2, 3, 4, 5], index=3)

#Sotano
datos["Bsmt Qual"]  = st.selectbox("Basement Quality", options=[1, 2, 3, 4, 5], index=3)
datos["Bsmt Exposure"] = st.selectbox("Basement Exposure", options=[1, 2, 3, 4], index=2)
datos["Bsmt Full Bath"]= st.number_input("Basement Full Bath", value=0.0, step=1.0)
datos["Basement Unf"] = st.number_input("Basement Unfinished SF", value=0)
datos["Total Bsmt SF"] = st.number_input("Total Basement Unfinished Surfase", value=0)


# Campos ordinales codificados
datos["Exter Qual"] = st.selectbox("Exterior Quality", options=[1, 2, 3, 4, 5], index=3)
datos["Fireplace Qu"] = st.selectbox("Fireplace Quality", options=[1, 2, 3, 4, 5], index=3)


# ============ Resultado parcial ============
st.subheader("Datos ingresados")
st.json(datos)



import pandas as pd
input_df = pd.DataFrame([datos])
# y luego: modelo.predict(input_df)



#Boton predecir 

st.subheader("Prediccion con el 11.43% de incertidumbre respecto al valor promedio real.")
if st.button("Predecir valor de casa"):
    #input_data = np.array( todas las variables)
    #prediccion = model.predict(input_data)[0]
    prediccion = model.predict(input_df)[0]
    st.success(f"Prediccion del precio de la casa: ${prediccion:.2f}")
