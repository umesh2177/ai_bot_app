
import requests
from bs4 import BeautifulSoup
from groq_llm import groq_api
from logging import getLogger

class web_url_scraper:
    def __init__(self,web_url,api_key):
        self.web_url=web_url
        self.para=""
        self.api_key=api_key
        getLogger().info(f"Web URL: {self.web_url}")
        

    def web_url_scraper_para(self,web_url):
        try:
            response = requests.get(web_url)
            response.raise_for_status()  # Raise an exception for bad status codes

            soup = BeautifulSoup(response.content, "html.parser")

            # print(soup)

            # Example: Extract all the links on the page
            links = [link.get("href") for link in soup.find_all("a", href=True)]
            titles = [link.get("title") for link in soup.find_all("a")]
            # Example: Extract all the text from paragraph tags
            paragraphs = [p.get_text() for p in soup.find_all("p")]

            # paragraphs = soup.get_text()
            # You can customize this part to extract any data you need
            # based on the website's structure

            # return {
            #     "links": links,
            #     "title": titles,
            #     "paragraphs": paragraphs,
            # }
            self.para=" ".join(paragraphs)

        except requests.exceptions.RequestException as e:
            # getLogger().error(f"Error fetching URL: {e}")
            return "Provided URL is not valid or not accessible.",400

        except Exception as e:
            getLogger().error(f"An unexpected error occurred: {e}")
            return None

   

    def get_summary(self,input,model):
        """
        Generates a summary of the given text.

        Args:
            text: The input text.

        Returns:
            A summary of the text.
        """
        try:
            system_prompt = {
            "role": "system",
            "content":""" You are a helpful Scam News Analyst expert assistant.
                    Be remember you have to give the answerin brief summary within provided context
                    You reply with proper summary within given context.
                    """
        }

            self.web_url_scraper_para(self.web_url)
            if self.para == "":
                getLogger().error("Provided URL is not valid or not accessible.")
                return "Provided URL is not valid or not accessible.",400
            else:
                res=groq_api.groq_api_call(api_key=self.api_key,model=model,user_input=input,text_context=self.para,system_prompt=system_prompt)
                return res
        except Exception as e:
            getLogger().error(f"An unexpected error occurred: {e}")
            # print(f"An unexpected error occurred: {e}")
            return None


    def get_key_points(self,input,model):
        """
        Extracts key points from the given text.

        Args:
            text: The input text.

        Returns:
            A list of key points.
        """
        # Replace with your actual key point extraction logic (e.g., using NLP techniques)
        # This is a simple example using sentence splitting
        # sentences = text.split('.')
        # return sentences[:3]  # Extract the first 3 sentences as key points
        # pass
        system_prompt = {
            "role": "system",
            "content":""" You are a helpful Scam News Analyst expert assistant .
                    Be remember you have to give the answer in points within provided context
                    You reply most keys ponits and factors within given context.
                    """
        }

        self.web_url_scraper_para(self.web_url)
        self.web_url_scraper_para(self.web_url)
        if self.para == "":
            getLogger().error("Provided URL is not valid or not accessible.")
            return "Provided URL is not valid or not accessible.",400
        else:    
            res=groq_api.groq_api_call(api_key=self.api_key,model=model,user_input=input,text_context=self.para,system_prompt=system_prompt)
            return res
