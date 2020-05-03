# [CIRCDATA](https://circeco-contribuite.herokuapp.com/)

mockup image 

User story
Do you wanna contribuite to a sustaianble future? Circeco is the platform for circular economy where to find shops that sell and accept recycled and reuse stuff or also where you can repair your own stuff! You can search for second hand shops for music, books, clothes, electronics and home stuff with the scope of give good hints on what good sustainable initiatives are available out there! You can also add unlimited circular initiatives to share with the community and contribuiting to build a circular ecosystem! 

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
2. [**Features**](#features)
    - [**Existing**](#existing)
    - [**Left to Implemtent**](#left-to-implement)
3. [**Technologies Used**](#technologies-used)
    - [**Front End Technologies**](#front-end-technologies)
    - [**Back End Technologies**](#back-end-technologies)
4. [**Database Schema**](#Database-schema)
5. [**Testing**](#testing)
6. [**Deployment**](#deployment)
7. [**Credits**](#credits)
#

## 1. UX 
This project is a **Data Centric Development Project** as part of my study in Full Stack Software Development at [Code Institute](https://codeinstitute.net/). The goal of this milestone project is to create "a web application that allows users to store and manipulate data records, with functionality that allow users to create, locate, display, edit and delete records (CRUD functionality)". 
I have great interest in sustaianblity, so I wanted to create a platform to group alternatives to a different type of consumption that look beyond the common take-make-dispose model. I personally often look for places and initiatives that allow me to resue, recycle or repair stuff, and often I exchange these info with other people into sustainabiltiy or people who came to me for advice. The platform can be a source for alternative consumption providing an assortment of initiatives to choose from that embrace the circular revolution as their core business value. 

### User Stories 
Below here there would be list of implemented features and functionalities available to the user. 
As a user I would like to: 
* View the site from my mobile, tablet or desktop
* Search specific circular initiatives 
* View all Circular initiatives
* Edit info about a circular initiative 
* Delete a circular initiative 
* Add a new circular initiative 
* Click on the link of each circular initiative for more info on their own webpage 

### Design
The design goal was to create a sleek and clear user interface, with focus on important reoccuring sustaianbility key words and an eyes-catching use of colors. 

#### External Dependency 
Several elements in the design rely on external dependency that are below listed: 
* [Materialize 1.0.2](https://materializecss.com/) I enjoyed using Materialize modern and professional-looking layout as a framework and the documentation was simple and clear for implementation with the ready-to-use codes
* [Google Font](https://fonts.google.com/) the font-family used have lettersforms that are dynamic, designed for a modular system with a good balancing and that avoide repetitiviness. Their styles are suatable for headlines, short paragraphs or single word, which is what this site is mostly made of 
  - [Khand](https://fonts.google.com/specimen/Khand?query=khand) 
  - [Bebas Neue](https://fonts.google.com/?query=Bebas+Neue)
* [Font Awesome 5.8.1](https://fontawesome.com/) Social Icon in the footer cannot be found in Materialize so Font Awesome can provide icons for more specific needs 

#### Color 
The use of colors is kept at a minimum that apart from the use of black and white, with also the employment of a type of red to highlight and catch attention and a type of green/blue in a different shade to represent different levels of circularity. This is also a reminder of the logo and of the sustainability theme often associated with green. The red color is also a reminder of the state of environmental emergency and the action to take. The colors employed and the font together create a specific custom theme recognizable among another website. 

#### other Frameworks
* [Flask 1.0.2](http://flask.pocoo.org/)
This microframework is used to render the back-end Python with the Front-End Materialize.

* [jQuery 3.2.1](https://code.jquery.com/jquery/)
This framework is very useful to keep the JS coding at minimum so can be used as fundation of my scripts. 

#### Wireframes
I have not used any program to make my wireframe but I have rather made a hand sketch [here](https://github.com/circeco/circdata/blob/master/static/img/circdata-sketch.jpg).


##### back to [top](#table-of-contents)

---
## 2. Features
Some extra featuers were added in this app as not part of requirements because made the project more useful for better user interaction. 

### Existing
**Search for Circular Initiatives**
The user can immediately search for Circular Initiative on the home page and can search for any type of word whether is the name of the initiative, something in the description, the type of initiative (Reuse, Reccyle, Repair) or a type of object sold, to donate or to repair (books, music, clothes, bikes or home stuff). 

**CRUD View All Circular Initiatives**
All initiatives can be diplayed all together on any devices mobile to computer mantaining clarity and easy access. 

**Sort Circular Initiatives**
When the user is viewing Circular Initiatives in the view page can sort cards of circular initiatives whether is looking only for clothes or for music or for home stuff and so on. 

**CRUD Create a Circular Initiative**
A new initiative can be added with a form that uses defensive programming so the user must adhere to minimal requirements when trying to add a new initiative. 

**CRUD Update a Recipe**
Initiatives can also be edited and updated by anyone

**CRUD Delete a Recipe**
The user can also delete and remove any circular initiative 

### Left to Implement
In the future, I would like to create to possibility for the user to create their own account and so being able save inititatives nad check them up later for examle, but also a user account would allow a more orderly track of changes made by users. Also would love to create a newsletter to update users to news and changes. Finally, would be very usefull to have an admin profile able to edit or delete any circular initiative and delete any user account also, but also to keep track of visitors and statistics of the site. 

##### back to [top](#table-of-contents)

---
## 3. Technology Used
[GitHub](https://github.com/) is been used as a storage of my code and as my primary IDE for coding. 

### Front End Technologies
* [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) 
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) 
* [jQuery 3.2.1](https://code.jquery.com/jquery/) 
* [Materialize 1.0.2](https://materializecss.com/) 

### Back End Technologies

**Flask**
    [Flask 1.0.2](http://flask.pocoo.org/) as a microframework.
    [Jinja 2.10](http://jinja.pocoo.org/docs/2.10/) to template with Flask.
    [Werkzeug 0.16](https://werkzeug.palletsprojects.com/en/0.16.x/) 
**Heroku**
    [Heroku](https://www.heroku.com) to host the app
**Python**    
    [Python 3.6.7](https://www.python.org/) for the back-end programming
    [MongoDB Atlas](https://www.mongodb.com/) to store my database
    [PyMongo 3.8.0](https://api.mongodb.com/python/current/) as Python API for MongoDB.

##### back to [top](#table-of-contents)

---
## 4. Database schema 
[MongoDB](https://www.mongodb.com/) is the main database used for this app. 
This is a non-relational DB, which worked well for the app because each document can store enough information for each circular initiative. Three collections were created within the app's database: 
- **Circular_Initiative** which contains information of the circular initiatives added by users 
- **Categories** which contains a prexisting selections of initiatives type such as Reuse, Recycle and Repair initiatives so they can be prefixed options for the user when adding or editing an initiative 
- **Goods_Services** is another prefixed selections of options that the user can choose among when create or edit an initiative but it also serves as the base for the sorting functionality which gives the user quick access to a selection of related goods or services


## 5. Testing 
I have manually tested all functuonalities both during the process of building the app and after completion. 
- :white_check_mark: Responsive webdesign for different devices and screen size
- :white_check_mark: Crossbrowser testing
- :white_check_mark: Add functionality, the possibility for the user to add a circular initiative 
- :white_check_mark: Edit functionality, the possibility for the user to update a circular initiative 
- :white_check_mark: Delete functionality, the possibility for the user to delete a circular initiative
- :white_check_mark: Search functionality, the possibility for the user to search among all information stored for the circular initiative (except weblink as would be not relevant)
- :white_check_mark: View circular initiative all together
- :white_check_mark: Sort circular initiative based on key goods and services 

### Code Validators 
**HTML** 
- [W3C HTML Validator](https://validator.w3.org) Document checking completed. No errors or warnings to show.

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Two errors and several warnings related to the Materialize framework used 

**JAVASCRIPT**
- [JavaScript](https://codebeautify.org/jsvalidate) - The web app does not contain any custon made JS codes but only few from the Materialize framework

##### back to [top](#table-of-contents)

---
## 6. Deployment 

### Local Deployment
Please note - in order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- Any IDE such as [Microsoft Visual Studio Code](https://code.visualstudio.com).
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [MongoDB](https://www.mongodb.com) to develop your own database either locally or remotely on MongoDB Atlas.

Next, there are several steps to take:
1- Clone the repository and download the project as a zip-file `git clone https://github.com/TravelTimN/ci-milestone04-dcd.git`
2- Navigate ot the file location after unzip the file `cd <path to folder>`
3- Create an `.env` file with your credentials including also your *MONGO_URI* and *SECRET_KEY* values 
4- Create a `.flaskenv` file and add the following entries: `FLASK_APP=run.py` , `FLASK_ENV=development`
5- Install all requirements from the requirements.txt file `sudo -H pip3 -r requirements.txt`
6- Create or login to an account in [MongoDB](https://www.mongodb.com) and create a new database called **CIRCDATA** with collections as follow: 

**Circular_Initiative**
```
_id: <ObjectId>
initiative_name: <string>
initiative_type: <string>
initiative_description: <string>
initiative_object: <array>
weblink: <string>
```

**Categories**
```
_id: <ObjectId>
initiative_type: <string>
```

**Goods_Services**
```
_id: <ObjectId>
initiative_object: <array>
```

7- Now the app can be launched using the command `flask run`
8- The app would be running on the local host!

### Remote Deployment
[Heroku](https://www.heroku.com/) is the platform where this app is deployed using the **master** branch of GitHub. In order to achieve this I have made the following steps: 
1- Create a requirements.txt file that allows Heroku to install the requirements dependencies needed to run the app `sudo pip3 freeze --local > requirements.txt`
2- Create a **Procfile** that comunicate to Heroku the type of application being deployed and so understand how to run it `echo web: python run.py > Procfile`
3- Log in or sign up for an Heroku account and create a project app, then click on the deploy tab and use the connect GitHub as deployment method and choose Automatic Deployment
4- In the setting tab, click on Reveal Config Vars and configure environmental variables as follows:

    - **IP** : `0.0.0.0`
    - **PORT** : `8080`
    - **MONGO_URI** : `<link to your Mongo DB>`
    - **SECRET_KEY** : `<your own secret key>`
    - **MY_ADDRESS** : `<your own email address>`
    - **SEND_TO** : `<recipient email address>`
    - **PASSWORD** : `<you own email password>`

5- Now the app should be successfully deployed through Heroku

### Pushing To The Respository:
- To add, commit and push files to the repository, e.g. index.html, open a New Terminal and type:
1. git add index.html
2. git commit -m "Leave a message here"
3. git push origin master - (which is for the master branch).

##### back to [top](#table-of-contents)

---
## 7. Credits
## Credits
The picture used on the website is from Pixabay and free to be used for commercial purpose, other styles and logos are custom made or in-line referenced. 
Circeco.org holds the copyright for the business idea, content and codes in this repository. 

### Authors and Acknowledgment:
- **Autor**: Author **Piero Grilli** can be contacted at grilli.piero@circeco.org
- **Acknowledgment**: Code Institute Slack, Code Institute Tutor Support, Assigned Mentor: Medale Oluwafemi

##### back to [top](#table-of-contents)





