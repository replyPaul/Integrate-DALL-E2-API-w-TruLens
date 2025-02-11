import streamlit as st
from openai import OpenAI

client = OpenAI()

def page2():
    st.markdown("# OpenAI DALL·E Image Generation :potted_plant: ")
    st.subheader("❄ Generate upto 4 numbers of novel Images using your creative prompts ❄")
    st.info("""###### NOTE: you can download image by \
    right clicking on the image and select save image as option""")

    with st.form(key='form'):
        prompt = st.text_input(label='Enter text prompt for image generation')
        size = st.selectbox('Select size of the images', 
                            ('256x256', '512x512', '1024x1024'))
        num_images = st.selectbox('Enter number of images to be generated', (1,2,3,4))
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if prompt:
            response = client.images.generate(prompt = prompt,
            n = num_images,
            size=size)
            
            for idx in range(num_images):
                image_url = response.data[idx].url

                st.image(image_url, caption=f"Generated image: {idx+1}",
                         use_column_width=True)
