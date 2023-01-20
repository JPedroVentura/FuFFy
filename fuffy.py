import requests
import pyfiglet
import argparse
from time import sleep
from request_allow_methods import request_allow_method
from argument_check import *
from url_parser import *
from content_response_type import *


parse = argparse.ArgumentParser()

parse.add_argument('-u', '--url', required=True,
                   help='URL TARGET: https:exemple.com.br/FUZZ')
parse.add_argument('-X', '--method', required=False,
                   help='HTTP METHOD. defalt: GET')
parse.add_argument('-hc', '--header_code', required=False,
                   help='Response status-code')
parse.add_argument('-mr', '--reader', required=False,
                   help='Search for word in response')
parse.add_argument('-e', '--extension', required=False)
parse.add_argument('-w', '--wordlist', required=False)
parse.add_argument('-d', '--data', help='Request content body')

args = parse.parse_args()


def app_banner(url, extension, method, payload, status_code=200):
    banner = pyfiglet.Figlet(font='slant')

    print(banner.renderText('   Fuffy'))
    print('v0.3 ------- Made By AZ4R')
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


def stop_app():
    print(':: App stopped! \n')
    exit(1)


def data_header(http_data):
    if http_data != None:
        data = http_data.split(':')
        return {data[0]: data[1]}
    pass


def request_fuzzing():
    url = str(args.url)
    method = request_allow_method(str(args.method))
    status_code = args.header_code
    content_reader = args.reader
    extension = args.extension
    payload = args.wordlist
    data = args.data

    payload_check(payload)
    method = method_check(method)
    extension = extension_check(extension)
    status_code = status_code_check(content_reader, status_code)

    app_banner(url, extension, method, payload, status_code)

    if not url_check(url):
        return

    if 'FUZZ' not in url and 'FUZZ' not in data:
        print(':: Missing FUZZ in target')
        return

    with open(payload) as file:
        line = file.readlines()
        conter = 0
    for index in line:
        try:
            request = requests.request(method, url_format(
                url, index), timeout=10, data=data_header(data))
        except KeyboardInterrupt:
            stop_app()
        if status_code != None:
            header_code_request(request, status_code, conter, line, index)
        if content_reader != None:
            header_content_reader(request, content_reader, conter, line, index)
        print(f'\rProgress: [{conter}: {len(line)}]',
              sep='', end='', flush=True)
        conter += 1


request_fuzzing()
