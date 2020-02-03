# Personal-blog

The blog project is my first Django project and is part of the Udemy course on Django full stack development which I recently completed. It is a typical blog web application which has features like posting, commenting, approving comments, deleting comments and posts, editing posts, storing posts as drafts, etc. Only the superusers can write posts for which they need to log in to the application whereas commenting can be done by anybody. Users can access the inline editor toolbar while writing posts using which they can keep some words italic, bold, increase font size, etc.

### Technology Stack:
**Frontend**: HTML, CSS, Bootstrap4, Javascript
**Backend**: Python3, Django2

To run the project, you need to follow these steps after cloning:
- Install python3 
- Install pip
- Install django2
- Install a text editor(preferably Atom or Sublime) to view the files.
- Run `npm install medium-editor` on the command line.
- Go to directory 'blog_project' which has a file 'manage.py'
- Run the following commands:
```python
python manage.py migrate
python manage.py makemigrations blog
python manage.py migrate
python manage.py runserver
```
- The output of the last command is an URL, copy the URL on your browser and run, now you can run the web application locally.
