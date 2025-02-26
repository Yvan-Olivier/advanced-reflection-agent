import datetime

from dotenv import load_dotenv
load_dotenv()
import os
 
from langchain_core.prompts import (ChatPromptTemplate, MessagesPlaceholder)
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from schemas import AnswerQuestion, ReviseAnswer

# llm
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo")

actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are expert researcher.
Current time: {time}

1. {first_instruction}
2. Reflect and critique your answer. Be severe to maximize improvement.
3. Recommend search queries to research information and improve your answer.""",
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("system", "Be sure to always answer the question using the correct format."),
    ]
).partial(
    time=lambda: datetime.datetime.now().isoformat(),
)

# Instantiate the prompt template with the first instruction
first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction="Provide a detailed answer to the user's question (250 words)"
)

# chain
first_responder = first_responder_prompt_template | llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")
# revised instruction
revise_instructions = """Revise your previous answer using the new information.
    - You should use the previous critique to add important information to your answer.
        - You MUST include numerical citations in your revised answer to ensure it can be verified.
        - Add a "References" section to the bottom of your answer (which does not count towards the word limit). In form of:
            - [1] https://example.com
            - [2] https://example.com
    - You should use the previous critique to remove superfluous information from your answer and make SURE it is not more than 250 words.
"""

revised_prompt_template = actor_prompt_template.partial(
    first_instruction=revise_instructions
)

# revised chain
revisor = revised_prompt_template | llm.bind_tools(tools=[ReviseAnswer], tool_choice="ReviseAnswer")

if __name__ == "__main__":
    human_message = HumanMessage(
        content="Write about AI reflexion agents and the Language Agent Tree Search (LATS) algorithm."
    )

    chain = (
        first_responder_prompt_template
        | llm.with_structured_output(AnswerQuestion, include_raw=False)
    )

    res = chain.invoke({"messages": [human_message]})
    print(res)

