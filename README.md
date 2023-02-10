## MULTI USER ROLE AUTHENTICATION SYSTEM
---

This is a fullstack reusable capstone project that handles multi user roles authentication system built with Django, React and Redux.

## Overview

I've always been fascinated by how applications with multiple user roles and permissions are run, developed, and configured. As a learning challenge, I decided to uncover and dig beneath the hood.


#### Setup and dependacies
##### General
- IDE of your choice

##### Backend
- Python 3.6 +
- Django 4.0.1 +
- Django Rest Framework
- More depedancies listed in **backend/requirements.txt**

##### Frontend
- Javascript
- Node
- Express
- Redux

### How to install this project
1. Clone this repository

```
    git clone https://github.com/John-Kimani/MULTI_USER_ROLE_AUTHENTICATION.git
```

2. Navigate into project base folder 
```
    cd MULTI_USER_ROLE_AUTHENTICATION
```

3. Open project in your IDE. i.e VsCode users
```
    code .
```

### Available scripts

### Backend

Move into the **backend** folder to configure the backend server.

Create virtual envirionment.

```
    virtualvenv venv
```
Activate the virtual environment

```
    pipenv shell
```

Install all the required dependacies.
```
    pip install requirements.txt
```
Create a _.env_ file to hold your hidden project environment variables.

Create a postrgress database for my production and development configuration alrather set mode to lite to user the preinstalled SQLite3 database

#### Environment Variables

```
- SECRET_KEY='django-secret-key' or 'you-will-never-guess'
- MODE='dev' // development
- DEBUG=True
- DEV_DB_NAME='blackpanther22'
- DEV_DB_USER='postgres user' or 'allowed psql user'
- DEV_DB_PASSWORD='you-will-never-guess' or Null
- DEV_DB_HOST=provide default
- ALLOWED_HOSTS=provide for localhost
- CLOUDINARY_CLOUD_NAME=your cloudinary username
- CLOUDINARY_API_KEY=your cloudinary api
- CLOUDINARY_API_SECRET=your cloudinary secret key
- CSRF_TRUSTED_ORIGINS =[ALLOWED_HOSTS]
- DISABLE_COLLECTSTATIC=0
```

#### Continue with setup

Make migrations to the new database.
```bash
    python manage.py makemigrations
```

Migrate new configurations to database.
```bash
    python manage.py migrate
```

If successfull you can now configure the frontend application.
Move back to projects root folder _MULTI_USER_ROLE_AUTHENTICATION_

```bash
    cd ..
```

### Frontend

An expressJs server engine is used to handle and fix CORS related issues during development by technically having the client app rendered and sending requests from a proxy host.

From base folder navigate into frontend folder.

``` bash
    cd frontend
```

To install required package dependancies run;

```
    npm install
```


Navigate into the **frontend** folder to set up the client-side server.

frontend/client

```
    cd client
```

Install required package for the SPA application dependancies run;

```
    npm install
```


In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

#### Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).


### AUTHOR
This project was designed and developed by : [Kimani John](https://kimanijohn.netlify.app/)