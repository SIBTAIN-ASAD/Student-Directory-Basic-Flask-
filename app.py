from flask import Flask, render_template , request, make_response
from Contact import Contact
from User import User
from AddressBookModel import AddressBookModel
app = Flask(__name__)

# global GID

model = AddressBookModel("localhost","root","","address")

@app.route('/')
def hello_world():
    return render_template("Login.html",error = False, errormsg = None) # jinja templating agent

# @app.route('/second')
# def test():
#     return 'Aslam o Alaikum!'

@app.route("/signupform")
def signupform():
    return render_template("Signup.html", error = False, errormsg = None)

@app.route('/dashboard')
def testdashboard():
    return  render_template("Dashboard.html", name = "TestUser")


# @app.route('/testtemplate')
# def testtemplate():
#     n="Ali"
#     text="this is text from server"
#     return render_template("Test.html",name=n,text=text)

@app.route("/login", methods=["POST"])
def login():
    email=request.form["email"]
    pwd=request.form["pwd"]
    u=User(email,pwd)

    ls = model.signIn(u)

    if len(ls) > 0:
        # AddressBookModel.user_id = ls[0][0]
        curr = model.AllData(ls[0][0])

        response = make_response(render_template("Dashboard.html",_email= ls[0][1] ,_passwd = ls[0][2],_curr= curr))

        response.set_cookie("user_id",str(ls[0][0]) )

        return response

    

        # return render_template("Dashboard.html",_email= ls[0][1] ,_passwd = ls[0][2],_curr= curr)
    else:
        return render_template("Login.html", error=True,errormsg="Invalid UserName or Password")

@app.route("/create", methods=["POST"])
def create_contact():
    # if AddressBookModel.user_id == -1:
    usid = request.cookies.get("user_id")
    if usid == None:
        return render_template("Login.html", error=True,errormsg="Session ended, Please enter again")

    # getting user data
    name = request.form["name"]
    mb = request.form["mobile"]
    city = request.form["city"]
    pro = request.form["pro"]
    # num = AddressBookModel.user_id

    num = int(usid)

    cont = Contact(num, name, mb, city, pro)

    if model.insertContact(cont, num) == True:
        print("=== CONTACT ADDED ===")

    data = model.find_user(num)

    curr = model.AllData(num)

    return render_template("Dashboard.html",_email= data[0][0] , _passwd = data[0][1] ,_curr= curr)

@app.route("/delete", methods=["POST"])
def delete_contact():

    # if AddressBookModel.user_id == -1:
    usid = request.cookies.get("user_id")
    if usid == None:
        return render_template("Login.html", error=True,errormsg="Session ended, please enter again")

    name = request.form["name"]

    model.delete_Data(name)
    # num = AddressBookModel.user_id
    num = int(usid)

    data = model.find_user(num)

    curr = model.AllData(num)

    return render_template("Dashboard.html",_email= data[0][0] , _passwd = data[0][1] ,_curr= curr)


@app.route("/update", methods=["POST"])
def update_contact():

    usid = request.cookies.get("user_id")
    if usid == None:
        return render_template("Login.html", error=True,errormsg="Session ended, please enter again")

    name = request.form["name"]

    check = model.isValidContactID(name)

    if check == False:
        num = int(usid)
        data = model.find_user(num)
        curr = model.AllData(num)

        return render_template("Dashboard.html",_email= data[0][0] , _passwd = data[0][1] ,_curr= curr, error=True,errormsg="Invalid Contact ID")
    # model.delete_Data(name)
    # num = AddressBookModel.user_id

    response = make_response(render_template("Update.html"))

    response.set_cookie("cid", name)

    return response


@app.route("/updateit" , methods=["POST"])
def update_now():
    usid = request.cookies.get("user_id")
    usid = int(usid)
    cid = request.cookies.get("cid")
    cid = int(cid)

    name = request.form["name"]
    mb = request.form["mobile"]
    city = request.form["city"]
    pro = request.form["pro"]
    # num = AddressBookModel.user_id
    cont = Contact(usid, name, mb, city, pro)

    model.Update_Contact(cont, usid, cid)

    data = model.find_user(usid)

    curr = model.AllData(usid)

    return render_template("Dashboard.html",_email= data[0][0] , _passwd = data[0][1] ,_curr= curr)
    


@app.route("/signup", methods=["POST"])
def signup():
    email = request.form["email"]
    password = request.form["pwd"]
    if len(password) < 8:
        return render_template("Signup.html",error = True , errormsg = "Password should be 8 characters")

    user = User(email,password)
    exist = model.checkAlreadyExist(user)
    if exist == False:
        insert = model.signupUser(user)
        
        if insert == True:
            return render_template("Signup.html",error=True , errormsg="Congratulations! You have successfully created your account")
        else:
            return render_template("Signup.html", error=True , errormsg="ERROR! IN inserting data in database")
    else:
        return render_template("Signup.html",error=True,errormsg="Email already exist")

@app.route("/data", methods=["POST"])
def new_data():
    data = model.getAllusersData()
    return render_template("showdata.html", ls = data)

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
    


@app.route("/logout", methods=["POST"])
def logout():
    # response = make_response(render_template("Login.html",error = True, errormsg = "user loged out"))
    # response.delete_cookie("user_id")
    # response.delete_cookie("cid")
    return render_template("Login.html",error = True, errormsg = "user loged out")

    # return  # jinja templating agent
