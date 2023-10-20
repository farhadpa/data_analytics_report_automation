"""
This module contains chatGPT classes which are a costumized
wrapper around langchain's Models and Agents. 
"""

import os
from dotenv import load_dotenv
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.utilities import BingSearchAPIWrapper
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


class ChatGPTBase:

    def __init__(self, model_name='gpt-4', api_key=api_key):
        self.model_name = model_name
        self.api_key = api_key
        llm = ChatOpenAI(temperature=0, model=model_name)
        llm.openai_api_key = api_key
        self.llm = llm
        

class ChatGPTGoogleSearch(ChatGPTBase):
    
    def __init__(self, model_name='gpt-4', api_key=api_key):
        super().__init__(model_name, api_key)
        search = GoogleSerperAPIWrapper(gl="UK", hl="en", lr="lang_en")
        tools = [
            Tool(
                name='Search',
                func=search.results,
                description='useful for searching the web and finding up-to-date information and answers.'
            )
        ]

        self.agent = initialize_agent(
            tools, self.llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
        )


class ChatGPTBingSearch(ChatGPTBase):
    
    def __init__(self, model_name='gpt-4', api_key=api_key):
        super().__init__(model_name, api_key)
        search = BingSearchAPIWrapper(k=10)
        tools = [
            Tool(
                name='Search',
                func=search.run,
                description='useful for searching the web and finding up-to-date information and answers'
            )
        ]

        self.agent = initialize_agent(
            tools, self.llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
        )
