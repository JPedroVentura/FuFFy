def url_check(url):
    url_is_valid = True
    if 'https://' not in url and 'http://' not in url:
        url_is_valid = False
        print('\n:: URL is invalid. "http://" or "https://" is missing" \n')
    return url_is_valid


def payload_check(payload):
    if payload == None:
        print('[+] Wordlist is Missing!')
        exit(1)


def extension_check(extension):
    extension = extension if extension != None else '----'
    return extension


def method_check(http_method):
    if http_method == None:
        http_method = 'GET'
    return http_method


def status_code_check(http_content, status_code):
    if http_content == None:
        status_code = [200, 301, 404, 403,
                       500] if status_code == None else status_code
    return status_code