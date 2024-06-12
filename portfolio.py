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
st.markdown("<br>", unsafe_allow_html=True)

# Projects

with st.container():
    st.markdown("<h4>Project 2 : Voice Assistant App</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: March 2024</h6>", unsafe_allow_html=True)
    st.markdown('''
    
    <p>This project is a simple voice assistant application, deployed using Streamlit, that allows users to interact with it via voice commands. The assistant leverages various powerful tools and libraries to process speech, generate responses, and handle user interactions efficiently.</p>
    
    <h5>Key Features:</h5>
    <ul>
        <li><strong>Voice Command Processing:</strong> The app utilizes <code>SpeechRecognition</code> for capturing and interpreting user voice inputs.</li>
        <li><strong>Natural Language Processing:</strong> The language processing capabilities are powered by <code>langchain</code> and <code>langchain-google-genai</code>, enabling the assistant to understand and respond to queries effectively.</li>
        <li><strong>Response Generation:</strong> For speech synthesis, the app uses <code>pyttsx3</code> and <code>gtts</code> to convert text responses into spoken words.</li>
        <li><strong>Efficient Query Handling:</strong> With <code>faiss-cpu</code>, the app ensures quick and efficient similarity searches for relevant information.</li>
        <li><strong>Audio Recording:</strong> The integration with <code>audio_recorder_streamlit</code> provides a seamless user experience for recording and processing voice commands.</li>
        <li><strong>Real-Time Audio Input:</strong> <code>pyaudio</code> facilitates real-time audio input for continuous and responsive interaction.</li>
    </ul>
    
    <h5>Tools and Libraries:</h5>
    <ul>
        <li><code>langchain</code> For building conversational AI and integrating language models.</li>
        <li><code>SpeechRecognition:</code> Captures and processes user voice input.</li>
        <li><code>faiss-cpu:</code> Enables efficient search and retrieval operations.</li>
        <li><code>audio_recorder_streamlit:</code> Provides an easy-to-use interface for recording audio in Streamlit apps.</li>
        <li><code>pyttsx3==2.90:</code> A text-to-speech conversion library for generating spoken responses.</li>
        <li><code>pyaudio==0.2.11:</code> Handles real-time audio input and processing.</li>
        <li><code>gtts:</code> Converts text to speech using Google's Text-to-Speech API.</li>
    </ul>
    
    <h5>Deployment:</h5>
    <p>The app is deployed on Streamlit, making it easily accessible via a web browser and providing a seamless and interactive user experience.</p>
           
            
                            ''', unsafe_allow_html=True)

 st.markdown("<br>", unsafe_allow_html=True)

    with st.expander(label="Gallery", expanded=True):
        st.image(image="project1/image1.png")
        st.image(image="project2/image2.png")
        st.image(image="project3/image3.png")


st.markdown("<br>", unsafe_allow_html=True)


