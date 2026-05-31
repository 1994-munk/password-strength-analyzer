from flask import Flask, render_template, request
import re 
import math 
import secrets
import string

#function to calculate password entropy using the formula: E = L * log2(N)
def calculate_entropy(password):
    pool=0
    if re.search(r'[a-z]', password):
        pool += 26
    if re.search(r'[A-Z]', password):
        pool += 26
    if re.search(r'\d', password):
        pool += 10
    if re.search(r'[!@#$%^&*()-+]', password):
        pool += 32
    if pool == 0:
        return 0
    return round(len(password) * math.log2(pool), 1)

#function to label entropy
def entropy_label(bits):
    if bits < 28:
        return 'Very Weak'
    elif bits < 36:
        return 'Weak'
    elif bits < 60:
        return 'Moderate'
    elif bits < 128:
        return 'Strong'
    else:
        return 'Very Strong'
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
        percentage = 33
        
    elif score<=4:
        strength = 'Moderate'
        percentage = 66
    else:
        strength = 'Strong'
        percentage = 100
    
    #calculate entropy    
    entropy = calculate_entropy(password)
    e_label = entropy_label(entropy)
    

    return percentage, feedback, strength ,entropy, e_label

#function to generate a random strong password
def generate_password(length=14):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-+"
    while True:
        pwd=''.join(secrets.choice(alphabet) for i in range(length))
        if (re.search(r'[A-Z]', pwd) and re.search(r'[a-z]', pwd) 
            and re.search(r'\d', pwd) and re.search(r'[!@#$%^&*()-+]', pwd)):
            return pwd
        
@app.route("/generate")
def generate():
    from flask import jsonify
    password = generate_password()
    return jsonify({'password': password, 'entropy': calculate_entropy(password), 'label': entropy_label(calculate_entropy(password))})
            

#home route 
@app.route("/", methods=['GET', 'POST'])
def home():
    
    percentage = 0
    strength = None
    feedback = []
    entropy = 0
    e_label = None
    
    #check if the form is submitted
    if request.method == 'POST':
        
        password = request.form['password']
        
        percentage, feedback, strength ,entropy, e_label = check_password_strength(password)
        
    return render_template(
        'index.html',
        strength=strength,
        feedback=feedback,
        percentage=percentage,
        entropy=entropy,
        e_label=e_label
    )

#run the application
if __name__ == '__main__':
    app.run(debug=True)
