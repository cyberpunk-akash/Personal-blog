# Personal-blog
Personal blog which has features like posting, commenting, approving comments, deleting posts, saving drafts and many more

The blog project is my first Django project and is part of the Udemy course on Django full stack development which I recently completed. It is a typical blog web application which has features like posting, commenting, approving comments, deleting comments and posts, editing posts, storing posts as drafts, etc. Only the superusers can write posts for which they need to log in to the application whereas commenting can be done by anybody. Users can access the inline editor toolbar while writing posts using which they can keep some words italic, bold, increase font size, etc.

The technology stack of the project is :
HTML, CSS, Bootstrap4, Javascript for frontend.
Python3 and Django2 for backend and server integration.

To use the project, you need to follow these steps after cloning:
1. Install python3 
2. Install django2
3. Install a text editor(preferably Atom or Sublime) to view the files.
4. Install pip
5. Run 'npm install medium-editor'
6. Go to directory 'blog_project' which has a file 'manage.py'
7. Run 'python manage.py migrate' on the terminal
8. Run 'python manage.py makemigrations post'

9.Run 'python manage.py migrate' again

10.Run 'python manage.py runserver'

11.The output of the previous command is an URL, copy the URL on your browser and run, now you can use the web application.


