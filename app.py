import streamlit as st

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Mental Health Risk Self-Assessment",
    page_icon="🧠",
    layout="centered"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🧠 Mental Health Risk Self-Assessment")

st.markdown(
    """
    This tool provides a **basic mental health risk assessment**
    based on academic, lifestyle, and well-being indicators.

    ⚠️ **Important:**  
    This is **not a medical diagnosis**.  
    It is an **AI-inspired decision-support tool** intended for awareness only.
    """
)

st.divider()

# --------------------------------------------------
# Questionnaire
# --------------------------------------------------
st.subheader("📋 Answer the following questions")

with st.form("mental_health_form"):
    age = st.slider("Age", 17, 30, 21)

    cgpa = st.slider("Current CGPA", 0.0, 10.0, 7.5, step=0.1)

    stress = st.slider("Stress Level (0–10)", 0, 10, 5)
    depression = st.slider("Depression Score (0–10)", 0, 10, 5)
    anxiety = st.slider("Anxiety Score (0–10)", 0, 10, 5)

    sleep = st.selectbox("Sleep Quality", ["Poor", "Average", "Good"])
    physical = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])
    diet = st.selectbox("Diet Quality", ["Poor", "Average", "Good"])
    social = st.selectbox("Social Support", ["Low", "Moderate", "High"])
    financial = st.selectbox("Financial Stress", ["Low", "Moderate", "High"])

    submit = st.form_submit_button("🔮 Assess Risk")

# --------------------------------------------------
# Risk Scoring Logic (Rule-Based)
# --------------------------------------------------
if submit:
    # Base psychological score
    risk_score = stress + depression + anxiety

    # Lifestyle modifiers
    if sleep == "Poor":
        risk_score += 2
    elif sleep == "Good":
        risk_score -= 1

    if physical == "Low":
        risk_score += 1
    elif physical == "High":
        risk_score -= 1

    if diet == "Poor":
        risk_score += 1
    elif diet == "Good":
        risk_score -= 1

    if social == "Low":
        risk_score += 2
    elif social == "High":
        risk_score -= 1

    if financial == "High":
        risk_score += 2
    elif financial == "Low":
        risk_score -= 1

    # Academic buffer
    if cgpa >= 8.5:
        risk_score -= 1
    elif cgpa < 6.0:
        risk_score += 1

    # --------------------------------------------------
    # Risk Level Mapping
    # --------------------------------------------------
    if risk_score <= 12:
        risk_level = "Low"
    elif 12 < risk_score <= 20:
        risk_level = "Medium"
    else:
        risk_level = "High"

    # --------------------------------------------------
    # Display Result
    # --------------------------------------------------
    st.divider()
    st.subheader("📊 Assessment Result")

    if risk_level == "Low":
        st.success("🟢 Low Mental Health Risk")
    elif risk_level == "Medium":
        st.warning("🟡 Medium Mental Health Risk")
    else:
        st.error("🔴 High Mental Health Risk")

    st.markdown(
        f"""
        **Risk Score:** `{risk_score}`

        ### 🧠 How to interpret this
        - **Low:** No immediate concern detected  
        - **Medium:** Monitoring and support may be beneficial  
        - **High:** Consider seeking professional guidance  

        ⚠️ This assessment is for **awareness only** and should not replace
        professional mental health evaluation.
        """
    )

    st.info(
        "If you or someone you know is struggling, please consider reaching out to "
        "a qualified mental health professional or local support services."
    )
