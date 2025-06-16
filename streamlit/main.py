
import streamlit as st
import joblib
import pandas as pd

# Cargar el modelo
model = joblib.load("/mount/src/tplabdatos/streamlit/modelo_lgbm33c.pkl")

# Título general
st.title("Predicción de precios de viviendas - Grupo 4")
st.markdown("Esta aplicación permite estimar el valor de una vivienda en base a sus características.")
st.markdown("Alumnos:")
st.markdown("Federico Coyra - Martin Campos - Santiago Rojas - Juan Jara")


# Tabs
tab1, tab2, tab3 = st.tabs([
    "1️⃣ Carga de Datos", 
    "2️⃣ Revisión de Datos", 
    "3️⃣ Predicción"
])

# ===================== TAB 1 =====================
with tab1:
    st.header("Carga de Datos de la Vivienda")
    st.markdown("Complete los datos solicitados para realizar la predicción del valor de la casa.")

    datos = {}
    # Categóricos con one-hot encoding simulado
    def radio_input(label, options):
        seleccion = st.selectbox(label, options, key=label)
        for op in options:
            datos[f"{label}_{op}"] = 1.0 if seleccion == op else 0.0


    st.subheader("🏠 Características Generales")
    
    radio_input("Condition 1", [
        "Artery", "Feedr", "Norm", "PosA", "PosN",
        "RRAe", "RRAn", "RRNe", "RRNn"
    ])
    datos["Lot Frontage"] = st.number_input("Frente del lote (pies)", 0, 313, 60)
    datos["Lot Area"] = st.number_input("Área del lote", 1300, 215245, 6000)
    radio_input("Land Contour", ["Low", "Lvl", "Bnk", "HLS"])
    radio_input("Neighborhood", [
        "Blmngtn", "Blueste", "BrDale", "BrkSide", "ClearCr", "CollgCr",
        "Crawfor", "Edwards", "Gilbert", "Greens", "GrnHill", "IDOTRR",
        "Landmrk", "MeadowV", "Mitchel", "NAmes", "NPkVill", "NWAmes",
        "NoRidge", "NridgHt", "OldTown", "SWISU", "Sawyer", "SawyerW",
        "Somerst", "StoneBr", "Timber", "Veenker"
    ])

    st.subheader("🧱 Calidad y Estado")
    datos["Overall Qual"] = st.selectbox("Calidad general (1-10)", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=3)
    datos["Overall Cond"] = st.selectbox("Condición general (1-9)", [1, 2, 3, 4, 5, 6, 7, 8, 9], index=3)

    st.subheader("🕰️ Antigüedad y reformas")
    datos["Year Built"] = st.number_input("Año de construcción", 1872, 2010, 2000)
    datos["Year Remod/Add"] = st.number_input("Año de remodelación", 1950, 2010, 2000)

    st.subheader("🏠 Techos y exteriores")
    radio_input("Exterior 1st", [
        "AsbShng", "AsphShn", "BrkComm", "BrkFace", "CBlock",
        "CemntBd", "HdBoard", "ImStucc", "MetalSd", "Plywood",
        "Stone", "Stucco", "VinylSd", "Wd Sdng", "WdShing"
    ])
    datos["Mas Vnr Area"] = st.number_input("Área de revestimiento de mampostería", 0.0, 1600.0, 0.0)

    st.subheader("🧍 Exterior")

    datos["Exter Qual"] = st.selectbox("Calidad exterior", [2, 3, 4, 5], index=1)

    st.subheader("🧱 Sótano")

    datos["Bsmt Unf SF"] = st.number_input("Sótano sin terminar (SF)", 0.0, 2336.0, 0.0)
    datos["Bsmt Qual"] = st.selectbox("Calidad del sótano", [0, 1, 2, 3, 4, 5], index=3)
    datos["Bsmt Full Bath"] = st.number_input("Baños completos en sótano", 0.0, 3.0, 0.0, step=1.0)
    datos["Bsmt Exposure"] = st.selectbox("Exposición del sótano", [0, 1, 2, 3, 4], index=2)
    datos["Total Bsmt SF"] = st.number_input("Superficie total del sótano", 0.0, 6110.0, 0.0)

    st.subheader("📐 Superficies")
    datos["1nd Flr SF"] = st.number_input("Superficie 1er piso (SF)", 334, 5095, 1000)
    datos["2nd Flr SF"] = st.number_input("Superficie 2do piso (SF)", 0, 2065, 0)
    datos["Gr Liv Area"] = st.number_input("Superficie habitable (Gr Liv Area)", 334, 5642, 1500)
    st.subheader("🛁 Baños y dormitorios")
    datos["Full Bath"] = st.selectbox("Baños completos", [0,1, 2, 3, 4], index=1)
    datos["Half Bath"] = st.selectbox("Medios baños", [0,1, 2], index=0)
    datos["Kitchen Qual"] = st.selectbox("Calidad de la cocina", [1, 2, 3, 4, 5], index=3)
    datos["TotRms AbvGrd"] = st.selectbox("Total de habitaciones sobre tierra",  [2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15], index=2)

    st.subheader("🔧 Funcionalidad y extras")
    datos["Fireplaces"] = st.selectbox("Cantidad de chimeneas", [0,1, 2, 3, 4], index=1)
    datos["Fireplace Qu"] = st.selectbox("Calidad de chimenea", [0, 1, 2, 3, 4, 5], index=3)
    radio_input("Functional", ["Min1", "Typ", "Sev", "Maj1", "Maj2", "Min2", "Sal", "Mod"])

    st.subheader("🚗 Garaje")
    datos["Garage Cars"] = st.number_input("Cantidad de autos en garage", 0.0, 5.0, 2.0, step=1.0)
    datos["Garage Area"] = st.number_input("Área del garage", 0.0, 1488.0, 400.0)
    

    st.subheader("🌳 Exterior adicional")
    datos["Open Porch SF"] = st.number_input("Superficie de porche abierto (SF)", 0, 742, 0)
    datos["Screen Porch"] = st.number_input("Superficie de galería con mosquitero", 0, 576, 0)
    datos["Wood Deck SF"] = st.number_input("Superficie de deck de madera", 0, 1424, 0)

    st.subheader("📅 Venta")
    datos["Mo Sold"] = st.selectbox("Mes de venta (1-12)", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], index=3)
    radio_input("Sale Condition", [
        "Abnorml", "AdjLand", "Alloca", "Family", "Normal", "Partial"
    ])


