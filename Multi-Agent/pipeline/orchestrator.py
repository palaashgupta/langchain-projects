import json
import os
from agents import researcher
from agents import writer
from agents import editor
from agents import seo

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../data/outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_pipeline(topic:str)->dict:
    research_notes = researcher.research(topic)
    
    draft = writer.write_articles(research_notes)
 
    refined = editor.edit_article(draft)

    seo_info = seo.generate_seo(refined)

    result = {
        "topic": topic,
        "research_notes": research_notes,
        "draft": draft,
        "refined": refined,
        "seo": seo_info
    }

    filepath = os.path.join(OUTPUT_DIR, f"{topic.replace(' ', '_')}.json")
    with open(filepath,"w") as f:
        json.dump(result, f, indent=2)

    return result