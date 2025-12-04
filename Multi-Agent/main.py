from pipeline.orchestrator import run_pipeline

def main():
    print("=== Multi-Agent Content Pipeline ===")
    topic = input("Enter a topic: ").strip()

    if not topic:
        print("Topic cannot be empty")
        return
    
    print("\nRunning pipeline...")
    try:
        result = run_pipeline(topic)
    except Exception as e:
        print(f"error running pipeline: {e}")
        return 
    
    print("\n=== Refined Article ===")
    print(result["refined"])

    print("\n=== SEO Information ===")
    print(result["seo"])

    print(f"\nAll outputs saved to data/outputs/{topic.replace(' ', '_')}.json")

if __name__ == "__main__":
    main()
