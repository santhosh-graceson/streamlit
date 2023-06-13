#Importing packages
import json
import websocket
import streamlit as st
import pandas as pd
import plotly.express as px
import time as t
import numpy as np
from datetime import datetime
from PIL import Image
RANGE=100000000

#Page setup
st.set_page_config(layout ="wide")
st.image("https://i.ibb.co/q059f9Q/Ai-Den-Medical-Rev-3-Mini-white.png",width=100)


#First row configuration
part2,part3=st.columns([15,3])
col1,col2,col3,col4,col5=part2.columns([3,1,2,10,2])
col6,col7,col8,col9=part3.columns([1,1,1,1])
with col2:
    st.markdown("<p style='font-size:0.8px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col2:  
    st.image("https://i.ibb.co/Y084PGJ/10522.png",width =40,use_column_width="auto")
with col2:
    st.markdown("<p style='font-size:0.01px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col6:
    st.markdown("<p style='font-size:1px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col6:
    plug_icon= st.image("https://i.ibb.co/nRmgTmw/wifi-icon-white.png",width=60)
with col7:
    st.markdown("<p style='font-size:1px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col7:    
    plug_icon= st.image("https://i.ibb.co/nRmgTmw/wifi-icon-white.png",width=60)
with col8:
    st.markdown("<p style='font-size:1px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col8:
    plug_icon= st.image("https://i.ibb.co/nRmgTmw/wifi-icon-white.png",width=60)
with col9:
    st.markdown("<p style='font-size:1px;text-align: center;gap: 0rem;padding:  0;color: #070D1C;font-synthesis: bold;'>1</p>", unsafe_allow_html=True)
with col9:
    plug_icon= st.image("https://i.ibb.co/nRmgTmw/wifi-icon-white.png",width=60)
with col3:
    st.markdown("<p style='font-size:0.001px;color: #070D1C;'>1</p>", unsafe_allow_html=True)
with col3:
    f="Patient ID"
    e="25"
    st.markdown("<p style='font-size:16px;text-align: center;gap: 0rem;padding:  0;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(e), unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;text-align: center;gap: 0rem;padding:  0;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(f), unsafe_allow_html=True)
with col1:
    st.markdown("<p style='font-size:0.001px;color: #070D1C;'>1</p>", unsafe_allow_html=True)
with col1:
    x = datetime.now()
    a=x.strftime("%d-%b-%y") 
    st.markdown("<p style='font-size:16px;gap: 0rem;padding:  0;text-align: center;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(a), unsafe_allow_html=True)
    b=x.strftime("%I:%M")
    st.markdown("<p style='font-size:16px;gap: 0rem;padding:  0;  text-align: center;color: #FFFFFF;font-synthesis: bold;'>{}</p>".format(b), unsafe_allow_html=True)
with col4:
    st.markdown("<h1 style='font-size:28px;text-align: center; color: #000000;'>Patient is Ventilated</h1>", unsafe_allow_html=True)
with col5:
    st.markdown("<h1 style='font-size:20px;text-align: center; color: #FFFFFF;'>Bi-Level</h1>", unsafe_allow_html=True)

#Second Row Configuration
First_Parameter = st.markdown("<h1 style='font-size:20px;text-align: left; color: #ff904f;width: 946px;'>FLOW</h1>", unsafe_allow_html=True)
chart_, values_container = st.columns([3, 1])
chart_container,null1 = chart_.columns([99,1])
# Second_parameter = st.markdown("<h1 style='font-size:20px;text-align: left; color: #ff904f;width: 940px;'>VOLUME</h1>", unsafe_allow_html=True)
# chart_1, values_container1 = st.columns([3, 1])
# chart_container1,null1 = chart_.columns([99,1])
insp_flow_container,awp_container = values_container.columns(2)
awp_container1,awp_container2=values_container.columns(2)
awp_container3, awp_container4= values_container.columns(2)
awp_container5, awp_container6 = values_container.columns(2)
chart = chart_container.empty()
chart1=chart_container.empty()
#Websocket connection establishment
websocket.enableTrace(True)
ws = websocket.WebSocket()
ws1 = websocket.WebSocket()
ws2 = websocket.WebSocket()
ws.connect("wss://i7kggwivc5.execute-api.us-west-2.amazonaws.com/production")
ws1.connect("wss://fr21il5ko7.execute-api.us-west-2.amazonaws.com/production")
ws2.connect("wss://svqvm4up0e.execute-api.us-west-2.amazonaws.com/production")
df_Inspiration_Flow = pd.DataFrame(columns=["Units","Inspiration_Flow"])
df_Volume = pd.DataFrame(columns=["Units","Volume"])
a=[]
b=[]
n=0

#Creating containers for the grid
last_insp_flow = insp_flow_container.empty()
last_insp_flow.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #80ff80;font-synthesis: bold;text-align:center;fill:#000000'>Ppeak</h2>", unsafe_allow_html=True)
last_insp_flow_value = insp_flow_container.empty() 
last_insp_flow_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #80ff80;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp = awp_container.empty()
last_awp.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #FFFFFF;font-synthesis: bold;text-align:center;'>O2</h2>", unsafe_allow_html=True)
last_awp_value = awp_container.empty()
last_awp_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #FFFFFF;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp1 = awp_container1.empty()
last_awp1.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'>Flow</h2>", unsafe_allow_html=True)
last_awp1_value = awp_container1.empty()
last_awp1_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp2 = awp_container2.empty()
last_awp2.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'>RR</h2>", unsafe_allow_html=True)
last_awp2_value = awp_container2.empty()
last_awp2_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp3 = awp_container3.empty()
last_awp3.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'>I:E</h2>", unsafe_allow_html=True)
last_awp3_value = awp_container3.empty()
last_awp3_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp4 = awp_container4.empty()
last_awp4.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #80ff80;font-synthesis: bold;text-align:center;'>PEEP</h2>", unsafe_allow_html=True)
last_awp4_value = awp_container4.empty()
last_awp4_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #80ff80;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

last_awp5 = awp_container5.empty()
last_awp5.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #87CEEB;font-synthesis: bold;text-align:center;'>VTi</h2>", unsafe_allow_html=True)
last_awp5_value = awp_container5.empty()
last_awp5_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #87CEEB;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)
last_awp6 = awp_container6.empty()
last_awp6.markdown("<h2 style='font-size:19px;gap: 0.1rem;color: #87CEEB;font-synthesis: bold;text-align:center;'>VTe</h2>", unsafe_allow_html=True)
last_awp6_value = awp_container6.empty()
last_awp6_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #87CEEB;font-synthesis: bold;text-align:center;'></p>", unsafe_allow_html=True)

counter=0

#Filling the gap for the first row  and the second row grid portion column


st.markdown("""
    <style> 
    div.css-ocqkz7.e1tzin5v3:nth-child(1),div.css-ocqkz7.e1tzin5v3:nth-child(2),div.css-ocqkz7.e1tzin5v3:nth-child(3){
       column-gap: 0.1rem;
    }
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
    <style>
    div.css-1r2k5ly.e1tzin5v0{
        row-gap: 0.1rem;
    }
    </style>
    """,unsafe_allow_html=True)

#Filling the gap for grid portion row
st.markdown("""
    <style>
    div.css-peenxw.e1tzin5v0{
        row-gap: 0.1rem;
    }
    </style>
    """,unsafe_allow_html=True)




#Background colour for Ppeak
st.markdown("""
    <style>
   h2#ppeak{
    background-color:#070D1C;
}
    </style>
    """,unsafe_allow_html=True)

#Background colour for Flow
st.markdown("""
    <style>
   h2#flow{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

#Background colour for Volume
st.markdown("""
    <style>
   h2#volume{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)
#Background colour for RR
st.markdown("""
    <style>
   h2#rr{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

#Background colour for I:E
st.markdown("""
    <style>
   h2#i-e{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

#Background colour for PEEP
st.markdown("""
    <style>
   h2#peep{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

#Background colour for VTi
st.markdown("""
    <style>
   h2#vti{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

#Background colour for VTe
st.markdown("""
    <style>
   h2#vte{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

#Background colour for p 
st.markdown("""
    <style>
   p{
background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

#Background colour for O2
st.markdown("""
    <style>
   h2#o2{
    background-color: #070D1C;
}
    </style>
    """,unsafe_allow_html=True)

# Background for Right side Icons
st.markdown("""
    <style>
   div.css-1l269bu.e1tzin5v1{
    background-color: #070D1C;
    text-align: center;
    justify-content: center;
    vertical-align: middle
}
    </style>
    """,unsafe_allow_html=True)

#Background for patient icon
st.markdown("""
    <style>
   div.css-103uxol.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)

#Background for Patient is Ventilated
st.markdown("""
    <style>
   div.css-949r0i.e1tzin5v1{
    background-color: #9EB8F5;
    border-radius: 8px;
}
    </style>
    """,unsafe_allow_html=True)


#Modes background colour
st.markdown("""
    <style>
   div.css-1m8p54g.e1tzin5v1{
    background-color: #070D1C;
    padding: 0;
    vertical-align: middle;
}
    </style>
    """,unsafe_allow_html=True)

# #Plotting colour
# st.markdown("""
#     <style>
#    div.user-select-none.svg-container{
#     # border-bottom-color: #535B6B;
#     # border-right-color: #535B6B;
#     border-left-color: #535B6B;
#     # border-right-style: solid;
#     # border-bottom-style: solid;
#     border-left-style: solid;
# }
#     </style>
#     """,unsafe_allow_html=True)

#Plotting colour
st.markdown("""
    <style>
   div.css-1f297am.e1tzin5v0{
    border-bottom-color: #535B6B;
    border-right-color: #535B6B;
    border-left-color: #535B6B;
    border-right-style: solid;
    border-bottom-style: solid;
    border-left-style: solid;
}
    </style>
    """,unsafe_allow_html=True)

# #Plotting colour
# st.markdown("""
#     <style>
#    div.css-1a32fsj.e19lei0e0:nth-last-of-type(n){
#     border-bottom-color: #535B6B;
#     # border-right-color: #535B6B;
#     # border-left-color: #535B6B;
#     # border-right-style: solid;
#     border-bottom-style: solid;
#     # border-left-style: solid;
# }
#     </style>
#     """,unsafe_allow_html=True)

#Background colour plotting box
st.markdown("""
    <style>
    h1#flow{
    border-top-color:#535B6B;
    border-right-color: #535B6B;
    border-left-color: #535B6B;
    border-right-style: solid;
    border-top-style: solid;
    border-left-style: solid;
}
    </style>
    """,unsafe_allow_html=True)

while True:
    try:  

        #Receiving value through websocket
        message = ws.recv()
        message1 = ws1.recv() 
        message2 = ws2.recv()
        data = json.loads(message)
        data1 = json.loads(message1)
        data2 = json.loads(message2)
        if n<=160:
            if counter<9:
                a.append(data)
                b.append(data2)
                counter=counter+1

            elif counter==9:
                counter = 0
                a.append(data)
                b.append(data2)

                # Update latest value display
                last_insp_flow_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #80ff80;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[4]), unsafe_allow_html=True)
                last_awp_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #FFFFFF;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[0]), unsafe_allow_html=True)
                last_awp1_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[1]), unsafe_allow_html=True)
                last_awp2_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[5]), unsafe_allow_html=True)
                last_awp3_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #ff904f;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[7]), unsafe_allow_html=True)
                last_awp4_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #80ff80;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[8]), unsafe_allow_html=True)
                last_awp5_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #87CEEB;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[2]), unsafe_allow_html=True)
                last_awp6_value.markdown("<p style='font-size:36px;gap: 0.1rem;color: #87CEEB;font-synthesis: bold;text-align:center;'>{}</p>".format(data1[3]), unsafe_allow_html=True)
                
                # Update chart
                for i in range(10):
                    # init_time=t.time()    
                    df_Inspiration_Flow = df_Inspiration_Flow.append({"Units":n+i, "Inspiration_Flow": a[i]}, ignore_index=True)
                     # Update the plot with the new data
                    fig = px.area(df_Inspiration_Flow.tail(161),x="Units",y="Inspiration_Flow",width=900,height=250)
                    # Update the placeholder with the new plot
                    chart.plotly_chart(fig.update_traces(line_color='orange').update_layout(yaxis_range=[0,120]))
                    df_Volume=df_Volume.append({"Units":n+i, "Volume": b[i]}, ignore_index=True)
                    fig1 = px.area(df_Volume.tail(161),x="Units",y="Volume",width=900,height=250)
                    # Update the placeholder with the new plot
                    chart1.plotly_chart(fig1.update_layout(yaxis_range=[0,2000]))

                    # final_time=t.time()
                    # time_taken=(final_time-init_time)
                    # rem_time=np.absolute(0.05-time_taken)
                    # t.sleep(rem_time)   
                a.clear()
                b.clear()
                n=n+10
        elif n>160:
            n=1 
        else:
            print("Data not received")
    except websocket.WebSocketConnectionClosedException:
        st.write("Web socket connection closed")
        break