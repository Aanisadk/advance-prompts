import json
from functools import lru_cache
from importlib.resources import files

@lru_cache(maxsize=1)
def all_prompts():
    """Return the bundled prompt catalogue."""
    path = files("advance_prompts").joinpath("data/all_prompts.json")
    return json.loads(path.read_text(encoding="utf-8"))

def get_prompt(prompt_id):
    """Get one prompt by its stable ID."""
    for item in all_prompts():
        if item["id"] == prompt_id: return item
    raise KeyError(f"Prompt not found: {prompt_id}")

def list_categories():
    """List prompt categories."""
    return sorted({item["category"] for item in all_prompts()})

def search_prompts(query, category=None):
    """Search prompt ID, title, description, and body."""
    q = str(query).casefold().strip(); out=[]
    for item in all_prompts():
        if category and item["category"].casefold() != str(category).casefold(): continue
        hay = " ".join([item["id"],item["title"],item["description"],item["prompt"]]).casefold()
        if q in hay: out.append(item)
    return out
