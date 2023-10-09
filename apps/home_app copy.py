import os
import streamlit as st
from hydralit import HydraHeadApp




class HomeApp(HydraHeadApp):

    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        try:
            # Define the three-level categories and their corresponding images
            categories = {
                "Industry": {
                    "Retail": [
                        "shopping-cart.png",
                        "clothes-hanger.png",
                        "shopping-cart.png",
                        "clothes-hanger.png",
                    ],
                    "Manufacturing": [
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150"
                    ],
                    "Transportation": [
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150"
                    ]
                },
                "Functionality": {
                    "Data Analysis": [
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150"
                    ],
                    "Visualization": [
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150",
                        "https://via.placeholder.com/150"
                    ]
                }
            }

            st.markdown("<h1 style='text-align:left;padding: 0px 0px;color:black;font-size:200%;'>LLM Gallery</h1>",unsafe_allow_html=True)    
            st.markdown("")
            st.markdown("")

            # Display the categories in an expandable section in the left column
            left_col, right_col = st.columns([1, 6])
            
            ########## the need is to have a button entity for each subcategory, and have a way to refer to it
            # b.c we cannot create a dynamic variable for button entity
            # we leverage dictionary, to fix key, then let value be dynamic entity
            

            # # Calculate the total number of second-level items using list comprehensions and sum()
            # second_level_count = sum(len(subcategory) for category in categories.values() for subcategory in category.values())
            
            # # Define a list of entity names
            # entity_names = 
            # for i in range(second_level_count):
            #     entity_names = ["Entity 1", "Entity 2", "Entity 3"]

            # Create a dictionary to store button states
            button_states = {}
            with left_col:
                for category, subcategories in categories.items():
                    with st.expander(f"**{category}**", expanded=False):
                        for subcategory in subcategories:
                            button_states[f'{category}-{subcategory}'] = st.button(f"{subcategory}")

            # Display the images for the selected category and subcategory in the right column
            with right_col:
                # Create three columns for the images, col1 is placeholder for vertical space
                col1, col2, col3, col4 = st.columns([1, 4, 4, 4])


                ########## define a function here, so it know col2, 3, 4 and categories
                def display_image_by_category(category, subcategory):
                    images = categories[category][subcategory]
                    num_images = len(images)
                    images_per_row = 3

                    base_image_loc = "./images"
                    # Loop through and display images in each row
                    for i, image_name in enumerate(images):
                        if i in range(0, num_images, images_per_row):
                            with col2:
                                st.image(f"{base_image_loc}/{image_name}", width=150)
                        elif i in range(1, num_images, images_per_row):
                            with col3:
                                st.image(f"{base_image_loc}/{image_name}", width=150)
                        else:
                            with col4:
                                st.image(f"{base_image_loc}/{image_name}", width=150)
                ##########

                # default display
                # category = 'Industry'
                # subcategory = 'Manufacturing'
                # display_image_by_category(category, subcategory)

                for entity, state in button_states.items():
                    if state:   
                        category, subcategory = entity.split('-')

                        st.markdown(f"""<h2 
                            style='text-align:center; 
                            padding: 0px 0px; 
                            color:blue;
                            font-size:150%;'>
                            {subcategory}
                            </h2>""",
                            unsafe_allow_html=True)  
                        with col1:
                            st.markdown("")

                        with col2:

                            display_image_by_category(category, subcategory)
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


        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            raise e





