from openpyxl import load_workbook
from datetime import datetime

wb = load_workbook("logbook.xlsx")
ws = wb.active
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ws.append([now,"作業ログを記録しました"])

wb.save("logbook.xlsx")
print("ログを記録しました")