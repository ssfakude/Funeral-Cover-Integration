from __future__ import print_function
from imaplib import _Authenticator
from itertools import count
import json
import pickle
from pathlib import Path
from unicodedata import name
import streamlit_authenticator as stauth
from re import X
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import plotly.graph_objects as go
import numpy as np
import requests
import timeit
import altair as alt
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import datetime as dt
import time
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta # to add days or years
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

start = timeit.default_timer()
st.set_page_config(page_title="Funeral Cover Integration", page_icon="")

#://returnxdigital.leadbyte.co.uk/api/submit.php?returnjson=yes&campid=FUNERAL-COVER&sid=24845&testmode=yes&email=test@test.com&firstname=Test&lastname=Test&phone1=0613394600&optinurl=http://url.com&optindate=INSERTVALUEyes&grossmonthlyincome=INSERTVALUE&acceptterms=true&offer_id=2512


def floatify(value):

 
    if pd.isna(value) ==True:
        return ""
    if ":" in str(value):
        return 0.0
    else:
   
        float_= value.replace(' ','')
        return float(float_.replace(',','.'))
not_found_order =[]
not_found_invoiced =[]
not_found_return =[]
time_out =[]
#----------User AUth----------
names = ["Simphiwe Fakude", "Jean-Pierre Myburg"]
usernames = ["simphiwef", "JP"]
file_path  = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,"aspol", "abcdef", cookie_expiry_days=30 )# cookie
name, authentication_status, username = authenticator.login('Please Login', 'main')


if authentication_status == False:
    st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')
elif authentication_status:
   
    def load_lottieurl(url: str): #load from the web
       
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    st.write(f'Welcome  *{name}*')
    lottie_dog=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_xBGyhl.json") 
    with st_lottie_spinner(lottie_dog, width= 300, key="dog"):


        @st.cache_data
        def read_file(data_file):
            
            xls = pd.ExcelFile(data_file)
            
            try:
                df_leads = pd.read_excel(xls, 'Leads')
            except Exception as e:
                st.error("Incorect Sheet name for Leads:(")
                st.stop()
           
            return df_leads




        #time.sleep(4)
        def main():
            st.title("Funeral Cover Integration")
            st.subheader("NB, make sure the file is type XLSX:")
            data_file = st.file_uploader("[Leads]",type=['xlsx'])
            # lottie_nodata=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_5awivhzm.json")
            # st_lottie(lottie_nodata, key="load", width=600)
            if st.button("Process"):

                if data_file is not None:
                    file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}

                    df_leads = read_file(data_file)
    
                    
                  
                    latest_iteration = st.empty()
                    print("-----------------------Leads------------------")
                    len_df_leads =len(df_leads.index)
                    
    

                    for i, j in df_leads.iterrows():
                        email = j[2]
                        if len_df_leads - i == 1:
                            latest_iteration.text('Done Loading Leads')
                        else:
                            latest_iteration.text(f'Leads: {len_df_leads - i} records left - {j[2]}')
                        if pd.isna(email) ==True:
                            break
                        else:
                           
                            
                            firstname=  j[0]
                            lastname =  j[1]
                            email = j[2]
                            dateTime =  j[4]
                            optinurl  =j[6]
                            phone1= str(j[3])
                            optindate = str(j[6])
                            testmode ="Yes"
                            grossmonthlyincome = str(j[5])
                            acceptterms = j[7].lower()
                            if acceptterms =="no":
                                acceptterms = "false"
                            else:
                                acceptterms = "true"
                            
                            offer_id = "2719"
                         
                            current_datetime = datetime.now()
                            current_date_time = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
                           
                            url = "https://returnxdigital.leadbyte.co.uk/api/submit.php?returnjson=yes&campid=FUNERAL-COVER&sid=24845&testmode=yes&email="+email+"&firstname="+firstname+"&lastname="+lastname+"&phone1="+phone1+"&optinurl="+optinurl+"&optindate="+optindate+"&grossmonthlyincome="+grossmonthlyincome+"&acceptterms="+acceptterms+"&offer_id="+offer_id
                          
                            
                         
                            response = requests.post(url = url)
                            print("Leads- ",response.status_code)
                            print("What is what: ",acceptterms)
                           
                    st.markdown("<h2 style='text-align: center; color: white;'>Synchronization completed!</h2>", unsafe_allow_html=True)
                    #lottie_nodata=load_lottieurl("https://lottie.host/?file=e686c78b-e554-498d-aaa1-e045ea2e2df9/iZMW2qsupf.json")
                    lottie_nodata=load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_rjqwaenm.json")
                    #st_lottie(lottie_nodata, key="done", width=270) https://lottie.host/?file=e686c78b-e554-498d-aaa1-e045ea2e2df9/iZMW2qsupf.json
                    st.balloons()
                    print("-----------------------------------------------")

        
        if __name__ == '__main__':
            main()




    # ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                #title {
                text-align: center
                </style>
                """
        
st.markdown(hide_st_style, unsafe_allow_html=True)


