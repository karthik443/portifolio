from flask import Flask,render_template,redirect,request
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def works(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        store_data_csv(data)
        # return redirect('thankyou.html')
        return 'form submmittes'


def store_data(data):
    with open('./database.txt', mode='a') as file:
        emails = data['email']
        subject = data['subject']
        message = data['message']
        file.write(f' \n{emails} , {subject} , {message}')

def store_data_csv(data):
    with open('./database.csv', mode='a') as file:
        emails = data['email']
        subject = data['subject']
        message = data['message']
        csv_file=csv.writer(file,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([emails,subject,message])