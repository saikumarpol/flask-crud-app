from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for users
users = ["John Doe", "Jane Smith", "Alice Johnson"]

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    # Get the username from the form
    new_user = request.form.get('username')
    if new_user:
        users.append(new_user)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
