from openpyxl import load_workbook
from datetime import datetime

wb = load_workbook("logbook.xlsx")
ws = wb.active
ws.append([datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"ログ記録"])
wb.save("logbook.xlsx")
print("ログ記録しました")