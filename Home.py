import streamlit as st
from Generator import generate_random_data
import json

def config():
    st.markdown('''
                <style>
                [data-testid="stToolbar"]{
                    display:none
                }
                </style>
                ''',unsafe_allow_html=True)



def main() :
    st.title('Welocme ... I am Chabane')
    st.markdown('---')
    st.subheader("If you're looking for fake data ,I've got you convered... \n I can provide you with a variety of sample data ;")
    st.caption('just choose the information you need.')
    st.markdown('---')
    code ='''
    data={"first name ":"Chabane","last name":"MESSOUS","email":"messouschabane77@gmail.com","id":525}
    '''
    st.text('data look like ')
    st.code(body=code,language='python')
    btn= st.button('get started')
    data=[]
    if btn :
        st.write("show sidebar")
    st.sidebar.header('fill the information you need ')
    with st.sidebar.form('data-form'):
        rows=st.number_input('how many row you wont : ',min_value=1,max_value=360,step=1)
        headers = st.multiselect('Choose the fields you want :  ',('first name','last name','id','email','phone','company'))
        formBtn= st.form_submit_button('Get Data')
        if formBtn : 
            data =generate_random_data(headers,rows) 
    if len(data)>0:
        json_data=json.dumps(data)
        st.markdown('---')
        st.header('Output')
        col1,col2 = st.columns(2)
        col1.subheader('You can downlaod your data')
        col2.download_button('downlad data',json_data,mime="text/json",file_name="data_fake.json")      
        expander=st.expander('view data')
        expander.write(data)
                
            
            
            
    
if __name__ == "__main__":
    config()
    main()