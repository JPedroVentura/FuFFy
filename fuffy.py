import requests
import pyfiglet
import argparse
from time import sleep
from bs4 import BeautifulSoup


parse = argparse.ArgumentParser()

parse.add_argument('-u', '--url', required=True, help='URL TARGET: https:exemple.com.br/FUZZ')
parse.add_argument('-X', '--method', required=False, help='HTTP METHOD. defalt: GET')
parse.add_argument('-hc', '--header_code', required=False, help='Response status-code')
parse.add_argument('-mr', '--reader', required=False, help='Search for word in response')
parse.add_argument('-x', '--extension', required=False)
parse.add_argument('-w', '--wordlist', required=False)

args = parse.parse_args()


def app_banner(url, extension, method, payload, status_code=200):
    banner = pyfiglet.Figlet(font='slant')

    print(banner.renderText('   Fuffy'))
    print('v0.2 Made By AZ4R')
    print('-' * 50, '\n')
    sleep(1)
    print(':: Method:       :', str(method))
    print(':: Payload:      :', str(payload))
    print(':: URL:          :', str(url))
    print(':: Extension:    :', str(extension))
    print(':: Status-Code:  :', str(status_code) + '\n')
    print('-' * 50, '\n')
    print('[+] Warning: This is fuzzing-based vulnerability testing software, do not use it without prior permission because this is an illegal action.')
    print('Use only in authorized environments and that have full control, I am not responsible for misuse of the application.\n')
    sleep(2)


def request_allow_method():
    HTTP_METHOD = str(args.method)
    allow_methods = ['GET', 'POST', 'OPTIONS',
                     'TRACE', 'HEAD', 'PUT', 'DELETE']
    error = f'\n:: Method {HTTP_METHOD} Not-Allowed or Not Exist\n'
    for method in allow_methods:
        if HTTP_METHOD == method:
            return method

    print(error)


def url_check(url):
    url_is_valid = True
    if 'https://' not in url and 'http://' not in url:
        url_is_valid = False
        print('\n:: URL is invalid. "http://" or "https://" is missing" \n')
    return url_is_valid


def url_format(url, index):
    return url.replace('FUZZ', index.strip())


def html_parser(request_text):
    return str(BeautifulSoup(request_text, 'html.parser'))


def stop_app():
    print(':: App stopped! \n')
    exit(1)


def header_code_request(request, status_code, conter, line, index):
    if type(status_code) != list:
        if request.status_code == int(status_code):
            print(f'\rProgress: [{conter}: {len(line)}]', end='')
            print(f' :------------: {index}\r', end='\n')

    for status in status_code:
        if request.status_code == int(status):
            print(f'\rProgress: [{conter}: {len(line)}]', end='')
            print(f' :------------: {index} + {status}\r', end='\n')


def header_content_reader(request, reader, conter, line, index):
    if str(reader) in html_parser(request.text):
        print(f'\rProgress: [{conter}: {len(line)}]', end='')
        print(f' :------------: {index}\r', end='\n')


def request_fuzzing():
    url = str(args.url)
    method = request_allow_method()
    status_code = args.header_code
    content_reader = args.reader
    extension = args.extension
    payload = args.wordlist

    if payload == None:
        print('[+] Wordlist is Missing!')
    if extension != None:
        url += extension
    if method == None:
        method = 'GET'
    if content_reader == None:
        if status_code == None:
            status_code = [200, 301, 404, 500]

    app_banner(url, extension, method, payload, status_code)

    if not url_check(url):
        return

    if 'FUZZ' not in url:
        print(':: Missing FUZZ in url target')
        return

    with open(payload) as file:
        line = file.readlines()
        conter = 0
    for index in line:
        try:
            request = requests.request(
                method, url_format(url, index), timeout=10)
        except KeyboardInterrupt:
            stop_app()
        if status_code != None:
            header_code_request(request, status_code, conter, line, index)
        if content_reader != None:
            header_content_reader(request, content_reader, conter, line, index)
        print(f'\rProgress: [{conter}: {len(line)}]', end='')
        conter += 1


request_fuzzing()
