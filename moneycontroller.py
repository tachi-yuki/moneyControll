import openpyxl
import datetime

def moneycontrol(date, item, price):
    wb = openpyxl.load_workbook('家計簿.xlsx')
    sheet = wb['Sheet1']

    cell = sheet.max_row + 1

    sheet['A{}'.format(cell)] = date
    sheet['B{}'.format(cell)] = item
    sheet['C{}'.format(cell)] = price

    wb.save('家計簿.xlsx')










    

