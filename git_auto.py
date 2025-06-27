import subprocess

def git_commit(msg):
    subprocess.run(['git','add','.'])
    subprocess.run(['git','commit','-m',msg])
    print("自動コミット完了")

git_commit("kurumi.py修正")