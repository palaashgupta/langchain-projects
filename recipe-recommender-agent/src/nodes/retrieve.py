from chromadb import PersistentClient
from src.config import CHROMA_DIR, TOP_K
from src.utils.embeddings import embed

def run(context):
    ingredients = context["normalized_ingredients"]
    query = ", ".join(ingredients)
    q_emb = embed(query)

    client = PersistentClient(path=str(CHROMA_DIR))

    col = client.get_collection("recipes")

    result = col.query(
        query_embeddings = [q_emb],
        n_results = TOP_K,
    )

    context["retrieved"] = result
    return context