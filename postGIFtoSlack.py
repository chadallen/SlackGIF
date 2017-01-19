from slackclient import SlackClient
import os
import urllib2
import re


def post_GIF_to_slack():
    # Set the API token for Slack
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    slack_client = SlackClient(slack_token)

    # Set the API token for The Cat API
    cat_api_token = os.environ["CAT_API_TOKEN"]

    # Build the URL for fetching image html from cat API
    cat_URL = (
        'http://thecatapi.com/api/images/get?format=html&api_key=' +
        cat_api_token +
        '&type=gif'
    )

    # Fetch the image html from cat api
    cat_image_URL = urllib2.urlopen(cat_URL)
    cat_image_HTML = cat_image_URL.read()

    # Strip down the HTML returned by The Cat API to get the image URL
    match = re.search(r'src="(.*)">', cat_image_HTML)
    cat_image_path = match.group(1)

    # Set Slack channel we're going to post to
    slack_channel = "@chadallen"

    # Post image URL to slack channel
    slack_client.api_call(
        "chat.postMessage",
        channel=slack_channel,
        as_user="true",
        attachments=[{"title": "Cat GIF", "image_url": cat_image_path}]
    )

    # Cheap debugging
    print cat_image_path

post_GIF_to_slack()