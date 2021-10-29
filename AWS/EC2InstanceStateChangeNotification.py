import boto3
import json
import logging
import os
import datetime

from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

SLACK_CHANNEL = os.environ.get('slackChannel', 'raphael_test')

HOOK_URL = os.environ['hookURL']
os.environ['TZ'] = 'Asia/Seoul'
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def convert_to_kst(time: str):
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    dt_strptime = datetime.datetime.strptime(time, date_format)
    timedelta_ = datetime.timedelta(hours=9)
    convert_time = dt_strptime + timedelta_

    return convert_time.astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')


def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    message = json.loads(event['Records'][0]['Sns']['Message'])
    logger.info("Message: " + str(message))
    time = convert_to_kst(event['Records'][0]['Sns']['Timestamp'])

    detailType = message['detail-type']
    time = convert_to_kst(event['Records'][0]['Sns']['Timestamp'])
    resources = message['resources']
    state = message['detail']['state']

    # logger.info("Message: " + str(message['detail']))

    sending_message = f"""
```
- trigger: {detailType}
- time: {time}
- resources: {resources}
- state: {state}
```
"""

    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': "%s" % sending_message
    }

    req = Request(HOOK_URL, json.dumps(slack_message).encode('utf-8'))

    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
