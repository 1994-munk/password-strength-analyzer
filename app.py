from flask import Flask, render_template, request
import re 
#create a Flask application
app = Flask(__name__)

#function to check password strength
def check_password_strength(password):
    
    score = 0
    feedback = []
    
    #check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append('Password should be at least 8 characters long.')

    #check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append('Password should contain at least one uppercase letter.')

    #check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append('Password should contain at least one lowercase letter.')

    #check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append('Password should contain at least one digit.')

    #check for special characters
    if re.search(r'[!@#$%^&*()-+]', password):
        score += 1
    else:
        feedback.append('Password should contain at least one special character.')

    #determine password strength
    if score<=2:
        strength = 'Weak'
    elif score<=4:
        strength = 'Moderate'
    else:
        strength = 'Strong'

    return score, feedback, strength

#home route 
@app.route("/", methods=['GET', 'POST'])
def home():
    
    strength = None
    feedback = []
    
    #check if the form is submitted
    if request.method == 'POST':
        
        password = request.form['password']
        
        score, feedback, strength = check_password_strength(password)
        
    return render_template(
        'index.html',
        strength=strength,
        feedback=feedback
    )

#run the application
if __name__ == '__main__':
    app.run(debug=True)
