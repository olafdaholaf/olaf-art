import os
import subprocess
from datetime import datetime, timedelta

# "LOL" pattern (7 rows for 7 days, each column = 1 day in a week)
lol = [
    " #      #   ###  ",
    " #      #  #   # ",
    " #      #  #   # ",
    " #      #  #   # ",
    " #      #  #   # ",
    " #      #  #   # ",
    " #####  #   ###  ",
]

# Choose start date ~52 weeks ago, and align it to a Sunday
start_date = datetime.today() - timedelta(weeks=52)
start_date -= timedelta(days=start_date.weekday() + 1)  # Align to Sunday

for week, row in enumerate(lol[0]):  # use row length to count weeks
    for day in range(7):  # each row is 7 days
        if lol[day][week] == "#":
            commit_date = start_date + timedelta(weeks=week, days=day)
            for _ in range(5):  # 5 commits = darker square
                with open("commit.txt", "a") as f:
                    f.write(f"Commit for {commit_date}\n")
                env = os.environ.copy()
                env['GIT_AUTHOR_DATE'] = commit_date.strftime('%Y-%m-%dT12:00:00')
                env['GIT_COMMITTER_DATE'] = commit_date.strftime('%Y-%m-%dT12:00:00')
                subprocess.run(["git", "add", "."], env=env)
                subprocess.run(["git", "commit", "-m", f"Commit on {commit_date}"], env=env)

print("Finished generating 'LOL'!")
