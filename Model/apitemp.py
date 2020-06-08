# import handledata

from util import getdata
class Apitemp:
    def __init__(self, apidata: getdata.Getdata):
        # getdata对象传入的data数据
        self.data = apidata.data
        # __apidata data数据的值
        self.__api_data = {}
        # api_id data数据的键 也作为 request_data的键
        self.api_id = ""
        self.handle_data()
        # 用于请求的字典数据
        self.request_data = {}
        # 用于转换request_data中数据的键和__api_data中数据的键
        self.__temp = {'method': '方法', 'headers': 'headers', 'params': '入参', 'url': 'api'}

    def handle_data(self):
        for key, value in self.data.items():
            self.api_id = key
            self.__api_data = value

    def __str__(self):
        return self.api_id+":"+str(self.request_data)

    def get_api_data(self):
        return self.__api_data

    def update_request_data(self, **kwargs):
        for k, v in kwargs.items():
            self.request_data[k] = v

    def set_request_data(self, keys=['url', 'method', 'params', 'headers']):
        for i in keys:
            self.request_data[i] = self.__api_data[self.__temp[i]]

    def get_apitemp(self):
        return {self.api_id: self.request_data}



if __name__ == '__main__':
    test1 = getdata.Getdata(filename="常用接口文档.xlsx", sheetname="安全保障app", id="togest-001")
    test = Apitemp(test1)
    test.set_request_data()
    test.update_request_data(headers = {"token":"test"})
    print(test.get_apitemp())