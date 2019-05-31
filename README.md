# Project 3

## Spellfinder General

Spellfinder General is companion app for both Adventurers and Dungeon Masters within the realms of Dungeons and Dragons 5e edition. This is my end of module project for Data Centric Development for Code Institutes Online full stack course. This project has become a labour of love, and finding where to stop adding features to get the project handed in has been a learning curve for myself, however I intend to fork the workspace in order to futher develop the extre features as described within the readme. 

Note:  Adventurers and Dungeon Masters will be collectively referred to as “players” from here on out, with DM being shorthand for Dungeon Master and DND referring to Dungeons and Dragons 5e edition

## UX
The app has been designed to allow users to view, edit, and add spells to a database. There is a simple to use navbar, which guides to all major routes within the app, as well as back buttons for where a step back would be more appropriate. The spells themselves have many defining features which can be targeted via catgeory using button press's at the top of the view all spells screen. This app also allows players to sign in to compliment their playing experience.

### User Stories
User 1 - Player - Adventurer 
* To look up for spells for their character 
* Searches driven by spell classes and level
* Easy to use to augment real world gameplay

User 2 - Player - Dungeon Master 
* Quickly find spell information for NPCs
* A tool to help adventurers build their characters

User 3 - Causal User/Potential player
* Easy to read info source on a key element of DnD game play
* Potentially including more eye catching media.

### Wireframes
[Index](static/wireframes/index_wf.png)
[Spells](static/wireframes/spells_wf.png)
[Login/Register](static/wireframes/login_wf.png)
[Add/Edit Spell](static/wireframes/form_wf.png)


For handling the data, I chose MongoDB as the database, due to its non relational format fitting the needs of the nature of DND (Escapism can’t be defined!) This allows certain spells with more conditions to be handled in a quicker manor. Using dbdiagram.io to create a mockup of the schema I chose to drill down the fixed outlines (Die Value, Spell level) into their own collections to allow each unique spell to pick values from said collections.


[Wireframe](static/schema/schema.png)


## Features
### Existing Features

Spellfinder
* Allow users to add, edit and delete spells, be them homebrew or offical spells
* When editing spells, spellfinder goes into mongodb and displays their current values

Key Searches 
* As this is a currently a smaller app I decided to go for key search terms to display in order rather than text indexing
* Basic search functions up and running, see next section for future details

Register/Login
* Users can register and login - Once logged in their username is displayed 
* Only logged in users can delete spells
* Login error messages redirected to approite paths 

Navbar 
* Easy to use navbar on both full screen and collapseable on smaller screens
* Displays if user is logged in
* Logout function only displays if user is logged in

### Features left to implement 

### Extra User Features

Using Spells
* Allow players to interact with a rng generator to use the spells while playing

Spell Slots
* Players have a certain amount of spell slots, which act as MP (Magic points)
* A new feature would be to include this within Spellfinder General

Spell List
* Allow users players to view, add, edit and delete spells from their own player spell lists

Password 
* User logins will require passwords in the future

### Extra app features

In Depth Searching
* Drill down deeper into search terms and sorting/limiting the results back

Extra Spell infomation 
* Description of spells to be added and displayed in a larger clickable card format
* Small Truncation on description existing spell cards to invite the user to click ahead

## Testing 

- HTML5/CSS3
  - The project uses HTML5/CSS3 To build and style.
- [Flask](http://flask.pocoo.org/)
  - The project uses flask and its addons for templating and logic
- [MongoDB](https://www.mongodb.com/)
  - Used MongoDB for the database which holds the user and recipe information
- [Materialize v1](https://materializecss.com/)
  - The project uses Materialize for styling, helpers and the grid system
- [Material Icons](https://material.io/tools/icons/?style=baseline)
  - Material Icons used for the various icons used throughout the site
- [Google fonts](https://fonts.google.com/)
  - The project uses Google fonts for fonts
- [JQuery](https://jquery.com)
  - The project uses **JQuery** to simplify DOM manipulation.
- [PyMongo](https://api.mongodb.com/python/current/)
  - The project uses PyMongo as the link between my project and MongoDB
- [Flask_PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
  - Flask-PyMongo bridges Flask and PyMongo and provides some convenience helpers.