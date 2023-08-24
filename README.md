# Nikolai Kapustin Works Database

A comprehensive database and API for the works of jazz/classical pianist Nikolai Kapustin.

## Table of Contents

- [Nikolai Kapustin Works Database](#nikolai-kapustin-works-database)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Setup and Installation](#setup-and-installation)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Testing the API](#testing-the-api)
    - [\[Steps to set up the frontend\]](#steps-to-set-up-the-frontend)
  - [API Endpoints](#api-endpoints)
    - [User Endpoints:](#user-endpoints)
    - [Works Endpoints](#works-endpoints)
  - [Design Documents](#design-documents)
  - [Contributors](#contributors)
  
## Introduction

Nikolai Kapustin, a renowned jazz/classical pianist, has a vast array of compositions. This project aims to create a detailed database of his works, providing an API for easy access and manipulation of the data.

## Features

- Comprehensive database of Kapustin's works.
- User authentication for API access.
- Advanced search and filter capabilities.

## Setup and Installation

### Requirements

1. You must have python(3) and pip installed.

### Installation

1.  Once the repository has been downloaded, navigate to the backend directory within the root.

```bash
cd backend/
```

2. To help with version control, I suggest using a venv before creating the database.

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the requirements using pip.

```bash
pip install -r requirements.txt
```

4.  Run the create_db.py and run_etl.py files to create and populate the SQLite database.

```bash
python3 etl/create_df.py
python3 etl/run_etl.py
```

5. Set the Flask application environment variable to the app.py, and set the Flask environment variable to be dev mode.

```bash
export FLASK_APP=api/app.py
export FLASK_ENV=development
```

6. Now, you can run the Flask application.

```bash
flask run
```

### Testing the API

1. With the server running, you can now use tools like curl or Postman to test the API endpoints. For example, to test the user registration endpoint:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "email":"test@user.com", "password":"testpasswd"}' http://127.0.0.1:5000/user
```

### [Steps to set up the frontend]

## API Endpoints

### User Endpoints:

| Description                   | Endpoint                    | Method |
|-------------------------------|-----------------------------|--------|
| **Register User**             | `/user`                     | POST   |
| **Login User**                | `/login`                    | POST   |
| **Logout User**               | `/logout`                   | POST   |

### Works Endpoints

| Description                           | Endpoint                                     | Method |
|---------------------------------------|----------------------------------------------|--------|
| Get All Works                         | `/opus`                                      | GET    |
| Add New Work                          | `/opus`                                      | POST   |
| Update Work                           | `/opus/{opusId}`                             | PUT    |
| Delete Work                           | `/opus/{opusId}`                             | DELETE |
| Get Work by Opus Number               | `/api/opus/{opusId}`                         | GET    |
| Get Works with No Recording           | `/opus/no-recording`                         | GET    |
| Get Works by Year                     | `/opus/year/{year}`                          | GET    |
| Get Works With 1 Section Only         | `/opus/one-section`                          | GET    |
| Get Works Referencing Other Artists   | `/opus/referenced`                           | GET    |
| Search Works by Title                 | `/api/opus/search/title?q={title}`           | GET    |
| Search Works by Section Name          | `/opus/search/section?name={sectionKeyword}` | GET    |
| Filter Works by Type                  | `/opus/filter?type={type}`                   | GET    |
| Filter Works by Year Range            | `/opus/year?start={startYear}&end={endYear}` | GET    |
| Filter Works by Instrument            | `/opus/filter?instruments={instrument1, ...}`| GET    |
| Filter Works by Number of Instruments | `/api/opus/search/title?q={title}`           | GET    |
| Filter Works by Maximum Length        | `/opus/filter?length-max={maxLength}`        | GET    |
| Filter Works by Minimum Length        | `/opus/filter?length-min={minLength}`        | GET    |
| Filter Works by Number of Sections    | `/opus/filter?num-sections={numSections}`    | GET    |


## Design Documents

- [Project Description and Timeline](./Design%20Documents/kapustin-DesignDoc.drawio.pdf)
- [Database UML](./Design%20Documents/kapustin-UML.drawio.pdf)
- [API Design](./Design%20Documents/kapustin-API.drawio.pdf)

## Contributors

- J. Alex Leeper
