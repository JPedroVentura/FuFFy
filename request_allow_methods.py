def request_allow_method(method):
    HTTP_METHOD = method
    allow_methods = ['GET', 'POST', 'OPTIONS',
                     'TRACE', 'HEAD', 'PUT', 'DELETE']
    error = f'\n:: Method {HTTP_METHOD} Not-Allowed or Not Exist\n'
    if HTTP_METHOD == 'None':
        return
    for method in allow_methods:
        if HTTP_METHOD == method:
            return method

    print(error)