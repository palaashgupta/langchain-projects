from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

llm = None
def get_llm():
    global llm
    if llm is None:
        print("Loading editor LLM...")
        generator = pipeline("text-generation", 
                            model="gpt2-medium", #should be swapped for better model
                            max_new_tokens=250)
        llm = HuggingFacePipeline(pipeline=generator)
        print("Editor LLM loaded")
    return llm

edit_prompt = PromptTemplate(
    input_variables=["article"],
    template="Edit and improve the following article for clarity, grammar, and style:\n\n{article}"
)

def edit_article(article_text: str) -> str:
    prompt_text = edit_prompt.format(article=article_text)
    edited = str(get_llm().invoke(prompt_text))
    edited = edited.replace(prompt_text, "").strip()
    return edited
