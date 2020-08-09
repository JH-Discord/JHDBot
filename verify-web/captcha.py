from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm, RecaptchaField
from multiprocessing import cpu_count
from webhook_loghandlers.handlers import DiscordHandler
import logging
import requests
import os


class VerificationForm(FlaskForm):
    recaptcha = RecaptchaField()


app = Flask(__name__)

app.config["SECRET_KEY"] = str(os.urandom(32))
app.config["RECAPTCHA_USE_SSL"] = False
app.config["RECAPTCHA_PUBLIC_KEY"] = os.environ.get("RECAPTCHA_PUBLIC_KEY")
app.config["RECAPTCHA_PRIVATE_KEY"] = os.environ.get("RECAPTCHA_PRIVATE_KEY")
BOT_TOKEN = os.environ.get("DISCORD_API_TOKEN")
SERVER_ID = os.getenv("DISCORD_SERVER_CHANNEL_ID")
app.config['RECAPTCHA_DATA_ATTRS']= {'theme': 'dark'}

logger = logging.getLogger('Web')
logger.setLevel(logging.INFO)
hookToken = os.getenv("LOGGING_WEBHOOK_TOKEN")
hookChannel = os.getenv("LOGGING_WEBHOOK_CHANNEL")
discordHandler = DiscordHandler(f'https://discordapp.com/api/webhooks/{hookChannel}/{hookToken}')
discordHandler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(name)s] (%(levelname)s): %(message)s')
discordHandler.setFormatter(formatter)
logger.addHandler(discordHandler)

def get_invite_link():
    data = b'{"max_age":3600,"max_uses":1,"target_user_id":null,"target_user_type":null,"temporary":true}'
    headers = {"content-type": "application/json", "Authorization": f"Bot {BOT_TOKEN}"}
    k = requests.post(
        "https://discord.com/api/v6/channels/{}/invites".format(SERVER_ID),
        headers=headers,
        data=data,
    )
    if k.status_code != 200:
        logger.error(f"API request for discord invite returned a {k.status_code}")
    return f"https://discord.gg/{k.json()['code']}"


@app.route("/verify", methods=["GET", "POST"])
def verify():
    form = VerificationForm()
    app.logger.error('test')
    if form.validate_on_submit():
        return redirect(get_invite_link())
    return render_template("verify.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
