# from duckduckgo_search import DDGS
# def duck_duckgo_search_call():
#     print("DuckDuckGo search")
#     # print(DDGS().text("python programming", max_results=5))
#     res=DDGS().chat("summarize details jharkhand mining scams include source", model='claude-3-haiku')
#     print(res)
#     return "DuckDuckGo search"

# duck_duckgo_search_call()


from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
load_dotenv()
import os

def web_search_agent_duckduckgo(api_key_input,model="llama3-70b-8192",description="",question="",state="India"):
    web_agent = Agent(
        # model=Groq(id=model,api_key=os.getenv("Groq_api_key")),
        model=Groq(id=model,api_key=api_key_input),
        # description="""You are a helpful Scam News Analyst expert assistant.
        #                 Be remember you have to give the answer in brief summary within provided context
        #                 You reply with proper summary within given context.""",
        description=description,
        add_chat_history_to_messages=True,
        tools=[DuckDuckGo(fixed_max_results=10)],
        instructions=[
            f"""You are a Scam News Analyst Expert in the india region. 
            You have to provide the main/primary context of scam news which happened in {state}.""",
            "Always include the accessible source url of sources in bullet points.",
            "Please try to explain in a brief and clear manner.",
            "You can use the tools to search for the information.",

            # """As an expert Scam News Analyst specializing in the India region, "
            # "please provide the primary context of scam-related news originating from a specified {state}. "
            # "Ensure that all provided information includes accessible source URLs in a bulleted list."""
        ],
        show_tool_calls=True,
        markdown=True,
    )
    # response = web_agent.print_response(question, stream=False)
    response=web_agent.run(question, stream=False).to_dict()
    print(f"{response.keys()=}")
    return response["messages"][-1]["content"]

  