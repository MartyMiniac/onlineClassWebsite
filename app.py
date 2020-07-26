from flask import *
import json

app=Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        try:
            name=request.form['name']
            cl=int(request.form['class'])
            sec=request.form['sections']
            js=getInfo(name=name, cl=cl, sec=sec)
        except:
            return render_template('index.html', show_hidden=True)

        return render_template('showattendance.html', js=js)
    else:
        return render_template('index.html', show_hidden=False)

def getInfo(name, cl, sec):
    if cl==12:
        f=open('static/json/class12.json', 'r')
        js=json.load(f)
        f.close()
    
    elif cl==10:
        f=open('static/json/class10.json', 'r')
        js=json.load(f)
        f.close()

    outp={}
    outp['student found']=False
    outp['name']=name
    outp['class']=cl
    outp['section']=sec
    for s in js['data']:
        if s['name']==name.lower() and s['class']==cl and s['section']==sec:
            arr={}
            for i in js['classes done on']:
                if i in s['days present']:
                    arr[i[:2]+'-'+i[2:4]+'-'+i[4:]]='Present'
                else:
                    arr[i[:2]+'-'+i[2:4]+'-'+i[4:]]='Absent'

            outp['attendance']=arr
            outp['student found']=True
            break

    return outp
if __name__=='__main__':
    app.run(debug=True)