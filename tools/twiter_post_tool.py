import os
import json
import requests
from crewai_tools import BaseTool
from dotenv import load_dotenv

load_dotenv()

class TwitterPostTool(BaseTool):
    name: str = "Twitter Post Tool"
    description: str = """Useful for creating a tweet with text and an image."""

    def __init__(self):
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    def _run(self, text: str, image_path: str):
        # First, upload the image
        media_id = self._upload_image(image_path)

        # Then, create the tweet with the uploaded image
        tweet_url = self._create_tweet(text, media_id)

        return json.dumps({"status": "success", "tweet_url": tweet_url})

    def _upload_image(self, image_path: str) -> str:
        url = "https://upload.twitter.com/1.1/media/upload.json"

        # Read the image file
        with open(image_path, 'rb') as image_file:
            files = {'media': image_file}

            auth = self._get_oauth1_auth()

            response = requests.post(url, files=files, auth=auth)

        if response.status_code != 200:
            raise Exception(f"Failed to upload image: {response.text}")

        media_id = response.json()['media_id_string']
        return media_id

    def _create_tweet(self, text: str, media_id: str) -> str:
        url = "https://api.twitter.com/2/tweets"

        payload = {
            "text": text,
            "media": {"media_ids": [media_id]}
        }

        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 201:
            raise Exception(f"Failed to create tweet: {response.text}")

        tweet_id = response.json()['data']['id']
        return f"https://twitter.com/user/status/{tweet_id}"

    def _get_oauth1_auth(self):
        return requests.auth.OAuth1(
            self.api_key,
            self.api_secret,
            self.access_token,
            self.access_token_secret
        )