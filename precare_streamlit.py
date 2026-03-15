# precare_streamlit.py
import streamlit as st
from streamlit_chat import message

# -------------------- Initialize session state --------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "inputs" not in st.session_state:
    st.session_state.inputs = {}

# -------------------- Sidebar navigation --------------------
with st.sidebar:
    st.title("PreCare Navigation")
    # Make sidebar reflect the current page
    page_selection = st.radio(
        "Go to page:", 
        ["Home", "Risk Assessment"], 
        index=0 if st.session_state.page == "Home" else 1
    )
    # Update session only if changed (prevents overwriting button click)
    if page_selection != st.session_state.page:
        st.session_state.page = page_selection

# -------------------- HOME PAGE --------------------
if st.session_state.page == "Home":
    st.markdown("<h1 style='text-align:center; color:#2FAF9B;'>PreCare AI</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#4E342E;'>Early Risk Detection for a Healthier Future</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>AI-powered disease risk analysis using family history and lifestyle data</p>", unsafe_allow_html=True)

    # Centered Get Started button
    if st.button("Get Started"):
        st.session_state.page = "Risk Assessment"

# -------------------- RISK ASSESSMENT PAGE --------------------
elif st.session_state.page == "Risk Assessment":
    st.markdown("<h1 style='text-align:center; color:#2FAF9B;'>Risk Assessment</h1>", unsafe_allow_html=True)
    st.write("Early health risk estimation based on lifestyle patterns and family medical history")

    # --- User Inputs ---
    st.subheader("Basic Health Information")
    age = st.number_input("Age", 1, 100)
    gender = st.selectbox("Gender", ["Male","Female","Other"])

    st.subheader("Lifestyle Information")
    diet = st.selectbox("Diet Quality", ["Poor","Moderate","Healthy"])
    activity = st.selectbox("Physical Activity Level", ["Low","Medium","High"])
    smoking = st.selectbox("Smoking Habit", ["No","Yes"])
    alcohol = st.selectbox("Alcohol Consumption", ["No","Yes"])

    st.subheader("Family Medical History")
    diabetes = st.checkbox("Family history of Diabetes")
    anemia = st.checkbox("Family history of Anemia")
    cancer = st.checkbox("Family history of Cancer")
    tb = st.checkbox("Family history of Tuberculosis")

    st.subheader("Observed Symptoms")
    fatigue = st.checkbox("Fatigue")
    weight = st.checkbox("Unexplained weight loss")
    cough = st.checkbox("Persistent cough")
    breath = st.checkbox("Shortness of breath")
    illness = st.checkbox("Frequent illness")

    # Save inputs in session for chatbot context
    st.session_state.inputs = {
        "age": age, "gender": gender, "diet": diet, "activity": activity,
        "smoking": smoking, "alcohol": alcohol,
        "diabetes": diabetes, "anemia": anemia, "cancer": cancer, "tb": tb,
        "fatigue": fatigue, "weight": weight, "cough": cough, "breath": breath, "illness": illness
    }

    # --- ML-style Risk Calculation ---
    score = None
    level = None
    if st.button("Calculate Risk Percentage"):
        score = 0
        # Age factor
        if age > 45: score += 20
        elif age > 30: score += 10
        # Diet factor
        if diet == "Poor": score += 15
        elif diet == "Moderate": score += 8
        # Activity factor
        if activity == "Low": score += 15
        elif activity == "Medium": score += 7
        # Smoking/Alcohol
        if smoking == "Yes": score += 20
        if alcohol == "Yes": score += 10
        # Family history
        if diabetes: score += 15
        if anemia: score += 10
        if cancer: score += 15
        if tb: score += 10
        # Symptoms
        if fatigue: score += 10
        if weight: score += 15
        if cough: score += 10
        if breath: score += 8
        if illness: score += 5
        # Cap
        if score > 100: score = 100
        # Risk level
        if score <= 20: level = "Low"
        elif score <= 50: level = "Moderate"
        else: level = "High"

        # Display results
        st.subheader("Risk Assessment Result")
        st.write(f"**Overall Disease Risk Percentage:** {score}%")
        st.write(f"**Risk Level:** {level}")

        st.subheader("Disease Risk Breakdown")
        st.write("Diabetes Risk")
        st.progress(int(min(score*0.8,100)))
        st.write("Anemia Risk")
        st.progress(int(min(score*0.6,100)))
        st.write("Cancer/TB Risk")
        st.progress(int(min(score*0.4,100)))

        st.subheader("Recommended Preventive Measures")
        st.markdown("- Maintain a balanced and nutritious diet")
        st.markdown("- Improve physical activity and daily movement")
        st.markdown("- Avoid smoking and alcohol consumption")
        st.markdown("- Maintain healthy body weight")
        st.markdown("- Follow regular health screening routines")
        st.markdown("- Seek medical consultation if symptoms persist")

        st.warning("PreCare AI provides early health risk awareness only. This is not a medical diagnosis.")

    # --- PreCare Assistant Chatbot ---
    st.subheader("💬 PreCare Assistant")
    user_input = st.text_input("Ask about your health risk or preventive tips:")

    # Quick-reply buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Explain Diabetes Risk"):
            user_input = "Explain Diabetes Risk"
    with col2:
        if st.button("Explain Anemia Risk"):
            user_input = "Explain Anemia Risk"
    with col3:
        if st.button("Explain Cancer/TB Risk"):
            user_input = "Explain Cancer/TB Risk"
    col4, col5 = st.columns(2)
    with col4:
        if st.button("Preventive Tips"):
            user_input = "Preventive Tips"
    with col5:
        if st.button("Lifestyle Advice"):
            user_input = "Lifestyle Advice"

    # Simple chatbot logic
    if user_input:
        response = ""
        inputs = st.session_state.inputs
        if "Diabetes" in user_input:
            response = f"Your Diabetes risk is based on diet, activity, and family history. Family history: {inputs['diabetes']}. Tips: reduce sugar intake, maintain healthy weight, increase activity."
        elif "Anemia" in user_input:
            response = f"Anemia risk depends on diet and family history. Family history: {inputs['anemia']}. Tips: eat iron-rich foods, vitamin C, monitor hemoglobin."
        elif "Cancer" in user_input or "TB" in user_input:
            response = f"Cancer/TB risk depends on family history and lifestyle habits. Family history: {inputs['cancer']}, {inputs['tb']}. Tips: avoid tobacco, balanced diet, regular check-ups."
        elif "Preventive" in user_input:
            response = "Maintain balanced diet, daily activity, avoid smoking/alcohol, regular screenings, seek consultation if symptoms persist."
        elif "Lifestyle" in user_input:
            response = "Focus on healthy diet, regular exercise, avoid smoking/alcohol, maintain consistent sleep schedule."
        else:
            response = "I can help explain your risk levels, preventive measures, and lifestyle advice. This is for awareness only. Consult a healthcare professional."

        st.session_state.chat_history.append((user_input, response))

    # Display chat history
    for user_msg, bot_msg in reversed(st.session_state.chat_history):
        message(bot_msg, key=bot_msg)
        message(user_msg, is_user=True, key=user_msg)