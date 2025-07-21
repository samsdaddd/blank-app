
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
if total == 0:
    st.success("✅ Aucun effet anticholinergique détecté!")
elif total <= 2:
    st.info("🟡 Risque faible (1–2) — surveiller si d'autres facteurs de fragilité")
elif total <= 5:
    st.warning("🟠 Risque modéré (3–5) — attention si patient fragile ou âgé")
else:
    st.error("🔴 Risque élevé (>5) — revoir l’ordonnance avec un professionnel")