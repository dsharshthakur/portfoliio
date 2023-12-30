import streamlit as st

st.markdown("<h1 style = 'text-align:center; text-decoration:underline;'>Harsh Singh</h1>", unsafe_allow_html = True)
st.markdown("<h5 style = 'text-align:center'>(Data Scientist)</h6>", unsafe_allow_html = True)

st.markdown("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown('''
    
<h4>Welcome to My Portfolio</h4>
<p>Welcome to my corner of the digital universe, where data comes to life, and algorithms tell compelling stories. I am thrilled to have you here!

In this space, you'll find a curated collection of my adventures in the realms of Machine Learning and Natural Language Processing. Each project is a testament to my passion for transforming data into actionable insights, solving complex problems, and contributing to the evolving landscape of technology.

As you explore, I invite you to witness the synergy of creativity and code, where innovation meets precision. Whether you're a fellow data enthusiast, a hiring manager seeking top-tier talent, or simply someone curious about the possibilities of AI, I hope you find inspiration within these virtual walls.

Thank you for taking the time to explore my work.
Let the journey begin!</p>

Best Regards,<br>
<b>Harsh Singh</b>
    ''', unsafe_allow_html=True)
st.write("Email- thakurharshsingh1612@gmail.com")

st.markdown("<hr>", unsafe_allow_html=True)

#project1

with st.container() :
    st.markdown("<h4>Project 1 : AI-powered Email Assistant for Students and Professionals</h4>", unsafe_allow_html=True)
    st.markdown("<h6>Date: December 2023</h6>", unsafe_allow_html= True)
    st.markdown('''
             Project Description
             
            <p>The model is an AI-powered email assistant built using <b>Google Gemini</b> and <b>Langchain</b> to generate personalized and effective emails for students and professionals. Deployed on Streamlit. Ditch the writer's block, say goodbye to generic templates, and hello to confident, efficient communication, 
             you're a student acing that application or a professional making a lasting impression.</p>
            <h6>Technical Skills:</h6>
            <ol>
            
            <li>Natural Language Processing (NLP): Utilized Google Gemini's advanced language model to understand user intent and context.</li>
            
            <li>Conversational AI: Implemented Langchain for conversational interaction, guiding users through email composition with prompts and suggestions.</li>
            
            <li>Model Deployment: Successfully deployed the model on Streamlit, creating a user-friendly web interface for easy access and interaction.</li>
             </ol>  
                            ''', unsafe_allow_html=True)
    with st.expander(label = "Gallery" , expanded = True):
        st.image(image= "project1/image1.png")
        st.image(image = "project1/image2.png")

st.markdown("<br>", unsafe_allow_html=True)

#project 2
with st.container():
    st.markdown("<h4>Project 2 : Stock Price Prediction Model</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: November 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
            Project Description
            
            <p>I embarked on a project to predict stock prices using <b>LSTM</b> networks and deployed it through Streamlit, showcasing my practical skills as an aspiring Data Scientist. In this project, I collected a diverse dataset of historical stock prices, meticulously preparing it for analysis by addressing missing values and applying normalization techniques.
            Leveraging TensorFlow and Keras, I constructed an LSTM-based model, training it to discern patterns in stock movements for accurate predictions.
            <p>In this endeavor, I designed the application to enable users to search for and predict stock prices for more than <b>2000+ NSE registered companies</b>, as well as select foreign companies, offering a comprehensive scope for analysis and prediction.</p>
            <p>The project extends beyond the development of the predictive model; it encompasses an intuitive Streamlit dashboard that vividly ilustrates both actual and predicted trends. The interface not only provides users with a clear visual representation but also allows them to actively engage by predicting future closing prices for a specified number of days.</p>
            
            <p>This hands-on experience reflects my proficiency in machine learning, emphasizing my ability to process and analyze data effectively. Moreover, the deployment aspect underscores my commitment to delivering user-friendly solutions, making complex models accessible to a broader audience. This project encapsulates my practical problem-solving approach and showcases my dedication to contributing meaningfully to the field of data science.
                           </p> ''', unsafe_allow_html=True)
    with st.expander(label="Gallery"):
        st.image(image="project2/image1.png")
        st.image(image="project2/image2.png")

st.markdown("<br>", unsafe_allow_html=True)

