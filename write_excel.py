from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws["A1"] = "こんにちは、Excel!"
wb.save("output.xlsx")
