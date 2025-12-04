import chromadb
from chromadb import PersistentClient
from chromadb.config import Settings
from tqdm import tqdm

from src.config import DATA_PATH, CHROMA_DIR
from src.utils.io import load_recipes
from src.utils.embeddings import embed

def recipe_to_text(r):
    return r["title"] + "\n" + "\n".join(r["ingredients"])

def main():
    recipes = load_recipes(DATA_PATH)

    client = PersistentClient(path=str(CHROMA_DIR))

    if "recipes" in [c.name for c in client.list_collections()]:
        client.delete_collection("recipes")

    collection = client.create_collection("recipes")

    for r in tqdm(recipes):
        text = recipe_to_text(r)
        e = embed(text)

        collection.add(
            ids = [r['id']],
            documents = [text],
            metadatas =[{"title": r["title"], "minutes": r["minutes"]}],
            embeddings = [e]
        )

    print("Vector DB ready!")

if __name__ == "__main__":
    main()