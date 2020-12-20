**Table of Contents**

1. [Code Testing](#code-testing)
  - [Validator Testing](#validator-testing)
  - [Python Unit Testing](#python-unit-testing)
2. [User Story Testing](#user-story-testing)
3. [Manual Testing](#manual-tesing)
  - [Lighthouse](#ighthouse)
  - [Responsive Testing](#responsive-testing)
   - [Desktop Testing](#desktop-testing)
   - [Laptop Testing](#laptop-testing)
   - [Tablet Testing](#tablet-testing)
   - [Mobile Testing](#mobile-testing)
4. [Bugs Discovered](#bugs-disccovered)
  - [Resolved Bugs](#resolved-bugs)
  - [Unresolved Bugs](#unresolved-bugs)
5. [Defensive Design](#defensive-design)
  - [Navbar](#navbar)
  - [Footer](#footer)
  - [Login/Signup](#login/signup)
  - [Products](#products)
  - [Checkout](#checkout)
  - [Blog](#blog)





# Mannual Testing 

- this will be the testing documentation 

## Code Testing 

### Automated Testing 

In addition to the full manual testing, I also decided to add some automated testing, as advised in the short testing section of the course. The automated testing can be improved.
I am not 100% confident with automated testing just yet! 

I created 11 automated tests in total. These include:

Checkout>tests.py: Order form testing
Products>tests.py: Product form testing and Product page view test

- In the terminal type the following command:
  `python manage.py test <<app name>>`
- The test results will be shown within the terminal.

### Validator Testing 

[W3C Markup Validation](https://validator.w3.org/nu/#textarea)

- HTML 

  
- CSS
 - No errors or warnings displayed
 

 [JSHINT](https://jshint.com/)

- When run through the [JSHint validator](https://jshint.com/) these metrics were returned:
 - There are 5 functions in this file.
 - Function with the largest signature take 1 arguments, while the median is 1.
 - Largest function has 10 statements in it, while the median is 5.
 - The most complex function has a cyclomatic complexity value of 3 while the median is 1.
 
[Python PEP8](https://pypi.org/project/autopep8/)

- The autopep8 extension was installed in the workspace.

- To install this enter this in the terminal:
  - `pip3 install --upgrade autopep8`

- Each and every .py file has been check over to make sure it complies with PEP8 formatting rules, both manually in the Gitpod window, as well as running the code through http://pep8online.com/.

There are no errors through the PEP8 check. However, there are a couple of highlighted rows of code where I have decided not to make the suggested corrections:
 - ‘Avoid using null=True on string based fields.’ Pages with error: Blog>models.py & products>models.py I have left this error as it is a string path to a source file.
 - ‘Avoid using null=True on string based fields.’ Pages with error: checkout>models.py, profiles>models.py, product>models.py
 - ‘Line too long’ Pages with error: settings.py, checkout>webhooks.py, checkout>webhook_handler.py, checkout>models.py These have been left as is as these lines should not be broken.


### Known Issues 


## Functional Testing

Testing User Stories from User Experience (UX) Section

### First Time Visitor Goals



### Returning Visitor Goals



### Frequent User Goals