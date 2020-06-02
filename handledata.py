
request_dict = {"api": "", "params": {}, "headers": {"token": "2100000000000000"}, "method": ""}


def get_params(value_dict: dict):
    """
    获取入参返回分割后数组
    :param value_dict:api字典
    :return:返回入参数组
    """
    params_str: str = value_dict['入参']
    params_list = []
    if params_str:
        params_list = params_str.split("\n")
    return params_list


def handle_paramslist(list1: list):
    """
    确认必填入参并将入参传入请求对象中
    :param list1:入参数组
    :return:
    """
    paramslist = list1.copy()
    paramsdict = {}
    for i in range(len(paramslist)):
        if paramslist[i].startswith("*"):
            paramsdict[paramslist[i].split("*")[1]] = '必填项'
        else:
            paramsdict[paramslist[i]] = ""
    global request_dict
    request_dict['params'] = paramsdict


def get_url(value_dict: dict):
    """
    获取url地址，此处之后会进行ip配置
    :param value_dict:
    :return:
    """
    global request_dict
    url_str: str = value_dict['api']
    request_dict['api'] = url_str


def get_method(value_dict: dict):
    """
    获取请求方法
    :param value_dict:
    :return:
    """
    global request_dict
    method_str: str = value_dict['方法']
    request_dict['method'] = method_str


if __name__ == '__main__':
    test_dict ={'描述': '安全用具', 'url': 'http://192.168.1.96:8092/jcw/produce/safetyTool/sync/list', '方法': 'get',
             '入参': '*syncDeptId\nsyncLastTime', '出参格式': 'json'}
    handle_paramslist(get_params(test_dict))
    get_url(test_dict)
    get_method(test_dict)

    print(request_dict)