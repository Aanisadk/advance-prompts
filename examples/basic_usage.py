from advance_prompts import get_prompt, list_categories
print("Categories:")
for category in list_categories(): print("-", category)
p = get_prompt("image-generation-001")
print(p["title"]); print(p["prompt"])
