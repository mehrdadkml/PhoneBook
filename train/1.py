import openpyxl as xl

wb=xl.load_workbook('transactions.xlsx')
sheet=wb['sheet1']
cell=sheet['a1']
cell=sheet.cell(1,1)
print(cell.values)