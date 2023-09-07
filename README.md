# Lemmy procyclingbot

WIP. A bot for https://lemmy.world/c/procycling. Creates scheduled posts for races, currently only for Vuelta stages. 


## Installation
```
git clone git@github.com:JLukeBlakey/lemmy_procyclingbot.git
cd lemmy_procyclingbot
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
```

## Todo
- post for all World Tour level races (per stage for Grand Tours only)
- use classes and generally tidy code

## Testing:
Modify credentials to your own. I have been using https://lemmy.world/c/bot_test community and immediately deleting post.
```
venv/bin/python3 main.py
```

## Contributing
All contributions welcome, raise a pull request, issue, comment etc. 
