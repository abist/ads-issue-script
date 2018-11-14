import subprocess
import git


def job():
    repo = git.Repo("./../ads-issue-tracker")
    repo.remotes.origin.pull()
    subprocess.call(["node", "./../ads-issue-tracker/grabDataScript.js"])
    repo.git.add(update=True)
    repo.git.commit("-m", "data update")
    repo.remotes.origin.push(refspec="master:master")


if __name__ == '__main__':
    job()
