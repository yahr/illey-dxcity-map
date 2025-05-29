import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import os

st.set_page_config(page_title="Naver Map Viewer", layout="wide")

st.title("Naver Map Viewer")
st.write("Upload a CSV file containing coordinates to display them on the map.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write("Data Preview:")
    st.dataframe(df.head())
    
    # Support both Korean and English column names
    if '위도' in df.columns and '경도' in df.columns:
        df['latitude'] = df['위도']
        df['longitude'] = df['경도']
    
    # Support both Korean and English name columns
    if '이름' in df.columns:
        df['marker_name'] = df['이름']
    elif 'name' in df.columns:
        df['marker_name'] = df['name']
    else:
        df['marker_name'] = [f"Location {i+1}" for i in range(len(df))]
    
    # Check if required columns exist
    required_columns = ['latitude', 'longitude']
    if not all(col in df.columns for col in required_columns):
        st.error("CSV file must contain either 'latitude'/'longitude' or '위도'/'경도' columns")
    else:
        # Create a map centered at the mean of coordinates
        center_lat = df['latitude'].mean()
        center_lng = df['longitude'].mean()
        
        m = folium.Map(location=[center_lat, center_lng], zoom_start=13)
        
        # Add markers for each coordinate
        for idx, row in df.iterrows():
            # Naver Map URL Scheme (app)
            nmap_url = f"nmap://place?lat={row['latitude']}&lng={row['longitude']}&name={row['marker_name']}"
            # Naver Map Web URL (fallback)
            web_url = f"https://map.naver.com/v5/search/{row['marker_name']}?c=15.00,{row['longitude']},{row['latitude']},0,0,0,0,d"
            # Popup HTML
            popup_html = f"""
            <b>{row['marker_name']}</b><br>
            <a href='{nmap_url}'>네이버 지도 앱으로 열기</a><br>
            <a href='{web_url}' target='_blank'>네이버 지도 웹으로 열기</a>
            """
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=row['marker_name']
            ).add_to(m)
        
        # Display the map
        folium_static(m, width=800, height=600)
else:
    st.info("Please upload a CSV file with 'latitude' and 'longitude' or '위도' and '경도' columns") 