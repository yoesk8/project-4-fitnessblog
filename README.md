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



## Design

The site uses the Bootstrap framework. I used a simple colour pallete that makes the article content pop out.

#### Colours and Shades

* The site uses a light shade of grey for the site’s header and footer, and a darker shade for the LogIn/SignUp buttons.

* The color of the background is white and text is black to reinforce the contrast and make it easier to read for the user.

* Colours are used consistently in association with a particular type of task:

* Dark grey is used on the login / signup buttons.

* Bootstrap's light blue (Primary) is used on the Read article button / and for the articles with the category "Training".

* Bootstrap's green (Success) is used for the articles with the category "Nutrition" and edit button.

* Bootstrap's red (danger) is used for the delete button.




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

The core feature of TrueFit is the ability to create unique posts for each user, even using HTML if the user wanted to for more flexibility on how his article is displayed. Full CRUD (create, read, update, delete) functionality is implemented for blog posts. This means although a visiting user can only read the already posted articles, signed up users can add, delete and edit their own posts while also being able to comment and like other people's posts.

* New blog posts (articles) are added by completing a form, which is located on the main navbar but only for logged in users.

![Add new article by filling a form](media/create_article.png)

* All articles are listed on the home page and the category of each article is color coded.

![List of articles](media/article_list.png)


* When editing an article, the form is prepopulated with the current values of that article.

![Prepopulated article form](media/edit_article_prepopulated.png)

### Article management


* By design, users can only edit or delete their own  articles, as this prevents altering of other people's article posts. This allows the user to remain confident that their articles won't be tampered with.

![View of edit and delete for user's article](media/article_edit_delete_scre.png)


### Donation Page

* In order to be able to support the owner of the website without having to resort to paid ads, I've added a donation page that allows logged in users to say thanks with a donation with the help of [Stripe](https://stripe.com/)'s API 

![Donation Page](media/donation_page.png)


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
12. [Pycodestyle](https://pypi.org/project/pycodestyle/) - Used to check Python code for errors.
13. [ChatGPT](https://chat.openai.com/chat) - Used to generate dummy articles and to explain and check code
14. [Stripe](https://stripe.com/) - Used to accept donations



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


* ##  Images not loading from Amazon s3 bucket.


This one was a tough one to spot as I was sure that I had followed step by step the tutorial on storing static files on my amazon bucket. When I uploaded my files to my amazon bucket, the deployed site was not displaying any images despite the css styling being applied, telling me that the error was exclusively with the images and not all staticfiles.

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

 ![CSS validator](media/css_validator.png)

 * [Nu Html Checker](https://validator.w3.org/) to test HTML

 ![HTML validator](media/html_validation.png)

 
 * [Pycodestyle](https://pypi.org/project/pycodestyle/) to test python files




***

## DEPLOYMENT
**Step 1:** Create a new app in Heroku, choose a unique name and region.
**Step 2:** Login to ElephantSQL, access the dashboard and create a new instance (input a name, select a region).
**Step 3:** Return to dashboard, copy the database URL:
![ElephantSQL](media/elephantsql_database.png)

**Step 4:** Create env.py file (ensure it is included in .gitignore file) and add environment the below variables. Paste the URL from above:

<img width="372" alt="image" src="https://user-images.githubusercontent.com/97494262/209531222-599282ee-2c54-490f-b543-1f09e5255490.png">

**Step 5:** Include a secret key in the variables:

<img width="800" alt="Screenshot 2022-12-26 at 11 25 13" src="https://user-images.githubusercontent.com/97494262/209531979-9ba177cc-3e44-48a7-80dc-884d06932f54.png">

**Step 6:** Include the below code to settings.py file:

<img width="301" alt="image" src="https://user-images.githubusercontent.com/97494262/209532128-acaa1e29-edea-45c3-93ce-2caaf0f71862.png">

**Step 7:** Link the database in settings.py and migrate then push to GitHub:

<img width="303" alt="image" src="https://user-images.githubusercontent.com/97494262/209532393-5283592f-5caf-4e81-b3fd-9d20bd62b111.png">

**Step 8:** In Heroku, add three config vars:

<img width="243" alt="image" src="https://user-images.githubusercontent.com/97494262/209532605-04bff00b-951f-4084-9ad5-6eff111ac6bf.png">

<img width="350" alt="image" src="https://user-images.githubusercontent.com/97494262/209532533-e9b3d879-a40a-4335-a56b-3c0e5c370a8a.png">

**Step 9:** Login to Cloudinary, copy the API Environmental variable to dashboard and add to env.py (see screenshot above) & to Heroku config vars:

<img width="571" alt="image" src="https://user-images.githubusercontent.com/97494262/209533286-4a79143c-6568-4055-99fc-76dd5821a02b.png">

**Step 10:** Add cloudinary to installed apps in settings.py, add static/media file settings:

<img width="407" alt="image" src="https://user-images.githubusercontent.com/97494262/209533445-8f6670c5-490b-4294-95cf-febaaaed2ab2.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/209533629-ab3fb31b-f096-4305-996e-970e4c950a3f.png">

**Step 11:** Add template directories in settings.py, add Heroku host name to allowed hosts and add directory files:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/97494262/209533879-b8284837-e7a1-4315-83e6-9b88d2125882.png">

<img width="501" alt="image" src="https://user-images.githubusercontent.com/97494262/209534100-46723f98-7bd6-40ed-91c1-5226ad6e950d.png">

<img width="313" alt="image" src="https://user-images.githubusercontent.com/97494262/209534271-772afed4-f299-45dc-b72d-d0843b7ad189.png">

**Step 12:** Create a Procfile, then commit and push to GitHub:

<img width="504" alt="image" src="https://user-images.githubusercontent.com/97494262/209534389-5b0cdd3c-54f7-44e8-8a21-99068431365a.png">

**Step 13:** Connect GitHub account in Heroku, connect and deploy branch. Open app and check:

<img width="421" alt="image" src="https://user-images.githubusercontent.com/97494262/209534580-c03fa4fd-8e52-487b-8ecc-23563fd30327.png">


## Other Credits and Acknowledgements

* [Code Institute](https://codeinstitute.net/) for their helpful lessons and reference materials.
* [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md) for the structure of this project's documentation and parts of the GitHub forking and cloning processes.