with st.container():
    st.markdown("<h4>Project 3 : MatchMyCV: Elevate Your Resume to Job Standards</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: January 2024</h6>", unsafe_allow_html=True)
    st.markdown('''
             Project Description
      
       <p> This project addresses a critical challenge in the recruitment process: effectively matching candidates with job descriptions (JDs) and streamlining the initial screening stage. It leverages cutting-edge AI technologies to create a user-friendly, interactive experience for both candidates and employers.</p>
        
        <br>
        <h5>Key Features:</h5>
        
        <h6>AI-Driven Resume Matching:</h6>
        <li>Leverages LangChain and Gemini for deep semantic understanding of resumes and JDs.</li>
        <li>Generates tailored feedback for candidates to improve resume alignment with JD requirements.</li>
        
        <h6>Conversational Interface:</h6>
    
        <li>Empowers employers to "talk" to resumes using natural language queries.</li>
        <li>Facilitates efficient information extraction and candidate assessment.</li>
        
        <h6>Streamlit Deployment:</h6>
        <li>Offers a user-friendly web interface for seamless access and interaction.</li>
        
        <br>
        <h5>Benefits:</h5>
        
        <h6>Enhanced Candidate Experience:</h6>
        <li>Guides candidates towards creating more impactful resumes.</li>
        <li>Increases chances of job selection through targeted feedback.</li>
        
        <h6>Optimized Employer Efficiency:</h6>
        
        <li>Streamlines initial screening process.</li>
        <li>Facilitates informed decision-making through comprehensive resume insights.</li>
        
        <h6>Improved Hiring Outcomes:</h6>
        <li>Fosters better alignment between candidate qualifications and job requirements.</li>
        <li>Reduces time-to-hire and potential for bias.</li>
        
        <br>
        <h5>Tech Stack:</h5>
    
        <li>LangChain</li>
        <li>Gemini</li>
        <li>Streamlit</li>
        <li>Python</li>
        
            
                            ''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander(label="Gallery", expanded=True):
        st.image(image="project11/image1.png")
        st.image(image="project11/image2.png")
        st.image(image="project11/image3.png")
        st.image(image="project11/image4.png")
        st.image(image="project11/image5.png")

st.markdown("<br>", unsafe_allow_html=True)





with st.container() :
    st.markdown("<h4>Project 4 : AI-powered Email Assistant for Students and Professionals</h4>", unsafe_allow_html=True)
    st.markdown("<h6>Date: December 2023</h6>", unsafe_allow_html= True)
    st.markdown('''
             Project Description
             
            <p>The model is an AI-powered email assistant built using Google Gemini and Langchain to generate personalized and effective emails for students and professionals. Deployed on Streamlit. Ditch the writer's block, say goodbye to generic templates, and hello to confident, efficient communication, 
             you're a student acing that application or a professional making a lasting impression.</p>
            <h6>Technical Skills:</h6>
            <ol>
            
            <li>Natural Language Processing (NLP): Utilized Google Gemini's advanced language model to understand user intent and context.</li>
            
            <li>Conversational AI: Implemented Langchain for conversational interaction, guiding users through email composition with prompts and suggestions.</li>
            
            <li>Model Deployment: Successfully deployed the model on Streamlit, creating a user-friendly web interface for easy access and interaction.</li>
             </ol>  
                            ''', unsafe_allow_html=True)
    with st.expander(label = "Gallery" , expanded = True):
        st.image(image= "project10/image1.png")
        st.image(image = "project10/image2.png")

st.markdown("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown("<h4>Project 5 : Stock Price Prediction Model</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: November 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
            Project Description
            
            <p>I embarked on a project to predict stock prices using <b>LSTM</b> networks and deployed it through Streamlit, showcasing my practical skills as an aspiring Data Scientist. In this project, I collected a diverse dataset of historical stock prices, meticulously preparing it for analysis by addressing missing values and applying normalization techniques. Leveraging TensorFlow and Keras, I constructed an LSTM-based model, 
            training it to discern patterns in stock movements for accurate predictions.
            In this endeavor, I designed the application to enable users to search for and predict stock prices for more than <b>2000+ NSE registered companies</b>, as well as select foreign companies, offering a comprehensive scope for analysis and prediction.
            The project extends beyond the development of the predictive model; it encompasses an intuitive Streamlit dashboard that vividly ilustrates both actual and predicted trends. The interface not only provides users with a clear visual representation but also allows them to actively engage by predicting future closing prices for a specified number of days.
            
            This hands-on experience reflects my proficiency in machine learning, emphasizing my ability to process and analyze data effectively. Moreover, the deployment aspect underscores my commitment to delivering user-friendly solutions, making complex models accessible to a broader audience. This project encapsulates my practical problem-solving approach and showcases my dedication to contributing meaningfully to the field of data science.
                           </p> ''', unsafe_allow_html=True)
    with st.expander(label="Gallery"):
        st.image(image="project9/image1.png")
        st.image(image="project9/image2.png")

