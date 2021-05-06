# Stylo Notebook


## Synopsis

Using machine learning techniques Stylo aims to provide investigators with authorship verification, identification and profiling tools. Capable of automatically retrieving text data from sites such as twitter and reddit, an investigator will be able to compare two or more users against each other to determine if they are the same person, or provide information that may narrow down the search for an anonymous user’s identity by detailing possible author traits such as gender, age, place of origin first or second language speaker. 


## Status Updates

## Status Update 1

## The plan for the last 3 weeks 

* Ian: Downloaded Python QT designer and created rough layouts for the visual portion of the software.



* Sam: Created a reddit developer application to use in praw web scraping corpus generation and started to lay out the framework for implementation.



* Andy: Created a Twitter developer account that will give me the tokens to properly access the Twitter API. Started working on python and Tweepy integration in version 3.8. Attended zoom meetings For project discussion.

* William: Research methods for authorship profiling, and the use of an embedding space as classification method when dealing with large amounts of data. 







## Recap of what was planned for the last 3 weeks



So far we have written out a rough sketch of general design features such as: Graphical interface

 * Three modes of stylometry with tiles and general planning for qt creator.



 * Twitter and Reddit Corpus Gathering



 * Andy was able to get the Tweepy package installed and imported into a python project



 * Research for how to create a classification algorithm that doesn’t need to be completely re-trained at the



 * introduction of a new user



## What was done during the last 3 weeks (by whom):

Ian: Downloaded Python QT designer and created rough layouts for the visual portion of the software.



Sam: Created a reddit developer application to use in praw web scraping corpus generation and started to lay out the framework for implementation. 



Andy: Created a Twitter developer account that will give me the tokens to properly access the Twitter API. Started working on python and Tweepy integration in version 3.8. Attended zoom meetings

For project discussion. 



William: Research methods for authorship profiling, and the use of an embedding space for extreme classification methods.





## Description of tasks completed



* Ian: I spent 3 hours working on rough layout along with an additional 4 attending meetings on zoom/discord.



* Sam: Spent 4 hours reading PRAW documentation, setting up developer account, and implementing

Authorization code to access reddit instances. Also attended meetings via zoom and discord.



* Andy: I spent 3 hours figuring out how to get Tweepy to be found through the interpreter to be able to get imported. Attended 4 meetings held across Zoom and Discord.



* William: I spent 4 hours reading papers about about recommendation algorithms in search of a method to create a classification method that won’t involve completely retraining the machine learning algorithm every time a new class is added.



## Status Update 2

# The Plan for the Last 3 Weeks



Andy - Was to fix any bugs with Twitter authentication codes. Read into OAUTH protocols and how it actually works with twitter. Created a small demo that can print out tweets from a specific users timeline. The basic program contains a list of names that is iterated through to get x amount of tweets for each user name in the list.





Sam- Fix any bugs in the Reddit comment gathering code. Get the comments to write to a corpus and format appropriately and filter out any comments that did not match the correct size.





William - Create and explore model for authorship authentication system. Completed with sk-learn and a support vector machine model. 





Ian - Create layouts for software gui windows using PyQt designer.





# What was Done During Last 3 Weeks



Andy - Created a small demo that can print out tweets from a specific users timeline. The basic program contains a list of names that is iterated through to get x amount of tweets for each user name in the list. Read more into OAUTH protocols to better understand how they work with the twitter API. Turns out though, all you actually need are the keys and the rest is if the application is a web app.





Sam: Created the base functions to instantiate reddit, get comments based on username, and write them to a file. Fix some bugs inside of those functions.





Ian - Used pyqt designer to create general layouts for software windows.





Willliam - Created and explored the model for authorship authentication system completed with sk-learn and a support vector machine model. 





# Successes



Andy - Got around any set-up bugs with Tweepy that were present. Then created a demo with Tweepy that also allowed for me to practice fundamentals.





Sam - Managed to get the base functions of the comment gathering program working for the most part.





William - Developed a reasonable and working model with many features from the texts and was able to achieve a decent EER of 20%.



## Status Update 3


## The Plan for the Last 3 Weeks



* Ian - Write functions for the GUI that interface with the backend scraping and twitter scrapers.* 



* William - Build model for authorship authentication and supporting classes and methods





* Sam - Write reddit scraping functions for user profiling





* Andy- Attempted a different method other than streamlistener to ge access to the twitter Public Sample. Ended up not working, next going to try using the streamlistener class to get the correct data.





## What was Done During Last 3 Weeks



* Ian - Wrote basic dummy methods that will be used with the backend python files.



* William - Finished Authorship authentication model, trained all necessary classes and found best class weights i.e. where FAR and FRR intersect.





* Sam - Wrote functions for reddit scraping data collection which appends and formats data correctly to the files in the format needed for the corpus. Ended not needing these bits of code however as a different method was used that did not need a reddit account to function.





* Andy- Trial and error with a different method of pulling Twitter tweets in a mass quantity. Figured out that it won’t work and now going to try the streamlistener class. 



 



## Successes



* Ian - Finished the basic gui mock-up excluding the functionality.





