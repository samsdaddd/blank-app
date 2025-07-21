
import streamlit as st
from base_medicaments import ACB_DATABASE

st.title("🧮 Calculateur de charge anticholinergique (ACB)")

meds_input = st.text_input("Entrez les médicaments (séparés par des virgules) :", "")

if st.button("Analyser"):
    meds_list = meds_input.split(",")
    total = 0
    details = {}

    for med in meds_list:
        med = med.lower().strip()
        score = ACB_DATABASE.get(med, None)
        if score is None:
            details[med] = "❓ Inconnu"
        else:
            total += score
            details[med] = score

    st.subheader("🔎 Résultats :")
    for med, score in details.items():
        st.write(f"- **{med.title()}** : {score}")

    st.markdown(f"### 🧮 Total ACB : **{total}**")
    if total >= 3:
        st.error("⚠️ Risque élevé (≥ 3)")
    else:
        st.success("✅ Risque faible (< 3)")
print("Médicaments analysés :", meds_list)