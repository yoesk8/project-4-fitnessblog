# TrueFit blog website

![TrueFit](media/home_desktop_view.png)

[Visit the live site](https://portfolio-4-fitnessblog.herokuapp.com/).

The purpose of this application is to help users find useful information on fitness, nutrition and other related subjects while also being able to post articles and interact with other blog members through the comment section.


* The Home page for first time users has an attractive image welcoming the user and with a brief explanation of what the blog is
* All users can create edit or delete their own articles, like and comment on other perople's articles if logged in.
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

TrueFit blog features a user account system whereby users can create a persistent account, accessed by username and password, and store blog posts associated with their account, also likes and comments posted on other user's posts are unique to each account to prevent duplicated comments or one user giving unlimited likes to one post.

* Users create accounts by filling in a simple registration form.

![Registration form](media/signup_mobile_view.png)

* Users sign in to their accounts by filling in a login form and sign out using a link in the navigation bar.

![Login form](media/login_mobile_view.png)

* The application uses Django pre written authentication to handle user signup and login functionality.

### Create new articles

The core feature of TrueFit is the ability to create unique posts for each user. Full CRUD (create, read, update, delete) functionality is implemented for blog posts. This means although a visiting user can only read the already posted articles, signed up users can add, delete and edit their own posts while also being able to comment and like other people's posts.

* New blog posts (articles) are added by completing a form, which is located on the main navbar but only for logged in users.

![Add new article by filling a form](media/create_article.png)

* All articles are listed on the home page and the category of each article is color coded.

![List of articles](media/article_list.png)


* When editing an article, the form is prepopulated with the current values of that article.

![Prepopulated article form](media/edit_article_prepopulated.png)

### Article management


* By design, users can only edit or delete their own  articles, as this prevents altering of other people's article posts. This allows the user to remain confident that their articles won't be tampered with.

![View of edit and delete for user's article](media/article_edit_delete_scre.png)





***

## Database Design

TrueFit uses a SQL database. Data is divided into three collections, with the following schema:

![Datbase diagram](media/database_schema.png)

***

## Future Features

The following features could be added in the future, given more development time:

### 1. Account Management Tools

* Helpful account management tools could be provided, such as the ability to update usernames, email addresses and passwords.
* A password recovery by email function could also be provided. Django authentication tools could be used for this.

### 2. Article Filters

* The ability for all users to filter the articles by category.


### 3. Search Articles

* The ability to search articles that contain a word or words in either the title or body 

### 4. Chat functionality

* The ability to chat with other users of the blog. Django channels could be used for this.

### 5. Code optimization and refactoring

* This was my first major project using Python and Django, so there are a few areas where I feel the code could be made neater and more efficient.
* In particular, replacing some function based views with class based view

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
3. [Balsamiq](https://balsamiq.com/) - Used to produce design wireframes.
4. [Bootstrap4](https://bootstrap.com/) - Bootstrap 4 CSS framework used extensively to create layout and styling of site.
5. [Python 3.8](https://www.python.org/) - Used to code the application.
6. [ElephantSQL](https://www.elephantsql.com/) - Used for the application's database.
7. [Django](https://www.djangoproject.com/) - Used to build the main application structure and page templates 
8. [Django storages](https://django-storages.readthedocs.io/en/latest/) - Used to connect web app with Amazon AWS S3 Bucket
9. [AWS](https://aws.com) Used to store static files
9. [Heroku](https://heroku.com/) - Used to deploy the site.
10. [W3C.org](https://www.w3.org/) - W3C [HTML Validator](https://validator.w3.org/nu/) and [CSS Validator](https://jigsaw.w3.org/css-validator/validator) used to check HTML and CSS code for errors.
11. [JSHint](https://jshint.com/) - Used to check JavaScript for errors.
12. [PEP8 Online](http://pep8online.com/) - Used to check Python code for errors.



***

## Testing

## Functionality testing 

 I used Chrome developer tools throughout the project for testing and solving problems with responsiveness and style issues.


## Compatibility testing
 Site was tested across multiple virtual mobile devices and browsers. I checked all supported devices in Chrome developer tools. 
 
 I tested on hardware devices such as: Ipad air with iOS, Iphone 13 mini with iOS 15.4, Macbook air with MacOS and Surface Pro with windows 10


## Unit Tests

I created unit tests for the login and signup page with django tests

![Unit tests](media/tests_screenshot.png)


---
# Issues found during site development

* ## Edit Article view creating additional article instead of editing existing one



When editing existing articles, once the "Update" button was clicked, the edit article view would create an aditional article onto the database instead of updating the existing one

> This was due to the action attribute on the form pointing to the "articles:create" url, as I had copy the form from the article_create html template and had forgotten to delete this, all I had to do to fix this error was to delete the action as shown on the picture bellow.


![testing-issue-1](media/article_edit_bug.png)


* ## Secret Key being exposed

When first creating my project I forgot to add the sqlite database to the .gitignore which cause django's secret key to be exposed when pushing to github

> Thankfully gitguardian let me know almost instantly that it had happened, so I generated a new secret key and made sure to add the sqlite database to the .gitignore before pushing to github.

![resolved4](media/secret_key_exposed.png)


* ## Hero image not loading from Amazon s3 bucket.


This one was a tough to spot as I was sure that I had followed step by step the tutorial on storing static files on my amazon bucket. When I uploaded my files to my amazon bucket, the deployed site was not displaying the hero image despite the css styling being applied, telling me that the error was exclusively with the image

> I have to give credit to the amazing CodeInstitute Slack comunity, which guided me in the right direction, it turns out that the url configuration is specific to the Region where the bucket is, and unlike the US region where the url just ends in ".s3.amazonaws.com" for the EU region the region has to also be added to the url, like the image shows below

![resolved](media/aws_region_bug.png)


## Performance testing

I run [Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool to check performance of the website.
Screenshots are presented below:


Final results:
![performance_final](media/light_house_truefit.png)

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
