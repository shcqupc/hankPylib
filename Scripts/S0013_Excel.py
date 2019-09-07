import openpyxl
import os

os.chdir(os.path.join(os.getcwd(), "Sources"))
wb = openpyxl.load_workbook("example.xlsx")
print(type(wb))

print('\n---------------Getting Sheets---------------------')
print('wb.sheetnames', wb.sheetnames)
sheet3 = wb.worksheets[0]
print('worksheets[0].title', sheet3.title)
print('wb.active.title', wb.active.title)
print('sheet3.max_column', sheet3.max_column)
print(sheet3['A1':'B3'])

print('\n---------------Getting Cells---------------------')
cell1 = wb.active.cell(2, 5)
print(type(cell1.value))
print('cell1.value', cell1.value)
print(cell1.row, cell1.column)

print('\n------------------------------------')
from openpyxl.utils import get_column_letter, column_index_from_string
print('get_column_letter(1)', get_column_letter(28))
print(r"column_index_from_string('AA')", column_index_from_string('AA'))