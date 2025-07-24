import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('./Notebooks/trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
    # change the input data to numpy array
    input_data_as_np_array= np.asarray(input_data)

    # reshape the array
    input_data_reshape = input_data_as_np_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)

    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic.'
    

def main():
    st.title('Diabetes Prediction Web App')
    st.subheader('Enter the following health metrics to predict diabetes risk.')

    col1, col2 = st.columns(2)
    # Input data -> Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
        Glucose = st.text_input('Glucose level')
        BloodPressure = st.text_input('Blood Pressure level')
        SkinThickness = st.text_input('SkinThickness')
    with col2:
        Insulin = st.text_input('Insulin level')
        BMI = st.text_input('BMI')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
        Age=st.text_input('Age of the person')

    # prediction
    result = ''

    if st.button('Diabetes Test Result'):
        result = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin, BMI,DiabetesPedigreeFunction, Age])
        if 'not diabetic' in result.lower():
            st.success(result)
        else:
            st.error(result)
            
    st.markdown("""
        ---
        Made with ❤️ by [Samuel Wanyua](https://github.com/samwanyua)  
        Model trained on the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
        """)

    


if __name__ == '__main__':
    main()




