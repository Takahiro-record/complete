from openpyxl import load_workbook, Workbook

wb_new = Workbook()
ws_kyukei = wb_new.active
ws_kyukei.title="休憩"
ws_gyomu = wb_new.create_sheet(title="業務")
ws_gakusyu = wb_new.create_sheet(title="学習")


wb = load_workbook("logbook.xlsx")
ws = wb["Log"]

ws_kyukei.append(["日付","内容"])
ws_gyomu.append(["日付","内容"])
ws_gakusyu.append(["日付","内容"])

for row in ws.iter_rows(min_row=2,values_only=True):
    if row[1] == "学習" and row[2]:
        ws_gakusyu.append([row[0],row[2]])
    elif row[1] == "業務" and row[2]:
        ws_gyomu.append([row[0],row[2]])
    elif row[1] == "休憩" and row[2]:
        ws_kyukei.append([row[0],row[2]])

wb_new.save("categorized_log.xlsx")