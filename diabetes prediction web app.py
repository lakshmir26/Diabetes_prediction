# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:42:14 2024

@author: laksh
"""

import numpy as np
import pickle
import streamlit

#loading the saved model

loaded_model = pickle.load(open('C:/Users/laksh/Downloads/trained_model.sav','rb'))
