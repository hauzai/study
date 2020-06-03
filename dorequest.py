import requests


def run(data_tuple):
    data = data_tuple[-1]
    session = requests.session()
    if data["method"] == "get":
        res = session.request(method="GET", url=data["api"], params=data["params"], headers=data["headers"])
        return res.json()
    elif data["method"] == "post":
        res = session.request(method="POST", url=data["api"], data=data["params"], headers=data["headers"])
        return res.json()


if __name__ == '__main__':
    data = {'api': 'http://192.168.1.96:8092/jcw/produce/safetyTool/sync/list', 'params': {'syncDeptId': '145425940813211', 'syncLastTime': ''}, 'headers': {'token': '2100000000000000'}, 'method': 'get'}
    print(run(data))