import streamlit as st

st.title("Calculadora de Leyes de los Gases")
st.markdown("""
Selecciona una ley de los gases y luego elige qué variable deseas calcular.  
Las unidades deben ser:
- Presión: atm
- Volumen: Litros (L)
- Temperatura: Kelvin (K)
""")

ley = st.selectbox("Selecciona la ley de los gases:", [
    "Ley de Boyle (P1·V1 = P2·V2)",
    "Ley de Charles (V1/T1 = V2/T2)",
    "Ley de Gay-Lussac (P1/T1 = P2/T2)"
])

if ley == "Ley de Boyle (P1·V1 = P2·V2)":
    variable = st.selectbox("Variable a calcular", ["P1", "V1", "P2", "V2"])
    if variable != "P1":
        P1 = st.number_input("P1 (atm)", min_value=0.01)
    if variable != "V1":
        V1 = st.number_input("V1 (L)", min_value=0.01)
    if variable != "P2":
        P2 = st.number_input("P2 (atm)", min_value=0.01)
    if variable != "V2":
        V2 = st.number_input("V2 (L)", min_value=0.01)

    if st.button("Calcular"):
        if variable == "P1":
            result = (P2 * V2) / V1
            st.success(f"P1 = {result:.4f} atm")
        elif variable == "V1":
            result = (P2 * V2) / P1
            st.success(f"V1 = {result:.4f} L")
        elif variable == "P2":
            result = (P1 * V1) / V2
            st.success(f"P2 = {result:.4f} atm")
        elif variable == "V2":
            result = (P1 * V1) / P2
            st.success(f"V2 = {result:.4f} L")

elif ley == "Ley de Charles (V1/T1 = V2/T2)":
    variable = st.selectbox("Variable a calcular", ["V1", "T1", "V2", "T2"])
    if variable != "V1":
        V1 = st.number_input("V1 (L)", min_value=0.01)
    if variable != "T1":
        T1 = st.number_input("T1 (K)", min_value=0.01)
    if variable != "V2":
        V2 = st.number_input("V2 (L)", min_value=0.01)
    if variable != "T2":
        T2 = st.number_input("T2 (K)", min_value=0.01)

    if st.button("Calcular"):
        if variable == "V1":
            result = (V2 * T1) / T2
            st.success(f"V1 = {result:.4f} L")
        elif variable == "T1":
            result = (V1 * T2) / V2
            st.success(f"T1 = {result:.4f} K")
        elif variable == "V2":
            result = (V1 * T2) / T1
            st.success(f"V2 = {result:.4f} L")
        elif variable == "T2":
            result = (V2 * T1) / V1
            st.success(f"T2 = {result:.4f} K")

elif ley == "Ley de Gay-Lussac (P1/T1 = P2/T2)":
    variable = st.selectbox("Variable a calcular", ["P1", "T1", "P2", "T2"])
    if variable != "P1":
        P1 = st.number_input("P1 (atm)", min_value=0.01)
    if variable != "T1":
        T1 = st.number_input("T1 (K)", min_value=0.01)
    if variable != "P2":
        P2 = st.number_input("P2 (atm)", min_value=0.01)
    if variable != "T2":
        T2 = st.number_input("T2 (K)", min_value=0.01)

    if st.button("Calcular"):
        if variable == "P1":
            result = (P2 * T1) / T2
            st.success(f"P1 = {result:.4f} atm")
        elif variable == "T1":
            result = (P1 * T2) / P2
            st.success(f"T1 = {result:.4f} K")
        elif variable == "P2":
            result = (P1 * T2) / T1
            st.success(f"P2 = {result:.4f} atm")
        elif variable == "T2":
            result = (P2 * T1) / P1
            st.success(f"T2 = {result:.4f} K")
