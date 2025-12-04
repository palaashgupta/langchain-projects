from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

llm = None
def get_llm():
    global llm
    if llm is None:
        print("Loading writer LLM...")
        generator = pipeline("text-generation", 
                            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", #should be swapped for better model
                            max_new_tokens=250)
        llm = HuggingFacePipeline(pipeline=generator)
        print("Writer LLM loaded")
    return llm

write_prompt = PromptTemplate(
    input_variables=["research"],
    template="You are a professional writer. Using only the research provided below, "
        "write a clear, concise, and well-structured article. Do not include any "
        "headings, prompts, or instructions—only the article content.\n\n"
        "Research:\n{research}"
)

def write_articles(research_text: str) -> str:
    # 700 tokens is a safe max for the research text (~2800 characters)
    MAX_TOKENS = 700 
    
    # ⚠️ Check the length of the research text 
    # (Note: This is a character-based estimate, which is simpler than a full token count)
    if len(research_text) > 2800:
        # Truncate to the safe limit
        research_text = research_text[:2800] + " [TRUNCATED FOR LLM CONTEXT LIMIT]"
        print("Warning: Research text was too long and has been truncated.")
        
    prompt_text = write_prompt.format(research=research_text)
    article = str(get_llm().invoke(prompt_text))
    article = article.replace(prompt_text, "").strip()
    return article