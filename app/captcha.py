from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm, RecaptchaField
import requests

class VerificationForm(FlaskForm):   
      recaptcha = RecaptchaField()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'shhhhhhhhhhhhhhhhssh'
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='INSERT KEY HERE'
app.config['RECAPTCHA_PRIVATE_KEY']='INSERT KEY HERE'


@app.route('/verify', methods=['GET', 'POST'])
def verify():
    
    form = VerificationForm()

    if form.validate_on_submit():
        link = requests.get("http://localhost:3452").text
        return redirect(link)

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
