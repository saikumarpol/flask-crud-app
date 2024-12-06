from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    if name:
        users.append(name)
    return redirect(url_for('index'))

@app.route('/delete/<string:name>', methods=['GET'])
def delete_user(name):
    if name in users:
        users.remove(name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
