import subprocess
import git
import schedule
import time


def job():
    repo = git.Repo("./../ads-issue-tracker")
    repo.remotes.origin.pull()
    subprocess.call(["node", "./../ads-issue-tracker/grabDataScript.js"])
    repo.git.add(update=True)
    repo.git.commit("-m", "data update")
    repo.remotes.origin.push(refspec="master:master")


schedule.every().hour.do(job())


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)

