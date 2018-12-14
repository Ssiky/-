import xlrd
excel =xlrd.open_workbook("./data/data.xlsx")
sheet=excel.sheet_by_name("添加加油卡")
sheet=excel.sheet_by_index(0)


print(sheet.nrows)
print(sheet.ncols)

print(sheet.row_values(0))
print(sheet.row_values(1))

print(sheet.cell(1,0).value)

sheet=excel.sheet_by_name("添加加油卡")
for i in range(1,sheet.nrows):
    print(sheet.row_values(i))