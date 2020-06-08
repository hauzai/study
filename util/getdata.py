import xlrd
import os
current_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_path, r"..\data")


class Getdata:
    def __init__(self, filename, sheetname, path=data_path, id=""):
        """
        :param filename: 获取文件名称
        :param sheetname: 获取sheet名称
        :param path: 文件所在目录
        :param id: 获取数据id
        """
        # 私有变量，获取文件夹路径、路径下文件名列表、文件sheet列表、sheet中的所有数据id列表
        self.__path = path
        self.__filenames = []
        self.__sheetnames = []
        self.__ids = []

        # 变量 解析的文件名、解析文件的sheet名、解析数据的id
        self.filename = filename
        self.sheetname = sheetname
        self.id = id

        # 定义需返回的 datas 及 data 变量
        self.datas = {}
        self.data = {}

        # 私有变量，解析文件的路径
        self.__filepath = os.path.join(self.__path, self.filename)

        # 声明文件对象、table对象
        self.__workbook: xlrd.book.Book = None
        self.__table: xlrd.sheet.Sheet = None

        # 获取文件所在目录的文件名称、获取文件对象、获取文件对象下的sheet名称、获取table对象
        self.setfilenames()
        self.get_file()
        self.setsheetnames()
        self.get_table()

        # 获取datas对象
        self.__getdatas()

        # 如果创建对象时传入了id则直接获取data
        if self.id:
            self.data = self.getdata(self.id)

    def __getdatas(self):
        # TODO:处理文档中数据，原样输出
        """
        获取数据表中数据，此处以id为键，行内所有数据字典为值
        :return:
        """
        merged_cells = self.__get_mergeddict()
        if self.__table.nrows > 1:
            data_key = self.__table.row_values(0)
            for row in range(1, self.__table.nrows):
                data = self.__table.row_values(row).copy()
                for col in range(len(data)):
                    if (row, col) in merged_cells.keys():
                        data[col] = merged_cells[(row, col)]
                data_temp = dict(zip(data_key, data))
                dict_key = data_temp['id']
                self.datas[dict_key] = data_temp
                self.__ids.append(dict_key)
        # print(self.datas)
        # pass

    def getdata(self, id=""):
        # TODO:根据data的键获取某特定的data
        if id:
            return {id: self.datas[id]}

    def __getdatasbyid(self, keyname, value_keyname):
        """
        通过给定的keyname及value对数据进行筛选并返回
        :param keyname:
        :param value_keyname:
        :return:
        """
        data = {}
        for i in self.datas:
            for x in self.datas[i]:
                if keyname == x and self.datas[i][x] == value_keyname:
                    data.update({i: self.datas[i]})
        return data

    # def get_datasbyvalue(self, **kwargs):
    #     datas = []
    #     for keyname, value_keyname in kwargs:
    #         datas.append(self.__getdatasbyid(keyname, value_keyname))
    #     print(datas[-1])

    def getdatas(self):
        return self.datas

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
        self.__sheetnames = self.__workbook.sheet_names()

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

    def __get_mergeddict(self):
        """
        获取表格中合并单元格，并组合为{(row,col):value}的形式，其中(row,col)为合并的单元格坐标,value为应填入的值
        :return:
        """
        merged_cell_dict = {}
        for i in self.__table.merged_cells:
            value = self.__table.cell_value(i[0], i[2])
            for rows in range(i[0], i[1]):
                for cols in range(i[2], i[3]):
                    merged_cell_dict.update({(rows, cols): value})
        return merged_cell_dict


    def __str__(self):
        return self.__path+"\n"+str(self.__filenames)+"\n"+str(self.__filepath)+"\n"+str(self.__sheetnames)+"\n"+str(self.__ids)


if __name__ == '__main__':
    # print(data_path)
    # test = Getdata(filename="常用接口文档.xlsx", sheetname="安全保障app")
    # test1 = Getdata(filename="常用接口文档.xlsx", sheetname="安全保障app", id="togest-001")
    # print(test1.data)
    test2 = Getdata(filename="常用接口文档.xlsx", sheetname="test-测试用例")
    print(test2.datas)
    print(vars(test2))
    print(test2._Getdata__getdatasbyid('apiId', 'togest-001'))
    print(test2._Getdata__getdatasbyid('apiId', 'togest-002'))