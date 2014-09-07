from cloudbot import hook

@hook.command("mibbit")
def mibbit(text, message):
	message("Hello " + text + " welcome to #Cauldron before you do anything please read http://cauldron.minecraftforge.net/threads/irc-guidelines.18/");
	return