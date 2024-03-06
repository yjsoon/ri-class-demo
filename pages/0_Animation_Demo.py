import streamlit as st
import openai

def generate_image(prompt): 
    client = openai.OpenAI(api_key=st.secrets["openai_api_key"])
    response = client.images.generate(
        prompt=prompt,
        n=1,
        size="256x256"
    )  
    image_url = response.data[0].url
    return image_url

def image_gen() -> None:
    st.set_page_config(
        page_title="Image Generation", 
        page_icon="📸")
    st.markdown("# Create Your Animal")
    st.sidebar.header("Image Generation")

    # Split page into 2 columns
    col1, col2 = st.columns ([3, 5])

    # Set up the options
    image_style = col2.selectbox('Choose your image style',["A photo of a ","An oil painting of a "])
    animal = col2.selectbox('Choose your animal',["baby panda ","British shorthair cat ","deer","Shiba Inu dog ","raccoon"])
    activity = col2.selectbox('Choose your activity',["playing a guitar ","skateboarding ", "riding a bike", "studying for exams"])
    input_text = st.text_area("Any additional image styling requests")
    run_button = st.button("Run")

    prompt = f"Help me generate an image based on the \
        following: {image_style} {animal} {activity}, with \
        some additional information: {input_text}. \
        Make sure it's very amusing."

    if run_button and input_text.strip() != "": 
        with col1: 
            with st.spinner("Loading"):
                image_url = generate_image(prompt)
                st.image(image_url)


image_gen()
