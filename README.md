# Tutor Resource Bot

## Purpose
TRB's purpose to read messages with embedded links and attachments in non-announcement channels, and forward them to another server's specified channel. In our case this was to read #videos channels in the PCC discord server, and forward them to separate tutoring servers for students to use as resources while they studied. 

### Permissions needed to run:
1. Read messages
2. Send messages
3. Embed links


**When inviting the bot to your Discord server(s), you should make sure that the bot role has these permissions in both 'channel1id' and 'channel2id'**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Success: 8/09/2023:20:30
# set server and channel variables
server1 = 1138259376109539338  # original server
channel1 = 1138267923987845150  # original server channel id
# server2 = 1138259376109539338 # new server id
channel2 = 1138259415515021342  # new server channel
Changes --
First successful run. This was just between two channels of same server.

Success: 8/10/2023:12:03.
# set server and channel variables
server1 = 1138259376109539338  # original server
channel1 = 1138267923987845150  # original server channel id
# server2 = 1138259376109539338 # new server id
channel2 = 1138259415515021342  # new server channel
Changes --
added if-elses for embedded links in the messages.

Success: 8/10/2023:14:42.
# set server and channel variables
server1 = 1138259376109539338  # original server
channel1 = 1138267923987845150  # original server channel id
# server2 = 1138259376109539338 # new server id
channel2 = 1139373875956813854  # new server channel
Changes --
Changing channel2 and server numbers. Attempting to get bot to post across 2 servers

Success: 8/10/2023:19:11.
# set server and channel variables
server1 = 1138259376109539338  # original server
channel1 = 1138267923987845150  # original server channel id
channel2 = 1139373875956813854  # new server channel
Changes --
Learned that a second server id is not needed so long as specific permissions are given to the bot. Now able to re-post
from one server to the other.

Success: 8/10/2023:19:26.
# set server and channel variables
server1 = 1138259376109539338  # original server
channel1 = 1138267923987845150  # original server channel id
channel2 = 1139373875956813854  # new server channel
Changes --
Patched logic to only call bot when there was a new post in the specified channels instead
of on every on_message event.
