import xlrd
import os
current_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_path, r"..\data")


class Getdata:
    def __init__(self, filename, sheetname, path=data_path, id=""):
        # 私有变量，获取文件夹路径、路径下文件名列表、文件sheet列表、sheet中的所有数据id列表
        self.__path = path
        self.__filenames = []
        self.__sheetnames = []
        self.__ids = []
        # 变量 解析的文件名、解析文件的sheet名、解析数据的id
        self.filename = filename
        self.sheetname = sheetname
        self.id = id

        self.datas = []
        # 私有变量，解析文件的路径
        self.__filepath = os.path.join(self.__path, self.filename)

        self.setfilenames()
        self.setsheetnames()

    def getdata(self):
        #TODO:处理文档中数据，原样输出
        pass

    def setfilenames(self):
        """
        设置self.__filenames
        :return:
        """
        for root, dirs, files in os.walk(self.__path):
            for name in files:
                # print(root+"/"+name)
                self.__filenames.append(name)

    def setsheetnames(self):
        """
        设置self.__sheetnames
        :return:
        """
        data = xlrd.open_workbook(self.__filepath)
        self.__sheetnames =  data.sheet_names()

    def __str__(self):
        return self.__path+"\n"+str(self.__filenames)+"\n"+str(self.__filepath)+"\n"+str(self.__sheetnames)


if __name__ == '__main__':
    # print(data_path)
    test = Getdata(filename="常用接口文档.xlsx", sheetname="安全保障app")
    print(test)