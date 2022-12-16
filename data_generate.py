import random as r

class SQLTableValues:
    '''creates data for user table from raw txt file'''
    def __init__(self,raw_file = 'raw_file.txt'):
        self.raw_file = raw_file
        self.note_count = r.randint(15,100)
        self.comments_no = r.randint(15,200)
        self.users_count = 0
        self.fileName_list = []
        self.raw_file_opener()

        self.user_dict = {}
        self.friend_dict = {}
        self.note_dict = {}
        self.event_dict = {}
        self.comment_dict = {}

    def raw_file_opener(self):
        '''opens file consisting of names'''
        file_handle = open(self.raw_file,'r')
        for line in file_handle:
            self.fileName_list.append(line.strip().split())
            self.users_count += 1 

    def create_user_dict(self):
        '''k: user_id, v:list of [first_name, last_name, username, password]'''
        name = self.fileName_list
        username = self.gen_username()
        password = self.gen_password()
        for user_id in range(self.users_count):
            self.user_dict[user_id] = [name[user_id][0], name[user_id][1], username[user_id], password[user_id]]

    def gen_username(self):
        username_list = []   
        for i in range(self.users_count):
            final = ''.join(self.fileName_list[i]) 
            if len(final) < 8:
                final += str(r.randint(0,9)) * (r.randint(8,14) - len(final))
            elif len(final) > 14:
                final = final[:r.randint(9,15)]  
            username_list.append(final)
        return username_list

    def gen_password(self):
        password_list = []
        for _ in range(self.users_count):
            passsword = ''
            for _ in range(r.randint(8,14)):
                digits = str(r.randint(0,9))
                upper_case_alpha = chr(r.randint(65,90))
                lower_case_alpha = chr(r.randint(97,122))

                passsword += r.choice([digits,upper_case_alpha,lower_case_alpha])

            password_list.append(passsword)
        return password_list

    def create_friend_dict(self):
        '''k: user_id, v: [friend_id]'''
        records_count = self.users_count
        user_id_list = r.sample(range(1,records_count),15) #creation of randomly generated sample from total
        for user_id in user_id_list:
            for _ in range(1,r.choice(range(1,10))): # creation of friends per user
                friend_id = r.randint(1,50)
                if user_id != friend_id:

                    if user_id not in self.friend_dict:
                        self.friend_dict[user_id] = [friend_id]               
                    else:
                        self.friend_dict[user_id].append(friend_id)
   
                    if friend_id not in self.friend_dict:
                        self.friend_dict[friend_id] = [user_id]                    
                    else:
                        self.friend_dict[friend_id].append(user_id) 
    
    def create_note_dict(self):
        ''' creates dict k: note_id, v: list- [user_id, title, text, visible_to]'''
        notes_list = self.gen_notes()

        for i in range(self.note_count):
            for _ in range(r.randint(1,10)): #no. of notes per user
                visibility = r.choice(['public','friends'])        
                self.note_dict[i+1] = [r.randint(1,self.users_count), notes_list[i][0], notes_list[i][1], visibility]

    def gen_notes(self):
        notes_list = []
        for _ in range(self.note_count):
            title = 'wefn'
            text = 'ewe'
            notes_list.append([title,text])
        return notes_list

    def create_event_dict(self):
        '''dict- k:event_id, v: list of [note_id, x_cordinate, y_cordinate, notification_range]'''
        event_id = 1
        for note_id in self.note_dict:
            for _ in range(r.randint(1,5)): # #no. of event per note
                x_cordinate = r.uniform(-180,180)
                y_cordinate = r.uniform(-90,90)
                ntf_range = r.randint(1,20)
                self.event_dict[event_id] = [note_id,x_cordinate, y_cordinate,ntf_range]
                event_id += 1
    
    def create_comment_dict(self):
        '''dict k: comment_id , v: list of [note_id, commenter_id, text]'''
        #creation of randomly generated sample of notes to be commented from total
        sample_note_list = r.sample(range(1,self.note_count+1),self.note_count) 
        comment_id = 1
        for note_id in sample_note_list:
            for comment_count in range(1,r.randint(1,10)):   #no. of comments per 
                if self.note_dict[note_id][-1] == 'public':
                    commenter_id = r.randint(1,self.users_count)
                else:
                    user_id = self.note_dict[note_id][0]
                    if user_id in self.friend_dict:
                        commenter_id = r.choice(self.friend_dict[user_id])
                text = 'wfev'
                self.comment_dict[comment_id] = [note_id, commenter_id, text]
                comment_id += 1
