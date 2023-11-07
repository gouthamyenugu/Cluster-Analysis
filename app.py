import streamlit as st
import pickle
from sklearn.cluster import KMeans

# Load the clustering model
model = pickle.load(open("kmeans.pkl", "rb"))

# Create a sidebar to allow the user to select the number of clusters
st.sidebar.header("Clustering Parameters")
num_clusters = st.sidebar.number_input("Number of Clusters", min_value=2, max_value=10)

def predict(CO2_Emissions, GDP, Health_Exp_GDP, Health_Exp_Capita,
            Infant_Mortality_Rate, Internet_Usage, Mobile_Phone_Usage,
            Population_15_64, Population_65, Population_Total,
            Population_Urban, Tourism_Inbound, Tourism_Outbound):
    data = [[CO2_Emissions, GDP, Health_Exp_GDP, Health_Exp_Capita,
             Infant_Mortality_Rate, Internet_Usage, Mobile_Phone_Usage,
             Population_15_64, Population_65, Population_Total,
             Population_Urban, Tourism_Inbound, Tourism_Outbound]]
    cluster = model.predict(data)
    return cluster[0]

def main():
    # Front-end elements of the web page
    st.header("Clustering Results")  
    # Get the user input data
    CO2_Emissions = st.number_input('CO2 Emissions')
    GDP = st.number_input('GDP')
    Health_Exp_GDP = st.number_input('Health Expenses /GDP')
    Health_Exp_Capita = st.number_input('Health Exp/Capita')
    Infant_Mortality_Rate = st.number_input('Infant Mortality Rate')
    Internet_Usage = st.number_input('Internet Usage')
    Mobile_Phone_Usage = st.number_input('Mobile Phone Usage')
    Population_15_64 = st.number_input('Population 15-64')
    Population_65 = st.number_input('Population 65')
    Population_Total = st.number_input('Population Total')
    Population_Urban = st.number_input('Population Urban')
    Tourism_Inbound = st.number_input('Tourism Inbound')
    Tourism_Outbound = st.number_input('Tourism Outbound')
    result = ""

    # When predict button is clicked
    if st.button('Find Clusters'):
        result = predict(CO2_Emissions, GDP, Health_Exp_GDP, Health_Exp_Capita,
                          Infant_Mortality_Rate, Internet_Usage, Mobile_Phone_Usage,
                          Population_15_64, Population_65, Population_Total,
                          Population_Urban, Tourism_Inbound, Tourism_Outbound)
        st.success('Global development measurement cluster number {}'.format(result))


if __name__ == '__main__':
    main()
