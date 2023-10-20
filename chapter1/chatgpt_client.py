"""
This module is a client for the chatgpt api. It is a wrapper around the openai api.
"""
import os
import openai
from dotenv import load_dotenv, find_dotenv
# from myutils import api_call_simulator  # temporary decorator to simulate an api call to avoid api charges during development

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


class ChatGPTClient:
    """
    ChatGPTClient is a wrapper around the openai api.
    """

    def __init__(self, model: str = "gpt-4"):
        self.model = model

    # @api_call_simulator  # temporary decorator to simulate an api call during development to avoid api charges
    def get_completion_from_messages(self, message: str,
                                     temperature: float = 0
                                     ):
        """
        send prompt to openai api and return response.
        :param message: str
        :param temperature: float(0-1)
        :param max_tokens: int
        :return: http response
        """
        for _ in range(3):
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[{"role": "system",
                            "content": message}],
                    temperature=temperature,
                )
                return response.choices[0].message["content"]

            except openai.error.APIError as e:
                print(f"OpenAI API returned an API Error: {e} Trying again...")
            except openai.error.APIConnectionError as e:
                print(f"OpenAI API returned an API Error: {e} Trying again...")
            except openai.error.RateLimitError as e:
                print(f"OpenAI API returned an API Error: {e} Trying again...")
            except openai.error.Timeout as e:
                print(f"OpenAI API returned an API Error: {e} Trying again...")        
        return "OpenAI API returned an API Error: {e}"



    # @api_call_simulator
    def analyze_prompt(self, prompt: str):
        """
        Analyze a prompt and return the pros and cons
        :param prompt: str
        :return: dict
        """
        message = "you are a prompt engineer. you are given the prompt delimited with triple backticks.\
              analyze the prompt and provide pros and cons for the prompt and what can be improved." \
                  + "```" + prompt + "```"
        return self.get_completion_from_messages(message)

    # @api_call_simulator
    def modify_prompt(self, prompt: str):
        """
        Modify a prompt and return the modified prompt
        :param prompt: str
        :return: dict
       """
        message = "you are a prompt engineer. you are given the prompt delimited with triple backticks.\
              analyze the prompt and provide a new prompt that can get better and more accurate answers from chatGPT" \
                  + "```" + prompt + "```"
        return self.get_completion_from_messages(message)
