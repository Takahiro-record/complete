from flask import Flask, request, render_template
import openpyxl

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit-report", methods=["POST"])
def submit_report():
    try:
        data = request.get_json()
        print("受信データ:", data)

        # Excelファイルを読み込み（なければ作成してもOK）
        wb = openpyxl.load_workbook("kazokulog.xlsx")
        ws = wb.active

        # データを1行追加（name, date, place, content）
        ws.append([data["name"], data["date"], data["place"], data["content"]])

        wb.save("kazokulog.xlsx")
        return "記録しました", 200

    except Exception as e:
        print("エラー:", e)
        return "処理中にエラーが発生しました", 500

if __name__ == "__main__":
    app.run(debug=True)
