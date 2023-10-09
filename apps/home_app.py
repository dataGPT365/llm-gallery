import os
import streamlit as st
from hydralit import HydraHeadApp

import base64

# Define the three-level categories and their corresponding images
categories = {
    "Popular": {
        "Smart Q&A": {
            "subcategory_details": "Smart Q&A systems powered by GenAI can provide natural language answers to user questions spanning a wide range of topics and domains.",
            "sub-subcategories": [
                {   
                    "image_title": "RAG",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Retrieval Augmented Generation",
                },
                {   
                    "image_title": "Long window",
                    "image_href": "http://localhost:8501",
                    "image_name": "long_window.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "Chat to Doc",
                    "image_href": "http://localhost:8501",
                    "image_name": "chat_to_doc.png",
                    "image_description": "Retrieval Augmented Generation",
                },
                {   
                    "image_title": "Chat to Data",
                    "image_href": "http://localhost:8501",
                    "image_name": "chat_to_data.png",
                    "image_description": "Retrieval Augmented Generation",
                },
            ]
        },
        "Code Generation": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
    },
    "Industry": {
        "Retail": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
        "Finance": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
        "Manufacturing": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
        "Transportation": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
    },
    "Functionality": {
        "HR": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
        "IT": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
    },
    "Capability": {
        "Data & Analytics": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
        "Software Development": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
        "Project Management": {
            "subcategory_details": "Retrieval Augmented Generation",
            "sub-subcategories": [
                {   
                    "image_title": "Add to Prompt",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                },
                {   
                    "image_title": "PEFT",
                    "image_href": "http://localhost:8501",
                    "image_name": "rag.png",
                    "image_description": "Add additional knowledge to the prompt",
                }
            ]
        },
    },
}



########## define a function here, so it know col2, 3, 4 and categories
def display_image_by_category(category, subcategory, categories, col2, col3, col4):
    subcategory = categories[category][subcategory]
    sub_subcategories = subcategory['sub-subcategories']
    # the number of sub-subcategories is our total image
    num_of_images = len(sub_subcategories)
    images_per_row = 3

    
    ## to add a rounded edge around image, use st.markdown, we need to load image using base64
    ## width is now controled through container
    #image_width = 100

    base_image_url = "."
    base_image_loc = "images"

    # Loop through and display images in each row
    for i, sub_subcategory in enumerate(sub_subcategories):
        image_title       = sub_subcategory['image_title']
        image_href        = sub_subcategory['image_href']
        image_name        = sub_subcategory['image_name']
        image_description = sub_subcategory['image_description']

        image_loc = f"{base_image_url}/{base_image_loc}/{image_name}"                
        # Load your image file as bytes (e.g., using open() or urllib)
        # Here, we're using a placeholder image for demonstration
        with open(image_loc, "rb") as image_file:
            image_bytes = image_file.read()
            # Encode the image bytes to base64
            image_base64 = base64.b64encode(image_bytes).decode()

        if i in range(0, num_of_images, images_per_row):
            with col2:

                # Create an HTML image tag with the base64 encoded image                
                st.markdown(
                    f"""
                    
                    <div class='card'>
                        <a href = {image_href}>
                            <img src="data:image/jpg;base64,{image_base64}" alt='foo' class='card-image'>
                        <div class="card-content">
                            <div class="card-title">{image_title}</div>
                        </a>
                            <div class="card-description">{image_description}</div>
                        </div>
                    </div>
                    """,    
                    unsafe_allow_html=True)

        elif i in range(1, num_of_images, images_per_row):
            with col3:
                st.markdown(
                    f"""
                    
                    <div class='card'>
                        <a href = {image_href}>
                            <img src="data:image/jpg;base64,{image_base64}" alt='foo' class='card-image'>
                        <div class="card-content">
                            <div class="card-title">{image_title}</div>
                        </a>
                            <div class="card-description">{image_description}</div>
                        </div>
                    </div>
                    """,    
                    unsafe_allow_html=True)
        else:
            with col4:
                st.markdown(
                    f"""
                    
                    <div class='card'>
                        <a href = {image_href}>
                            <img src="data:image/jpg;base64,{image_base64}" alt='foo' class='card-image'>
                        <div class="card-content">
                            <div class="card-title">{image_title}</div>
                        </a>
                            <div class="card-description">{image_description}</div>
                        </div>
                    </div>
                    """,    
                    unsafe_allow_html=True)
##########
# Function to toggle the expander states
def toggle_expander():
    any_value = any(st.session_state.is_expanded.values())
    for category in categories.keys():
        st.session_state.is_expanded[category] = not any_value


