from openpyxl import Workbook
from datetime import datetime

#実行日の日付を取得
today = datetime.now().strftime("%Y-%m-%d")

#出力ファイル名を動的に決定!
filename = f"output_{today}.xlsx"

wb = Workbook()
ws = wb.active
ws["A1"] = f"作成日：{today}"
ws["B1"] = "日付入りExcelファイルだよ！"
wb.save(filename)

print(f"{filename}を保存しました！")
import os
print("保存先:", os.getcwd())
print("ファイル一覧:", os.listdir())
