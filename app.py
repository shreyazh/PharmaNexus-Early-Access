# REPURPOSING DRUG USING KNOWLEDGE GRAPHS
#dependencies
import streamlit as st
import pandas as pd


st.set_page_config(page_title="PharmaNexus", 
                   page_icon=":pill:",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

def p_title(title):
    st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:24px;">{title}</h3>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: gray; font-size:28px;'>PharmaNexus - Drug Repurposing using Knowledge Graph Embeddings</h1>", unsafe_allow_html=True)
"""
[![Star](https://img.shields.io/github/stars/shreyazh/PharmaNexus.svg?logo=github&style=social)](https://github.com/shreyazh/PharmaNexus.git)
[![Follow](https://img.shields.io/twitter/follow/iamsrivastva?style=social)](https://www.twitter.com/iamsrivastva)
"""

#SIDEBAR

st.sidebar.header('I want to:')
nav = st.sidebar.radio('',['Get drug recommendations :pill:', 'Visualize graph :eyes:', 'About this App'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')

#CONTACT

expander = st.sidebar.expander('Contact')
expander.write("I'd love your feedback :smiley: Want to collaborate? Develop a project? Find me on [LinkedIn](https://www.linkedin.com/in/shreyashsrivastva/), [Twitter](https://twitter.com/iamsrivastva) and [Instagram](https://instagram.com/shreyazh)")


#DRUG RECOMMENDATION

if nav == 'Get drug recommendations :pill:':
    st.text('')
    p_title('Get drug recommendations')
    st.text('')

    disease_selection = st.selectbox("Select a disease", ["Dengue", "Chagas", "Malaria", "Yellow Fever", "Leishmaniasis", "Filariasis", "Schistosomiasis"], 
                                     help='Select a disease and perform predictions of new drugs on it. This project is focused on seven vector-borne diseases (dengue, chagas, malaria, yellow fever, leishmaniasis, filariasis, and schistosomiasis), but it can be extended to additional ones.')
    model_selection = st.selectbox("Select an embedding model", ["TransE", "TransR", "TransH", "UM", "DistMult", "RESCAL", "ERMLP"],
                                  help='Knowledge graph embedding models can encode biological information in a single mathematical space. Select an embedding model and perform drug predictions on the target diseases. This project is focused on seven embedding models (TransE, TransR, TransH, UM, DistMult, RESCAL, and ERMLP), which can be extended to additional ones.')

    if st.button("Get recommendations"):
        #Drug recommendations
        final_selection = disease_selection + model_selection
        ranking_file = pd.read_csv('embedding_models/' + final_selection + '.csv',  sep = ',')

        st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>Drugs recommendations<b></h3>", unsafe_allow_html=True)
        st.write(ranking_file)
        st.write('The interpretation of the values in the "score" column is model-dependent, and usually it cannot be directly interpreted as a probability.')
        st.write('The "in_clinical_trials" column states "yes" if the compound exists in ClinicalTrials.gov for the target diseases, and "no" otherwise.')

        #Disease direct connections in DRKG
        st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>Direct connections in DRKG for the target disease<b></h3>", unsafe_allow_html=True)
        st.write('Find below all entities in GNBR subgraph that are directly linked to the target disease. Compounds are highlighted in red.')

        import pandas as pd
        import streamlit.components.v1 as components

        #Visualize
        HtmlFile = open('graphs/knowledge_graph_' + disease_selection + '.html', 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        components.html(source_code, height = 625,width=750)

        #Model performance
        performance_file = pd.read_csv('embedding_models/performance_metrics.csv', sep = ';')
        # Filter rows where the 'final_selection' column matches final_selection
        filtered_data = performance_file[performance_file['final_selection'] == final_selection]
        st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>Embedding model performance<b></h3>", unsafe_allow_html=True)
        st.dataframe(filtered_data[['Measure', 'Value']], hide_index=True)


#VISUALIZING GRAPH HERE

if nav == 'Visualize graph :eyes:':
    st.text('')
    p_title('Visualize graph')
    st.text('')
    number_triples = st.selectbox('Select number of triples to sample from GNBR subgraph', ('50', '100', '250', '500'))

    st.write('Zoom in to see graph details')

    import pandas as pd
    import streamlit.components.v1 as components

    #ShowinG GNBR graph

    HtmlFile = open('graphs/knowledge_graph_gnbr_filter_' + number_triples + '.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 625,width=750)


#ABOUT THIS APP 

if nav == 'About this App':
    st.text('')
    p_title('About this App')
    st.text('')

    st.write("Drug repurposing methods can identify already approved drugs to treat them efficiently, reducing development costs and time. At the same time, knowledge graph embedding techniques can encode biological information in a single structure that allows users to operate relationships, extract information, learn connections, and make predictions to discover potential new relationships between existing drugs and vector-borne diseases.")
    st.write("In this project, we compare seven knowledge graph embedding models (TransE, TransR, TransH, UM, DistMult, RESCAL, and ERMLP) applied to Drug Repurposing Knowledge Graph (DRKG), analyzing their predictive performance over seven different vector-borne diseases (dengue, chagas, malaria, yellow fever, leishmaniasis, filariasis, and schistosomiasis), measuring their embedding quality and external performance against a ground-truth.")
    st.write("This project is based on the paper [Drug Repurposing Using Knowledge Graph Embeddings with a Focus on Vector-Borne Diseases: A Model Comparison](https://link.springer.com/chapter/10.1007/978-3-031-40942-4_8) as developed by [Shreyash Srivastva](https://www.linkedin.com/in/shreyashsrivastva/) and [Dr.Anshumaan Kumar](https://www.linkedin.com/in/anshumaan-kumar-7a4193281/) for BioHacks Hackathon 2024.")
