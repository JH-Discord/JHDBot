from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm, RecaptchaField
from multiprocessing import cpu_count
import requests
import os

class VerificationForm(FlaskForm):   
      recaptcha = RecaptchaField()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('CSRF_SECRET_KEY')
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']= os.environ.get('RECAPTCHA_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY']= os.environ.get('RECAPTCHA_PRIVATE_KEY')


@app.route('/verify', methods=['GET', 'POST'])
def verify():
    
    form = VerificationForm()

    if form.validate_on_submit():
        link = requests.get("http://localhost:3452").text
        return redirect(link)

    return render_template("verify.html", form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
