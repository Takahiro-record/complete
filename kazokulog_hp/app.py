from flask import Flask,request,render_template
import openpyxl
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit-report",methods=["POST"])
def submit_report():
    try:
        data = request.get_json()
        print("受信データ:",data)
        wb = openpyxl.load_workbook("report.xlsx")
        ws = wb.active
        ws.append([data["name"],data["date"],data["task"],data["time"]])
        wb.save("report.xlsx")
        return "報告を受け付けました！"
    except Exception as e:
        print("エラー:",e)
        return "処理中にエラーが発生しました",500

if __name__ == "__main__":
    app.run(debug=True)