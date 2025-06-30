from openpyxl import load_workbook
from datetime import datetime

filename = "logbook.xlsx"
wb = load_workbook(filename)
ws = wb["Log"]

# ---------------入力パート--------
category = "休憩"
massage = "コーヒー飲んでひと休み"
# ------------------------------------

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 条件付き追記：学習・業務の時だけ記録
if category in ["学習", "業務"]:
    ws.append([now, category, message])
    wb.save(filename)
    print(f"✅ {category}：ログ追加完了！")
else:
    print(f"ℹ️ {category}は記録スキップ中（条件外）")