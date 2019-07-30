from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('a.html')

@app.route('/submit',methods=['GET','POST'])
def index1():
    v1 = request.form.get('LINES',type=int)
    v2 = request.form.get('WORDS',type=int)
    v3=  request.form.get('CHARACTERS',type=int)
    print(v1,v2,v3)
    n="KLE INSTITUTE OF TECHNOLOGY"
    d=len(n)
    c=d-n.count(' ')
    print(c)
    a = n.split()
    words=len(a)
    b = n.split('\n')
    lines=len(b)
    if v1==lines and v2==words and v3==c:
        return "success"
    else:
        return "fail"
if __name__=="__main__":
    app.run()