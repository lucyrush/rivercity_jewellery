# **Rivercity Jewellery**


View live project [here](https://rivercity-jewellery.herokuapp.com/) 


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
- Easily recover my password if I forget it so that I can recover access to my account
- Have a personalised user account so that I can view my personal order history and order confirmations, and save my payment information
- Easily navigate to the blog so that I can read the latest blog posts
- See short descriptions of each blog, so that I can quickly decide which blog post I would like to read
- Easily navigate to the blog post details so that I can read the full blog post to learn new information about jewellery
- Easily leave comments, pending approval by the site user so that I can express my thoughts on the blog post 

### As a site owner, I want to be able to:
- Easily add new products to sell, so that I can keep my store reflecting new products in my inventory
- Easily edit/update existing products that are listed, so that I can keep my products listing up to date with the correct information 
- Quickly delete products should they no longer be available to the shopper, so that I can make sure the shopper does not select a product that is no longer available 
- Easily create new blog post, edit existing blog posts and delete blog posts, so that I can keep my blog up to date with new posts and delete post that may no longer be relevant

### As a shopper, I want to be able to:
- Sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products
- Sort a specific category of product so that I can find the best rated or best priced product within a specific category
- Sort multiple categories of products simultaneously so that I can find the best rated or best priced product within a specific category such as 'rings' or 'necklaces'
- Sort for a product by name, description and artist so that I can Find a specific product with known keywords
- Easily see what I have searched for so that I can quickly see if the product I have searched for is available
- Easily select the quantity of a product when purchasing it so that I can ensure I dont select the wrong product, or quantity
- Adjust the quantity of items I would like to buy, so that I can make sure that I am buying the desired amount
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
The responsive navigation bar contains four main sections. The first is the Rivercity Jewellery logo which is just a heading, following the logo link to navigate the user back to the landing page. 

The second section is the search bar, where the user can search for products by their name and description.

The next section is the details for My Account page, with the dropdown menu directing the superuser to the Product and Blog management form, if the user is not a superuser, they can direct themselves to their Profile page or to log out. Then the Shopping cart is included, the user should be able to see the monetary value of the products they have added to their cart. 

If the user is visiting the site and would like to register they can do so via the ‘My Account’ button. They will register themselves with their email address and receive an email confirmation once they have registered, the email confirmation will contain the link they need to follow to completely sign in. 

The fourth section is the product navigation section. Where the user can navigate to different product categories. The user will also be able to navigate through to the Blog section. 

 
#### Footer 
The footer was included to keep up with standard site navigation. The links to the social media accounts can be used to direct the user to the sites relevant social media. This footer also includes a quick copyright write up as this project is only for educational purposes. 

### Features of individual pages

#### Home Page 
The hero image is that of a woman swimming in dark water with attention drawn to a gold chain and pendant. I feel that this image plays well to the name of the store. 

You will find two call to action buttons on the landing page. The ‘Shop Now’ button directs the user to the All products page. The ‘Artist’s Blog’ page directs the user to the blog list 

#### Products Pages
The products page allows the user to see exactly which products are for sale. The products can be sorted by price, rating, name or category. Users can click on the product image to navigate to the product details page. They can then add the product to their shopping cart and proceed to checkout should they wish. 

Superusers can update the details of a product easily either by clicking the delete button found under the items on the Product Details page, and then amending the form.
 
#### Blog Page
The blog app currently has 3 blog posts. When navigating to the blog page, the user will see a list of the blog posts. An image for each blog post has been included. As more blog posts are added by the superuser/site owner the user will be able to see them. Should the user click on the ‘See More’ button, they will be directed to the blog details page where they can read the blog post with more detail. 

The user will be able to leave comments on each of the blog posts in the blog details page. The comments will be approved by the site owner and can be deleted at any time. 

The blog posts can also be edited and deleted by the superuser. This allows the site owner to be able to make changes to the blog list as they see fit. 

#### Profile Page 
Users will be able to navigate to their Profile page via the navigation bar at the top of site. This page is where they will be able to update their profile details like their shipping address and full name. Users will also be able to see an order history details. If they have made purchases before, they will be able to see then here, if not the order history will be empty. 

#### Checkout
Similar to the Profile page, this is where the user will be able to confirm the shipping address. The user will be prompted to fill out their information to complete the order here. The user will also be able to order a summary, including the quantity per product they are purchasing, the subtotal per product and then the grand total of their order. I have implemented Stripe to manage payments. Once the order has been completed and payment has been processed, the user will receive an email confirmation. 

## Features Left To Implement 
- Defensive delete button: Currently, the Delete button to delete a product has no defence to stop it being accidentally/automatically pressed. A confirmation of delete should be added.

- Leave reviews beneath products: Reading reviews are a great way to help users decide to purchase a product. This feature would be great to include in the future but was not seen as imperative for launch.



# Technologies Used

## Front-End Technologies
- [HTML](https://html.com/)
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
- [JQuery](https://jquery.com/) to simplify DOM manipulation.
- [Stripe](https://stripe.com/) as a payment platform to validate and accept credit card payments securely.
- [AWS S3](http://aws.amazon.com/) to store images held in the database
- [MDBoostrap](https://mdbootstrap.com/) a front end framework used to create responsive aspects across the site.
- [Bootstrap](https://getbootstrap.com/) 4 to help with other responsive aspects of the site.

## Back-End Technologies
- [Python](https://www.python.org/) The backend programming language
- [Django 3.0](https://docs.djangoproject.com/en/3.0/releases/3.0/) the backend framework for rapid development & clean designs
- [Heroku](http://heroku.com/) the hosting platform used for deployment
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQLite](https://www.sqlite.org/index.html) for development database, provided by django.

## Other Tools Used
- [Gitpod](http://gitpod.io/) the cloud based IDE used for development
- [Github](https://github.com/) to store and share all project code remotely.
- [Balsamiq](https://balsamiq.com/?gclid=Cj0KCQjwo6D4BRDgARIsAA6uN1-NxDOthq9pGqYzB_1iRxlBvHVwi_4_LaZuGqQT46csctF0xCiTXUMaAqmuEALw_wcB) used to create low fidelity wireframes
- [Google Sheets](https://www.google.com/sheets/about/) Used to create the database schema diagram
- [Unsplash](https://unsplash.com/) used to get the images
- [AutoPep8](https://pypi.org/project/autopep8/) a python add on, to format code into PEP8 formatting.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable the creation, configuration, and management of AWS S3.
- [Django allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) to create the signup/login functionality across the site.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style Django forms.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with Django to work with boto3 and AWS S3.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in the deployment of the Django project to Heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) a python imaging library to aid in processing image files to store in the database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.

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
- https://unsplash.com/photos/s8SJ8pmxPDA?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
- https://unsplash.com/photos/zTxp7jb5osM?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink




