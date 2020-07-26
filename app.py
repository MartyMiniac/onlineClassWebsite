from flask import *
app=Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        try:
            print(request.form['name'])
            print(request.form['class'])
            print(request.form['sections'])
        except:
            return render_template('index.html', show_hidden=True)
        return ""
    else:
        return render_template('index.html', show_hidden=False)

if __name__=='__main__':
    app.run(debug=True)