class HomeApp(HydraHeadApp):

    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        try:
            title_col, button_col, _ = st.columns([1.4, 1, 10])

                    
            with title_col:
                html_content = """
                <h1 style='text-align:left;padding: 0px 0px;color:black;font-size:200%;'>
                    GenAI Gallery
                </h1>
                """
                st.markdown(html_content, unsafe_allow_html=True)
                st.markdown("")
                st.markdown("")

            with button_col:
                toggle = st.button("📁")
                if toggle:
                    toggle_expander()
            
            #toggle1 = st.button("*gallery*")

            # # Loop through the categories and create expanders
            # for category in categories:
            #     # Use the expander state from the dictionary
            #     is_expanded = expander_states[category]
                
            #     # Create an expander element with the state
            #     with st.expander(f"{category}", expanded=is_expanded):
            #         # Add content for each expander
            #         st.write(f"This is the content for {category}")

            # You can also use st.checkbox or st.button within expanders to control their individual states


            # Display the categories in an expandable section in the left column
            # make right column wide as 6-to-1 ratio
            left_col, right_col = st.columns([1, 6])
            
            ########## the need is to have a button entity for each subcategory, and have a way to refer to it
            # b.c we cannot create a dynamic variable for button entity
            # we leverage dictionary, to fix key, then let value be dynamic entity
            # Create a dictionary to store button states
            if 'is_expanded' not in st.session_state:
                st.session_state['is_expanded'] = {}
            
            button_states = {}
            with left_col:
                for category, subcategories in categories.items():

                    if category not in st.session_state['is_expanded']:
                        st.session_state['is_expanded'][category] = False
                    
                    # Name the expander as category
                    with st.expander(f"**{category}**", expanded=st.session_state['is_expanded'][category]):

                        for subcategory in subcategories:
                            # Name the button subcateogry, assign it as an entity in a dictionary, so we achieve dynamic variable
                            button_states[f'{category}-{subcategory}'] = st.button(f"{subcategory}")
                    


            # Display the images for the selected category and subcategory in the right column
            with right_col:
                for entity, state in button_states.items():
                    if state:   
                        category, subcategory = entity.split('-')
                        subcategory_details = categories[category][subcategory]['subcategory_details']

                        ## Middle left title
                        # Notice for padding: top, right, bottom, left, make left padding 50px
                        st.markdown(f"""<h2 
                                         style='text-align:left; 
                                                padding: 0px 0px 0px 50px;    
                                                color:blue;
                                                font-size:150%;'
                                        >
                                        {subcategory}
                                        </h2>
                                     """,
                                     unsafe_allow_html=True
                                    )  
                        
                        st.markdown(f"""<p
                                         style='text-align:left; 
                                                padding: 10px 0px 0px 50px;    
                                                color:black;
                                                font-size:100%;
                                                font-style: italic;
                                                '
                                        >
                                        {subcategory_details}
                                        </p>
                                     """,
                                     unsafe_allow_html=True
                                    )  


                        # Create three columns for the images, col1 is placeholder for vertical space
                        col1, col2, col3, col4 = st.columns([1, 4, 4, 4])



                        display_image_by_category(category, subcategory, categories, col2, col3, col4)
                        break


            import hydralit_components as hc

            # define what option labels and icons to display
            option_data = [
                {'icon':"fa fa-question-circle",
                 'label':"Unsure"},

                {'icon': "bi bi-hand-thumbs-down", 
                 'label':"Disagree"
                },

                {'icon': "bi bi-hand-thumbs-up", 
                 'label':"Agree",
                 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"}]},

            ]

            # override the theme, else it will use the Streamlit applied theme
            over_theme = {'txc_inactive': 'black','menu_background':'purple','txc_active':'yellow','option_active':'blue'}
            font_fmt = {'font-class':'h2','font-size':'150%'}


            # display a version version of the option bar
            op2 = hc.option_bar(option_definition      = option_data,
                                title                  = '',
                                key                    = 'PrimaryOption',
                                override_theme         = over_theme,
                                font_styling           = font_fmt,
                                horizontal_orientation = False)


            # # Create a dictionary to store the state of each expander
            # expander_states = {}

            # # Define a list of categories
            # categories = ["Category 1", "Category 2", "Category 3"]

            # Initialize expander states to False (collapsed)


            st.markdown("""
                <div class="footer">
                    <a href="https://www.flaticon.com/search?word=" title="icons">Icons created by Authors - Flaticon</a>
                    <p>&copy; DataGPT365</p>
                </div>""", unsafe_allow_html=True)

        except Exception as e:
            st.markdown("<h1 style='text-align:center;padding: 0px 0px;color:black;font-size:200%;'>Coming Soon ... </h1>",unsafe_allow_html=True)     
            raise e





