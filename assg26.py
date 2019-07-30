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
    
    "HTML CODE"
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>GAME TIME</title>
</head>
<body>

<form name="myform" style="position:absolute;top:25%;left:40%;">
    <h1>KLE INSTITUTE OF TECHNOLOGY</h1>
    <h1>HUBBALLI</h1>
</form>




<form name="myform"   method="post" >
            <div style="position:absolute;top:45%;left:10%;">
No of Lines:<p><input type="number"name="LINES" id="lines" style="font-size:18pt;height=35px;width=200px;"></p>
No of Words:<p><input type="number"name="WORDS" id="words" style="font-size:18pt;height=35px;width=200px;"></p>
No of Characters:<p><input type="number"name="CHARACTERS" id="char" style="font-size:18pt;height=35px;width=200px;"></p></div>
          <div style="position:absolute; bottom:10%;right:45%; font-size:40pt;">
        <input type="submit"  formaction="/submit" name="submit" id="submit" value="SUBMIT">
            </div>

<div id="timer" style="position:absolute; top:5%;right:5%; font-size:40pt; color:red;"></div>

<script type="text/javascript">

var timeoutHandle;
function countdown(minutes,seconds){
 function tick(){
  var counter=document.getElementById("timer");

  counter.innerHTML=minutes.toString()+":" + (seconds<10 ? "0" : "")+ String(seconds);
  seconds--;
  if(seconds>=0) {
  timeoutHandle=setTimeout(tick,1000);
  }else {
   if(minutes>=1) {
   setTimeout(function() {
   countdown(minutes-1,59);
   }, 1000);
   }
  }
 }
 tick();
 }
 countdown(1,30);
var auto_refresh=setInterval(function(){
submitform();
},90000);

function submitform() {
document.getElementById("submit").click();
}
</script>
</form>
</body>
</html>
