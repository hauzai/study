import getdata
import handledata
import dorequest
from util.showhtml import Showhtml
class Requestdata:
    def __init__(self, filename=None, sheetname=None):
        getdata.get_filenames()
        self.filenames = getdata.filenames
        if not (filename and sheetname):
            self.filename = input("输入api文件名称\n")
            self.sheetnames = getdata.get_sheetnames(getdata.filenames[self.filename])
            self.sheetname = input("请输入sheetname\n")
            self.apidicts = getdata.get_datasdict(getdata.get_datas(self.sheetname, self.filename))
        else:
            self.filename = filename
            self.sheetnames = getdata.get_sheetnames(getdata.filenames[self.filename])
            self.sheetname = sheetname
            self.apidicts = getdata.get_datasdict(getdata.get_datas(self.sheetname, self.filename))

    def __str__(self):
        return "文件名："+self.filename+"\nsheet名："+self.sheetname+"\napi字典："+str(self.apidicts)

    def handle_apidict(self, apiname: str):
        handledata.get_url(self.apidicts[apiname])
        handledata.get_method(self.apidicts[apiname])
        handledata.handle_paramslist(handledata.get_params(self.apidicts[apiname]))
        requestdata = apiname, handledata.request_dict
        # print(requestdata)
        return requestdata

    def simple_request(self, apidict):
        return dorequest.run(apidict)

if __name__ == '__main__':
    # test = Requestdata("常用接口文档.xlsx", "安全保障app")
    # print(test)
    # test.handle_apidict("同步部门")
    # test.handle_apidict("数据更新")
    # test.handle_apidict("安全用具")
    # test.simple_request(test.handle_apidict("同步部门"))
    # res = test.simple_request(test.handle_apidict("同步人员"))
    # print(res)
    # table = Showhtml(res, "测试")
    # table.set_html(table.get_table())
    test = Requestdata("常用接口文档.xlsx", "安全保障app")
    print(test)
    #  print(test.handle_apidict("同步部门"))
    apidict = test.handle_apidict("同步部门")
    res = test.simple_request(apidict)
    table = Showhtml(res["data"], apidict[0])
    table.set_html(table.get_table())
