# Komi-San
Telegram Group Management Bot based on Pyrogram

<b> More updates coming soon </b>

[Support Group](https://t.me/Komisan_Support)

<b> Open a Pull request
if you wana contribute </b>


Example for making new plugins

```
from nksama import bot 
from pyrogram import filters

@bot.on_message(filters.command('hi'))
def hi(_,message):
  message.reply('hi')
  


```


# How to deploy ?

__Vars__ :

```
API_ID - my.telegram.org
API_HASH -  my.telegram.org
BOT_TOKEN - @botfather
MONGO_URL

```
<p align="center"><a href="https://dashboard.heroku.com/new?template=https://github.com/ashui501/Komi-San"> <img 
src="https://img.shields.io/badge/Deploy%20To%20Heroku-pink?style=flat&logo=heroku" width="210" height="34.45" /></a></p>

