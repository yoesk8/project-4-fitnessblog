# TrueFit blog website

![TrueFit](media/home_desktop_view.png)

[Visit the live site](https://portfolio-4-fitnessblog.herokuapp.com/).

The purpose of this application is to help users find useful information on fitness, nutrition and other related subjects while also being able to post articles and interact with other blog members through the comment section.


* The Home page for first time users has an attractive image welcoming the user and with a brief explanation of what the blog is
* All users can add create articles, like and comment on posts once logged in.
* If the first time user doesn't want to sign-up he can still read the articles



***

## User Experience

### New User Stories

* As a new user, I want to be able to easily navigate the website and find relevant information on different types of exercises and workout plans.
* As a busy working professional, I want to be able to access short training articles that can be read in a short amount of time, such as 5 minutes or less.
* As someone recovering from an injury, I want to be able to find short articles that provide information and tips on how to safely exercise with specific limitations.


### Returning User Stories

* As a returning user, I want to be able to quickly access the features I’m interested in.
* As a returning user, I want to be able to leave comments on articles to share my own experiences and provide feedback to the author.
* As a returning user, I want to be able to like or upvote articles that I find helpful or informative, so that other users can easily see which articles are most valuable.



### Design

The site uses the Bootstrap framework. I used a simple colour pallete that makes the article content pop out.

#### Colours and Shades

* The site uses a light shade of grey for the site’s header and footer, and a darker shade for the LogIn/SignUp buttons.

* The color of the background is white and text is black to reinforce the contrast and make it easier to read for the user.

* Colours are used consistently in association with a particular type of task:

* Dark grey is used on the login / signup buttons.

* Bootstrap's light blue (Primary) is used on the Read article button / and for the articles with the category "Training".

* Bootstrap's green (Success) is used for the articls with the category "Nutrition".




#### Typography

* The site logo uses the Rowdies font [Rowdies font](https://fonts.google.com/specimen/Rowdies) from Google Fonts. This font was selected for its high legibility and simple yet elegant design.

* All other text on the site uses the standard Bootstrap framework font stack, which consists of a number of simple, legible sans-serif fonts targeted at a range of different viewing devices and operating systems.

#### Imagery

* [Font Awesome 6](https://fontawesome.com/) icons are used for the logo and the comment and like buttons.

* [Unsplash ](https://unsplash.com/) I used a stock photo from unsplash the home page.(https://unsplash.com/photos/zQNDCje06VM)
* [Unsplash ](https://unsplash.com/) I used stock photos from unsplash for all 3 of the pre-written articles thumbnails.(https://unsplash.com/photos/)

## Wireframes

The site is responsively designed to adapt to the user's viewing device.

### Desktop view wireframe

 ![desktop wireframe](media/desktop_wireframe.png)


### Mobile view wireframe

 ![Mobile wireframe](media/mobile_wireframe.png)


## Home Desktop view

 ![Home desktop view](media/home_desktop_view.png)

 ## Mobile Home view

 ![Mobile Home view](media/home_mobile_view.png)
 
 ## Log in desktop view

 ![login desktop view](media/login_desktop_view.png)  

  ## Log in mobile view

 ![login mobile view](media/login_mobile_view.png)  

 ## Sign up mobile view

 ![Sign up mobile view](media/signup_mobile_view.png)  
***

## Features

### User Accounts

PoolTest Buddy features a user account system whereby users can create a persistent account, accessed by username and password, and store tests associated with their account.

* Users create accounts by filling in a simple registration form.

![Registration form](static/documentation_images/sign_up_screenshot.png)

* Users sign in to their accounts by filling in a login form and sign out using a link in the navigation bar.

![Login form](static/documentation_images/login_screenshot.png)

* The application uses the Flask session object to handle user login functionality and passwords are hashed using Werkzeug helper functions.

### Pool tests Log

The core feature of PoolTest buddy is a log allowing users to record their completed pool tests. Full CRUD (create, read, update, delete) functionality is implemented for tests logs, so the admin user can add, delete and edit their records as he wishes while regular users can only add logs.

* Tests logs are added by completing a form, which is linked to from buttons on the New reading page.

![Add workout logs by filling a form](static/documentation_images/add_reading_screenshot.png)

* All test logs are listed on the home page.

![List of tests logs](static/documentation_images/readings_screenshot.png)


* When editing a log entry, the form is prepopulated with the current values of that log.

![Prepopulated edit log form](static/documentation_images/edit_reading.png)

### Pool test Management


* By design, users cannot edit or delete the pool test records, as this prevents altering of previous records which could cause issues. However, the ‘admin’ user account can add, edit or delete records. This allows the site admin to make changes to the any error a normal user might have comitted while also adding a barrier to avoid dishonest behaviour.

![Admin view of previous test](static/documentation_images/admin_edit.png)


*  When editing a test, the form is prepopulated with the current values of that routine.

![Edit test logs are prepopulated](static/documentation_images/edit_reading.png)


### FAQ

New users are adviced to visit the F.A.Q page at the home screen. The FAQ page has answers to common questions.


* The FAQ page provides answers to common questions in a collapsible accordion. Users can find detailed instructions for how to complete a test here.

![FAQ accordion](static/documentation_images/faq.png)



***

## Database Design

TrueFit uses a SQL database. Data is divided into three collections, with the following schema:

![Datbase diagram](media/database_schema.png)

***

## Future Features

The following features could be added in the future, given more development time:

### 1. Account Management Tools

* Helpful account management tools could be provided, such as the ability to update usernames, email addresses and passwords.
* A password recovery by email function could also be provided. The [flask-security](https://pythonhosted.org/Flask-Security/features.html) extension can provide this functionality, as well as some other more advanced account management tools.

### 2. Additional Log Filters

* Admin user to be able to filter the log page by date range.


### 3. Simplification of the add readings form

* Eliminating the "Combined chlorine selection option and just subtracting the Total minus the free and populating that area accordingly

### 4. Email notification to the admin when readings are outside parameters

* Admin to automatically receive an email whenever readings are outside parameters and action is needed

### 5. Code optimization and refactoring

* This was my first major project using Python and Flask, so there are a few areas where I feel the code could be made neater and more efficient.
* In particular, more helper functions could be employed to avoid repeating common tasks across the different functions.


***

## Technologies

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.m.wikipedia.org/wiki/JavaScript)
* [Python](https://en.m.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [GitHub](https://github.com/) - Used for version control.
2. [GitPod](https://gitpod.io/) - Used to write all code and test before deploying to GitHub.
3. [Mockplus](https://mockplus.com/) - Used to produce design wireframes.
4. [Materialize](https://materializecss.com/) - Materialize CSS framework used extensively to create layout and styling of site.
5. [jQuery](https://jquery.com/) - Used to initialise Materialize components and validate select elements.
6. [Python 3.8](https://www.python.org/) - Used to code the application.
7. [MongoDB](https://www.mongodb.com/) - Used for the application's database.
7. [Flask](https://palletsprojects.com/p/flask/), [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) and [Werkzeug](https://palletsprojects.com/p/werkzeug/) - Used to build the main application structure, page templates (Jinja) and account security (Werkzeug).
8. [PyMongo](https://github.com/mongodb/mongo-python-driver) - Used to connect Python with MongoDB
9. [Heroku](https://heroku.com/) - Used to deploy the site.
10. [W3C.org](https://www.w3.org/) - W3C [HTML Validator](https://validator.w3.org/nu/) and [CSS Validator](https://jigsaw.w3.org/css-validator/validator) used to check HTML and CSS code for errors.
11. [JSHint](https://jshint.com/) - Used to check JavaScript for errors.
12. [PEP8 Online](http://pep8online.com/) - Used to check Python code for errors.
13. [Kaffeine Heroku](http://kaffeine.herokuapp.com/) -Used to ensure that heroku page doesn't hibernate (Note that page goes to 'sleep' at midnight until 6 am and is not available during those 6 hours)


***

## Testing

## Functionality testing 

 I used Chrome developer tools throughout the project for testing and solving problems with responsiveness and style issues.


## Compatibility testing
 Site was tested across multiple virtual mobile devices and browsers. I checked all supported devices in Chrome developer tools. 
 
 I tested on hardware devices such as: Ipad air with iOS, Iphone 13 mini with iOS 15.4, Macbook air with MacOS and Surface Pro with windows 10


---
## Issues found during site development

* ### Edit reading page not pre-populating the previously selection


![testing-issue-1](static/documentation_images/pre_populating_edit.png)

When clicking on the 'edit' button on a previously recorded pool test, I noticed that the right fields were not being selected and on some ocassions not even appearing on the select fields

> I fixed this by adding the 'value' attribute to the options tag and populating it with the correct Jinja expression to access the relevant data.



* ### Logo overflowing on small and extra small devices

> I fixed this by adding a media query which removes the logo completely by setting the display to 'none' when in small devices.

![resolved4](static/documentation_images/media_query_fix.png)


* ### Login not working.

![testing_issue_2](static/documentation_images/endpoint_non_existent.JPG)

This one was a tough one for me, as I changed the name of some of the templates, the endpoint was not being built properly as it was still pointing to non-existing pages.

> I fixed this by updating the relevant python functions with the new names of the html pages that flask was pointing to.

![resolved](assets/readme-images/counter1.png)


## Performance testing

I run [Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool to check performance of the website.
Screenshots are presented below:


Final results:
![performance_final](static/documentation_images/light_house_testing.png)

I noticed that this tests scores vary from time to time and depends on external libraries as well. 



## Code Validation
 At the end of the project I used three websites to validate my code:
 
 * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS

 ![CSS validator](static/documentation_images/css_validation.png)

 * [Nu Html Checker](https://validator.w3.org/) to test HTML

 ![HTML validator](static/documentation_images/home_html_validation.png)

 * [JShint](https://jshint.com/) to test JavaScript

 ![JS validator](static/documentation_images/javascript_va;idation.png)
 
 * [Pep8](https://pypi.org/project/pep8/) to test python

 ![JS validator](static/documentation_images/pep8_validation.png)




***

## Deployment

### Forking the GitHub Repository

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/yoesk8/pooltesting_buddy_PP3)
2. At the top right of the page, click the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

You can download the project source code as a zip file by clicking the 'Code' dropdown at the top right of the file navigation window and selecting "Download as ZIP". You can then unzip that file to wherever you want your local copy to be.

If you have Git installed on your computer, you can clone the project by following these steps:

1. Log in to GitHub and locate the [repository](https://github.com/yoesk8/pooltesting_buddy_PP3)
2. Click the 'Code' dropdown at the top right of the file navigation window.
3. Copy the link under 'Clone' and 'HTTPS' to clone the repository using HTTPS.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/yoesk8/pooltesting_buddy_PP3
```
7. Press Enter. Your local clone will be created.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://github.com/yoesk8/pooltesting_buddy_PP3)

### Database Setup

The project uses MongoDB, so for either local or remote deployment you'll need a properly configured database.

1. If you don't have a MongoDB account, sign up for a free account at [MongoDB](https://www.mongodb.com/).
2. If you don't have any clusters, create a new cluster.
3. Add a new database to your cluster with the name: **pooltesting_buddy**
4. The pooltesting_buddy database should have three collections with the following setup:

**users**
```
_id: <ObjectId>
username: <string>
name: <string>
password: <string>
```

**pool_type**
```
_id: <ObjectId>
max_batherload: <string>
type: <string>
```

**readings**
```
_id: <ObjectId>
date: <string>
time: <string>
pool_type: <string>
free_chlorine: <string>
total_chlorine: <string>
combined_chlorine: <string>
ph: <string>
water_temperature: <string>
outside_parameters: <string>
```



In order to connect to the database, you'll need to create a user and generate a MongoDB URI. 

#### Creating a Database User

1. Go to the Overview page of your cluster 
2. Click Database Access under Security in the side menu
3. Next click Add New Database User
4. Select Password as the authentication method and then enter a username and password
5. Under "Built-in role" select "Read and write to any database"
6. Click "Add User"

#### Generating a MongoDB URI

1. Go to the Overview page of your cluster
2. Click the "Connect" button
3. Select "Connect your application"
4. Make sure 'Python' is selected for the driver, then copy the URI provided in the box
5. Replace the "password" and "myFirstDatabase" parts of the URI with your database user's password and the name of your database

### Local Deployment

Follow the steps below to deploy the project locally using VSCode.

(N.B. These instructions are for deployment on a Windows system)

1. Download and install [VSCode](https://code.visualstudio.com/)
6. Open VSCode and click File > Open Folder, then select the folder containing your local cloned repository
7. Download and install [Python](https://www.python.org/downloads/)
8. Download and install the [VSCode Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
9. In VSCode, open the command palette (Ctrl + Shift + P on Windows) and search for the Python: Select Interpreter. Click it, then select the version of Python you have installed.
10. Open a terminal in VSCode and enter the following commands to create and activate a virtual environment:
```
py -3 -m venv .venv
.venv\scripts\activate
```
11. Open the command palette and search for Python: Select Interpreter again. You should see your new virtual environment. Select it.
12. In the terminal, enter the following command to install all required packages:
```
python -m pip install -r requirements.txt
```
13. Create a new file in your project directory called "env.py"
14. Add the following to the env.py file, replacing YOUR_MONGO_URI with your MongoDB URI, YOUR_DATABASE_NAME with your database name, and YOUR_SECRET_KEY with a suitable [secret key](https://flask.palletsprojects.com/en/2.0.x/config/#SECRET_KEY):
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
os.environ.setdefault("MONGO_URI", "YOUR_MONGO_URI")
os.environ.setdefault("MONGO_DBNAME", "YOUR_DATABASE_NAME")
os.environ.setdefault("ENV_DEBUG", "True")
```
15. In the terminal, type `python app.py` to run the app. A link to the locally running instance of the app should be printed in the terminal window.

### Remote Deployment

The app is currently deployed on Heroku [here](https://pooltesting-buddy.herokuapp.com/).

To deploy your own copy of the app, follow the steps below:

1. Sign up for a [Heroku account](https://www.heroku.com/).
2. Check that you have a "requirements.txt" in your app's root directory. This tells Heroku what packages are required by the app. If you've cloned the main branch, this should already be present. If it's missing or if you have added any additional packages, you can generate a requirements.txt file by running the following command from the terminal of your IDE:
```
pip3 freeze --local > requirements.txt
```
3. Check that you have a "Procfile" in your app's root directory. This tells Heroku what kind of application you are trying to run. Again, if you've cloned the main branch, this should already be present. If it's missing, you can create a procfile by running the following command from the terminal of your IDE:
```
echo web: python app.py > Procfile
```
4. Check that there are no trailing blank lines at the bottom of your procfile. Delete any empty lines
5. From your Heroku dashboard, click "New", then "Create a new app"
6. Give the app a unique App name, pick the region closest to you, then click "Create App"
7. From the "Deploy" menu, select GitHub as the Deployment Method, then enter your GitHub repository details and click "Connect"
8. Open the "Settings" menu, scroll down to "Config Vars" and click "Reveal Config Vars"
9. Enter the following Config Vars, replacing YOUR_MONGO_URI with your MongoDB URI, YOUR_DATABASE_NAME with your database name, and YOUR_SECRET_KEY with a suitable [secret key](https://flask.palletsprojects.com/en/2.0.x/config/#SECRET_KEY):
```
IP: 0.0.0.0
PORT: 5000
SECRET_KEY: YOUR_SECRET_KEY
MONGO_URI: YOUR_MONGO_URI
MONGO_DBNAME: YOUR_DATABASE_NAME
ENV_DEBUG:
```
10. Note that ENV_DEBUG should be left blank, unless you wish to deploy the application with debug mode enabled
11. Return to the "Deploy" menu, scroll to "Automatic deploys" and click "Enable Automatic Deploys"
12. Choose your branch and then click "Deploy Branch"
13. Once the application has finished deploying, click "View" to visit the site.

***

## Other Credits and Acknowledgements

* [Code Institute](https://codeinstitute.net/) for their helpful lessons and reference materials.
* [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md) for the structure of this project's documentation and parts of the GitHub forking and cloning processes.
