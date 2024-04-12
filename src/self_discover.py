import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

from prompts import SELECT_PROMPT, ADAPT_PROMPT, IMPLEMENT_PROMPT, REASONING_PROMPT, ANSWERING_PROMPT

load_dotenv()


def self_discover(task_description: str, streaming: bool = False):
    """
    SELF-DISCOVER prompt (see: https://arxiv.org/abs/2402.03620)

    Args:
        task_description (str): The example of the task

    Returns:
        str: the final answer
    """

    llm = ChatOpenAI(
        model="gpt-4-turbo", 
        temperature=0
    )

    # SELECT
    select_prompt = PromptTemplate(
        input_variables=["task_description"],
        template=SELECT_PROMPT,
    )
    select_chain = LLMChain(llm=llm, prompt=select_prompt)

    # ADAPT
    adapt_prompt = PromptTemplate(
        input_variables=["selected_modules"],
        template=ADAPT_PROMPT.replace("{task_description}", task_description),
    )
    adapt_chain = LLMChain(llm=llm, prompt=adapt_prompt)

    # IMPLEMENT
    implement_prompt = PromptTemplate(
        input_variables=["adapted_modules"],
        template=IMPLEMENT_PROMPT.replace("{task_description}", task_description),
    )
    implement_chain = LLMChain(llm=llm, prompt=implement_prompt)

    # REASONING
    reasoning_prompt = PromptTemplate(
        input_variables=["reasoning_structure"],
        template=REASONING_PROMPT.replace("{task_description}", task_description)
    )
    reasoning_chain = LLMChain(llm=llm, prompt=reasoning_prompt)

    # ANSWERING
    answering_prompt = PromptTemplate(
        input_variables=["reasoning_result"],
        template=ANSWERING_PROMPT.replace("{task_description}", task_description)
    )
    answering_chain = LLMChain(llm=llm, prompt=answering_prompt)

    overall_chain = SimpleSequentialChain(
        chains=[select_chain, adapt_chain, implement_chain, reasoning_chain, answering_chain],
        verbose=True,
    )
    result = overall_chain(task_description)

    return result["output"]
