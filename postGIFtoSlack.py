from slackclient import SlackClient
import os
import urllib2
import re



def postGIFtoSlack():
    # Set the API token for Slack
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    sc = SlackClient(slack_token)

    # Set the API token for The Cat API
    cat_api_token = os.environ["CAT_API_TOKEN"]

    # Build the URL for fetching image html from cat API
    catURL = (
        'http://thecatapi.com/api/images/get?format=html&api_key=' +
        cat_api_token +
        '&type=gif'
    )

    # Fetch the image html from cat api
    catImageURL = urllib2.urlopen(catURL)
    catImageHTML = catImageURL.read()

    # Strip down the HTML returned by The Cat API to get the image URL
    match = re.search(r'src="(.*)">', catImageHTML)
    catImagePath = match.group(1)

    # Set Slack channel we're going to post to
    slackChannel = "@chadallen"

    # Post image URL to slack channel
    sc.api_call(
        "chat.postMessage",
        channel=slackChannel,
        as_user="true",
        attachments=[{"title": "Cat GIF", "image_url": catImagePath}]
    )

    # Cheap debugging
    print catImagePath

postGIFtoSlack()