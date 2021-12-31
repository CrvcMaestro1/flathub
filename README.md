# Flat Challenge

## About

The project is developed using Python 3.7 and Django REST Framework.

## Installation

Once Python 3.7 is installed, proceed to:

- Clone project.

- Install dependencies from the file `requirements.txt` or:

  ```
  pip install Django==2.2
  pip install djangorestframework==3.12.1
  ```
  
- Go to the [flathub/settings.py](https://github.com/CrvcMaestro1/flathub/blob/ded7146d891867094a14e3056652a38b8075aba3/flathub/settings.py#L120) and edit the three variables with the following information:

  - `GITHUB` Replace owner and repo according to url pattern (better if repo is public). Example:
    
    ```
    GITHUB = 'https://api.github.com/repos/FlatDigital/fullstack-interview-test'
    ```

  - `TOKEN` In your profile, in the developer settings tag, request a token and grant permissions for public repositories. Then replace here. Example:

    ```
    TOKEN = 'ghp_QWERTY'
    ```

  - `BASE_URL` Replace with your url and port of your choice. Example:

    ```
    BASE_URL = 'http://127.0.0.1:8000/api'
    ```
    
 - Then finally in the root of `manage.py` run:

    ```
    python manage.py runserver
    ```

## About API URL's

-	A view where we can see the existing branches
	
    ```
    http://127.0.0.1:8000/api/branch/
    ```

-	A branch detail view where we can see all the commits to one specific branch, with commit messages, authors and timestamps. Inside the branches view you can see the commits of each branch by following the `commits` key link. Where the parameter is the sha of the branch.
      
      ```
      http://127.0.0.1:8000/api/branch/d2f1be17877ef9d7c90e6e2d5414cc966064dcd0/commits
      ```

- A commit detail view where we can see the commit message, timestamp, and number of files changed and author names / emails. Inside the commits view you can see the commit information following the link of the `commit` key. Where the parameter is the sha of the commit.

    ```
    http://127.0.0.1:8000/api/commits/d2f1be17877ef9d7c90e6e2d5414cc966064dcd0/commit
    ```


-	A "PR" create view, where we can choose two branches (base and compare), and merge them together, just like Pull Requests work in GitHub. You will be able to create PR's by going to the end of the interface where you will have a form provided by Django REST to fill out.

    ```
    http://127.0.0.1:8000/api/pulls/
    ```
    
    Example
    
    ![image](https://user-images.githubusercontent.com/25228719/147788577-a6418a96-f7b7-49bf-9f7e-13c673d900b4.png)


-	A "PR" list view, where we see all created PRs and the following info: Author, Title, Description and Status (Open, Closed, Merged). If the status is Open, there should be a button that allows us to mark it as Closed. Inside the PR's view you can change the status of the PR if it is open following the link of the "close_pull" key and inside it go to the end to send by PUT the pull number parameter.

    ```
    http://127.0.0.1:8000/api/pull/6/
    ```
    
 ## Notes
 
 If you have any comments on the project or its execution, please let me know by mail [Crvc1998@gmail.com](mailto:Crvc1998@gmail.com).
