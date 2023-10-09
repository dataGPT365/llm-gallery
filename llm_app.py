from hydralit import HydraApp
import hydralit_components as hc
import apps
#from apps import signup
import streamlit as st
import datetime


#make it look nice from the start
st.set_page_config(layout='wide',initial_sidebar_state='collapsed')

page_layout = """
    <style>


        /* Style for the card container */
        .card {
            display: flex; /* Use flexbox to arrange elements horizontally */
            align-items: center; /* Vertically align elements in the middle */
            border: 1px solid #ccc;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            background-color: #f5f5f5;
            width: 350px;
        }

        /* Style for the card image */
        .card-image {
            max-width: 100px; /* Adjust the image width as needed */
            height: auto;
            border-radius: 5px;
            margin-right: 20px; /* Add some margin to separate image and text */
        }

        /* Style for the card title */
        .card-title {
            font-size: 18px;
            font-weight: bold;
            color: #444;
        }

        /* Style for the card description */
        .card-description {
            font-size: 16px;
            color: #666;
            margin-top: 20px;
        }

        /* Footer styles */
        .footer {
            text-align: center;
            background-color: #f5f5f5; 
            color: black;
            padding: 1px;
        }

    </style>
    """
st.markdown(page_layout, unsafe_allow_html=True)



if __name__ == '__main__':
    over_theme = {'txc_inactive': 'white','menu_background':'blue','txc_active':'black','option_active':'white'}
    #this is the host application, we add children to it and that's it!
    app = HydraApp(
        #   title                  = 'Secure Hydralit Data Explorer',
        #   favicon                = "🐙",
          hide_streamlit_markers = True, #False,
          #use_navbar             = True,
          #navbar_sticky          = True,
          #navbar_animation       = True,
          navbar_theme           = over_theme
    )

    #Home button will be in the middle of the nav list now
    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='LLM Gallery'), is_home=True)

    #add all your application classes here
    #app.add_app("Cheat Sheet", icon="📚", app=apps.CheatApp(title="Cheat Sheet"))
    # app.add_app("Sequency Denoising",icon="🔊", app=apps.WalshApp(title="Sequency Denoising"))
    # app.add_app("Sequency (Secure)",icon="🔊🔒", app=apps.WalshAppSecure(title="Sequency (Secure)"))
    #app.add_app("Solar Mach", icon="🛰️", app=apps.SolarMach(title="Solar Mach"))
    #app.add_app("Spacy NLP", icon="⌨️", app=apps.SpacyNLP(title="Spacy NLP"))
    #app.add_app("Uber Pickups", icon="🚖", app=apps.UberNYC(title="Uber Pickups"))
    #app.add_app("Solar Mach", icon="🛰️", app=apps.SolarMach(title="Solar Mach"))
    app.add_app("Loader Playground", icon="⏲️", app=apps.LoaderTestApp(title="Loader Playground"))
    #app.add_app("Cookie Cutter", icon="🍪", app=apps.CookieCutterApp(title="Cookie Cutter"))

    #we have added a sign-up app to demonstrate the ability to run an unsecure app
    #only 1 unsecure app is allowed
    app.add_app("Signup", icon="🛰️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)

    #we want to have secure access for this HydraApp, so we provide a login application
    #optional logout label, can be blank for something nicer!
    # app.add_app("Login", apps.LoginApp(title='Login'),is_login=True) 

    # #specify a custom loading app for a custom transition between apps, this includes a nice custom spinner
    # app.add_loader_app(apps.MyLoadingApp(delay=0))

    #we can inject a method to be called everytime a user logs out
    #---------------------------------------------------------------------
    # @app.logout_callback
    # def mylogout_cb():
    #     print('I was called from Hydralit at logout!')
    #---------------------------------------------------------------------

    #we can inject a method to be called everytime a user logs in
    #---------------------------------------------------------------------
    # @app.login_callback
    # def mylogin_cb():
    #     print('I was called from Hydralit at login!')
    #---------------------------------------------------------------------

    # if st.button('click me'):
    #     st.info('You clicked at: {}'.format(datetime.datetime.now()))


    if st.sidebar.button('About LLM Gallery'):
        st.info('You clicked at: {}'.format(datetime.datetime.now()))

    # #can apply customisation to almost all the properties of the card, including the progress bar
    # theme_bad = {'bgcolor': '#FFF0F0','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
    # theme_neutral = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
    # theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}

    # cc = st.columns(4)

    # with cc[0]:
    # # can just use 'good', 'bad', 'neutral' sentiment to auto color the card
    #     hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good',bar_value=77)

    # with cc[1]:
    #     hc.info_card(title='Some BAD BAD', content='This is really bad',bar_value=12,theme_override=theme_bad)

    # with cc[2]:
    #     hc.info_card(title='Some NEURAL', content='Oh yeah, sure.', sentiment='neutral',bar_value=55)

    # with cc[3]:
    # #customise the the theming for a neutral content
    #     hc.info_card(title='Some NEURAL',content='Maybe...',key='sec',bar_value=5,theme_override=theme_neutral)


    # Create a dictionary of industry names and their respective image URLs
    # industry_images = {
    #     "Finance": "https://example.com/finance_image.jpg",
    #     "Healthcare": "https://example.com/healthcare_image.jpg",
    #     "Technology": "https://example.com/technology_image.jpg",
    #     # Add more industries and image URLs here
    # }

    # # Create a gallery of images
    # for industry, image_url in industry_images.items():
    #     st.subheader(industry)
    #     st.image(image_url, use_column_width=True, caption=industry)


    #get the id of the menu item clicked
    #st.info(f"{menu_id}")

    #if we want to auto login a guest but still have a secure app, we can assign a guest account and go straight in
    app.enable_guest_access()

    #check user access level to determine what should be shown on the menu
    user_access_level, username = app.check_access()

    # print(user_access_level)
    #user_access_level = 0
    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
    if user_access_level > 1:
        complex_nav = {
            'Home': ['Home'],
            'Loader Playground': ['Loader Playground'],
            'Intro 🏆': ['Cheat Sheet',"Solar Mach"],
            'Hotstepper 🔥': ["Sequency Denoising","Sequency (Secure)"],
            'Clustering': ["Uber Pickups"],
            'NLP': ["Spacy NLP"],
            'Cookie Cutter': ['Cookie Cutter']
        }
    elif user_access_level == 1:
        complex_nav = {
            'Home': ['Home'],
            'Loader Playground': ['Loader Playground'],
            # 'Intro 🏆': ['Cheat Sheet',"Solar Mach"],
            # 'Hotstepper 🔥': ["Sequency Denoising"],
            # 'Clustering': ["Uber Pickups"],
            # 'NLP': ["Spacy NLP"],
            # 'Cookie Cutter': ['Cookie Cutter']
        }
        # complex_nav = {
        #     'Home': ['Home'],
        #     'Loader Playground': ['Loader Playground'],
        #     'Intro 🏆': ['Cheat Sheet',"Solar Mach"],
        #     'Hotstepper 🔥': ["Sequency Denoising"],
        #     'Clustering': ["Uber Pickups"],
        #     'NLP': ["Spacy NLP"],
        #     'Cookie Cutter': ['Cookie Cutter']
        # }
    else:
        complex_nav = {
            'Home': ['Home'],
        }

  
    #and finally just the entire app and all the children.
    app.run(complex_nav)




    #print user movements and current login details used by Hydralit
    #---------------------------------------------------------------------
    # user_access_level, username = app.check_access()
    # prev_app, curr_app = app.get_nav_transition()
    # print(prev_app,'- >', curr_app)
    # print(int(user_access_level),'- >', username)
    # print('Other Nav after: ',app.session_state.other_nav_app)
    #---------------------------------------------------------------------
