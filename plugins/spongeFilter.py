from cloudbot import hook

@hook.sieve()
def spongeSieve(bot, input, plugin):
	#print(dir(plugin)) #This will show all attributes for an object
	if "#sponge" in input.chan:
		if "flard" in plugin.function_name || has_permission("ignore"):
			return input
		else:
			return None
	else:
		return input