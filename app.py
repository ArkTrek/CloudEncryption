from flask import Flask, render_template, request, redirect, url_for, session
import pyminizip
import temp as tmp_file

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'abc23'  # Change this to a secure secret key

# Mock user database (replace with your actual user database)
users = {
    'admin': 'abc',
    'user': 'abc1'
}

@app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Invalid credentials')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))
    
@app.route('/upload', methods=['POST'])
def upload():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        files = request.files['file']
        outp = "test.zip"
        password = request.form['password']
        # abc = pyminizip.compress(files, None, outp, password, 5)
        if file and password:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            result = pyminizip.compress(filename, None, outp, passwords, 5)
        # return abc 
        # return redirect(url_for('result'))
    # file = request.files['file']
    # password = request.form['password']
    # if file and password:
    #     # Save the uploaded file to the server
    #     filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    #     file.save(filename)
        #result = 
        # Process the uploaded file and password
        # Example: result = process_file_and_password(filename, password)

        # Redirect to a page showing the result
        result = 'File and password received successfully.'
        return send_file(tmp_file.name, as_attachment=True, attachment_filename=filename)
        return redirect(url_for('upload_processing', result=result))

@app.route('/upload_processing')
def upload_processing():
    return render_template('upload.html')
    return render_template('result')

@app.route('/result')
def result():
    # Get the result from processing and pass it to the template
    result = request.args.get('result')
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
