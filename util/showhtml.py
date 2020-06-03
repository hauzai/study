import prettytable


class Showhtml:
    def __init__(self, datalist: list, htmlfilename: str):
        self.jsondata = datalist
        self.htmlfilename = htmlfilename


    def get_table(self):
        """
        处理接口返回的有关数据的列表
        :return:prettytable类型的table对象
        """
        table = prettytable.PrettyTable()
        if self.jsondata:
            table.field_names = self.jsondata[0].keys()
            for i in self.jsondata:
                table.add_row(i.values())
            return table
        else:
            return None

    def set_html(self, table: prettytable.PrettyTable = None):
        """
        :param  table:
        :return:
        """
        if table:
            html_str = table.get_html_string()
            with open('htmlpage/'+self.htmlfilename+'.html', 'w') as f:
                f.write(""""
                        <html>
                            <head>
                                <title>{0}</title>
                            </head>
                            <body>{1}
                            </body>
                        </html>
                        """.format(self.htmlfilename, html_str))
        else:
            print("table数据为空")

