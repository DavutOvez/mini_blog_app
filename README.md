# Django Blog App

This is a simple blog application built with Django. Users can create, edit, delete posts, and add comments to posts.  

> **Note:** This project was developed by Davut Ovezov, inspired by Oguzhan Mavi's Django Blog app.

## Features

- Create new blog posts
- Edit and delete existing posts
- View post details
- Add comments to posts

## Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/django-blog.git
  ```
2. Navigate to the project directory:
  ```bash
  cd mini_blog_app
  ```

3. Create a virtual environment and activate it:
  ```bash
  python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate
  ```

4. Apply migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

5.	Run the server:
  ```bash
  python manage.py runserver
  ```
  