st.markdown("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown("<h4>Project 6 : Your AI-Powered Language Hub</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: December 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
        Project Description:
        
        <h4>Introducing: Your AI-Powered Language Hub</h4>

        <h6>Harnessing the Power of AI for Effortless Translation and Summarization</h6>

        <p>Streamlit Gemini puts the power of language understanding and generation at your fingertips with an intuitive, user-friendly app. Built on the cutting-edge capabilities of Google Gemini and LangChain, it offers:</p>
        
        <b>Key Features:</b>
        <ol>
        <li>Instant Summaries: Get to the heart of any text in seconds with concise, AI-generated summaries that capture key points and save you time.</li>
        <li>Accurate Translations: Break down language barriers with natural-sounding and grammatically correct translations across a wide range of languages.</li>
        <li>Streamlined Interface: Experience a user-friendly interface that makes interacting with AI simple and accessible, even for those without technical expertise.</li>
        </ol>
        <h5>Unlock a World of Possibilities:</h5>
        <ol>
        <li>Boost Productivity: Summarize lengthy documents, emails, and articles to quickly grasp essential information and make informed decisions.</li>
        <li>Enhance Learning: Translate and summarize educational materials to accelerate comprehension and retention, mastering new subjects and languages with ease.</li>
        <li>Expand Reach: Communicate effectively with global audiences, translate marketing materials, and reach customers across cultures and borders.</li>
        </ol>
        <p>Streamlit Gemini bridges the gap between languages and empowers you to communicate, learn, and explore like never before. Dive into a 
        </p>
            ''', unsafe_allow_html=True)

    with st.expander(label="Gallery", expanded = True):
        st.image(image="project8/image1.png")
        st.image(image="project8/image2.png")

st.markdown("<br>", unsafe_allow_html=True)

with st.container():

    st.markdown("<h4>Project 7 : Restaurant Recommendation System</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: October 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
        Project Description:
            
        <p>Developed a comprehensive restaurant recommendation model as a part of a personal project tailored for the Ghaziabad region, leveraging natural language processing (NLP) algorithms from the ground up.</p>
        <p>Conducted an extensive data collection process by proficiently employing web scraping methods, ensuring the acquisition of accurate and relevant data sets crucial for training the recommendation engine.</p>
        <p>Implemented various vital tasks, including data preprocessing, feature engineering,eda and text encoding showcasing a strong command of key data science concepts and techniques.</p>
        <p>Leveraged Python for the entire project, utilizing libraries such as BeautifulSoup and Selenium for web scraping, pandas for data manipulation, Nltk for model development, and Streamlit for seamless deployment, thereby highlighting comprehensive technical proficiency and adaptability.</p>
        <p>Ensured the seamless deployment and user-friendly accessibility of the model by leveraging the Streamlit service, allowing for a dynamic and interactive user experience.</p>
        <p>Gained valuable insights into data-driven decision-making, problem-solving, and project management, highlighting a strong commitment to achieving project goals.</p>
        <p>Demonstrated a keen interest in the practical application of machine learning and NLP in real-world scenarios, showcasing a passion for leveraging data to derive actionable insights and create tangible solutions.</p>
            ''', unsafe_allow_html=True)

    with st.expander(label="Gallery", expanded = True ):
        st.image(image="project7/image1.png")
        st.image(image="project7/image2.png")
        st.image(image="project7/image3.png")
        st.image(image="project7/image4.png")

st.markdown("<br>", unsafe_allow_html=True)


with st.container():
    st.markdown("<h4>Project 8: Movie Recommendation System</h4>",
                unsafe_allow_html=True)
    st.markdown("<h6>Date: October 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
        Project Description:
        <p>
        Designed and implemented a movie recommendation system as part of a personal project to apply data science and machine learning concepts.
        Utilized Python and relevant libraries (such as Pandas,nltk,streamlit and scikit-learn) to develop the system.
        </p>''', unsafe_allow_html=True)

    with st.expander(label="Gallery"):
        st.image(image="project6/image1.png")
        st.image(image="project6/image2.png")

st.markdown("<br>", unsafe_allow_html=True)


with st.container():
    st.markdown("<h4>Project 9 : WhatsApp Chat Analysis</h4>",unsafe_allow_html=True)
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


with st.container():

    st.markdown("<h4>Project 10 : Spam Email Classifier</h4>",unsafe_allow_html=True)
    st.markdown("<h6>Date: September 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
            Project Description:
            
            <p>
            Developed a machine learning-based spam email 
            classifier as a data science project to gain hands-on experience in data science and natural language processing (NLP).
            </p>


            ''', unsafe_allow_html=True)

    with st.expander(label="Gallery"):
        st.image(image="project4/image1.png")


st.markdown("<br>", unsafe_allow_html=True)


with st.container():

    st.markdown("<h4>Project 11: Laptop Price Prediction</h4>",unsafe_allow_html=True)
    st.markdown("<h6>Date: August 2023</h6>", unsafe_allow_html=True)
    st.markdown('''
            Project Description:
            
            <p>
            As a recent graduate aspiring to break into the field of data science,
             I undertook a laptop price prediction project that showcased my analytical and machine learning skills.
            </p>


            ''', unsafe_allow_html=True)

    with st.expander(label="Gallery"):
        st.image(image="project3/image1.png")

