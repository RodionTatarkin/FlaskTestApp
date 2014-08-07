from flask import Flask, render_template, url_for, request, redirect, flash
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    username = request.form['username']
    if request.form['password'] != 'rodion':
      error = 'Invalid password'
    else:
      #flash('You were logged in')
      #return 'Welcome %s' % username
      return redirect(url_for('show_username', username=username))
  return render_template('login.html', error=error)

#@app.route('/user/')
#@app.route('/user/<username>')
#def show_username(username):
#  return 'User %s' % username

@app.route('/user/')
@app.route('/user/<username>')
def show_username(username=None):
  return render_template('hello.html', username=username)

@app.route('/about/')
def about():
  return 'The about page'

if __name__ == '__main__':
  app.run(debug=True)
