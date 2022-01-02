import pymysql as pym
from User import User
class AddressBookModel:
    user_id = -1
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password = password
        self.database = database
        try:
            #create DB connection
            connection = pym.connect(host=self.host, user= self.user, password = self.password, database=self.database)
            self.connected = connection
            dbCursor = self.connected.cursor()
            self.dcursor = dbCursor
        except:
            print("DB not connected")
        

    def signupUser(self,user):
        query = "insert into user(user_email, user_password) values(%s, %s)"
        arg = (user.email, user.password)
        self.dcursor.execute(query, arg)
        self.connected.commit()
        return True
  
    def checkAlreadyExist(self,user):
        # create / get Cursor object
        dbCursor = self.dcursor
        dbCursor.execute("Select user_email from user")
        emailList=dbCursor.fetchall()
        for e in emailList:
            print(e)
            if e[0] == user.email:
                return True
            
        return False

    def isValid(self, user):
        dbCursor = self.dcursor
        dbCursor.execute("Select user_email, user_password from user")
        emailList=dbCursor.fetchall()
        for e in emailList:
            if e[0]==user.email and e[1] == user.password:
                return True
            
        return False



    def signIn(self,user):
        dbCursor = self.dcursor
        if self.isValid(user) == False:
            print("Invalid Email or password")
            return []
        else:
            dbCursor.execute("Select * from user where user_email = %s", user.email)
            ls = dbCursor.fetchall()
            return ls

    def insertContact(self, contact, id):
        query = "insert into addressbook(user_id,   Contact_name,	Contact_mobile,	Contact_city,	Contact_profession	) values(%s, %s,%s, %s,%s)"
        arg = (id, contact.name, contact.mobile, contact.city, contact.profession)
        self.dcursor.execute(query, arg)
        self.connected.commit()
        return True

    def UpdateContact(self, contact, id):
        query = "UPDATE addressbook set  Contact_name = %s,	Contact_mobile = %s,	Contact_city = %s,	Contact_profession = %s where user_id = %s"
        arg = (contact.name, contact.mobile, contact.city, contact.profession, id)
        self.dcursor.execute(query, arg)
        self.connected.commit()
        return True

    def Update_Contact(self, contact, uid, cid):
        query = "UPDATE addressbook set  Contact_name = %s,	Contact_mobile = %s,	Contact_city = %s,	Contact_profession = %s where user_id = %s and contact_id = %s"
        arg = (contact.name, contact.mobile, contact.city, contact.profession, uid, cid)
        self.dcursor.execute(query, arg)
        self.connected.commit()
        return True


    def searchData(self, data):
        dbCursor = self.dcursor
        dbCursor.execute("Select * from addressbook")
        emailList=dbCursor.fetchall()
        ls = ()
        count = 0
        for e in emailList:
            if data in e[2] or data == e[4] or data == e[5]: 
                ls = list(ls)
                ls.insert(count, e)
                ls = tuple(ls)
                count = count + 1
        return ls

    def AllData(self, ID):
        dbCursor = self.dcursor
        dbCursor.execute("Select * from addressbook where user_id = %s", ID)
        contactLs = dbCursor.fetchall()

        return contactLs
        
    def deleteData(self,ID):
        dbCursor = self.dcursor
        dbCursor.execute("Delete from addressbook where contact_id = %s", ID)
        self.connected.commit()

    def delete_Data(self,name):
        dbCursor = self.dcursor
        dbCursor.execute("Delete from addressbook where Contact_name = %s", name)
        self.connected.commit()


    def find_user(self, user_id):
        dbCursor = self.dcursor
        dbCursor.execute("Select user_email, user_password from user where user_id = %s", user_id)
        contactLs = dbCursor.fetchall()
        print("----------------------------------------------")
        print(contactLs)
        print(user_id)
        print("----------------------------------------------")
        return contactLs
    

    def __del__(self):

        if self.connected!=None:
            self.connected.close()


    def getAllusersData(self):
        dbCursor = self.dcursor
        dbCursor.execute("Select * from user")
        contactLs = dbCursor.fetchall()
        return contactLs


    def isValidContactID(self, id):
        dbCursor = self.dcursor
        dbCursor.execute("Select * from addressbook")
        contactLs = dbCursor.fetchall()
        for i in contactLs:
            if str(i[0]) == str(id):
                return True

        return False
