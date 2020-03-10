from flask import Flask, render_template, request, url_for, redirect
import subEncrypt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/penc', methods = ['POST', 'GET'])
def penc():
    emsg = request.form
    # print(emsg)
    # print(emsg['message'])

    outmsg = subEncrypt.encrypted(emsg['message'])

    return render_template('out.html', value = outmsg)

# if __name__ == '__main__':
#    app.run(debug = True)

