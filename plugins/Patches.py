from cloudbot import hook

@hook.command("patches")
def patches(message):
	message("http://cauldron.minecraftforge.net/threads/important-how-to-apply-bps-patches.487 Patches only exist for 1.7.10 so far not 1.6.4");
	message("Read that entirely if you have any questions ask")
	return
