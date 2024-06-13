#load packages
import streamlit as st
import requests
from streamlit_option_menu import option_menu
from rdkit import Chem
from rdkit.Chem import Draw
from mordred import Calculator, descriptors
from supervised.automl import AutoML
import pandas as pd
import numpy as np
import time
import hashlib
import json
import html
from streamlit.components.v1 import html
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image
from streamlit_ketcher import st_ketcher
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="SGLT2pred")

#background of webpage
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://raw.githubusercontent.com/anish19292/SGLT2pred/main/vecteezy_abstract-medical-concept-with-molecule-pattern-background_7355270.jpg");
background-size: cover;
background-position: top;
#background-repeat: repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);

}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

#clearning SMILES input button
def clear_text():
    st.session_state["text"] = ""

# Import necessary packages
import streamlit as st

# Set page configuration
st.set_page_config(page_title="SGLT2pred")

# Define custom CSS for styling
custom_css = """
<style>
    @keyframes text-gradient-title {
        0% { color: #FFD700; }
        50% { color: #91b3bd; }
        100% { color: #FFD700; }
    }

    .text-gradient-title {
        position: sticky;
        top: 0px;
        animation: text-gradient-title 4s ease-in-out infinite;
        font-size: 130px;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        font-style: italic;
    }
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Display the main title
st.markdown('<h1 class="text-gradient-title">SGLT2pred</h1>', unsafe_allow_html=True)
