import re

# Remove emojis from the text
def remove_emojis(text):
    # Emoji patterns to be removed
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642" 
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    
    # Remove emojis from the text
    return emoji_pattern.sub(r'', text)



# Remove Markdown formatting from the text
def clean_markdown(data):
    # Remove emphasis (bold, italics)
    data = re.sub(r'\*\*(.*?)\*\*', r'\1', data)  # **text**
    data = re.sub(r'\*(.*?)\*', r'\1', data)      # *text*
    data = re.sub(r'__(.*?)__', r'\1', data)      # __text__
    data = re.sub(r'_(.*?)_', r'\1', data)        # _text_

    # Remove links
    data = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', data)  # [text](link)

    # Remove images
    data = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', data)  # ![alt text](image)

    # Remove inline code
    data = re.sub(r'`([^`]+)`', r'\1', data)  # `code`

    # Remove code blocks
    data = re.sub(r'```[\s\S]*?```', '', data)  # ```code block```

    # Remove headers
    data = re.sub(r'^\s*#.*$', '', data, flags=re.MULTILINE)  # # Header
    data = re.sub(r'^\s*##.*$', '', data, flags=re.MULTILINE)  # ## Header
    data = re.sub(r'^\s*###.*$', '', data, flags=re.MULTILINE)  # ### Header
    data = re.sub(r'^\s*####.*$', '', data, flags=re.MULTILINE)  # #### Header
    data = re.sub(r'^\s*#####.*$', '', data, flags=re.MULTILINE)  # ##### Header
    data = re.sub(r'^\s*######.*$', '', data, flags=re.MULTILINE)  # ###### Header

    # Remove blockquotes
    data = re.sub(r'^\s*>.*$', '', data, flags=re.MULTILINE)  # > Blockquote

    # Remove horizontal rules
    data = re.sub(r'\n-{3,}\n', '\n', data)  # ---
    data = re.sub(r'\n\*{3,}\n', '\n', data)  # ***
    data = re.sub(r'\n_{3,}\n', '\n', data)  # ___

    # Remove lists
    data = re.sub(r'^\s*[-*+]\s+', '', data, flags=re.MULTILINE)  # - list item, * list item, + list item
    data = re.sub(r'^\s*\d+\.\s+', '', data, flags=re.MULTILINE)  # 1. list item

    # Remove URLs but keep the text
    # data = re.sub(r'\bhttps?://\S+\b', '', data)  # URLs

    # Remove extra newlines
    data = re.sub(r'\n+', '\n', data).strip()

    return data