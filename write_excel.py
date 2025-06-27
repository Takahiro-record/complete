from openpyxl import Workbook
from datetime import datetime

#現在の日付と時刻を取得
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#データ(ログ)を用意
log_data = [
	["タイムスタンプ","処理内容"],		#<=ヘッダー
	[now,"ログ出力成功!"]			#<=1件目のデータ
]

# Excelファイル作成
wb = Workbook()
ws = wb.active

#行ごとに書き込み
for row in log_data:
    ws.append(row)

# 保存ファイル名
filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
wb.save(filename)
print(f"{filename}を保存しました")
