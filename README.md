The main purpose of this program to display the current status of a door monitor. (Closed or open) 

Please edit the settings.py to add the widget ID from your DM sensor. You can find the widget ID for any sensor by selecting it from the Samsara Dashboard. The widget ID is at the end of the URL when viewing a temperature sensor. 

For example:
https://cloud.samsara.com/o/ORGNAME/WIDGETID


The groupID and API token can be found in the settings page on your org in the API Tokens section. If you don’t already have an API token you’ll need to create one.



Features:

- Displays live data of door status (open or closed)


Quick Start on Mac:

1. Install libraries (Matplotlib, JSON, requests through pip or otherwise) 
2. Open terminal window. Type “python3 ” then drag the main.py file into the terminal window. Hit enter to start.

For example:
Michaels-MacBook-Pro-4:~ michaelbalzer$ python3 /Users/michaelbalzer/GraphTempProgram/main.py 

