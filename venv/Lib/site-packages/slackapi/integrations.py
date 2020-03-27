# -*- coding: utf-8 -*-

"""
Slack API library
~~~~~~~~~~~~~~~~~

slackapi is a library for authors of Slack API integrations (webhooks, slash commands, bots, etc.)
"""

import json
import requests

class IncomingWebHook:

    """Implements Custom Integrations Incoming WebHooks for the given
    team. This type of integration is typically used by in-house scripts,
    e.g. Ansible deployment playbooks and is not designed for use by
    other teams (consider SlashCommand and/or BotUser for such cases).
    See: https://api.slack.com/

    Basic usage:

    >>> from slackapi.integrations import IncomingWebHook
    >>> hook = IncomingWebHook(webhook_url="https://hooks.slack.com/services/...")
    >>> hook.send_message()
    <Response [200]>
    """

    def __init__(self, webhook_url):

        """Intialize Incoming Webhook object.
        See: https://api.slack.com/incoming-webhooks

        Args:
            webhook_url: the Slack Webhook URL created using the Slack API developer
                         website. Unique for each channel, but can be overriden (see
                         docstring send_message()).
        """

        self.webhook_url = webhook_url

    def send_message(self, channel=None, text="Hello!", username="mechanizeme.com", icon_emoji=":computer:", icon_url=None, attachments=[], unfurl_links=False):

        """Sends message to the Slack channel associated with self.webhook_url. The default
        values will get you started.

        Args:
            channel: optional channel name, each webhook_url is associated with a
                     default channel, but you can override it with channel="#channel" or
                     send a direct message with channel="@channel"
            text: your message, can include urls (<http://mechanizeme.com>) and emoji
                  (:dog2::dash:)
            username: you can set it to anything, even other user"s name, but Slack will
                      add the BOT slug next to the username to indicate that this is not
                      a human, so do not try to impersonate people who do not share your
                      sense of humor
            icon_emoji: set the emoji you want to use to represent your bot (you can
                        change it every time you post), e.g. ":computer:", ":dog:"
            icon_url: if you provide it, the image this URL points to will replace icon_emoji
            attachments: a list of attachments dicts
            unfurl_links: set to True Slack will create attachments for the links your use
                          in the message text

        Usage:
    
        Send a simple message:

        >>> from slackapi.integrations import IncomingWebHook
        >>> hook = IncomingWebHook(webhook_url="https://hooks.slack.com/services/...")
        >>> hook.send_message()
        <Response [200]>

        Send a simple message with an embedded URL:

        >>> from slackapi.integrations import IncomingWebHook
        >>> hook = IncomingWebHook(webhook_url="https://hooks.slack.com/services/...")
        >>> hook.send_message(text="Watch this video: <https://youtu.be/cnQRYIMxl2o?list=PLGakirX3jyElmR7o2cLW8duHOdayIIlHE> Wow!")
        <Response [200]>

        Send a simple message to #random:

        >>> from slackapi.integrations import IncomingWebHook
        >>> hook = IncomingWebHook(webhook_url="https://hooks.slack.com/services/...")
        >>> hook.send_message(channel="#random", text="Watch this video: <https://youtu.be/cnQRYIMxl2o?list=PLGakirX3jyElmR7o2cLW8duHOdayIIlHE> Wow!")
        <Response [200]>

        Send a simple message to #random under a different name (Slack will add a BOT string to the message header, so don"t do anything that would get you in trouble):

        >>> from slackapi.integrations import IncomingWebHook
        >>> hook = IncomingWebHook(webhook_url="https://hooks.slack.com/services/...")
        >>> hook.send_message(channel="#random", text="Just a random post...", username="Your Mechanized Assistant")
        <Response [200]>

        Send a message with attachments to #random under a different name (Slack will add a BOT string to the message header, so don"t do anything that would get you in trouble):

        >>> from slackapi.integrations import IncomingWebHook
        >>> hook = IncomingWebHook(webhook_url="https://hooks.slack.com/services/...")
        >>> af_1 = hook.make_attachment_field(title="Attachment 1 Title", value="Attachment 1 Text", short=False)
        >>> af_2 = hook.make_attachment_field(title="Attachment 2 Title", value="Attachment 2 Text", short=False)
        >>> af_3 = hook.make_attachment_field(title="Attachment 3 Title", value="Attachment 3 Text", short=False)
        >>> af_4 = hook.make_attachment_field(title="Attachment 4 Title", value="Attachment 4 Text", short=False)
        >>> a_1 = hook.make_attachment(fallback="Attachment 1 Fallback", pretext="Attachment 1 Pretext", color="#000000", fields=[af_1, af_2])
        >>> a_2 = hook.make_attachment(fallback="Attachment 2 Fallback", pretext="Attachment 2 Pretext", fields=[af_3, af_4])
        >>> hook.send_message(channel="#random", text="Just a random post...", username="Your Mechanized Assistant", attachments=[a_1, a_2])
        <Response [200]>

        """

        payload={"text": text, "username": username, "attachments": attachments, "unfurl_links": unfurl_links}

        if channel:
            payload["channel"] = channel

        # override icon_emoji if icon_url is given
        if icon_url:
            payload["icon_url"] = icon_url
        else:
            payload["icon_emoji"] = icon_emoji

        data = {"payload": json.dumps(payload)}

        return requests.post(self.webhook_url, data=data)

    @staticmethod
    def make_attachment_field(title="Default title", value="Default value", short=False):

        """A helped method for creating fields for attachemnts for messages.
        """

        return {"title": title, "value": value, "short": short}

    @staticmethod
    def make_attachment(title="Attachment Title", title_link="http://mechanizedme.com/youpostedtoslack/", pretext="Default pretext", text="Main attachment text", fallback="Default fallback", author_name="Mechanized Me", author_link="http://mechanizedme.com", author_icon="http://mechanized.com/slack_icon.png", image_url="http://mechanizeme.com/attachment_image.png", thumb_url="http://mechanizeme.com/attachment_thumbnail.png", color="#000000", mrkdwn=True, mrkdwn_in=["text", "pretext", "fields"], fields=[]):

        """A helped method for creating attachemnts for messages.
        """

        return {"title": title, "title_link": title_link, "pretext": pretext, "text": text, "fallback": fallback, "author_name": author_name, "author_link": author_link, "author_icon": author_icon, "image_url": image_url, "thumb_url": thumb_url, "color": color, "mrkdwn": mrkdwn, "mrkdwn_in": mrkdwn_in, "fields": fields} 


class SlashCommand(object):

    """A stub of a slash command handler. A stub, because you make it whatever you want it to be.
    Start with a view that receives a POST request (see slackapi.views).
    When you want to send a response, use IncomingWebHook.
    """

    pass

class BotUser(object):

    """An async bot user implementation. Use it to write management commands.
    When you want to send a response, use IncomingWebHook.
    """

    pass

class OutgoingWebHook(object):

    """Not implemented. Reserved for possible future use. Have a look at views.outgoing_webhook.
    When you want to send a response, use IncomingWebHook.
    """

    pass
