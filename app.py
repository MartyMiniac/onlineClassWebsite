from flask import *
import json
import requests
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        try:
            name=" ".join(request.form['name'].split())
            cl=int(request.form['class'])
            sec=request.form['sections']
            js=getInfo(name=name, cl=cl, sec=sec)
        except:
            return render_template('index.html', show_hidden=True)
        print(js)
        return render_template('showattendance.html', js=js)
    else:
        return render_template('index.html', show_hidden=False)

def getInfo(name, cl, sec):
    try:
        if cl==12:
            f=open('static/json/class12.json', 'r')
            js=json.load(f)
            f.close()
        
        elif cl==10:
            f=open('static/json/class10.json', 'r')
            js=json.load(f)
            f.close()
    except:
        print('file not found creating files')
        url = "https://sfsonline-f942.restdb.io/rest/filejson"

        headers = {
            'content-type': "application/json",
            'x-apikey': "5d64e8dbc2fa8af2172050d1134e103d0da28",
            'cache-control': "no-cache"
            }
        response = requests.request("GET", url, headers=headers)
        js=json.loads(response.text)
        for s in js:
            print(s['class'])
            f=open('static/json/'+s['class'], 'w')
            f.write(json.dumps(s['json'], indent=4))
            f.close()

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
        if s['name'].lower()==name.lower() and s['class']==cl and s['section']==sec:
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

@app.route('/masterconsole', methods=['POST', 'GET'])
def console():
    if request.method=='POST':
        f = request.files['file']
        f.save('static/json/'+f.filename)


        url = "https://sfsonline-f942.restdb.io/rest/filejson"

        headers = {
            'content-type': "application/json",
            'x-apikey': "5d64e8dbc2fa8af2172050d1134e103d0da28",
            'cache-control': "no-cache"
            }
        response = requests.request("GET", url, headers=headers)
        js=json.loads(response.text)

        obid=""
        for s in js:
            if s['class']==f.filename:
                obid=s['_id']

        url = "https://sfsonline-f942.restdb.io/rest/filejson/"+obid
        g=open('static/json/'+f.filename, 'r')
        payload = "{\"json\": "+g.read()+"}"
        g.close()
        headers = {
            'content-type': "application/json",
            'x-apikey': "5d64e8dbc2fa8af2172050d1134e103d0da28",
            'cache-control': "no-cache"
            }

        response = requests.request("PUT", url, data=payload, headers=headers)

        return str(response.text)
    else:
        return render_template('console.html')

@app.route('/videouploads', methods=['POST'])
def videoupload():
    if request.method == 'POST':
        js=request.json
        url = "https://sfsonline-f942.restdb.io/rest/fileuploads"

        payload = json.dumps( js )
        headers = {
            'content-type': "application/json",
            'x-apikey': "5d64e8dbc2fa8af2172050d1134e103d0da28",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        return response.text

@app.route('/getlessons', methods=['GET'])
def lessons():
    try:
        f=open('static/json/lessons.json','r')
        js=json.load(f)
        f.close()
    except:
        url = "https://sfsonline-f942.restdb.io/rest/fileuploads"

        headers = {
            'content-type': "application/json",
            'x-apikey': "5d64e8dbc2fa8af2172050d1134e103d0da28",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers)

        js=json.loads(response.text)
        f=open('static/json/lessons.json','w')
        f.write(json.dumps(js, indent=4))
        f.close()
    
    return render_template('lessons.html', js=js)

@app.route('/teacherlogin', methods=['POST','GET'])
def teacherlogin():
    if request.method=='POST':
        password=request.form['password']
        if password=='thisismypassword':
            try:
                f=open('static/json/class12.json', 'r')
                js12=json.load(f)
                f.close()
            
                f=open('static/json/class10.json', 'r')
                js10=json.load(f)
                f.close()
            except:
                print('file not found creating files')
                url = "https://sfsonline-f942.restdb.io/rest/filejson"

                headers = {
                    'content-type': "application/json",
                    'x-apikey': "5d64e8dbc2fa8af2172050d1134e103d0da28",
                    'cache-control': "no-cache"
                    }
                response = requests.request("GET", url, headers=headers)
                js=json.loads(response.text)
                for s in js:
                    print(s['class'])
                    f=open('static/json/'+s['class'], 'w')
                    f.write(json.dumps(s['json'], indent=4))
                    f.close()

                f=open('static/json/class12.json', 'r')
                js12=json.load(f)
                f.close()
                
                f=open('static/json/class10.json', 'r')
                js10=json.load(f)
                f.close()
            
            arr=[]
            for s in js10['data']:
                t={}
                t['name']=s['name']
                t['class']=s['class']
                t['section']=s['section']
                t['days present']=s['days present']
                t['number of days present']=s['number of days present']
                arr.append(t)
            
            for s in js12['data']:
                t={}
                t['name']=s['name']
                t['class']=s['class']
                t['section']=s['section']
                t['days present']=s['days present']
                t['number of days present']=s['number of days present']
                arr.append(t)
            
            return render_template('attendancelist.html', arr=arr)
        else:
            return render_template('teacherlogin.html', show_hidden=True)
    else:
        return render_template('teacherlogin.html', show_hidden=False)

@app.route('/test', methods=['POST','GET'])
def exam():
    return render_template('exam.html')

@app.route('/testengine', methods=['GET'])
def testengine():
    return open('static/htmls/testengine.html','r').read()

@app.route('/getquestions', methods=['POST'])
def getquestion():
    try:
        f=open('static/json/examquestions.json','r')
        js=json.load(f)
        f.close()
    except:
        #Logic to get questions from database
        print('failed to load questions')
        f=open('static/json/examquestions.json','r')
        js=json.load(f)
        f.close()
    qno=request.get_json(force=True).get('qno',"")
    if qno=='all':
        return jsonify(js['data'])
    ques=js['data'][int(qno)]
    return jsonify(ques)

if __name__=='__main__':
    app.run(debug=True)