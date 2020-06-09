#TODO：testcase类，封装测试用例，与apitemp对象封装构成requestdict对象。
from util import getdata

class Testcase:
    def __init__(self, testcasedata: getdata.Getdata,id):
        if testcasedata.get_data(id):
            self.__testcase = testcasedata.get_data(id)
        else:
            self.__testcase = {}

    def get_testcase(self):
        return self.__testcase


if __name__ == '__main__':
    test2 = getdata.Getdata(filename="常用接口文档.xlsx", sheetname="test-测试用例")
    # print(test2.get_datas_by_kv('apiId', 'togest-002'))
    testcases = Testcase(test2, "togest-001-001")
    print(testcases.get_testcase())
