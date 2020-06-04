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

        self.datas = {}
        # 私有变量，解析文件的路径
        self.__filepath = os.path.join(self.__path, self.filename)

        self.__workbook: xlrd.book.Book = None
        self.__table: xlrd.sheet.Sheet = None

        self.setfilenames()
        self.get_file()
        self.setsheetnames()
        self.get_table()

    def getdatas(self):
        # TODO:处理文档中数据，原样输出
        """
        获取数据表中数据，此处以描述为键，行内所有数据字典为值
        :return:
        """
        if self.__table.nrows > 1:
            data_key = self.__table.row_values(0)
            for i in range(1, self.__table.nrows):
                data_temp = dict(zip(data_key, self.__table.row_values(i)))
                dict_key = data_temp['描述']
                self.datas[dict_key] = data_temp
                self.__ids.append(dict_key)
        print(self.datas)
        # pass

    def getdata(self,id=""):
        # TODO:获取某特定的data
        if id:
            return self.datas[id]
        else:
            return self.datas[self.id]

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
        self.__sheetnames =  self.__workbook.sheet_names()

    def get_file(self):
        """
        根据传入filename返回file对象
        :return: xlrd.file
        """
        self.__workbook = xlrd.open_workbook(self.__filepath)

    def get_table(self):
        """
        根据传入filename及sheetname获取table
        :return: xlrd.sheet
        """
        self.__table = self.__workbook.sheet_by_name(self.sheetname)

    def __str__(self):
        return self.__path+"\n"+str(self.__filenames)+"\n"+str(self.__filepath)+"\n"+str(self.__sheetnames)+"\n"+str(self.__ids)


if __name__ == '__main__':
    # print(data_path)
    test = Getdata(filename="常用接口文档.xlsx", sheetname="安全保障app")
    test.getdatas()
    print(test)