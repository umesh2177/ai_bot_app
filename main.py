import logging
import streamlit as st
import duck_duckgo_search
def main_app():
    st.title("News Expert Agent APP")
    api_key = st.text_input("Enter your groq API Key:", "")

    model_options = ["llama3-70b-8192","llama-3.3-70b-versatile"]#"llama-3.1-8b-instant","mixtral-8x7b-32768"] 
    selected_model = st.selectbox("Select Model", model_options)

    # Display the selected model
    st.write("Selected Model:", selected_model) 
    question = st.text_input("Enter your question (optional):", "")

    options = st.multiselect(
            "Select options:",
            ["Summary", "Key Points","Members"]
        )


    if st.button("Submit"):
            if not api_key:
                st.warning("Please enter your Groq API Key.")
            else:
                with st.spinner('Analyzing...'):
                    if question and options:
                        if "Summary" in options:
                            description="""You are a helpful Scam News Analyst expert assistant.
                             Be remember you have to give the answer in brief summary within provided context
                             You reply with proper summary within given context."""
                            summary = duck_duckgo_search.web_search_agent_duckduckgo(description=description,question=question,model=selected_model)
                            # print(f"Agent Response: {summary}")
                            st.subheader("Summary:")
                            st.markdown(summary)

                        if "Key Points" in options:
                            description="""You are a helpful Scam News Analyst expert assistant .
                            Be remember you have to give the answer in points within provided context
                        You reply most keys ponits and factors within given context."""
                            key_points = duck_duckgo_search.web_search_agent_duckduckgo(description=description,question=question,model=selected_model)
                            # print(f"Agent Response: {key_points}")
                            st.subheader("Key Points:")
                            st.markdown(key_points)
                        if "Members" in options:
                            description="""You are a helpful Scam News Analyst expert assistant .
                             You reply with the names of all members involved in the scam and provide a brief history of their involvement within the given context.
                            """
                            key_Members = duck_duckgo_search.web_search_agent_duckduckgo(description=description,question=question,model=selected_model)
                            # print(f"Agent Response: {key_Members}")
                            st.subheader("Key Members:")
                            st.markdown(key_Members)

                    else:
                        st.warning("Please enter a Question and select at least one option summary/keys points.")





def setup_logger(log_file='logger.log'):
    """
    Sets up a logger to write logs to the specified file.

    Args:
        log_file (str, optional): The name of the log file. Defaults to 'logger.log'.

    Returns:
        logging.Logger: The configured logger object.
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)  # Set the handler's logging level (can be different from the logger's level)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    logger = setup_logger()

    logger.info("This is an informational message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")

    try:
        main_app()
    except Exception as e:
        logger.exception("An exception occurred:")
        print(e.with_traceback())