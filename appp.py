from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import pandas as pd 
import numpy as np 
from io import StringIO
import csv

app = Flask(__name__)

# Configuration for allowed uploads - you'll want to change this! 
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

def allowed_file(filename):
    return ('.' in filename) and (filename.split('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS'])

def calculate_results(data_file, missing_values, string_cols, number_cols):
    # Identify missing value symbols
    yourdata = pd.read_csv(data_file)
    olddf = yourdata
    df = pd.read_csv(yourdata, na_values=missing_values)
    
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

    # Create a CSV string in memory
    si = StringIO()
    cw = csv.writer(si)
    cw.writerows(df)
    output_csv_string = si.getvalue()
    return output_csv_string
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_csv_file = request.files['file']  # Access uploaded CSV
        form_data = request.form  # Access other form data
        
        # Validate uploaded file type
        if not allowed_file(uploaded_csv_file.filename):
            return "Invalid file type. Please upload a CSV file."
        
        # Read uploaded CSV data
        uploaded_csv_data = uploaded_csv_file.stream.read().decode("utf-8")

        output_csv_string = calculate_results(uploaded_csv_data, form_data)

        # Send the CSV file as a download
        return send_file(
            StringIO(output_csv_string),
            mimetype='text/csv',
            attachment_filename='processed_data.csv',
            as_attachment=True
        )

    return render_template('index.html')  # Your form template


if __name__ == '__main__':
    app.run(debug=True)