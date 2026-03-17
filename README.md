# expense_tracker

A web app to record expenses. Please view expense_tracker/tracker/* for the main feature.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT


## Basic Commands
The commands below uses docker compose as this app is built using docker. Please ensure to have docker installed.

### Build And Run The App Locally
- To build the app
    ```
    docker compose -f docker-compose.local.yml build
    ```
- To run the app
    ```
    docker compose -f docker-compose.local.yml up
    ```
### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:
    ```
    docker compose -f docker-compose.local.yml run --rm django uv run python manage.py createsuperuser
    ```
For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Running tests with pytest
```
docker compose -f docker-compose.local.yml run --rm django pytest
```

## Features

### API
#### User Token
- retrieve user token to access Record API
1. POST `api/auth-token/`
    - expected data: username, password
    - expected result: token
#### Record API
- allows list, detail, delete, patch and put record using user's token by having `Authorization: Token \<token\>`
1. GET `api/record/`
    - gets a list of record
    - expected result:
        - SUCCESS: list of records
        ```
        {
            "date": "YYYY-MM-DD",
            "name": <name>,
            "description": <description>,
            "amount": <amount>,
            "category_name": <category_name>
        }
        ```
2. GET `api/record/<pk>/`
    - get record
    - expected result:
        - SUCCESS: the record
        ```
        {
            "date": "YYYY-MM-DD",
            "name": <name>,
            "description": <description>,
            "amount": <amount>,
            "category_name": <category_name>
        }
        ```
        - ERROR: record not found
3. DELETE `api/record/<pk>/`
    - delete record
    - expected result:
        - SUCESS: the record is deleted
        - ERROR: record not found
4. PUT `api/record/<pk>/`
    - make full update of record
    - expected data: amount, name, category, date
    - expected result:
        - SUCCESS : record is updated
        - ERROR: record not found or field given is incorrect
5. PATCH `api/record/<pk>/`
    - update speficied field of record
    - expected data: amount, name, category, date
    - expected result:
        - SUCCESS : record is updated
        - ERROR: record not found or field given is incorrect

### Django Admin
- user with admin rights can view all data in the app
![django_admin](docs\\Images\\django_admin.jpg)

### Record Page
- only accessible for logged in user
#### /tracker/record
- contains the list of tracker and allows filtering the list of records
- allows user to add new record and view record.
![record_main](docs\\Images\\record_page_main.jpg)

#### /tracker/record/add
- allow user to add record
![record_add](docs\\Images\\record_page_add.jpg)

#### /tracker/record/\\<pk\\>/
- allow user to view record details and edit it
![record_detail](docs\\Images\\record_page_detail.jpg)

#### /tracker/record/\\<pk\\>/edit
- allow user to edit the record
![record_detail_edit](docs\\Images\\record_page_detail_edit.jpg)
