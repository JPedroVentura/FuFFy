from url_parser import html_parser

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

