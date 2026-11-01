from advance_prompts import search_prompts
for p in search_prompts("project"):
    print(p["id"], p["title"])
