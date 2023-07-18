import streamlit as st 
from PIL import Image


# set config page
st.set_page_config(page_title="itsmebraiyen",page_icon=":tada:",layout="wide")


#header section ( container its like a function)
with st.container():
    st.subheader("Hi, i am Braiyen Massora:wave:")
    st.title("A Data Engineer and Flutter Developer")
    st.markdown("Experience working as Data Engineering and Technical Documentation to describe the functionalities and features of a product,  \nfor the software product development and engineering industry.")

with st.container():
    st.write("------")
    x_left,x_right = st.columns(2)
    with x_left :
        st.header("What I do")
        st.write("")
        st.markdown('**Data Engineer at CODEX powered by Telkom Indonesia**')
        st.markdown('Apr 2021 - Present')
        st.caption("""
                 
                    - Data ingestion
                    - Data standardization
                    - Monitoring and logging
                    - Data pipeline process
                    - Working with other teams, Data Analyst and Data Scientists

                    Tools:
                    - Apache Airflow
                    - Apache Spark
                    - Google Cloud Platform ( BigQuey, VM, CloudSQL,Cloud Run )
                    - MongoDB
                    - PostgreSQL
                    - Airbyte
                    - Apache Drill
                 """)
        st.markdown('**Software Documentation Engineer at Telkom Indonesia** ')
        st.markdown('Sep 2018 - Present')
        st.caption("""
                   
                    - Create, update, and maintain all documentation each of software/product life cycle.
                    - Within a cross-functional team, collaborate with other developers, software architects, quality assurance, 
                    UI designers, UX researchers, product owners, and scrum masters.
                    - Scripting for API Documentation and Mockup.
                    - Learn multiple tools for the job.
                    - Create data model, diagram, workflow, and so forth to assist the technical team.

                    Tools
                    - Confluence
                    - Postman
                    - Swagger
                    - RDBMS/Non RDBMS
                    - Agile Methodology
                   """)
        st.markdown('**Software Documentation Engineer at Telkom Indonesia** ')
        st.markdown('Sep 2018 - Present')
        st.caption("""
                   
                    - Create, update, and maintain all documentation each of software/product life cycle.
                    - Within a cross-functional team, collaborate with other developers, software architects, quality assurance, 
                    UI designers, UX researchers, product owners, and scrum masters.
                    - Scripting for API Documentation and Mockup.
                    - Learn multiple tools for the job.
                    - Create data model, diagram, workflow, and so forth to assist the technical team.

                    Tools
                    - Confluence
                    - Postman
                    - Swagger
                    - RDBMS/Non RDBMS
                    - Agile Methodology
                   """)
        
# what i do 
with st.container():
    st.write("------")
    x_left,x_right = st.columns(2)
    with x_left :
        st.header("Projects")
        st.write("")
        st.markdown("Build Data Pipelines with Apache Airflow")
        st.caption("Develop and maintaining a data pipeline for the Talent Management System project at CODEX, ensuring proper documentation for the pipeline, service, and data integration solutions utilizing MongoDB, Spark, and Google Cloud Platform to accommodate evolving business requirements.")
    
        st.write("")
        st.markdown("Build Resume Parser with NLP")
        st.caption("Develop and maintaining a data pipeline for the Talent Management System project at CODEX, ensuring proper documentation for the pipeline, service, and data integration solutions utilizing MongoDB, Spark, and Google Cloud Platform to accommodate evolving business requirements.")
      
        st.write("")
        st.markdown("Build Booking Tickets App")
        st.caption("Build a booking ticket app using Flutter and Firebase that helps people book tickets for destinations and seats.")
  
# bottom section (container is like a function)
with st.container():
    
    st.write("")
    st.markdown('<style>.centered-caption {text-align: center;}</style>', unsafe_allow_html=True)
    st.caption('<p class="love centered-caption">Made with ❤️ in Jakarta</p>', unsafe_allow_html=True)
