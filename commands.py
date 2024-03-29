import requests
import json
import config
import dateutil.parser
import datetime
from utility import utils
from random import randint

def cmds_resp():
    return "Avaliable Commands: !cmds !uptime !title !setup !editor !emacs !atick !insult"


def leakinfo_resp():
    return

def uptime_resp():
    headers = {'Client-ID': config.client_id}
    r = requests.get(f'{config.helix_base}/streams?user_id={config.user_id}',
            headers=headers).json()['data'][0]
    today = datetime.datetime.now()
    s_time = dateutil.parser.parse(r['started_at'])
    tzone_adjust = 6
    live_hour = (today.hour+tzone_adjust - s_time.hour)
    live_min = (today.minute - s_time.minute)

    return f"{r['user_name']} has been live for {live_hour} hours and {live_min} minutes"

def title_resp():
    headers = {'Client-ID': config.client_id}
    r = requests.get(f'{config.helix_base}/streams?user_id={config.user_id}',
            headers=headers).json()['data'][0]

    return "Current Title: {}".format(r['title'])

def setup_resp():
    comp = 'Intel i7 w/ GTX 980 Ti'
    os = 'Ubuntu 16.04 w/ i3-Gaps'
    mbp = '15" MacBook Pro w/ i7'
    per = 'Gigabyte Keyboard w/ MX-Blues and a Logitech Mouse'
    return f'Comps: {comp} running {os} and a {mbp} ---- Peripherals: {per}'

def editor_resp():
    return 'VIM ----- THERE IS NO OTHER EDITOR ----- https://www.vim.org/'

def emacs_resp():
    return '%s/emacs/vim/g'

def atick_resp():
    reaction = utils.get_reaction()
    subject = utils.get_subject()
    insult = utils.get_insult()
    tick = str(randint(1, 1000))
    response = [
        reaction + " " + tick + " ticks have passed, DUH",
        reaction + " " + tick + " ticks have passed " + insult,
        insult + " " + reaction + " DUH " + tick + "s have GONE BY DUDE",
    ]

    return response[randint(0, len(response)-1)]

def insult_resp(name):
    if name == "":
        name = '@wowotek'
    elif name == "@blizz191":
        return holy_resp("@blizz191")
    else:
        name = name
    r = requests.get(f'https://insult.mattbas.org/api/insult.json?who={name}').json()
    if r['error'] != 'False':
        return r['insult']
    else:
        return "the api failed probably because you suck"

def holy_resp(name):
    return f"Holy Shit, {name}'s IQ is {randint(250, 10000)}. Now We Are the Children of {name}"

def fucks_resp(name=""):
    if name == "":
        return f"This Guy Fucks"
    else:
        return f"{name}'s Fucks"

def github_resp():
    return 'github.com/mmcintire96'


cmd_list = [
    {'cmd': 'cmds', 'resp': cmds_resp()},
    {'cmd': 'uptime', 'resp': uptime_resp()},
    {'cmd': 'title', 'resp': title_resp()},
    {'cmd': 'setup', 'resp': setup_resp()},
    {'cmd': 'editor', 'resp': editor_resp()},
    {'cmd': 'emacs', 'resp': emacs_resp()},
    {'cmd': 'github', 'resp': github_resp()},
]


