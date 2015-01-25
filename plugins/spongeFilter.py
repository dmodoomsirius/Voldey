from cloudbot import hook

@hook.sieve()
def spongeSieve(bot, input, plugin):
	#print(dir(plugin)) #This will show all attributes for an object
	if "#sponge" in input.chan:
		if plugin.function_name == "flard":
			return input
		else:
			return None
	else:
		return input