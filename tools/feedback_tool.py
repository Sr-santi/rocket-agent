import json
import os
from typing import Dict, List

import requests
from crewai_tools import BaseTool
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

class TwitterAnalysisTool(BaseTool):
    name: str = "Twitter Analysis Tool"
    description: str = """Useful for fetching tweet replies, analyzing sentiment,
    summarizing replies, and fetching public metrics for a tweet."""

    def __init__(self):
        self.twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        self.jigsawstack_api_key = os.getenv('JIGSAWSTACK_API_KEY')

    def _run(self, tweet_id: str):
        # Fetch tweet replies
        replies = self._fetch_tweet_replies(tweet_id)

        # Analyze sentiment and summarize replies
        sentiment_summary = self._analyze_and_summarize_replies(replies)

        # Fetch public metrics
        public_metrics = self._fetch_public_metrics(tweet_id)

        # Combine results
        result = {
            "sentiment_summary": sentiment_summary,
            "public_metrics": public_metrics
        }

        return json.dumps(result, indent=2)

    def _fetch_tweet_replies(self, tweet_id: str) -> List[str]:
        url = f"https://api.twitter.com/2/tweets/{tweet_id}/replies"
        headers = {"Authorization": f"Bearer {self.twitter_bearer_token}"}
        params = {"tweet.fields": "text"}

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        return [tweet['text'] for tweet in data.get('data', [])]

    def _analyze_and_summarize_replies(self, replies: List[str]) -> Dict:
        sentiments = []
        for reply in replies:
            sentiment = self._analyze_sentiment(reply)
            sentiments.append(sentiment)

        # Calculate average sentiment
        avg_sentiment = sum(s['score'] for s in sentiments) / len(sentiments)

        # Summarize replies (you may want to use a more sophisticated summarization technique)
        summary = f"Analyzed {len(replies)} replies. Average sentiment: {avg_sentiment:.2f}"

        return {
            "summary": summary,
            "sentiments": sentiments
        }

    def _analyze_sentiment(self, text: str) -> Dict:
        url = "https://api.jigsawstack.com/v1/ai/sentiment"
        payload = {"text": text}
        headers = {
            "content-type": "application/json",
            "x-api-key": self.jigsawstack_api_key
        }

        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def _fetch_public_metrics(self, tweet_id: str) -> Dict:
        url = f"https://api.twitter.com/2/tweets/{tweet_id}"
        headers = {"Authorization": f"Bearer {self.twitter_bearer_token}"}
        params = {"tweet.fields": "public_metrics"}

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        return data['data']['public_metrics']