import pandas as pd
import streamlit as st
import joblib

x_number = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_list = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancellation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }

dict_list = {}

for item in x_list:
    for value in x_list[item]:
        dict_list[f'{item}_{value}']=0

for item in x_number:
    if item == 'latitude' or item == 'longitude':
        value = st.number_input(f'{item}', step=0.00001, value=0.0, format='%.5f')
    elif item == 'extra_people':
        value = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        value = st.number_input(f'{item}', step=1, value=0)
    x_number[item] = value

for item in x_tf:
    value = st.selectbox(f'{item}', ('Sim', 'Não'))
    if value == 'Sim':
        x_tf[item] = 1
    else:
        x_tf[item] = 0

for item in x_list:
    value = st.selectbox(f'{item}', x_list[item])
    dict_list[f'{item}_{value}'] = 1

button = st.button('Prever Valor do Imóvel')

if button:
    dict_list.update(x_number)
    dict_list.update(x_tf)

    value_x = pd.DataFrame(dict_list, index=[0])

    data = pd.read_csv('dados.csv')
    columns = list(data.columns)[1:-1]

    print(value_x.columns)

    newDF = value_x[columns]

    model = joblib.load('model.joblib')
    price = model.predict(newDF)
    st.write(price[0])