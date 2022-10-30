import xlrd
import json
from data import data_path
import os
# class read_excel():
jd_path = data_path.get_path()

def get_book(sheet_name,title_value):
    #try:
            #1.excel路径
        xlspath = os.path.join(jd_path,"Interface_data.xlsx")
        #path = data_path.get_path() + "\\Interface_data.xlsx"
            #2.打开excel
        workbook = xlrd.open_workbook(xlspath)
        #workbook = xlrd.open_workbook(path)
            #3.选取指定的sheet
        sheet = workbook.sheet_by_name(sheet_name)
            #4.获取标题
        title = sheet.col_values(0)
            #获取标题所在的位置
        title_position = title.index(title_value)
            #根据标题所在的位置获取当前行的数据
        row_data = tuple(sheet.row_values(title_position))
            #获取第一行：标题行
        first_row = sheet.row_values(0)
            #把标题和值转换为字典
        case_data = dict(zip(first_row,row_data))
        list = []
        if case_data.get("method") == "get":
            list.append((case_data.get("path"), case_data.get("query"), json.loads(case_data.get("headers")),
                     case_data.get("method")))

        elif case_data.get("method") == "post":
            list.append((case_data.get("path"), json.loads(case_data.get("headers"), strict=False),
                     json.loads(case_data.get("body"),strict=False), case_data.get("method")),)
        else:

            return print("别他妈瞎改请求方式")

        return list


def get_book02(sheet_name,title_value):
    # 1.excel路径
    xlspath = os.path.join(jd_path, "Interface_data.xlsx")
    # path = data_path.get_path() + "\\Interface_data.xlsx"
    # 2.打开excel
    workbook = xlrd.open_workbook(xlspath)
    # workbook = xlrd.open_workbook(path)
    # 3.选取指定的sheet
    sheet = workbook.sheet_by_name(sheet_name)
    # 4.获取标题
    title = sheet.col_values(0)
    # 获取标题的下标值
    title_index =  [i for i,x in enumerate(title) if x==title_value]
    # 获取第一行的数据
    first_row = sheet.row_values(0)
    list = []
    i = 0
    while i < len(title_index):
        row_data = tuple(sheet.row_values(title_index[i]))
        case_data = dict(zip(first_row, row_data))
        if case_data.get("method") == "get":
            try:
                list.append((case_data.get("path"), json.loads(case_data.get("query")), json.loads(case_data.get("headers")),
                            case_data.get("method"),json.loads(case_data.get("expect"),strict=False),case_data.get("case")))
            except:
                list.append(
                    (case_data.get("path"), case_data.get("query"), json.loads(case_data.get("headers")),
                     case_data.get("method"), json.loads(case_data.get("expect"), strict=False), case_data.get("case")))
            #list2.append((case_data.get("expect"),case_data.get("expect_status")))
        elif case_data.get("method") == "post":
            list.append((case_data.get("path"), json.loads(case_data.get("headers"), strict=False),
                        json.loads(case_data.get("body"),strict=False), case_data.get("method"),json.loads(case_data.get("expect"),strict=False),case_data.get("case")))
            #list2.append((case_data.get("expect")))
        else:
            return print("别他妈瞎改请求方式")
        i += 1
    return list






if __name__ == '__main__':
    print(get_book02("Games_explore","explore"))



