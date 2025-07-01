from openpyxl import load_workbook

wb = load_workbook("logbook.xlsx")
ws = wb.active

for row in ws.iter_rows(min_row=2,max_col=2):
    category = row[1].value
    print(category)