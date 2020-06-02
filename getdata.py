import xlrd
import os
#list_keys = ["描述", "url", "方法", "入参", "出参格式"]
list_keys = []
filenames = {}

def get_filenames():
    """
    获取data文件夹下所有文件
    :return:返回全局变量filenames字典，键为文件名，值为path
    """
    global filenames
    for root, dirs, files in os.walk('data'):
        for name in files:
            # print(root+"/"+name)
            filenames[name] = root+"/"+name
    print(filenames)


def get_sheetnames(filepath):
    """
    获取excel文件所有的sheet名称
    :param filepath: excel文件路径
    :return: 返回sheet名称组成的列表
    """
    data = xlrd.open_workbook(filepath)
    print(data.sheet_names())
    return data.sheet_names()


def get_interfaces(sheetname, filename="常用接口文档.xlsx"):
    """
    从数据表中获取所有api
    :param sheetname: 数据表名称
    :param filename: excel文件名称
    :return: 返回所有api组成的list
    """
    data = xlrd.open_workbook(filenames[filename])
    table = data.sheet_by_name(sheetname)
    # 若数据大于1行，则解析
    if table.nrows > 1:
        # 全局变量list_keys,作为api字典的键值在之后进行拼接
        global list_keys
        # list_keys取数据表中的第一行
        list_keys = table.row_values(0)
        return [table.row_values(i) for i in range(1, table.nrows)]
    else:
        return []


def get_interfacesdict(list_value):
    """
    传入list_value即api数据，结合表头list_keys,将api组装为dict
    :param list_value:从excel中解析到的api列表
    :return:返回以描述为键，api字典为值的字典
    """
    global list_keys
    '''list1 = []
    for i in list_value:
        list1.append(dict(zip(list_keys, i)))
    return list1'''
    return {i[0]: dict(zip(list_keys, i)) for i in list_value}


if __name__ == '__main__':
    get_filenames()
    print(get_sheetnames(r'C:\Users\Administrator\Desktop\test-read.xlsx'))
    print(get_interfacesdict(get_interfaces("沈阳6C")))
    print(filenames)
