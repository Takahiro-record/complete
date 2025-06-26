from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws["A1"] = "こんにちは、Excel!"
ws["B1"] = "すでに何回目かの変更"
wb.save("output.xlsx")
