from transformers import pipeline
from newspaper import Article

# Load only once
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_articles(urls):
    all_summaries = []

    for url in urls:
        try:
            article = Article(url)
            article.download()
            article.parse()
            content = article.text

            if len(content.split()) < 50:
                continue

            summary = summarizer(content, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
            all_summaries.append(f"- {summary.strip()}")
        except Exception as e:
            print("Error summarizing:", e)
            continue

    return all_summaries
