from openpyxl import load_workbook

wb = load_workbook("logbook.xlsx")
ws = wb["Log"]

for row in ws.iter_rows(min_row=2,values_only=True):
    print(row[2])