* Andy- No success, just trial and error





* William - Completed authorship authentication model, and the supporting classes for feature extraction, preprocessing and feature selection. Performed testing to find optimal class weight.



* Sam- No successes, but gained a good understanding of reading and writing to files and the scraping workflow.





## Roadblocks Challenges



* Ian- Waiting on team to finish their side so functions can be used as part of the GUI



# The Plan for the Last 3 Weeks



Ian - Write functions for the GUI that link the verification/id/profiling models to the frontend display.





William - Build model for authorship identification and supporting classes and methods





Sam - Update the reddit scraper to handle errors and update model functions to work with the new scrapper.





Andy- Complete the twitter scraper and add error checking functionality.





# What was Done During Last 3 Weeks



Ian - Wrote methods that can activate the models and display basic results to the user.





William - Finished Authorship identification model. Began finding the best hyper-parameters to for authorship identification





Sam - Added error checking to the reddit scrapper which makes the function exit smoothly on an error, and returns appropriate values based on the error.





Andy- Completed the Twitter scraper so it can pull individual users or a list of users through a for loop. Added basic error checking to prevent the program from crashing on error.



 



# Successes



Ian - Finished the basic gui mock-up excluding the functionality.





Andy- Was able to complete the  Twitter Scraper and its functionality 





William - Completed the authorship identification model. Began integrating the identification and authentication models with the frontend.



Sam- Completed error handling and updating the verification function to use the new function.





# Roadblocks Challenges

None



## Videos

Status #1: https://www.youtube.com/watch?v=wO9pK9ZcS_k

Status #2:  https://www.youtube.com/watch?v=HEP5GPddDvI

Status #3: https://www.youtube.com/watch?v=sdiI3Oz0_UU



## Project Planning Documents


### Project Management Plan


#### **Project Management Approach**

Team members will meet at least once weekly to discuss progress they’ve made on various fronts and to discuss issues and concerns they have. Important decisions will be made democratically after thorough discussion.


#### **Project Scope**
The scope of Stylo includes planning, design, development and testing. This software will meet or exceed software standards. All project work will be completed using Python and its various packages. No changes will be required to the operating system and the project should be able to run on both Unix, Linux and Windows based machines.

 


#### **Milestone List**
The below chart lists the major milestones for the Stylo Project.  This chart is comprised only of major project milestones such as completion of a project phase or gate review.  There may be smaller milestones which are not included on this chart but are included in the project schedule and WBS.  If there are any scheduling delays which may impact a milestone or delivery date, the project manager must be notified immediately so proactive measures may be taken to mitigate slips in dates.  Any approved changes to these milestones or dates will be communicated to the project team by the project manager. 



#### **Schedule Baseline and Work Breakdown Structure**
Team members will be required to put in at least 4 hours of work per week but no more than 168 hours of work per week as exceeding the latter will require some sort of time dilation device for which we do not have the budget. At the beginning of the week team members will discuss what it is they would like to complete this week and discuss the progress they made the prior week. 


#### **Change Management Plan**
The following steps comprise Stylo’s change control and bug reporting process:

First  they will identify the need for a change or discover a bug in the current system

Then they will submit a bug report to the issues page on the project’s github filling out the provided template. 

The change or bug report will be brought up at the next meeting and depending on its importance will be considered for immediate implementation or fix


#### **Communications Management Plan**This plan identifies the roles of the team members as they pertain to communications. It also includes a communication matrix which maps the communication requirements to this project.



This Communications Management Plan sets the communications framework for this project.  It will serve as a guide for communications throughout the life of the project and will be updated as communication requirements change.  This plan identifies and defines the roles of Stylo project team members as they pertain to communications.  It also includes a communications matrix which maps the communication requirements of this project, and communication conduct for meetings and other forms of communication.  A project team directory is also included to provide contact information for all stakeholders directly involved in the project.



Communications Conduct:


Meetings:


The Project Manager will distribute a meeting agenda at least 2 days prior to any scheduled meeting and all participants are expected to review the agenda prior to the meeting.  During all project meetings the timekeeper will ensure that the group adheres to the times stated in the agenda and the recorder will take all notes for distribution to the team upon completion of the meeting.  It is imperative that all participants arrive at each meeting on time and all cell phones and blackberries should be turned off or set to vibrate mode to minimize distractions.  Meeting minutes will be distributed no later than 24 hours after each meeting is completed.


Email:


All email pertaining to the Stylo Project should be professional, free of errors, and provide brief communication.  Email should be distributed to the correct project participants in accordance with the communication matrix above based on its content.  All attachments should be in one of the organization’s standard software suite programs and adhere to established company formats.  If the email is to bring an issue forward then it should discuss what the issue is, provide a brief background on the issue, and provide a recommendation to correct the issue.  The Project Manager should be included on any email pertaining to the Stylo Project.  


Informal Communications:


While informal communication is a part of every project and is necessary for successful project completion, any issues, concerns, or updates that arise from informal discussion between team members must be communicated to the Project Manager so the appropriate action may be taken.



