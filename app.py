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

st.set_page_config(page_title="SerotoninAI")

#background of webpage
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/anish19292/SGLT2pred/blob/c0440f004fea283df80a969b69726aa2dcbf6fed/vecteezy_abstract-medical-concept-with-molecule-pattern-background_7355270.jpg");
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
