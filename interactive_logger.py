from openpyxl import load_workbook
from datetime import datetime

filename = "logbook.xlsx"
wb = load_workbook(filename)
ws = wb["Log"]

#ユーザーから情報を取得
category = input ("カテゴリ(学習/業務/休憩 など）を入力してください：")
message = input("ログの内容を入力してください:")

#日付を取得して追記
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ws.append([now,category,message])
wb.save(filename)
print("ログを記録しました")