from advance_prompts import all_prompts, get_prompt, list_categories, search_prompts
def test_count(): assert len(all_prompts()) == 200
def test_lookup(): assert get_prompt("claude-001")["title"] == "XML task brief"
def test_categories(): assert len(list_categories()) == 10
def test_search(): assert search_prompts("project")
def test_missing():
    try: get_prompt("missing-id")
    except KeyError: return
    assert False
