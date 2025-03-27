#  Scam Details in India 

This repository hosts the codebase for a tool designed to retrieve and present information about scams in India. 
It leverages the power of Large Language Models (LLMs) through the Groq API, the DuckDuckGo search engine for information retrieval, and is built using Python. 
The application is accessible via a Streamlit interface.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_color_light.svg)](https://aibotapp-bujwlbqtjfdtsjqjbxmiz8.streamlit.app/)

## Overview

The goal of this project is to provide users with a platform to:

* **Search for information on known scams in India.** This can include various types of scams such as financial fraud, online scams, phishing attempts, and more.
* **Potentially identify patterns and details associated with different scams.** By using an LLM, the tool aims to synthesize information from search results to provide a more comprehensive understanding of a particular scam.
* **Offer a user-friendly interface** through Streamlit for easy interaction.

**Please note:** This tool is intended for informational purposes only. It should not be used as a definitive source for legal or financial advice. If you believe you have been a victim of a scam, please report it to the appropriate authorities.

## Features

* **LLM Powered:** Utilizes the Groq API to process and understand information about scams. This allows for more nuanced analysis of search results compared to simple keyword matching.
* **DuckDuckGo Integration:** Employs the DuckDuckGo search engine to gather relevant information from the web about reported scams.
* **Python Backend:** Built using Python, a versatile and widely used programming language.
* **Streamlit Frontend:** Provides an intuitive and easy-to-use web interface for users to interact with the tool.
* **Search Functionality:** Users can input keywords or descriptions related to a suspected scam to find relevant information.
* **Summarized Insights:** The LLM attempts to provide summarized insights based on the search results, potentially highlighting key details, modus operandi, and affected demographics.

## Technologies Used

* **Python:** The primary programming language used for the backend logic.
* **Groq API:** For leveraging the capabilities of Large Language Models to process and understand scam-related information.
* **DuckDuckGo Search:** Used for fetching information from the internet. The specific library used for integration (e.g., `duckduckgo-search`) would be in the requirements.
* **Streamlit:** For creating the interactive web application.

## Setup and Installation

To run this application locally, you will need to have Python installed on your system. Follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [repository URL]
    cd [repository directory name]
    ```
    *(Replace `[repository URL]` with the actual URL of this GitHub repository and `[repository directory name]` with the name of the cloned directory.)*

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure you have a `requirements.txt` file in the repository that lists the necessary libraries like `streamlit`, `duckduckgo-search`, and the Groq API client library.)*

3.  **Set up the Groq API key:**
    * You will need an API key from Groq to use their LLM service.
    * Store your Groq API key as an environment variable. For example:
        ```bash
        export GROQ_API_KEY="YOUR_GROQ_API_KEY"
        ```
        *(Replace `"YOUR_GROQ_API_KEY"` with your actual Groq API key.)*
    * Alternatively, the application might have a configuration file where you can input the API key. Refer to the application's specific code for details.

4.  **Run the Streamlit application:**
    ```bash
    streamlit run main.py
    ```
    *(Replace `main.py` with the name of your main Streamlit application file.)*

5.  **Access the application:** Once the application starts, Streamlit will provide a local URL (usually `http://localhost:8501`) that you can open in your web browser to use the tool.

## Usage

1.  Open the Streamlit application in your web browser.
2.  You will likely see a search bar or input field.
3.  Enter keywords or a description related to the scam you are interested in (e.g., "fake job offer India," "online investment fraud," "UPI scam").
4.  Click the "Search" or a similar button.
5.  The application will then use DuckDuckGo to search for relevant information and send the results to the Groq API for processing.
6.  The output will be displayed on the screen, potentially including:
    * Summarized information about the scam.
    * Details about how the scam operates.
    * Common indicators or red flags.
    * Potentially affected regions or demographics in India.

## Contributing

Contributions to this project are welcome. If you have suggestions for improvements, bug fixes, or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your contribution.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

Please ensure that your contributions adhere to any coding style guidelines or contribution guidelines outlined in the repository.

## Disclaimer

This tool provides information based on publicly available data and the interpretations of an LLM. The accuracy and completeness of the information cannot be guaranteed.
The developers are not responsible for any actions taken based on the information provided by this tool. 
Always exercise caution and verify information from multiple reliable sources before making any decisions related to potential scams. 
If you suspect you have been a victim of a scam, please contact your local law enforcement agency and relevant cybercrime authorities in India.

## License

NONE

## Contact US
