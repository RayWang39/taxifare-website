import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

st.header('Ride Parameters')

col1, col2 = st.columns(2)

with col1:
    pickup_date = st.date_input('Pickup Date', value=datetime.date.today())
    pickup_time = st.time_input('Pickup Time', value=datetime.datetime.now().time())
    
    st.subheader('Pickup Location')
    pickup_longitude = st.number_input('Pickup Longitude', value=-73.985428, format="%.6f")
    pickup_latitude = st.number_input('Pickup Latitude', value=40.748817, format="%.6f")

with col2:
    passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8, value=1)
    
    st.subheader('Dropoff Location')
    dropoff_longitude = st.number_input('Dropoff Longitude', value=-73.985428, format="%.6f")
    dropoff_latitude = st.number_input('Dropoff Latitude', value=40.748817, format="%.6f")

pickup_datetime = f'{pickup_date} {pickup_time}'





'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'http://localhost:8501/'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
