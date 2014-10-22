from cloudbot import hook
import re

matchString = re.compile('(\.yay)|(\.rage)')
@hook.regex(matchString)
def brycey(nick, match, notice):
		notice(nick +" I can spam annoying commands as well")
		notice(nick +" I can spam annoying commands as well")
		notice(nick +" I can spam annoying commands as well")
		notice(nick +" I can spam annoying commands as well")
		notice(nick +" I can spam annoying commands as well")