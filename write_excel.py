from openpyxl import Workbook
from datetime import datetime
import os

# ファイル名(固定)を定義
filename = "logbool.xlsx"

# ログデータの準備
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = [now,"ログ追記成功！"]

# ファイルが存在するかチェック
if os.path.exists(filename):
    wb = load_workbook(filename)
    ws = wb.active
else:
    wb = Workbook()
    ws = wb.active
    ws.append(["タイムスタンプ","処理内容"])  #ヘッダーだけ先につけておく

# 新しいログを書き込み
ws.append(log_entry)

# 保存
wb.save(filename)
print(f"{filename}に追記しました！")

