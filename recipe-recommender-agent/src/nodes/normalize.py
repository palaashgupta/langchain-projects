def run(context):
    raw = context.get("ingredients", "")
    normalized = [i.strip().lower() for i in raw.split(",")]
    context["normalized_ingredients"] = normalized
    return context
