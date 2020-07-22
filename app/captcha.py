from flask import Flask, render_template, request
from flask_wtf import FlaskForm, RecaptchaField

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
        print("it's working")
        return "DONE :D"
        #do your thing from here fume

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)