# ===================== TAB 2 =====================
with tab2:
    st.header("Datos cargados")
    st.markdown("Aquí puede revisar los datos ingresados antes de hacer la predicción.")
    st.json(datos)

# ===================== TAB 3 =====================
with tab3:
    st.header("Predicción del Precio")
    st.markdown("Presione el botón para obtener una predicción basada en los datos ingresados.")

    input_df = pd.DataFrame([datos])

    # VALIDACIONES
    errores = []

    total_floor = datos["1nd Flr SF"] + datos["2nd Flr SF"]
    if total_floor > datos["Lot Area"]:
        errores.append("⚠️ La superficie total de los pisos supera el área del lote.")

    if datos["Garage Area"] > datos["1nd Flr SF"]:
        errores.append("⚠️ El área del garage no puede superar la del primer piso.")

    bsmt_total_estimado = datos["Bsmt Unf SF"] + datos["Total Bsmt SF"]
    if bsmt_total_estimado > datos["Lot Area"]:
        errores.append("⚠️ El sótano total (terminado + no terminado) supera el área del lote.")

    if datos["Gr Liv Area"] < total_floor:
        errores.append("⚠️ La superficie habitable es menor que la suma de 1er y 2do piso.")

    if errores:
        st.error("Se encontraron inconsistencias en los datos ingresados:")
        for e in errores:
            st.write(e)
        st.stop()

    if st.button("Predecir valor de casa"):
        prediccion = model.predict(input_df)[0]
        st.success(f"Predicción del precio de la casa: ${prediccion:,.2f}")
        st.caption("La predicción tiene un margen de incertidumbre del 11.43% respecto al valor promedio real.")
