import os
import subprocess
from datetime import datetime, timedelta

# Set start date to 1 year ago
start_date = datetime.today() - timedelta(days=365)

for i in range(366):  # 365 days + 1 for leap year coverage
    commit_date = start_date + timedelta(days=i)
    for _ in range(3):  # You can increase this number to make it darker
        with open("commit.txt", "a") as f:
            f.write(f"Commit for {commit_date}\n")
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = commit_date.strftime('%Y-%m-%dT12:00:00')
        env['GIT_COMMITTER_DATE'] = commit_date.strftime('%Y-%m-%dT12:00:00')
        subprocess.run(["git", "add", "."], env=env)
        subprocess.run(["git", "commit", "-m", f"Commit on {commit_date}"], env=env)

print("✅ All commits generated for the full year!")
