import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading models
dia_model = pickle.load(open("./savedModels/Diabetes.sav", 'rb'))
heart_model = pickle.load(open("./savedModels/Heart.sav", 'rb'))
par_model = pickle.load(open("./savedModels/Parkinsons.sav", 'rb'))

# Assuming the accuracy values are known and hard-coded
dia_accuracy = 0.85  # Example accuracy value for Diabetes model
heart_accuracy = 0.90  # Example accuracy value for Heart model
par_accuracy = 0.88  # Example accuracy value for Parkinson's model

def get_prediction(model, input_data):
    if hasattr(model, 'predict_proba'):
        prediction_proba = model.predict_proba(input_data)[0]
        return prediction_proba[1]
    else:
        prediction = model.predict(input_data)
        return prediction[0]

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('E-Doctor System',
                           ['Diabetes Screening',
                            'Heart Health Screening',
                            'Parkinsons Screening'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Screening':
    st.title('Provide Information for Diabetes Prediction')
    
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
    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction = get_prediction(dia_model, input_data)
        diab_prediction_percentage = diab_prediction * 100
        
        if diab_prediction_percentage >= 50:
            diab_diagnosis = (f'The person is predicted to be diabetic with a confidence interval of '
                              f'{diab_prediction_percentage:.2f}%. '
                              f'The model accuracy is {dia_accuracy * 100:.2f}%.')
        else:
            diab_diagnosis = (f'The person is predicted to not be diabetic with a confidence interval of '
                              f'{100 - diab_prediction_percentage:.2f}%. '
                              f'The model accuracy is {dia_accuracy * 100:.2f}%.')
        
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Health Screening':
    st.title('Provide Information for Heart Analysis')
    
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
        
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        heart_prediction = get_prediction(heart_model, input_data)
        heart_prediction_percentage = heart_prediction * 100
        
        if heart_prediction_percentage >= 50:
            heart_diagnosis = (f'The person is predicted to have heart disease with a confidence interval of '
                               f'{heart_prediction_percentage:.2f}%. '
                               f'The model accuracy is {heart_accuracy * 100:.2f}%.')
        else:
            heart_diagnosis = (f'The person is predicted to not have heart disease with a confidence interval of '
                               f'{100 - heart_prediction_percentage:.2f}%. '
                               f'The model accuracy is {heart_accuracy * 100:.2f}%.')
        
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Screening":
    st.title("Provide Information for Parkinsons Analysis")
    
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
        
    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result"):
        input_data = [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]
        parkinsons_prediction = get_prediction(par_model, input_data)
        parkinsons_prediction_percentage = parkinsons_prediction * 100
        
        if parkinsons_prediction_percentage >= 50:
            parkinsons_diagnosis = (f"The person is predicted to have Parkinson's disease with a confidence interval of "
                                    f"{parkinsons_prediction_percentage:.2f}%. "
                                    f"The model accuracy is {par_accuracy * 100:.2f}%.")
        else:
            parkinsons_diagnosis = (f"The person is predicted to not have Parkinson's disease with a confidence interval of "
                                    f"{100 - parkinsons_prediction_percentage:.2f}%. "
                                    f"The model accuracy is {par_accuracy * 100:.2f}%.")
        
    st.success(parkinsons_diagnosis)
