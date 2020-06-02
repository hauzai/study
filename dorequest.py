import requests


def run(data):
    session = requests.session()
    if data["method"] == "get":
        res = session.request(method="GET", url=data["api"], params=data["params"], headers=data["headers"])
        print(res.json())
    elif data["method"] == "post":
        res = session.request(method="POST", url=data["api"], data=data["params"], headers=data["headers"])
        print(res.json())


if __name__ == '__main__':
    data = {'url': 'http://192.168.1.96:8092/jcw/produce/safetyTool/sync/list', 'params': {'syncDeptId': '145425940813211', 'syncLastTime': ''}, 'headers': {'token': '2100000000000000'}, 'method': 'get'}
    run(data)