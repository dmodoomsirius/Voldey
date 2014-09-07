from cloudbot import hook
import time

@hook.irc_raw("JOIN")
def join(message, nick, mask, notice):
	if "Mibbit" in mask:
		time.sleep(2)
		message("Hello and welcome to #Cauldron IRC "+nick+". Please read http://cauldron.minecraftforge.net/threads/irc-guidelines.18/ BEFORE doing anything else")
		message("Cauldron has been DMCAed, don't ask about downloads|The future of servers is uncertain")
		notice(nick +" You really want to read that link, you might get kicked otherwise (there are instructions to preform)")