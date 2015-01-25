from cloudbot import hook

@hook.sieve()
def spongeSieve(bot, input, plugin):
	if "#sponge" in input.chan:
		return None
	else:
		return input