import numpy as np
import pickle
import streamlit

loaded_model = pickle.load(open('./Notebooks/trained_model.sav', 'rb'))

# make a predictive system
input_data = (1,85,66,29,0,26.6,0.351,31)
# change the input data to numpy array
input_data_as_np_array= np.asarray(input_data)
# reshape the array
input_data_reshape = input_data_as_np_array.reshape(1,-1)
print(input_data_reshape)
prediction = loaded_model.predict(input_data_reshape)
print(prediction)

if (prediction[0] == 0):
    print('The person is not diabetic')
else:
    print('The person is diabetic.')