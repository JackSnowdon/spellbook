#Project 3

##Spellfinder General

Spellfinder General is companion app for both Adventurers and Dungeon Masters within the realms of Dungeons and Dragons 5e edition. This is my end of module project for Data Centric Development for Code Institutes Online full stack course.

Note:  Adventurers and Dungeon Masters will be collectively referred to as “players” from here on out, with DM being shorthand for Dungeon Master and DND referring to Dungeons and Dragons 5e edition

##UX
The app has been designed to allow users to view, edit, and add spells to a database. The spells themselves have many defining features which can be targeted via a search function. This app also allows players to sign in and create their own character sheets to compliment their playing experience 

###User Stories
User 1 - Player - Adventurer 
*To look up for spells for their character 
*Searches driven by spell class and level
*Easy to use to augment real world gameplay
User 2 - Player - Dungeon Master 
*Quickly find spell information for NPCs
*A tool to help adventurers build their characters
User 3 - Causal User/Potential player
*Easy to read info source on a key element of DnD game play
*Potentially including more eye catching media.

Links to wireframes/schema
For handling the data, I chose MongoDB as the database, due to its non relational format fitting the needs of the nature of DND (Escapism can’t be defined!) This allows certain spells with more conditions to be handled in a quicker manor. Using dbdiagram.io to create a mockup of the schema I chose to drill down the fixed outlines (Die Value, Spell level) into their own collections to allow each unique spell to pick values from said collections.

##Features
###Existing Features

Spellfinder
*Allow users to search for spells filtering and ordering using key queries
Spell List
*Allow players to view, add, edit and delete spells from their own player spell lists
Register/Login
*Log in to view personalised character  spell lists
*While logged into characters can add their own homebrew spells

###Features left to implement 
Using Spells
*Allow players to interact with a rng generator to use the spells while playing
Spell slots
*Players have a certain amount of spell slots, which act as MP (Magic points)
*A new feature would be to include this within Spellfinder General
