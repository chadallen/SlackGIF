from slackclient import SlackClient
import os
import urllib2
import re

slack_token = os.environ["SLACK_BOT_TOKEN"]
sc = SlackClient(slack_token)

cat_api_token = os.environ["CAT_API_TOKEN"]
print slack_token

# URL for fetching image html from cat API
catURL = (
    'http://thecatapi.com/api/images/get?format=html&api_key=' +
    cat_api_token +
    '&type=gif'
)

# Fetch the image html from cat api
catImageURL = urllib2.urlopen(catURL)
catImageHTML = catImageURL.read()

# Get just the image path from image html
match = re.search(r'src="(.*)">', catImageHTML)
catImagePath = match.group(1)

print catImagePath


sc.api_call(
    "chat.postMessage",
    channel="@chadallen",
    as_user="true",
    attachments=[{"title": "Cat GIF", "image_url": catImagePath}]
)

