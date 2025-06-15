from agents.planner import plan_goal
from agents.news_agent import fetch_bitcoin_news
from agents.summary_agent import summarize_articles

def main():
    print("Device set to use cpu")
    print("Welcome to the Multi-Agent AI System!")
    goal = input("Enter your goal: ")
    plan = plan_goal(goal)

    if not plan:
        print("Could not understand goal.")
        return

    data = None  # carry result across agents

    for step in plan:
        if step == "fetch_bitcoin_news":
            data = fetch_bitcoin_news()
            if not data:
                print("No news found.")
                return

        elif step == "summarize_articles":
            print("\nSummaries from latest news:")
            summaries = summarize_articles(data)
            for i, summary in enumerate(summaries, 1):
                print(f"{i}. {summary}")

if __name__ == "__main__":
    main()
