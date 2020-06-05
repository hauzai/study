import handledata

from util import getdata
class Apitemp:
    def __init__(self, apidata: getdata.Getdata):
        self.data = apidata.data

        self.__api_data = {}
        self.api_id = ""
        self.handle_data()

        self.request_data = {}
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
        return {self.api_id:self.request_data}



if __name__ == '__main__':
    test1 = getdata.Getdata(filename="常用接口文档.xlsx", sheetname="安全保障app", id="togest-001")
    test = Apitemp(test1)
    test.handle_data()
    test.set_request_data()
    print(test)
    print(test.request_data)
    print(test.get_apitemp())
    test.update_request_data(headers={"token": "2100000000000000"})
    print(test.request_data)