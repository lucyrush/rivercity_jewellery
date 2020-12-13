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

### As a site user, I want to be able to:
- Easily register for an account, so that I can be able to have a personal account and be able to view my profile 
- Easily login and logout, so that I can access my personal account and easily logout to quit the session
- Easily revoer my password if I forget it so that I can recover access to my account
- Have a personalised user account so that I can view my personal order history and order confirmations, and save my payment information
- Easily navigate to the blog so that I can read the latest blog posts
- See short desriptions of each blog, so that I can quickly decide which blog post I would like to read
- Easily naigate to the blog post details so that I can read the full blog post to learn new information about jewellery
- Easily leave comments, pending approval by the site user so that I can express my thoughts on the blog post 

### As a site owner, I want to be able to:
- Easily add new products to sell, so that I can keep my store reflecting new products in my inventory
- Easily edit/update existing products that are listed, so that I can keep my products listing up to date with the correct information 
- Quickly delete products should they no longer be available to the shopper, so that I can make sure the shopper does not select a product that is no longer available 
- Easily create new blog post, edit existing blog posts and delete blog posts, so that I can keep my blog up to date with new posts and delete post that may no longer be relevant

### As a shopper, I want to be able to:
- Sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products
- Sort a specific category of product so that I can find he best rated or best priced product within a specific category
- Sort multiple categories of products simaltaneously so that I can find he best rated or best priced product within a specific category such as 'rings' or 'necklaces'
- Sort for a product by name, description and artist so that I can Find a specific product with known keywords
- Easily see what I have searched for so that I can quickly see if the product I have searched for is available
- Easily select the quantity of a product when purchasing it so that I can ensure I dont select the wrong product, or quantity
- Adjust the quantitiy of items I would like to buy, so that I can make sure that I am buying the desired amount
- Easily see the subtotal for each item, so that I can get an idea of how much I am spending on each item 
- Safely and securely use my card details to make the payment, so that I can have peace of mind that the payment is safe
- Save my details on the site, so that I can be a return shopper without the hassle of re-entering all of my details 
- View an order confirmation after checkout, so that I can verify that I have not made any mistakes
- Receive an email confirmation after checkout, so that I can keep the confirmation of what I have purchased in my records

## Design


### Colour Scheme



### Typography



### Imagery


## Wireframes

- [Home](readme-additions/home-wireframe.JPG)
- [Sign In/Register](readme-additions/signin-wireframes.JPG)
- [Products](readme-additions/products-wireframes.JPG)
- [Product Details](readme-additions/prudctdeets-wireframes.JPG)
- [Checkout](readme-additions/checkout-wireframes.JPG)
- [Blog](readme-additions/blog-wireframes.JPG)
- [Blog Details](readme-additions/blogdeets-wireframes.JPG)
 

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

For more information about the testing of this site, please continue to the [testing.md](readme-additions/testing.md) documentation

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

 



