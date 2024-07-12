import pickle
import streamlit as st

try:
    from streamlit_option_menu import option_menu
except ImportError as e:
    st.error(f"Error importing streamlit_option_menu: {e}")
    raise

# Loading models
try:
    dia_model = pickle.load(open("/mnt/data/Diabetes.sav", 'rb'))
    heart_model = pickle.load(open("/mnt/data/Heart.sav", 'rb'))
    par_model = pickle.load(open("/mnt/data/Parkinsons.sav", 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading model files: {e}")
    raise
except pickle.UnpicklingError as e:
    st.error(f"Error unpickling model files: {e}")
    raise

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('E-Doctor Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity', 'heart', 'person'],
                          default_index=0)

# Function to get prediction and probability
def get_prediction_and_proba(model, features):
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(features)[0][1] * 100
        prediction = model.predict(features)
        return prediction, proba
    else:
        prediction = model.predict(features)
        return prediction, None

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        features = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction, diab_probability = get_prediction_and_proba(dia_model, features)
        
        if diab_prediction[0] == 1:
            if diab_probability is not None:
                diab_diagnosis = f'The person is diabetic with a probability of {diab_probability:.2f}%.'
            else:
                diab_diagnosis = 'The person is diabetic.'
        else:
            if diab_probability is not None:
                diab_diagnosis = f'The person is not diabetic with a probability of {100 - diab_probability:.2f}%.'
            else:
                diab_diagnosis = 'The person is not diabetic.'
        
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Code for Prediction
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        heart_prediction, heart_probability = get_prediction_and_proba(heart_model, features)
        
        if heart_prediction[0] == 1:
            if heart_probability is not None:
                heart_diagnosis = f'The person is having heart disease with a probability of {heart_probability:.2f}%.'
            else:
                heart_diagnosis = 'The person is having heart disease.'
        else:
            if heart_probability is not None:
                heart_diagnosis = f'The person does not have any heart disease with a probability of {100 - heart_probability:.2f}%.'
            else:
                heart_diagnosis = 'The person does not have any heart disease.'
        
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # Code for Prediction
    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        features = [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]
        parkinsons_prediction, parkinsons_probability = get_prediction_and_proba(par_model, features)
        
        if parkinsons_prediction[0] == 1:
            if parkinsons_probability is not None:
                parkinsons_diagnosis = f"The person has Parkinson's disease with a probability of {parkinsons_probability:.2f}%."
            else:
                parkinsons_diagnosis = "The person has Parkinson's disease."
        else:
            if parkinsons_probability is not None:
                parkinsons_diagnosis = f"The person does not have Parkinson's disease with a probability of {100 - parkinsons_probability:.2f}%."
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease."
        
    st.success(parkinsons_diagnosis)
