from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__,template_folder='template')
b=[]
c= []
s = []
d = []
e =[]
f=[]
g=[]
h= []
l =-1


@app.route("/",methods = ['POST', 'GET'])
def home():
    name = ''
    roll =''
    physics = ''
    chemistry = ''
    maths = ''
    english = ''
    physical = ''

    
    global b
    global c
    global l
    global s
    global e
    global f
    global g
    global h
    # global d
    
    if request.method =='POST':
        name= request.form.get('name')
        roll = request.form.get('roll number')
        physics =request.form.get('physics mark') 
        chemistry =request.form.get('chemistry mark') 
        maths =request.form.get('maths mark') 
        english =request.form.get('english mark') 
        physical =request.form.get('physical mark') 
        l = l+1
        b.append(name)
        c.append(roll)
        s.append(physics)
        e.append(chemistry)
        f.append(maths)
        g.append(english)
        h.append(physical)
        
        d.append(l)
        l = len(c)
        
       
        
        

    return render_template("index.html", c=c,b=b,g=g, d=d,s=s,e=e,h=h ,f=f)



    


if __name__ == "__main__":
    app.run(debug=True)


