import subprocess
from datetime import datetime

#日時付きメッセージを生成
now = datetime.now().strftime("%Y-%m-%d %H:%M")
msg = f"ログ自動更新({now})"

subprocess.run(['git','add','.'],check=True)
subprocess.run(['git','commit','-m',msg],check=True)
subprocess.run(['git','push'],check=True)

print("Git自動Push完了")
print(f"コミットメッセージ:{msg}")