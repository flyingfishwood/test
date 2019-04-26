import xlsxwriter
import xlrd
import json
import operator
import os;
 #此接口主要用于excel数据的读取和写入
 
def get_excel_data(paths,sheetName):
    open_workbook=xlrd.open_workbook(paths);
    open_sheet=open_workbook.sheet_by_name(sheetName);
    rows=open_sheet.nrows;
    listkey = [];
    listcanshu1 = [];
    listcanshu2 = [];
    listyuqi = [];
    listresult = [];
    for item_row in range(1, rows):
        listkey.append(open_sheet.cell(item_row, 0).value);
        listcanshu1.append(open_sheet.cell(item_row, 1).value);
        listcanshu2.append(open_sheet.cell(item_row, 2).value);
        listyuqi.append(open_sheet.cell(item_row, 3).value);
#         try:
            
        listresult.append(open_sheet.cell(item_row, 3).value);
#         except:
#             print('索引错误',Exception)
        return listkey,listcanshu1,listcanshu2,listyuqi,listresult;
    