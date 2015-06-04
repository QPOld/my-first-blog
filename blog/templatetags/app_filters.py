from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

import soundcloud


register = template.Library()

@register.filter()
@stringfilter
def SCURL(string):
    # # create a client object with your app credentials
    client = soundcloud.Client(client_id='YOUR_CLIENT_ID')
    #
    # # get a tracks oembed data
    track_url = str(string)
    embed_info = client.get('/oembed', url=track_url)
    #
    # # print the html for the player widget
    return embed_info.html
