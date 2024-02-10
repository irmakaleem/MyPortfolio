import requests 
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader) 
   
st.set_page_config(page_title="Portfolio", page_icon=":tada:", layout="wide")
names = ["irma kaleem", "omer khan"]
usernames = ["irma", "omer"] 
# cookie_expiry_days=30 
file_path = Path(__file__).parent / "hashed_pw.pkl"
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "irma.pdf"

  

with file_path.open("rb") as file:
   hashed_passwords= pickle.load(file) 
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# authenticator = stauth.Authenticate(names, usernames, hashed_passwords,"My_Webpage","abcdef",cookie_expiry_days=30) 
name, authentication_status, username = authenticator.login()

if authentication_status==False:
   st.error("Username/password is incorrect")

if authentication_status== None:
   st.warning("Please enter your username and password")

if authentication_status:      
    #header
    st.subheader("Hi, I'm Irma Kaleem :wave:")
    st.title("A BSIT Student")
    st.write("I am passionate about learning new things, and currently, I am learning Python. I am skilled in web designing using Figma and proficient in web development (HTML, CSS, WordPress). Additionally, I have knowledge in various programming languages such as Java, C, and C++, and a keen interest in AI." )
    EMAIL = "irmakaleem12@gmail.com"
    st.markdown(
    """
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    """,
    unsafe_allow_html=True
)

    SOCIAL_MEDIA ={
       "LinkedIn": "https://www.linkedin.com/in/irma-kaleem-246237235/?originalSubdomain=pk",
       "Github": "https://github.com/irmakaleem",
       "Twitter":"https://twitter.com/Irma96112",
    }
    # Define icons for each platform
    icons = {
    "LinkedIn": "<i class='fa-brands fa-linkedin'></i>",
    "Github": "<i class='fa-brands fa-github'></i>",
    "Twitter": "<i class='fa-brands fa-x-twitter'></i>",
}

    with open(resume_file, "rb") as pdf_file:
       PDFbyte = pdf_file.read()

    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)  
    st.write("#") 
    cols=st.columns(len(SOCIAL_MEDIA))
    for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
      cols[index].write(f"<a href='{link}' target='_blank'>{icons[platform]}</a> [{platform}]({link})", unsafe_allow_html=True)
    #   st.markdown(f"<a href='{link}' target='_blank'>{icons[platform]}</a>", unsafe_allow_html=True)
    #  cols[index].write(f"[{platform}]({link})")

    def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()

    def load_lottieurll(url):
        r=requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()

    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("styles/style.css")


    lottie_coding = load_lottieurl("https://lottie.host/67c06251-9fa0-497a-9ce7-1c235c943948/fyVpV9JHvJ.json")
    lottie_design = load_lottieurll("https://lottie.host/bb0d0fd5-435d-4194-ad7e-bac2426a5be5/ihTZKhWkGa.json")
    lottie_email = load_lottieurl("https://lottie.host/1f6b6841-45ea-479f-889b-4637b42fe714/AtD2PCCI42.json")


    with st.container():
        selected=option_menu(
            menu_title= None,
            options=["About", "Projects", "Contact"],
            icons=["house","book","envelope"],
            # menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )

    if selected == "About":
    # what i do
        with st.container():
         st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                As an ambitious designer, I bring a unique blend of skills and experiences to the table. Here's what I have done and what I can offer:

            - ✔️  Strong foundation in UI/UX design using Figma.
            - ✔️  Proficient in front-end development, creating HTML and CSS websites for practice.
            - ✔️  Experience in WordPress website development.
            - ✔️  Solid understanding of programming languages such as Java, C, and C++.
            - ✔️  Completed various projects utilizing these languages during university education.
            - ✔️  Eager to apply my diverse skill set and passion for design to create innovative and user-friendly digital experiences.
    """
            )

        with right_column:
         st_lottie(lottie_coding, height=500, key="coding")
        
    elif selected=="Projects":
     with st.container():
        st.write("---")
        st.header("My projects")
        st.write("##")
        left_column, right_column = st.columns(2)
        with right_column:
            st.subheader(" Design of Airlift website")   
            st.write(
                """
                In this design i replicate Airlift website 
    """
            )
            st.markdown("[Click Here To See The Design](https://www.figma.com/file/37f0O9aHtz1KGBC0rLsZdM/airlift?type=design&node-id=0-1&mode=design&t=RIMiMcIe7ecEt0V9-0)") 

            st.subheader(" Design of Furniture mobile app")   
            st.write(
                """
                I design this mobile app furniture design
    """
            )
            st.markdown("[Click Here To See The Design](https://www.figma.com/file/nzVBraiHyANsBizJTb1g2K/furniture-site-design?type=design&mode=design&t=RIMiMcIe7ecEt0V9-0)") 

            st.subheader(" Design of Quran App")   
            st.write(
                """
                I design Quran app
    """
            )
            st.markdown("[Click Here To See The Design](https://www.figma.com/file/FfDmLc5MPJP5mnPdGbRLH0/Untitled?type=design&mode=design&t=RIMiMcIe7ecEt0V9-0)") 

            st.subheader(" Design of E-commerce app")   
            st.write(
                """
                Designed a E commerce cosmetics app
    """
            )
            st.markdown("[Click Here To See The Design](https://www.figma.com/file/OThkV7nw5OLdHUnyCe75a9/Untitled?type=design&node-id=0-1&mode=design&t=8KlPQU5OPc2eQlUx-0)") 

        with left_column:
            st_lottie(lottie_design, height=500, key="design")

    elif selected=="Contact":
    #contact
      with st.container():
        st.write("---")
        st.header("Get in Touch With Me")
        st.write("##")    
        contact_form = """
        <form action="https://formsubmit.co/irmakaleem12@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder= "your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
    """
        
      left_column,right_column=st.columns(2)
      with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
      with right_column:
        st_lottie(lottie_email, height=300, key="email")
if authentication_status:
    if st.button("Reset Password"):
        try:
            if authenticator.reset_password(username):
                st.success('Password modified successfully')
        except Exception as e:
            st.error(e)
authenticator.logout()






 

    




