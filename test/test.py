import xlrd

if __name__ == '__main__':
    workbook = xlrd.open_workbook(r'..\data\常用接口文档.xlsx')
    table = workbook.sheet_by_name('Sheet2')
    print(table.nrows)

    merged_cell_dict = {}
    for i in table.merged_cells:
        value = table.cell_value(i[0], i[2])
        for rows in range(i[0], i[1]):
            for cols in range(i[2], i[3]):
                merged_cell_dict.update({(rows, cols): value})

    print(merged_cell_dict)

    for i in range(1, table.nrows):
        data = table.row_values(i)
        for cols in range(len(data)):
            if (i, cols) in merged_cell_dict.keys():
                data[cols] = merged_cell_dict[(i, cols)]
        print(data)
    print(table.merged_cells)

    print(list(range(1,4)))
    # print(table.cell_value(1, 0))

