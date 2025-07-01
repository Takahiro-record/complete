import subprocess
from datetime import datetime

filename = input("削除したいファイル名を記入してください(例：sample.xlsx)")

try:
    subprocess.run(["git","rm",filename],check=True)
    msg = f"{filename}を削除({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
    subprocess.run(["git","commit","-m",msg],check=True)
    subprocess.run(["git","push"],check=True)
    print(f"gitから{filename}を削除しました")
except subprocess.CellsdProcessError:
    print(f"エラー：{filename}が存在しないか、gitで管理されていない可能性があります")