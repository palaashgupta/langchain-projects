import argparse
from .graph import build_graph

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ingredients", type = str, required = True, help = "Comma-separated ingredient list")
    args = parser.parse_args()

    graph = build_graph()
    result = graph.invoke({"ingredients": args.ingredients})

    print("Recipe Found: \n")
    print(result["answer"])

if __name__ == "__main__":
    main()