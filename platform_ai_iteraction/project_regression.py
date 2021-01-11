import streamlit as st

def expected_step_one(code):
    expected = ["import numpy","import matplotlib.pyplot as plot","import pandas",
                 "from sklearn.model_selection import train_test_split",
                 "from sklearn.linear_model import LinearRegression"]
    sucess = []
    for i in range(len(code)):
        if code[i] == expected[i]:
            sucess.append(1)
    if len(sucess) == 5:
        return True
    else:
        return False

def import_libraries(libraries):
    for i in libraries:
        exec(i)
    return True
    
    