#### **Quality Management Plan**Each team member will be responsible for testing their portion of the code to make sure it works completing tests before merging into the main branch. Unit testing should be performed. 



All members of the Stylo project team will play a role in quality management.  It is imperative that the team ensures that work is completed at an adequate level of quality from individual work packages to the final project deliverable.  The following are the quality roles and responsibilities for the Stylo Project:


Quality assurance for the Stylo Project will ensure that all processes used in the completion of the project meet acceptable quality standards.  These process standards are in place to maximize project efficiency and minimize waste.  For each process used throughout the project, the Project Manager will track and measure quality against the approved standards with the assistance of the Quality Specialists and ensure all quality standards are met. If any changes are proposed and approved by the Project Sponsor and CCB, the Project Manager is responsible for communicating the changes to the project team and updating all project plans and documentation.


#### **Quality Baseline**
The Stylo Project must meet the quality standards established in the quality baseline.  The quality baseline is the baseline which provides the acceptable quality levels of the Stylo Project.  The software must meet or exceed the quality baseline values in order to achieve 




#### **GUI**

When the application opens the user will be presented with 3 different options representing the types of tests they can perform: Authorship identification, verification and profiling. Depending on the option chosen you will go to one of the following menus below.


#### **Authorship Identification**


The authorship identification menu includes a list of users to test against on the left hand side, and on the right side of that list is the user which we are attempting to match against. The “+” button adds an additional user to the left hand side. The number of users on the left side should be at least 3. The test passes the data to a start function which organizes it into different function calls, beginning to download and pre-process the data as it comes in. Once all data has been downloaded it the machine learning algorithm will test train itself with c-value (if provided otherwise default) and to test the data. 


**Test button**:

The GUI should be able to call the function: 

startIdent(user: string, userList: list, topMatches: int = 3, cVal: float = tbd, source: int = 1)

Where userList is a string of users to test against and user is the primary user.

#### **Authorship Verification**



The authorship verification menu takes two users shown on the left hand side of the GUI and then determines how well they match together. The test button does the same as above.


**Test button**

The test button should be able to call the function:

startVerif(userOne: string, userTwo: string, cVal: float = tbd, source: int = 1)

Where source is either a 1 or a 2 representing Reddit, or Twitter respectively with the default being 1 or Reddit.


**Authorship Profiling**

The authorship profiling menu only takes one user. The test button does the same as above.

**Test Button**

The test button should be able to call the function:

startProf(user: string, source: int = 1)

Where source is an integer from 1, 2 and represents whether the text data should come from Reddit or Twitter respectively.

**Results menu**

The results menu displays the results returned once testing is completed. The results returned will be formatted as a string to be displayed in the text box in this menu. At the bottom of the menu is a button that will return the user to the opening GUI, saving the results before closing. 

**Automatic user scraping**

Scraping system. The function to call in order to scrape data will be:

**autoCollect(userList: List, source: int = 1) -> List**

userList: The list of users to download text data/include data for.
Source: either 1 or 2 referring to Reddit or Twitter, respectively.    

Error handling:
```
    In the case where it was not able to find a specific user:
        Pop-up box issuing warning with message: “Not able to find user <user>”
    In the case where it was not able to find enough text data for the specific user:
        Pop-up box issuing warning with message: “Not able to gather enough data for user: <user>”
        Users successfully downloaded will be added to the json file: corpora/users.json
Two categories inside json: Reddit and Twitter saving users to their respective category depending on the source value.  
If a user is already present inside of users.json then it will not download data for them
Returns a list of users it was successfully able to collect data for.
```


**scrapeReddit(user: string) -> int**


This function will scrape reddit for the user’s text data saving comments that are more than 350 characters long. Comments that are greater than 350 characters long will be cut-off after 350 characters. Save the file to corpora/reddit_corpus/<username>.txt

User: the user to scrape

Returns -1 if it can’t find the user

Returns -2 if it there is not enough data available

Returns  0 if successful

**scrapeTwitter(user: string) -> int**


This function will scrape Twitter for user’s text data saving tweets until the character count of 50 * 240 is reached. Save the file to corpora/twitter_corpus/<username>.txt
 
User: The user to scrape

Returns -1 if it can’t find the user

Returns -2 if it there is not enough data available

Returns  0 if successful

**Profile generation**


These functions will create the profile for the new user


**profCreate(source: int = 1, user: string)***


This will create the profile for the specific user saving it to a csv file. Depending on the source it will either save it into: corpora/reddit_csv/<username>.csv or corpora/reddit_csv/<username>.csv

     

Source: either 1 or 2 referring to Reddit or Twitter respectively

User: the user name from which to draw text data and to name the saved the csv file

**modelTrain(userList: List, source: int = 1, t: int = 1)**

This takes all the csv files created by profCreate and then trains and then tests the model. Returning as a string the results. 

userList: the list of users to include in the training and testing.

Source: whether to draw from reddit corpus or Twitter corpus for negatively labelled text 

Data

T: the type of data. The type of model to train where 1 = authorship identification, 2= 

authorship verification, and 3 = authorship profiling. 

