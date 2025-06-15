def plan_goal(goal: str):
    goal = goal.lower()
    plan_steps = []

    if "bitcoin" in goal and "news" in goal and "summarize" in goal:
        plan_steps = ["fetch_bitcoin_news", "summarize_articles"]

    return plan_steps
