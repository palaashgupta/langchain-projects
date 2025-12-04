from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

llm = None
def get_llm():
    global llm
    if llm is None:
        print("Loading SEO LLM...")
        generator = pipeline("text-generation",
                            model="gpt2-medium", #should be swapped for better model
                            max_new_tokens=50)
        llm = HuggingFacePipeline(pipeline=generator)
        print("SEO LLM loaded")
    return llm

seo_prompt = PromptTemplate(
    input_variables=["article"],
    template="Suggest SEO-friendly keywords and meta description for the following article:\n\n{article}"
)

def generate_seo(article_text: str) -> str:
    prompt_text = seo_prompt.format(article=article_text)
    seo_info = str(get_llm().invoke(prompt_text))
    seo_info = seo_info.replace(prompt_text, "").strip()
    return seo_info