#Project 3
with st.container():
    st.markdown("<h4>Project 3 : Your AI-Powered Language Hub</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: December 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
        Project Description:
        
    <h4>Introducing Streamlit Gemini: Your AI-Powered Language Hub</h4>

    <h4>Harnessing the Power of AI for Effortless Translation and Summarization</h4.

    <p>Streamlit Gemini puts the power of language understanding and generation at your fingertips with an intuitive, user-friendly app. Built on the cutting-edge capabilities of Google Gemini and LangChain, it offers:</p>
    
    <b>Key Features:</b>
    <ol>
    <li>Instant Summaries: Get to the heart of any text in seconds with concise, AI-generated summaries that capture key points and save you time.</li>
    <li>Accurate Translations: Break down language barriers with natural-sounding and grammatically correct translations across a wide range of languages.</li>
    <li>Streamlined Interface: Experience a user-friendly interface that makes interacting with AI simple and accessible, even for those without technical expertise.</li>
    </ol>
    <h4>Unlock a World of Possibilities:</h4>
    <ol>
    <li>Boost Productivity: Summarize lengthy documents, emails, and articles to quickly grasp essential information and make informed decisions.</li>
    <li>Enhance Learning: Translate and summarize educational materials to accelerate comprehension and retention, mastering new subjects and languages with ease.</li>
    <li>Expand Reach: Communicate effectively with global audiences, translate marketing materials, and reach customers across cultures and borders.</li>
    </ol>
    <p>Streamlit Gemini bridges the gap between languages and empowers you to communicate, learn, and explore like never before. Dive into a 
    </p>
            ''', unsafe_allow_html=True)

    with st.expander(label="Gallery"):
        st.image(image="project8/image1.png")
        st.image(image="project8/image2.png")









#project4
with st.container():

    st.markdown("<h4>Project 4 : Restaurant Recommendation System</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: October 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
        Project Description:
            
        <p>Developed a comprehensive restaurant recommendation model as a part of a personal project tailored for the <b>Ghaziabad</b> region, leveraging <b>natural language processing (NLP)</b> algorithms from the ground up.</p>
        <p>Conducted an extensive data collection process by proficiently employing web scraping methods, ensuring the acquisition of accurate and relevant data sets crucial for training the recommendation engine.</p>
        <p>Implemented various vital tasks, including data preprocessing, <b>feature engineering</b>,<b>eda</b> and <b>text encoding</b> showcasing a strong command of key data science concepts and techniques.</p>
        <p>Leveraged Python for the entire project, utilizing libraries such as <b>BeautifulSoup</b> and <b>Selenium</b> for web scraping, <b>pandas</b> for data manipulation, <b>Nltk</b> for model development, and Streamlit for seamless deployment, thereby highlighting comprehensive technical proficiency and adaptability.</p>
        <p>Ensured the seamless deployment and user-friendly accessibility of the model by leveraging the <b>Streamlit service</b>, allowing for a dynamic and interactive user experience.</p>
        <p>Gained valuable insights into data-driven decision-making, problem-solving, and project management, highlighting a strong commitment to achieving project goals.</p>
        <p>Demonstrated a keen interest in the practical application of machine learning and NLP in real-world scenarios, showcasing a passion for leveraging data to derive actionable insights and create tangible solutions.</p>
            ''', unsafe_allow_html=True)

    with st.expander(label="Gallery"):
        st.image(image="project3/image1.png")
        st.image(image="project3/image2.png")
        st.image(image="project3/image3.png")
        st.image(image="project3/image4.png")

st.markdown("<br>", unsafe_allow_html=True)


#project4
with st.container():
    st.markdown("<h4>Project 4 : Movie Recommendation System</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: October 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
        Project Description:
        <p>
        Designed and implemented a movie recommendation system as part of a personal project to apply data science and <b>machine learning</b> concepts.
        Utilized Python and relevant libraries (such as Pandas,nltk,streamlit and scikit-learn) to develop the system.
        </p>''', unsafe_allow_html=True)

    with st.expander(label="Gallery"):
        st.image(image="project4/image1.png")
        st.image(image="project4/image2.png")

st.markdown("<br>", unsafe_allow_html=True)

#project 5
with st.container():
    st.markdown("<h4>Project 5 : WhatsApp Chat Analysis</h4>",unsafe_allow_html=True)
    st.markdown("<h6>Date: September 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
            Project Description:
            <p>
            As a passionate and data-driven fresher aspiring to excel in the field of data science, I undertook a WhatsApp chat analysis project to demonstrate my analytical and problem-solving skills.
            Leveraging Python and data visualization tools, I collected and analyzed WhatsApp chat data to uncover valuable insights, such as communication patterns, monthly trends and frequently used keywords.
            </p>


            ''', unsafe_allow_html=True)

    with st.expander(label="Gallery"):
        st.image(image="project5/image1.png")
        st.info("Sorry can't show more images for this project because of privacy concerns.")

st.markdown("<br>", unsafe_allow_html=True)

#project 6
with st.container():

    st.markdown("<h4>Project 6 : Spam Email Classifier</h4>",unsafe_allow_html=True)
    st.markdown("<h6>Date: September 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
            Project Description:
            
            <p>
            Developed a machine learning-based spam email classifier as a data science project to gain hands-on experience in data science and natural language processing (NLP).
            </p>
            
            ''', unsafe_allow_html=True)

    with st.expander(label="Gallery"):
        st.image(image="project6/image1.png")


st.markdown("<br>", unsafe_allow_html=True)

#project 7
with st.container():

    st.markdown("<h4>Project 7 : Laptop Price Prediction</h4>",unsafe_allow_html=True)
    st.markdown("<h6>Date: August 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
            Project Description:
            
            <p>
            As a recent graduate aspiring to break into the field of data science,
             I undertook a laptop price prediction project that showcased my analytical and machine learning skills.
            </p>


            ''', unsafe_allow_html=True)

    with st.expander(label="Gallery"):
        st.image(image="project7/image1.png")

