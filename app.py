import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu



st.set_page_config(layout="wide")
st.title("Circket Team Dashboard")

df=pd.read_csv("cleanedfile.csv")

select=option_menu(
    menu_title=None,
    options=["Home","Player Analysis","Country Insights","Comparision","Data Explorer","About Project"],
    icons=["house","person","globe","bar-chart","table"],
    orientation="horizontal"
)

if select== "Home":
    st.title("Cric Analysis")

    col1,col2,col3,col4,col5=st.columns(5)


    col1.metric("Total Player",df["Player"].nunique())
    col2.metric("Total Countries",df["Country"].nunique())
    col3.metric("Total Matches",df["Matches"].sum())
    col4.metric("Total Runs",df["Runs"].sum())
    col5.metric("Total Sixes",df["6s"].sum())
    st.dataframe(df.head(5))



elif select== "Player Analysis":
    st.title("Cricket Player Analysis")

    player = st.selectbox("select player",df["Player"])

    pdata= df[df["Player"]==player]

    df2=pdata[["Matches","0","6s","4s","100","50","Inns"]]

    #st.dataframe(df2)

    df2=df2.T.reset_index()
    st.dataframe(df2)
    fig = px.bar(df2,x="index",y=df2.columns[1],color="index")
    st.plotly_chart(fig)

    

elif select== "Country Insights":
    st.title("Country Insights")
    col1,col2=st.columns(2)
    with col1:
        country_runs=df.groupby("Country")["Runs"].sum().reset_index()

        fig=px.pie(country_runs,names="Country",values="Runs")
        st.plotly_chart(fig)

    with col2:   
        st.title("Country wise player insights")
        country_sel=st.selectbox("select country",df["Country"].unique())
        c_da=df[df["Country"]==country_sel]

        fig_run=px.pie(c_da,names="Player",values="Runs")
        st.plotly_chart(fig_run,use_container_width=True)

       

elif select== "Comparision":
    st.title("Player Comparision")

    players=st.multiselect("compare players",df["Player"],df["Player"].head(3)) 
    compare=df[df["Player"].isin(players)]
    fig=px.scatter(compare,x="Strike_Rate",y="Average_Score",size="Runs",color="Country")
    st.plotly_chart(fig)

elif select=="Data Explorer":
    st.title("Data Explorer")

    st.dataframe(df)

elif select=="About Project":
    st.title("About Project")
    st.markdown("How this project evolved with the Data Analysis Skills by Muhammad Saim ")


