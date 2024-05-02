import streamlit as st
import pandas as pd
import time

# Sample dataset (replace with your own dataset)
sample_data = pd.read_csv("lettuce_dataset.csv")

def automatic_image_display_page():
    st.title("Automatic Image Display for Growth Days")

    # Placeholder for the image and parameters
    image_placeholder = st.empty()
    parameters_placeholder_gd = st.empty()
    parameters_placeholder_temp = st.empty()
    parameters_placeholder_hum= st.empty()
    parameters_placeholder_tds= st.empty()
    parameters_placeholder_ph = st.empty()

    # Iterate through each growth day
    for index, row in sample_data.iterrows():
        display_data(image_placeholder, parameters_placeholder_gd,parameters_placeholder_temp,parameters_placeholder_hum,parameters_placeholder_tds,parameters_placeholder_ph, row)
        time.sleep(0.7)


def display_data(image_placeholder, parameters_placeholder_gd,parameters_placeholder_temp,parameters_placeholder_hum,parameters_placeholder_tds,parameters_placeholder_ph, row):
    # Replace the previous image with the new one
    parameters_placeholder_gd.empty()
    parameters_placeholder_gd.write(f"#### Growth Day: {row['Growth Day']}")
    parameters_placeholder_temp.write(f"Temperature: {row['Temperature']}")
    parameters_placeholder_hum.write(f"Humidity: {row['Humidity']}")
    parameters_placeholder_tds.write(f"TDS Value: {row['TDS Value']}")
    parameters_placeholder_ph.write(f"pH Level: {row['pH Level']}")
    image_placeholder.image(f"./bgremovedimgfromt3emp/{row['Growth Day']}.png")
    

automatic_image_display_page()


