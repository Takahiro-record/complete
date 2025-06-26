from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws["A1"] = "こんにちは、Excel!"
ws["B1"] = "すでに何回目かの変更"
ws["C1"] = "だいぶ流れに慣れてきただろうか"
wb.save("output.xlsx")
