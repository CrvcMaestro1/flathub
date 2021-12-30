•	A view where we can see the existing branches

http://127.0.0.1:8000/api/branch/

•	A branch detail view where we can see all the commits to one specific branch, with commit messages, authors and timestamps.

Inside the branches view you can see the commits of each branch by following the "commits" key link. http://127.0.0.1:8000/api/branch/d2f1be17877ef9d7c90e6e2d5414cc966064dcd0/commits
Where the parameter is the sha of the branch.


•	A commit detail view where we can see the commit message, timestamp, and number of files changed and author names / emails.

Inside the commits view you can see the commit information following the link of the "commit" key.
http://127.0.0.1:8000/api/commits/d2f1be17877ef9d7c90e6e2d5414cc966064dcd0/commit/
Where the parameter is the sha of the commit.


•	A "PR" create view, where we can choose two branches (base and compare), and merge them together, just like Pull Requests work in GitHub.

http://127.0.0.1:8000/api/pulls/
You will be able to create PR's by going to the end of the interface where you will have a form provided by Django REST to fill out.


•	A "PR" list view, where we see all created PRs and the following info: Author, Title, Description and Status (Open, Closed, Merged). If the status is Open, there should be a button that allows us to mark it as Closed.

To view the PR's
http://127.0.0.1:8000/api/pulls/
Inside the PR's view you can change the status of the PR if it is open following the link of the "close_pull" key and inside it go to the end to send by PUT the pull number parameter.
http://127.0.0.1:8000/api/pull/6/
