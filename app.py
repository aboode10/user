import requests
import flask
from flask import *
app = Flask("__name__")
app.config["JSONIFY_PRETTYPRINT_REGULAR"]= True
app.config["JSON_AS_ACSII"] = False
@app.route("/")
def q():
 return jsonify(check=False, user=" ", Telegram="@JJJJzJJJ")
@app.route("/check/telegram/")
def sh():
    user = request.args.get("User")
    re = requests.get("https://t.me/{user}").text
    if "tgme_username_link" in re:
        return jsonify(Telegram="@JJJJzJJJ",User="True")
    else:
        return jsonify(Telegram="@JJJJzJJJ",User="False")


if __name__ == "__main__":
	app.run()
