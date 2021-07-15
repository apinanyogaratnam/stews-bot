import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

question = input("Enter a question: ")
response = openai.Completion.create(
  engine="davinci",
  prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: {}\nA:".format(question),
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)

answer = response["choices"][0]["text"]

# response1 = openai.Answer.create(
#     search_model="ada", 
#     model="curie", 
#     question="Hello there!", 
#     file="file-2ksWL61f0Q5c5vCYOLwUuhPk", 
#     examples_context="In 2017, U.S. life expectancy was 78.6 years.", 
#     examples=[["What is human life expectancy in the United States?", "78 years."]], 
#     max_rerank=10,
#     max_tokens=5,
#     stop=["\n", "<|endoftext|>"]
# )

print(answer)
