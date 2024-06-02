import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Resume",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown("""
    <style>
    
           /* Remove blank space at top and bottom */ 
           .block-container {
               padding-top: 0rem;
               padding-bottom: 0rem;
            }
           
           /* Remove blank space at the center canvas */ 
           .st-emotion-cache-z5fcl4 {
               position: relative;
               top: -62px;
               }
           
           /* Make the toolbar transparent and the content below it clickable */ 
           .st-emotion-cache-18ni7ap {
               pointer-events: none;
               background: rgb(255 255 255 / 0%)
               }
           .st-emotion-cache-zq5wmm {
               pointer-events: auto;
               background: rgb(255 255 255);
               border-radius: 5px;
               }
    </style>
    """, unsafe_allow_html=True)
# Load profile picture
profile_picture = Image.open('img/profile.jpeg').rotate(90,expand=True)

# Profile Picture
st.image(profile_picture,width=150)

# Personal Information
st.title('Ronnie Castillo')
st.subheader('Data Scientist | Machine Learning Engineer')

st.write('''
**Email:** ronniemonsalecastillo@outlook.com 
**Phone:** +123 456 7890  
**LinkedIn:** [linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)  
**GitHub:** [github.com/johndoe](https://github.com/johndoe)
''')

# Summary
st.header('Summary')
st.write('''
Experienced Data Scientist with a demonstrated history of working in the information technology and services industry.
Skilled in Python, Machine Learning, Data Analysis, and Statistical Modeling. Strong engineering professional with a Master of Science (M.Sc.) focused in Data Science.
''')

# Work Experience
st.header('Work Experience')
st.subheader('Data Scientist | XYZ Company')
st.write('January 2020 - Present')
st.write('''
- Developed and deployed machine learning models for predictive analytics.
- Led a team of 5 data scientists on various projects.
- Improved model accuracy by 15% through feature engineering and hyperparameter tuning.
''')

st.subheader('Machine Learning Engineer | ABC Corp')
st.write('June 2018 - December 2019')
st.write('''
- Built and maintained end-to-end machine learning pipelines.
- Collaborated with cross-functional teams to deliver data-driven solutions.
- Automated data preprocessing workflows, reducing manual efforts by 30%.
''')

# Education
st.header('Education')
st.subheader('Master of Science in Data Science')
st.write('University of Example, 2016 - 2018')

st.subheader('Bachelor of Science in Computer Science')
st.write('University of Example, 2012 - 2016')

# Skills
st.header('Skills')
st.write('''
- Programming Languages: Python, R, SQL
- Machine Learning: Scikit-learn, TensorFlow, Keras
- Data Visualization: Matplotlib, Seaborn, Plotly
- Tools: Jupyter, Git, Docker
''')

# Projects
st.header('Projects')
st.subheader('Project Title 1')
st.write('''
Description of the project, tools used, and the outcome.
''')

st.subheader('Project Title 2')
st.write('''
Description of the project, tools used, and the outcome.
''')

# Certifications
st.header('Certifications')
st.write('''
- Certified Data Scientist, Data Science Council of America (DASCA)
- TensorFlow Developer Certificate, TensorFlow
''')

# Contact
st.header('Contact')
contact_form = """
<form action="https://formsubmit.co/YOUR_EMAIL@example.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
