class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()
    def menu(self):  
        user_input=input("""welcome to chatbook // how would you proceed?
                        1. press 1 tosignup
                        2. press 2 for signin
                        3. press 3 to write a post
                        4. press 4 to message a friend
                        5. press any other key to exit""")
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            self.my_post()
        elif user_input=='4':
            self.sendmsg()
        else:
            exit()
    def signup(self):
        email=input('enter your email here -> ')
        pwd=input('enter your password here ->') 
        self.username=email
        self.password=pwd
        print('you have signed up successfully')
        self.menu()
    def signin(self):
        if self.username==''and self.password=='':
            print('please signup first by pressing  1 in the main menu')
        else:
            uname=input('enter your email/username here ->')
            pwd=input('enter your password here ->')
            if self.username==uname and self.password==pwd:
                print('you have signed in succesfully')
                self.loggedin=True
            else:
                print('please input correct credentials..')
        print('\n')
        self.menu()            
    def my_post(self):
        if self.loggedin==True:
            txt=input('enter your message here -> ')
            print(f'following content has been posted -> {txt}')
        else:
            print('you need to signin first to post something...')
        print('\n')
        self.menu()
    def sendmsg(self):
        if self.loggedin==True:
            txt=input('enter your message here ->')
            frnd=input ('whom to send to {frnd}')
            print(f'your message has been sent to {frnd}')
        else:
            print('you need to signin first to post something...') 
        print('\n')
        self.menu()       





   

   
obj=chatbook()        
          