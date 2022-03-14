from flask import render_template, url_for, redirect, request
from pathlib import Path
import os
# from werkzeug import secure_filename
from app import app

parentPath = Path(__file__).parent.absolute();

def get_user_scripts_path():
    return Path().joinpath(str(parentPath) + "/user-scripts/")

def get_user_scripts():
    folderPath = get_user_scripts_path();
    dirList = os.listdir(folderPath);
    
    userScripts = []

    for file in dirList:
        if ".py" in file:
            if ".pytest_cache" not in file:
                userScripts.append(file)

    return userScripts;

@app.route('/')
@app.route('/index')
def index():
    userScripts = get_user_scripts();
    return render_template('index.html', scripts=userScripts)

@app.route('/button_update', methods = ['POST', 'GET'])
def button_update():
    userScripts = get_user_scripts();
    if request.method == 'POST':
        userInput = request.form.get('userInput');
        print(userInput);
    elif request.method == 'GET':
        print("GET")
    return redirect(url_for('index'))

@app.route('/select_script', methods = ['POST', 'GET'])
def select_script():
    userScripts = get_user_scripts();
    if request.method == 'POST':
        script = request.form.get('selectScript');
        scriptIn = True;
        return render_template('index.html', scripts=userScripts, selectedScript=script, scriptIn=scriptIn)
    elif request.method == 'GET':
        print("GET")
    return redirect(url_for('index'))

@app.route("/script_test/<Script>", methods=['GET', 'POST'])
def script_test(Script):
    userScripts = get_user_scripts();
    folderPath = get_user_scripts_path();
    scriptIn = True;
    if request.method == 'POST':
        scriptPath = Path().joinpath(str(folderPath) + "/" + str(Script))
        isPytest = request.form.get('isPytest')
        if isPytest:
            cmd = "pytest " + str(scriptPath) + " --demo";
        else:
            cmd = str(scriptPath);
        print(cmd)
        os.system(cmd)
    elif request.method == 'GET':
        print("GET")
    return redirect(url_for('index'))

@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
    userScripts = get_user_scripts();
    folderPath = get_user_scripts_path();
    if request.method == 'POST':
        f = request.files['file']
        #   f.save(secure_filename(f.filename))
        f.save(str(folderPath) + "/" + f.filename)
        print("file uploaded successfully");
    elif request.method == 'GET':
        print("GET")
    return redirect(url_for('index'))



    
