### Step 1: Clone the Repository

Clone the repository containing the Streamlit app to your local machine.

```bash
git clone https://github.com/feliciien/integrating-dall-e-2-api-with-trulens-elevating-image-generation-capabilities
cd dall-e
```

### Step 2: Create and Activate a Virtual Environment

Create a virtual environment to isolate the dependencies for the app.

```bash
python3.8 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the required Python dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Step 4: Integrate TruLens Evals

Implement TruLens Evals to enhance the DALL-E 2 output. Follow TruLens documentation [here](https://colab.research.google.com/drive/1n77IGrPDO2XpeIVo_LQW0gY78enV-tY9?usp=sharing#scrollTo=Osch8gN27v1s) or integration guide for specific instructions.

```bash
import sys
!{sys.executable} -m pip install trulens
!{sys.executable} -m pip install torchvision
!{sys.executable} -m pip install matplotlib

### Step 5: Create and Activate a Conda Environment for DALL-E

Create a Conda environment named "dall-e" to isolate the dependencies for the app.

```bash
conda create -n dall-e
```

### Activate the "dall-e" Environment

Activate the "dall-e" environment using the following command:

```bash
conda activate dall-e
```

### Install Necessary Libraries

Install the necessary libraries using pip:

```bash
pip install streamlit langchain trulens-eval openai
```

### Set Up Streamlit Secrets

To incorporate your OpenAI API key and HuggingFace Access Token into Streamlit secrets, follow these steps:

1. Create a `.streamlit/secrets.toml` file within your project directory:

```bash
touch .streamlit/secrets.toml
```

### Configure API Keys

To configure your API keys for OpenAI and HuggingFace, follow these steps:

1. create `.streamlit/secrets.toml` file in your project directory.

2. Add the following lines to the file, replacing `"YOUR_API_KEY"` and `"YOUR_ACCESS_TOKEN"` with your respective keys:

```toml
OPENAI_API_KEY = "YOUR_API_KEY"
HUGGINGFACE_API_KEY = "YOUR_ACCESS_TOKEN"
```

### Step 6: Run the Streamlit App

Run the Streamlit app using the `streamlit` command.
```bash
pip install -r requirements.txt
```


```bash
streamlit run main.py
```

### Step 7: Access the App

Access the Streamlit app in your web browser by navigating to the URL provided by Streamlit, typically [http://localhost:8501](http://localhost:8501).

### Using the DALL-E Application

1. **Navigate to the Text-to-Image Feature**
   
   Go to the sidebar and select the "Text to Image" option.

   ![Text to Image Sidebar](https://i.ibb.co/60vMbLh/Capture-d-e-cran-2024-02-12-a-21-44-52.png)

2. **Enter Your Prompt**

   Once on the "Text to Image" page, enter your prompt. For example, you can input "beautiful pitbull".

   ![Example Prompt](https://i.ibb.co/6ZhjqSb/prompt.png)

3. **Click on Submit**

   After entering your prompt, click on the "Submit" button.

4. **View the Result**

   You will receive the resulting image based on your prompt.

   ![Resulting Image](https://i.ibb.co/BjBKMZH/result-dog.png)

5. **View Result in Editor**

   Additionally, you can view the result in the editor, which will display the output of Truelens.

   ![Truelens Result in Editor](https://i.ibb.co/TgJnPkV/truelens-result-on-terminal.png)
