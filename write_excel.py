from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Log"
ws.append(["日時","カテゴリ","内容"])
wb.save("logbool.xlsx")
print("logbool.xlsx を新規作成しました")