from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
import torch
import re

# -----------------------------
# Lazy-load LLM with GPU detection
# -----------------------------
llm = None
def get_llm():
    global llm
    if llm is None:
        print("Loading researcher LLM...")

        # Detect GPU
        device = 0 if torch.cuda.is_available() else -1
        if device == 0:
            print(f"GPU detected: {torch.cuda.get_device_name(0)}")
        else:
            print("No GPU detected, using CPU")

        # Use higher-quality instruction-tuned model
        generator = pipeline(
            "text-generation",
            model="gpt2-medium", #should be swapped for better model
            max_new_tokens=400,
            device=device,
            return_full_text=False
        )

        llm = HuggingFacePipeline(
            pipeline=generator,
            model_kwargs={"return_full_text": False}
        )
        print("Researcher LLM loaded")
    return llm

# -----------------------------
# Prompt template
# -----------------------------
research_prompt = PromptTemplate(
    input_variables=["topic"],
    template="[INST] Provide detailed, relevant information about the topic: '{topic}'. The information must be exactly 3 informative paragraphs. [/INST]"
)
# -----------------------------
# Research function (Minor Fix)
# -----------------------------
def research(topic: str) -> str:
    print(f"[DEBUG] Generating information for topic: {topic}")

    prompt_text = research_prompt.format(topic=topic)

    # 3. Invoke the LLM
    summary = str(get_llm().invoke(prompt_text))

    # 4. Clean up the response: We no longer need to replace(prompt_text, "") 
    # because of the 'return_full_text=False' setting above.
    summary = summary.replace(prompt_text,"")

    return summary