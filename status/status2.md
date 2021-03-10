

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


Ian - Was able to create general panes per design document for each part of the stylometry software: Identification, Verification, and Profiling.


# Roadblocks Challenges

Andy - Encountered some API authorization issues that were resolved simply by regenerating my tokens and being able to input them properly.


Sam - Struggled to find time to get the comment gathering in full working order and did not end up getting it to fully functional.


William - Working with numpy to create a fast entropy discretization class that could be called by the pipeline function of sk-learn. 


Ian - Working to create functioning windows that incorporate the back-end functionality of the software. 


# Changes/Deviations from the Plan (if Applicable)

NA

# Description of Goals for Next 3 Weeks


Willliam - Begin working on and modifying the authorship authentication methods,classes and feature set to create the authorship identification classes. 


Sam - Filter out comments that do not meet the size requirements, format the corpuses when writing to the files.


Andy - Separating tweets into individual files that are sorted by account thus creating the corpus.

Making sure tweets are the set length, else figure out what's going on.


Ian - Working with William to link together back end software with front end functionality.

# Confidence on Completion from each Team Member 


Andy - 5


William - 5


Ian - 4


Sam - 4
