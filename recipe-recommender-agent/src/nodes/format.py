def run(context):
    results = context["retrieved"]

    out = []

    for title, doc, meta in zip(results["metadatas"][0],
                                results["documents"][0],
                                results["metadatas"][0]):
        out.append(f"{meta['title']} - {meta["minutes"]} min\n")

    context["answer"] = "\n".join(out)
    return context

