# Django Basic for Backend:

- start a new project: `django-admin startproject <project_name>`
- running the server: `python manage.py runserver`
- build an application web: `python manage.py startapp <app_name>`
- 

## Application:
- Routes: `urls.py` routing and render the responsive
- Views: `views.py` config the server
- Template, Static: using `HTML,CSS` to build a web page
- Models, migrations: `model.py`, config the database and tables

## [hello_application:](/server/hello/)
Two main routes: `index` and `greet`
>  **`index`:** hello, world!
>  **`greet`:** routing `hello`/`<input:string>`

## [newyear_app:](/server/newyear/)
Just one routes:
    `index`: Is today newyear? If not, send `NO`, else send `YES`

## [tasks_app:](/server/tasks/)
Two routes: `index` and `add`
> **add:** to create task and send by django-form to **index**