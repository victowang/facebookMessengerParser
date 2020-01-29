# Parser for Facebook messenger

## Why ?
Explore your messenger data, you might find some fun or interesting insight.

## What can this parser do ?
* Find out how many message reactions each user of a conversation has

## How to get your data ?  
You can download your Facebook messenger data in your [personal information](https://www.facebook.com/settings?tab=your_facebook_information) as html files.  
Note : Be careful with the downloaded data as it may contain sensitive information concerning you or your contacts

## Get the number of reactions for each user in the conversation
### Example
from messengerParser import *  <br/>
path = "data/facebook-<username>/messages/inbox/<conversation_name>/"   # Path to the directory where your html files are  
result = getReceivedReactionsFromDir(path)  
print(result.to_string)                                                 # Print result in the console  
result.to_csv(r'receivedReactions.csv')                                 # write results to csv  