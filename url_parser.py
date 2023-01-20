from bs4 import BeautifulSoup

def url_format(url, index):
    return url.replace('FUZZ', index.strip())


def html_parser(request_text):
    return str(BeautifulSoup(request_text, 'html.parser'))