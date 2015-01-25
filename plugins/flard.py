from cloudbot import hook
import time
import re

lines = ['Congratulations for choosing FLARD! You may now experience the incredible joy of FLARD, the','Revolutionary new Wonder Product derived from incredible hard labour!'
,'The FLARD is not only eco-friendly Foodstuff and/or Beverage, building material, and surfactant.','Many, many more applications are possible due to unique biochemical and structural properties.',
'Experimental applications include as a Language, Levitation, and Virtual Brain Enhancement.','Caution is to be engaged in unauthorised compression of FLARD for your non-exploding safety.',
'FLARD is Sterilised by Irradiation for your safety and enjoyment. This also permits FLARD to be','deployed as emergency illumination, and proves its utility as an effective Reactor Shielding.',
'Military uses of FLARD are not sanctioned by Yggdrasyl Laboratories, although we are willing to','enter into negotiations with sufficiently authorised and funded friendly megalomaniacs.']
matchString = re.compile('^(\.eta)')
@hook.regex(matchString)
def flard(message, nick, mask, notice, chan):
	if "#sponge" in chan:
		for i in range(len(lines)):
			notice(lines[i])