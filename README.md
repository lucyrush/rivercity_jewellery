# **Rivercity Jewellery**


View live project here 


# Table of Contents

1. [User Experience](#user-experience(ux))
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
2. [Wireframes](#wireframes)
3. [Features](#features)
  - [Existing Features](#existing-features)
    - [Features On All Pages](#features-on-all-pages)
    - [Features Of Individual Pages](#features-of-individual-pages)
  - [Features Left To Implement](#features-left-to-implement)
4. [Technologies Used](#technologies-used)
  - [Front-End Technologies](#front-end-technologies)
  - [Back-End Technologies](#back-end-technologies)
  - [Database Schema](#database-schema)
5. [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [Functional Testing](#functional-testing)
6. [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Remote Deployment](#remote-deployment)
7. [Content](#content)
  - [Media](#media)
  - [Credits](#credits)

# User Experience (UX)

## User Stories

### First Time Visitor Goals



### Returning Visitor Goals


### Frequent User Goals

## Design


### Colour Scheme



### Typography



### Imagery


## Wireframes

- Desktop


- Tablet

  
- Mobile
 

The current site layout is different to the wireframes due to a change in image choices and colour scheme.

# Features

## Existing Features 

### Features on all pages

#### Navbar
- There will be a difference in the navbars that is depenndent if the user is logged in or not by using their username and password. A jinja loop is used to determine which navbar to display
  - If not in session:  the homepage, listings page, register page and login page will be displayed. With a responsive navbar that contains links to the Home, Register and Login pages.
  - If in session: the homepage, listings page, profile page, new listing page and logout will be displayed. This is also responsive. 
 
#### Footer 
- A footer is at the bottom of every page 
  - The footer contains the contact details of the Adapt Easy creators, links to top of the page, login page and the register page. 
  - The footer is responsive

### Features of individual pages

#### Home Page 
- The hero image
  - The hero image is on 3 people walking a safe distance from each other, wearing masks. This image is a sign of times and a sight that all of us are used to by now!

 
- Extra Navigation Buttons


#### Products Pages


 
 #### Blog Page
 

  
#### Blog CRUD Pages


#### Profile Page 



## Features Left To Implement 



# Technologies Used

- Gitpod - Used as the IDE for this application.
- Github used for the remote storage of the code online.

## Font-End Technologies
- HTML - Used to create the structure of the application.
- CSS - Used as the base for styling.
- Javascript - Used to create interactivity within the project
- JQuery - Used for some of the main javascript functionality.
.

## Back-End Technologies
- Flask - Used as the microframework.
- Jinja - Used for templating with Flask.
- Heroku - Used to host the application
- Python - The back-end programming language.
- Pymongo - Used to connect the python with the database.
- MongoDB Atlas - Used to store the database.

## Database Schema






# Testing 

## Code Testing 

### Validator Testing 

[W3C Markup Validation](https://validator.w3.org/nu/#textarea)

- HTML 
 
  
- CSS
 

 [JSHINT](https://jshint.com/)

- When run through the [JSHint validator](https://jshint.com/) these metrics were returned:
 


[Python PEP8](https://pypi.org/project/autopep8/)

- The autopep8 extension was installed in the workspace.

- To install this enter this in the terminal:
  - `pip3 install --upgrade autopep8`

- Then, you can format the code into PEP8 formatting by entering this command into the terminal:
  - `autopep8 --in-place --aggressive --aggressive app.py`
  


### Known Issues 


## Functional Testing

Testing User Stories from User Experience (UX) Section

### First Time Visitor Goals



### Returning Visitor Goals



### Frequent User Goals


# Deployment

## Local Deployment 

### To run this project locally

In order to run this project locally, you will need to install the following:
- An IDE, such as [VS Code](https://code.visualstudio.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) to install the app requirements.
- [Python3](https://www.python.org/downloads/) to run the application
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for version control
- [MongoDB](https://www.mongodb.com/) to develop the database.
 -Once this is done, you will need need to download the .ZIP file of the repository, unzip this file and then in the CLI with GIT installed, enter the following command:
  - ``https://github.com/lucyrush/adapt-easy.git``

- Navigate to the to path using the ``cd`` command.

- Create a `.env` file with your credentials. Be sure to include your `MONGO_URI` and `SECRET_KEY` values.

- Install all requirements from the ``requirements.txt`` file using the following command:
  - ``sudo -H pip3 -r requirements.txt``

- Sign up for a free account on MongoDB and create a new Database called adapt-easy. The names of the databases collections can be found in the database schema section.

- You should then be able to launch your app using the following command in your terminal:
  - ``python app.py``

## Remote Deployment 

- Create a ``requirements.txt`` file using the terminal command ``pip freeze > requirements.txt``
- Create a Procfile with the terminal command ``echo web: python app.py > Procfile``
- ``git add`` and ``git commit`` the new requirements and Procfile and then ``git push`` the project to GitHub.
- Navigate over to [Heroku](https://id.heroku.com/login)
- Click the "new" button, give the project a name & set the region to Europe.
- From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
- Confirm the linking of the heroku app to the correct GitHub repository.
- In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
- Set the following config vars:

| KEY           | Value         | 
| ------------- |:-------------:| 
| DEBUG          | FALSE         | 
| IP            | 	0.0.0.0      |
| PORT          | 5000           | 
| MONGODBNAME   | <database_name>   | 
| MONGO_URI      | mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority  | 
|SECRET_KEY     | <secret_key>    | 


# Content



## Media 



## Credits

 



