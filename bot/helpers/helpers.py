import re

youtube_regex = re.compile(
    r'^(?:https?://)?'                  # Optional http or https protocol
    r'(?:www\.)?'                       # Optional www subdomain
    r'(?:'                              # Start of group for domain and path
        r'youtube\.com/(?:watch\?v=|embed/|v/)'  # Matches youtube.com with different paths
        r'|'                          # OR
        r'youtu\.be/'                 # Matches shortened youtu.be links
    r')'
    r'([A-Za-z0-9_-]{11})'               # Captures the 11-character video ID
    r'(?:\S+)?$',                       # Optional other parameters until the end of the string
    re.IGNORECASE
)

def is_youtube_link(text):
    return youtube_regex.match(text) is not None
