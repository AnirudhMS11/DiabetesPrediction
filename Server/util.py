import json
import pickle
import numpy as np
import pandas as pd

__gender = None
__smoking_history = None
__model = None
__data_columns = None

def get_Prediction(age,ht,hd,bmi,hb,bgl,gender,smoking):
    input_vector = np.zeros(len(__data_columns))

    col_index_map = {col: idx for idx, col in enumerate(__data_columns)}

    if 'age' in col_index_map:
        input_vector[col_index_map['age']] = age
    if 'hypertension' in col_index_map:
        input_vector[col_index_map['hypertension']] = ht
    if 'heart_disease' in col_index_map:
        input_vector[col_index_map['heart_disease']] = hd
    if 'bmi' in col_index_map:
        input_vector[col_index_map['bmi']] = bmi
    if 'HbA1c_level' in col_index_map:
        input_vector[col_index_map['HbA1c_level']] = hb
    if 'blood_glucose_level' in col_index_map:
        input_vector[col_index_map['blood_glucose_level']] = bgl

    gender_col = f'gender_{gender}'
    if gender_col in col_index_map:
        input_vector[col_index_map[gender_col]] = 1

    smoking_history = f'smoking_history_{smoking}'
    if smoking_history in col_index_map:
        input_vector[col_index_map[smoking_history]] = 1

    input_df = pd.DataFrame([input_vector], columns=__data_columns)
 
    return __model.predict(input_df)[0]


def clean_gender_smoking():
     global __gender
     global __smoking_history

     __gender = __gender.replace("gender_","")
     __smoking_history = [sh.replace("smoking_history_","") for sh in __smoking_history]

     print("Gender and Smoking History are cleaned")


def get_gender():
    return __gender

def get_smoking_history():
    return __smoking_history

def load_artifacts():
    print("Loading artifacts")
    global __gender
    global __smoking_history
    global __model
    global __data_columns

    with open("./artifacts/columns.json",'r') as f:
                __data_columns = json.load(f)['data_columns']
                __gender = __data_columns[6]
                __smoking_history = __data_columns[7:11]

    with open("./artifacts/DCM.pickle",'rb') as f:
                __model = pickle.load(f)
                print(__model)

    clean_gender_smoking()

    print("Loaded Artifacts")

if __name__ == '__main__':
    load_artifacts()
    #print(get_gender())
    #print(get_smoking_history())
    #print(get_Prediction(30.0,0,0,37.87,5.0,145,'Female','never'))
    #print(get_Prediction(80.0,0,0,31.39,5.7,100,'Male','not current'))
    #print(get_Prediction(52.0,0,0,30.17,7.5,126,'Male','current'))