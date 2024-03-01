#导入xlrd模块，此模块只能读取xls文件，不能读取xlsx文件,通过pip install xlrd下载的
import xlrd

#打开一个xls文件，打开的是和代码在同一个目录里的文件
wb=xlrd.open_workbook('123.xls')
#打印出这些显示
print (wb)

#把这个文件中的工作簿赋值给ws
ws=wb.sheets()
#打印出当前有多少个工作簿
print(ws)

#以下三个都是读取xls中工作簿名称的。先把工作簿名称赋值给wsname,然后通过不同的读取方式，第一个是直接读取工作簿名字，第二是按索引读取名字，第三个也是按索引。
wsname=wb.sheet_names()
print(wsname)
ws1=wb.sheet_by_name('第一工作表')
print(ws1)
ws2=wb.sheet_by_index(2)
print(ws2)
ws3=wb.sheets()[2]
print(ws3)