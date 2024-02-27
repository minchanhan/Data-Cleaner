from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import pandas as pd 
import numpy as np 

app = Flask(__name__)

# Configuration for allowed uploads - you'll want to change this! 
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return ('.' in filename) and (filename.split('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS'])

def calculate_results(data_filename, missing_values, string_cols, number_cols):
    print(data_filename)
    df = pd.read_csv(data_filename, na_values=missing_values)
    olddf = df
    
    # Detecting numbers in string type columns, turn to NaN
    for strcol in string_cols:
        if(not strcol in df.columns):
            print("This isn't a valid column! Remember Case Sensitive!")
            continue
        i=0
        for row in df[strcol]:
            try:
                int(row)
                df.loc[i, strcol]=np.nan
            except ValueError:
                try:
                    float(row)
                    df.loc[i, strcol]=np.nan
                except ValueError:
                    pass
            i+=1

    # Detecting strings in number type columns (int or float), turn to NaN
    for numcol in number_cols:
        if(not numcol in df.columns):
            print("This isn't a valid column! Remember Case Sensitive!")
            continue
        i=0
        for row in df[numcol]:
            try:
                int(row)
            except ValueError:
                try:
                    float(row)
                except ValueError:
                    df.loc[i, numcol]=np.nan
                    pass
            i+=1

    return df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')

        # Extracting uploaded file name
        data_filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))

        if file.filename == '':
            return render_template('index.html', error="Please select a file.")
        if not allowed_file(file.filename):
            return render_template('index.html', error="Please upload CSV files.")

        # Get other form data
        missing_values = request.form['missing_values'].split(',')
        string_cols = request.form['string_cols'].split(',')
        number_cols = request.form['number_cols'].split(',')

        result = calculate_results(data_filename, missing_values, string_cols, number_cols)
        result.to_csv('result.csv')  # Save in the desired location
        return send_file('result.csv', as_attachment=True, download_name='result.csv', mimetype='text/plain')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

