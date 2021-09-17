import streamlit as st
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from src.data_management import load_pkl_file

def clf_prediction_evaluation(y, prediction, label_map):


  Map = list() 
  for key, value in label_map.items():
    Map.append( str(key) + ": " + value)

  st.write('#### Confusion Matrix')
  st.code(pd.DataFrame(confusion_matrix(y_true=prediction, y_pred=y),
        columns=[ ["Actual " + sub for sub in Map] ], 
        index= [ ["Prediction " + sub for sub in Map ]]
        ))



  st.write('#### Classification Report')
  st.code(classification_report(y, prediction),"\n")




def clf_performance_train_validation_test_set(version):

    class_indices = load_pkl_file(file_path= f"outputs/{version}/class_indices.pkl")
    class_indices = {v: k for k, v in class_indices.items()}

    for dataset in ['train', 'validation', 'test']:
        st.info(f"**{dataset.title()} Set**")
        y = pd.read_csv(f"outputs/{version}/actual_values_{dataset}_set.csv")
        prediction = pd.read_csv(f"outputs/{version}/predictions_{dataset}_set.csv")
        clf_prediction_evaluation(y, prediction, label_map=class_indices)