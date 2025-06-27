import subprocess
from datetime import datetime

msg = f"ログ自動更新({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"

def git_commit(msg):
    subprocess.run(['git','add','.'])
    subprocess.run(['git','commit','-m',msg])
    subprocess.run(['git','push'])
    print("自動コミット完了")

git_commit("kurumi.py修正")