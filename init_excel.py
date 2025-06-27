from openpyxl import Workbook

wb = Workbook()
wb.save("logbook.xlsx")
print("✅ 新しいExcelファイルを作成しました！")
