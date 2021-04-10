# DisTrackur
DisTrackur is a .py script made for information gathering off users on the Platform, Discord.  

# What does it do?
DisTrackur as of right now has one purpose, and that is logging. </br>
As this script is made for more specific targets, one instance of this script logs all messages from the specified user. </br>
Obviously, it will work in dm's, groups, and (mutual) servers.

DisTrackur will also relay the time each message has been sent, for more accurate visualation.
NOTE: "discord.py" is a required module to run this script. It will not run without it!

# Example
![Logo](https://github.com/9socket/DisTrackur/blob/main/example/DisTrackur_example.png)

# Features
1. Logging and keeping track of users messages. </br>
2. Fast and accurate tracking. </br>
3. Quick and easy to set up. </br>
4. Easy to edit and read. </br>
5. Does not inform the user about data logging.

# How to set it up?
DisTrackur is simple to set up. </br>
First git clone, or download the zip file and extract it onto your system. </br>
Next you will notice 3 .py (python) files. 'TARGETID', 'TOKEN', and the main file itself, 'DisTrackur'.

Now, you will need the discord token of the user your using to listen onto your target. </br>
(guide for retreiving your discord token is further down)

Next, you will open the 'TOKEN.py' file, and see an empty variable labled 'token'. </br>
This is where you will enter your discord token. Now your user will read/run commands.

After that, you will need the user id of your target. Simply right click their username and </br>
'Copy ID'. Now open 'TARGETID.py', and paste the id in the empty variable, 'targetid'. </br>
NOTE: Do not quote the ID in the targetid.

Now you have your account, and the targets account linked to the script. </br>
Simply just execute 'DisTrackur.py', and assuming everything went right, it'll start logging.

# Disclaimer
This script was not made for stalking or harrasement. It's made for OSINT and information gathering. </br>
(Yes, there is a difference)

Most important of all, this script falls into the catagory of a self bot. These are a violation of Discord's TOS, </br>
and they will terminate the account if a self bot is found being ran on the account. </br>
Use an account you don't care about and is willing the risk of termination. </br>
AS LONG, as you don't tell anyone or spread the word your user should be perfectly safe from termination. Be careful.

# Retrieving Discord token
As mentioned earlier, your Discord token is needed for this script to run correctly. </br>
Getting it is easy, and it starts off with logging onto discord in an online browser. </br>
After your logged on, right click of F12 to open Inspect Element. </br>
Towards/at the top, go into the 'Application' tab, then click on 'https://discord.com' in 'Local Storage'. (on the left) </br>
You should now see several columns of Keys, along with Values on the right of them. You should then notice a search bar on the top. </br>
Just enter 'token' in that search bar, and your token should pop up. Now you can simply copy and paste it.

NOTE: This guide was made for the Chrome browser. It has not been tested on any other!!!



