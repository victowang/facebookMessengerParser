# Parser for Facebook messenger

## Why ?
Explore your messenger data, you might find some fun or interesting insight about your friends who are in the same conversation.

#### Examples :  
* Who uses the most reactions
* Who receives the most reactions

## What can this parser do ?

#### Data :
* Find out how many message reactions each user has received
* Find out how many message readctions each user has sent

#### Scope :  
* A single HTML file
* All the html files in a directory

## How to get your data ?  
You can download your Facebook messenger data in your [personal information](https://www.facebook.com/settings?tab=your_facebook_information) as html files.  
Note : Be careful with the downloaded data as it may contain sensitive information concerning you or your contacts

## Get the number of reactions for each user in the conversation
#### Example :
from messengerParser import *  <br/>
path = "data/facebook-your_username/messages/inbox/conversation_name/"   # Path to the directory where your html files are  
result = getReceivedReactionsFromDir(path)  # Get dataframe with data about received reactions
print(result.to_string())                                                 # Print result in the console  
result.to_csv(r'receivedReactions.csv')                                 # Write results to csv 

## Display the data with Dash  

* Bar charts of sent and received reactions
* Radar charts representing each user

##### In project root run :
python dashApp/app.py  

##### with your browser go to :  
http://127.0.0.1:8050/

## Notes

It would probably be more efficient code the same process with data from facebook imported as JSON.
 