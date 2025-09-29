# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from  dotenv import load_dotenv
from graph.graph import app
#from langchain_core.prompts import PromptTemplate
#from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "what is agent memory?"}))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#def main():
   # print('Hello')
#information = """

   # """
#summary_template = """

    #"""
#summary_prompt_temple =PromptTemplate(
#input_variables=["information"], template=summary_template
#)
# Dùng Gemini thay cho OpenAI/Ollama
#llm = ChatGoogleGenerativeAI(
    #model="gemini-1.5-flash",  # hoặc gemini-1.5-pro
  # temperature=0
#)
#llm = ChatOllama(
   # model="gemma3:270m",
    #temperature=0
#)

#chain = summary_prompt_temple | llm

#response = chain.invoke(input={"information": information})
#print(response.content)
