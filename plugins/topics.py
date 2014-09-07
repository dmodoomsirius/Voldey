from cloudbot import hook

@hook.command
def nextstep(text, message):
	message("Hello "+text+". Please read http://bit.ly/1wcq2ic it contains everything about the Next Step")