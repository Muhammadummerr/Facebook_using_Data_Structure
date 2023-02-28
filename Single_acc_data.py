class AVL_TREE:
    def __init__(self):
        self.root = None
        # self.menu()
    def add(self,node):
        if self.root  is not None:
            root = self.root
            while root !=None:
                if node.id <= root.id:
                    if root.left == None:
                        root.left = node
                        return self.backtracking(self.root,0,None)
                    else:
                        root = root.left
                else:
                    if root.right == None:
                        root.right = node
                        return self.backtracking(self.root,1,None)
                    else:
                        root = root.right
        else:
            return node
    def right_right_rotation(self,root,parent_node):
        temp2 = parent_node
        temp = root.right.left
        if parent_node != None:
            parent_node.right= root.right
        else:
            temp2 = root.right
        root.right.left = root
        root.right = temp
        return temp2
    def left_left_rotation(self,root,parent_node):
        print(root,root.left,root.right)
        temp = root.left.right
        temp2 = parent_node
        if parent_node !=None:
            parent_node.left = root.left
        else:
            temp2 = root.left
        root.left.right = root
        root.left = temp
        return temp2

    def backtracking(self,root,flag,parent_node = None):
        if root is None:
            return
        if flag ==0:
            self.backtracking(root.left,0,root)
        elif flag ==1:
            self.backtracking(root.right,1,root)
        else:
            self.backtracking(root.left,None,root)
            self.backtracking(root.right,None,root)
        bf = self.balancing_factor(root)
        # print(root.id,bf)
        if bf >1 or bf<-1:
            if bf <0:
                if root.right !=None:
                    bf_of_right_of_root = self.balancing_factor(root.right)
                    if bf_of_right_of_root <0:
                        return  self.right_right_rotation(root,parent_node)
                    else:
                        temp = root.right
                        root.right = temp.left
                        temp.left= root.right.right
                        root.right.right = temp 
                        return  self.right_right_rotation(root,parent_node)
            if bf >0:
                if root.left !=None:
                    bf_of_left_of_root = self.balancing_factor(root.left)
                    if bf_of_left_of_root >0:
                        return self.left_left_rotation(root,parent_node)
                    else:
                        temp = root.left
                        root.left= temp.right
                        temp.right = root.left.right
                        root.left.left = temp
                        return self.left_left_rotation(root,parent_node)  
        return root
    def delete(self,root,node):
        parent_node= None
        while True:
            if root.id>node.id:
                parent_node = root
                root = root.left
            elif root.id<node.id:
                parent_node = root
                root = root.right
            else:
                if root.left == None and root.right == None:
                    if parent_node == None:
                        self.root = None
                    elif parent_node.left == root:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    break
                elif root.left ==None or root.right== None:
                    if root.left!=None:
                        temp = root.left
                    else:
                        temp = root.right
                    if parent_node==None:
                        self.root = temp
                    else:
                        if parent_node.left == root:
                            parent_node.left = temp
                        else:
                            parent_node.right =  temp
                    break
                else:
                    try :
                        temp = root.left
                        while temp.right!=None:
                            if temp.right.right !=None:
                                temp = temp.right
                            else:
                                temp2 =temp.right
                                temp.right = None
                                temp = temp2
                                break
                        temp.right = root.right
                        # temp.left = root.left
                    except:
                        temp = root.right
                        while temp.left!=None:
                            if temp.left.left !=None:
                                temp = temp.left
                            else:
                                temp2 =temp.left
                                temp.left = None
                                temp = temp2
                                break
                        temp.left = root.left
                        # temp.right = root.right
                    if parent_node !=None:
                        if parent_node.left == root:
                            parent_node.left = temp
                        elif parent_node.right == root:
                            parent_node.right = temp
                    else:
                        self.root = temp
                    break
        return self.backtracking(self.root,None,root)
                    

    def in_order(self,root):
        if root == None:
            return
        self.in_order(root.left)
        # print(root.id,end='==>')
        self.in_order(root.right)
    def level_traversal(self,root):
        lst = [root]
        while len(lst) !=0:
            temp = lst.pop(0)
            if temp.left is not None :
                lst.append(temp.left)
            if temp.right is not None:
                lst.append(temp.right)
            print(temp.name)

    def balancing_factor(self,root):
        return self.height(root.left)-self.height(root.right)
    def height(self,root):
        if root is None:
            return 0
        else:
            return 1+max(self.height(root.left),self.height(root.right))
    def menu(self):
        while True:
            print('\n')
            if self.root !=None:
                print('root = ',self.root.id)
            else:
                print(self.root)
            task = input('Enter 1 to add')
            if task =='1':
                self.root = self.add(node(int(input('enter number'))))
                # self.in_order(self.root)
                self.level_traversal(self.root)
            elif task == '2':
                self.root = self.delete(self.root,int(input('Enter number to delete')))
                self.in_order(self.root)
                self.level_traversal(self.root)
            else:
                pass
class node :
    def __init__(self,userid,username,name,age,bio,location):
        self.id = userid
        self.username = username
        self.name = name
        self.age = age
        self.bio = bio
        self.location = location
        self.left= None
        self.right = None
        self.next = None
class node_for_posts:
    def __init__(self,content,comment,likes,time,userid):
        self.content = content
        self.likes = likes
        self.comment = comment
        self.time = time
        self.userid = userid
        self.next = None
class queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self,node):
        node.next = self.tail
        self.tail= node
    def pop(self):
        if self.isnull():
            return None
        temp = self.head
        self.head = temp
        return temp
    def isnull(self):
        if self.head == None:
            return True
        return False
class linked_list :
    def __init__(self):
        self.top = None
    def add_at_start(self,node):
        node.next = self.top
        self.top = node
    def remove_from_start(self):
        temp = self.top
        self.top = self.top.next
        return temp
# from stack.py import stack
class messages_node:
    def __init__(self,sender,message,status,deleted,time):
        self.message = message
        self.sender = sender
        self.seen_status = status
        self.delete_status = deleted
        self.time = time
        self.next = None
class linked_list_for_msgs:
    def __init__(self):
        self.top = None
        # self.menu()
    def push(self,node):
        node.next = self.top
        self.top = node
    def pop(self):
        temp = self.top
        self.top = self.top.next
        return temp
    def isNull(self):
        if self.top == None:
            return True
        return False
    
class stack:
    def __init__(self):
        self.container = linked_list_for_msgs()
        # self.menu()
    def push(self,node):
        self.container.push(node)
    def pop(self):
        if self.container.isNull():
            print("NO MESSAge")
            return
        return self.container.pop()
    def isNull(self):
        if self.container.isNull():
            return True
        return False
    def menu(self):
        while True:
            task = input("enter 1 to add \n 2 to display")
            if task == "1":
                self.push(messages_node())
            elif task == "2":
                print(self.pop())
import mysql.connector
from mysql.connector import Error
import datetime
import re
import getpass
from collections import deque
def connection_creator(hostname,username,password):
    connection = None
    try:
        connection = mysql.connector.connect(host = hostname,user = username,password=password)
        print("connection to MYSQL is successfull")
    except Error as err:
        print("The error ",{err} ," occured")
    return connection
def create_database(connection ,query):
    mycursor = connection.mycursor()
    try:
        mycursor.execute(query)
        print("Database created")
    except Error as err:
        print(f"The error '{err}' occurred")
    
class Account:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost" ,username="root" ,passwd="imranfrommoradabad231321", db = "FacebookDatabase")
        self.mycursor = self.db.cursor(buffered=True)
        while True:
            self.signupANDsingninpage()
    def signupANDsingninpage(self):
        task = int(input("WELCOME TO FACEBOOK\n 1.press 1 to sign in \n 2.press 2 to sign up "))
        if task == 1:
            self.create_account_method()
        elif task == 2:
            self.login_method()
    def create_account_method(self):
        self.id =None
        self.name = self.set_name()
        self.username = self.set_username()
        self._passwrod = self.set_password()
        self.date_of_birth = self.set_date_of_birt()
        print(self.date_of_birth,10000)
        self.age  = self.calculate_age(self.date_of_birth)
        self.bio = self.set_bio()
        self.location = self.set_location()
        print(self.username,self.name,self._passwrod,self.date_of_birth,self.age,self.bio,self.location)
        self.mycursor.execute("DESCRIBE accounts_data")
        for i in self.mycursor:
            print(i)	
        self.mycursor.execute(" INSERT INTO accounts_data (username ,name ,password ,dob ,age,bio ,location )  VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.username,self.name,self._passwrod,self.date_of_birth,self.age,self.bio,self.location));
        self.db.commit()
        # id_query= "SELECT userid FROM accounts_data WHERE username = "+ "'"+str(self.username)+"'"
        # self.id = None
        # print(self.mycursor.execute(id_query))
        # self.db.commit()
        id_query = "SELECT userid FROM accounts_data WHERE username = %s"
        username = (self.username,)
        self.mycursor.execute(id_query, username)
        result = self.mycursor.fetchone()
        if result is not None:
            self.userid = result[0]
            print(self.userid)
            self.db.commit()
        friends_request_table_creation_query = "CREATE TABLE "+str(self.userid)+"_friends_request_notifications (userid int,seen_status BOOLEAN)"
        self.mycursor.execute(friends_request_table_creation_query)
        self.db.commit()
        # self.mycursor.execute("SELECT * FROM accounts_data")
        # print(self.mycursor)
        friendship_table_creation_query = "CREATE TABLE "+str(self.userid)+"_friendships (userid int,date_of_friendship DATE)"
        self.mycursor.execute(friendship_table_creation_query)
        self.db.commit()
        #-------------------------
        newsfeed_table_creation_query = "CREATE TABLE "+str(self.userid)+"_newsfeed (post_id int,user_id int)"
        self.mycursor.execute(newsfeed_table_creation_query)
        self.db.commit()
        #------------------------------------
        self.mycursor.execute("SHOW TABLES")
        tables = self.mycursor.fetchall()

# iterate through all tables and print column names
        for table in tables:
            self.mycursor.execute(f"DESCRIBE {table[0]}")
            columns = self.mycursor.fetchall()
            print(f"Table Name: {table[0]}")
            for column in columns:
                print(column[0])
        # self.friends = True
        # self.block_acc = True
        # self.messages = True
        # self.notifications = True
    def friend_request_notifications(self):
        table_name = str(self.id)+"_friends_request_notifications"
        query = "SELECT userid FROM "+str(table_name)+" WHERE seen_status = 0"
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        if result is not None:
            requesters_ids = linked_list()
            for i in result:
                query = "SELECT username,name,age,bio,location FROM accounts_data WHERE userid = "+str(i[0])
                self.mycursor.execute(query)
                node_info = self.mycursor.fetchall()
                for account_info in node_info:
                    temp_node= node(i[0],account_info[0],account_info[1],account_info[2],account_info[3],account_info[4])
                requesters_ids.add_at_start(temp_node)
            while requesters_ids.top != None:
                requesters_node = requesters_ids.remove_from_start()
                requesters_id = requesters_node.id
                # query = "SELECT username FROM accounts_data WHERE userid = "+str(requesters_id)
                # self.mycursor.execute(query)
                # result = self.mycursor.fetchone()
                username = requesters_node.name
                # self.db.commit()
                task_accept_friend_request = input(f"{username} sent you a friend request\nwant to accept it press 1\nwant to delete it press 2\n want to mark as read press 3")
                if task_accept_friend_request == "1":
                    self.add_users_in_friends_tabe_of_each_other(requesters_id,self.id)
                    # self.mark_friend_request_as_read(requesters_id,table_name)
                    self.mycursor.execute(f"DELETE  FROM {table_name} WHERE userid = {requesters_id}")
                    self.db.commit()

                    # self.mycursor.execute("SELECT * FROM "+str(table_name))
                    # for i in self.mycursor:
                    # 	print(i)
                    # mycursor.execute(f"SELECT * FROM "+str(table_name))
                    # for i in mycursor:
                    # 	print(i)
                elif task_accept_friend_request == "2":
                    self.delete_request_from_table(table_name,requesters_id)
                    # self.mycursor.execute(f"DELETE  FROM {table_name} WHERE userid = {requesters_id}")
                    # self.db.commit()
                else:
                    pass
    def delete_request_from_table(self,table_name,requesters_id):
        self.mycursor.execute(f"DELETE  FROM {table_name} WHERE userid = {requesters_id}")
        self.db.commit()
        return
    def mark_friend_request_as_read(self,requesters_id,table_name): 
        query = "UPDATE "+str(table_name)+" SET seen_status = %s WHERE userid = %s"
        user_id = requesters_id
        values = (True, user_id)
        self.mycursor.execute(query,values)
        self.db.commit()
    def add_users_in_friends_tabe_of_each_other(self,other_user_id,my_id):
        table_1 = str(other_user_id)+"_friendships"
        table_2 = str(my_id)+"_friendships"
        # query_1 = "INSERT INTO "+str(table_1)+"(userid,date_of_friendship) VALUES(%s,%s)",(my_id,datetime.date.today().isoformat());
        # query_2 = "INSERT INTO "+str(table_2)+"(userid,date_of_friendship) VALUES(%s,%s)",(other_user_id,datetime.date.today().isoformat());
        self.mycursor.execute("INSERT INTO "+str(table_1)+"(userid,date_of_friendship) VALUES(%s,%s)",(my_id,datetime.date.today().isoformat()));
        self.db.commit()
        self.mycursor.execute("INSERT INTO "+str(table_2)+"(userid,date_of_friendship) VALUES(%s,%s)",(other_user_id,datetime.date.today().isoformat()));
        self.db.commit()
        return
    def login_method(self):
        while True:
            username= input("Enter your username")
            _password = getpass.getpass(prompt="enter password")
            username = "'"+ str(username) + "'"
            query = "SELECT password ,userid FROM accounts_data WHERE username = "+ str(username)
            # print(query)
            self.mycursor.execute(query)
            # for i in self.mycursor:
            # 	if i == ('mer23',):
            # 		print(True)
            # 	else:
            # 		print(False)
            # print(self.mycursor.fetchall(),999)
            result = self.mycursor.fetchone()
            
            # print(self.mycursor)
            # result = self.mycursor.fetchall()
            # print(result)
            # print(self.mycursor.execute("SELECT TRUE FROM accounts_data WHERE username = {username}"))
            if result:
                # index_of_username = Account.usernames_list.index(username)
                # print(index_of_username)
                __password_from_db = result[0]
                if __password_from_db== _password:
                    print("you are logged in")
                    
                    self.id = result[1]
                    self.friends_list = AVL_TREE()

                    query = f"SELECT userid FROM {str(self.id)}_friendships"
                    self.mycursor.execute(query)
                    friends_id = [i[0] for i in self.mycursor.fetchall()]
                    self.db.commit()
                    for i in friends_id:
                        # print(i,friends_id)
                        query2 = "SELECT username,name,age,bio,location FROM accounts_data WHERE userid =" +str(i)
                        self.mycursor.execute(query2)
                        friends_info = self.mycursor.fetchall()
                        for friends_info in friends_info:
                            pass
                            # print(friends_info)
                        # friends_info = friends_info.fetchall()
                            temp_node = node(i,friends_info[0],friends_info[1],friends_info[2],friends_info[3],friends_info[4])
                            self.friends_list.root = self.friends_list.add(temp_node)
                    # print(self.friends_list.root)
                    # self.friends_list.level_traversal(self.friends_list.root)
                    self.display_friends()
                    table_name = str(self.id)+"_friends_request_notifications"
                    query = f"SELECT * FROM {str(table_name)}"
                    self.mycursor.execute(query)
                    # for i in self.mycursor:
                        # print(i)
                    self.db.commit()
                    self.friend_request_notifications()
                    self.messages_notifications()
                    self.main_page_of_logged_in_account()
                    # print(self.id)
                    break
                else:
                    print(__password_from_db,_password)
                    print("Incorrect password")
            else:
                print("Email Doesn't exist")
    def messages_notifications(self):
        query = f"SELECT sender_id FROM messages WHERE reciever_id = {str(self.id)} AND seen_status = 0"
        self.mycursor.execute(query)
        messages_senders = self.mycursor.fetchall()
        total_messages = []
        for ids in messages_senders:
            if ids not in total_messages:
                total_messages.append(ids)
        if len(total_messages)>0:
            print(f"You have {len(total_messages)} new messages")
            try:
                task = input("Do you want see them?y/n")
                if task == "Y" or task == "y":
                    for i in total_messages:
                        self.print_chat(i[0],False)
                        self.mark_messages_as_read(i[0])
                        reply = input("Do you want to reply?y/n")
                        if reply =="Y" or reply == "y":
                            self.send_message(i[0])
                        else:
                            pass
                else:
                    pass
            except Exception as e:
                print(e)
    def creat_post(self,post_content):
        try : 
            query = "INSERT INTO posts (user_id,post_content,likes_count,comments_count,time) VALUES(%s,%s,%s,%s,%s)"
            self.mycursor.execute(query,(self.id,post_content,0,0,datetime.datetime.now()))
            self.db.commit()
            query = "SELECT post_id FROM posts WHERE post_content = `{}`".format(post_content)
            self.mycursor.execute(query)
            self.mycursor.fetchall()
            for id in self.mycursor:
                print(id)
                return id[0]
        except Exception as e:
            print(e)
        
        
        
    def add_post_to_friends_newsfeed(self,postid):
        try :
            print(postid)
            query = f"SELECT userid FROM {str(self.id)}_friendships"
            self.mycursor.execute(query)
            users = self.mycursor.fetchall()
            users.append((self.id,))
            for user in users:
                table_name = str(user[0])+"_newsfeed"
                query = f"INSERT INTO "+str(table_name) +" (post_id,user_id) VALUES(%s,%s)"
                self.mycursor.execute(query,(postid,self.id))
                self.db.commit()
        except Exception as e:
            print(e)

    def user_node_creator(self,id):
        query2 = "SELECT username,name,age,bio,location FROM accounts_data WHERE userid =" +str(id)
        self.mycursor.execute(query2)
        friends_info = self.mycursor.fetchall()
        for friends_info in friends_info:
            pass
            print(friends_info)
        # friends_info = friends_info.fetchall()
            temp_node = node(id,friends_info[0],friends_info[1],friends_info[2],friends_info[3],friends_info[4])
        return temp_node
    def display_friends(self):
        # root = self.friends_list.root
        print("Friends List")
        try:
            self.friends_list.level_traversal(self.friends_list.root)
        except:
            print("NO Friends Yet")
    def main_page_of_logged_in_account(self):
        print("\t\t\tWelcome to Facebook")
        print("You can perform following operations\n1.search People\t\t\t2.message People\t\t\t3.Post Something")
        task = int(input())
        
        # print(result)
        # print(type(result))
        
                # print(account_id)
        if task == 1:
            search = input("Enter people name:")
            query = "SELECT username FROM accounts_data"   ##make func to send friend_request
            self.mycursor.execute(query)
            result_username = [username[0] for username in self.mycursor.fetchall()]
            self.db.commit()
            for i in result_username:
                if search in i :
                    print("username = ",i)
                    query3 = "SELECT userid FROM accounts_data WHERE username = %s"
                    self.mycursor.execute(query3,(i,))
                    account_id = self.mycursor.fetchone()[0]
                    query4 = "SELECT TRUE FROM "+str(self.id)+"_friendships WHERE userid ="+str(account_id) 
                    self.mycursor.execute(query4)
                    try : 
                        answer_of_is_friend_or_not = self.mycursor.fetchone()[0]
                        self.db.commit()
                    except:
                        answer_of_is_friend_or_not = 0
                    friend_status = lambda answer_of_is_friend_or_not: "Friend" if answer_of_is_friend_or_not == 1 else "Not Friend"
                    profile_see_input = input("Do you want to see this profile?y/n")
                    try :

                        if profile_see_input == "Y" or profile_see_input == "y":
                            query2 = "SELECT name,bio,location,age,dob FROM accounts_data WHERE username = %s"
                            self.mycursor.execute(query2, (i,))
                            result = self.mycursor.fetchall()[0]
                            # print(result)
                            print(f"Name :{result[0]}\t\tFriendship Status: {friend_status(answer_of_is_friend_or_not)}\nD.O.B:{result[4]}\t\tAge: {result[3]}\nLocation:{result[2]}\t\tBio: {result[2]}")
                            self.db.commit()
                        else:
                            pass
                    except Exception as e:
                        print(e)
                    if answer_of_is_friend_or_not ==0:
                        print("Do You want to send him a friend Request?")
                        task_send_friend_request = input('Enter 1 to send friend request\nEnter 2 to see next \n enter 3 to exit' )
                        if task_send_friend_request == '1':
                            
                            id_query = "SELECT userid FROM accounts_data WHERE username = %s"
                            username = (i,)
                            self.mycursor.execute(id_query, username)
                            result = self.mycursor.fetchone()
                            if result is not None:
                                userid = result[0]
                                print(userid)
                                self.db.commit()
                            else:
                                print("error in userid name")
                            table_name = str(userid)+"_friends_request_notifications"
                            try:
                                friend_request_send_check_query = f"SELECT TRUE FROM {str(table_name)} WHERE userid = %s"
                                friend_request_send_check_username = (self.id,)
                                self.mycursor.execute(friend_request_send_check_query, friend_request_send_check_username)
                                friend_request_send_check_answer = self.mycursor.fetchone()
                                self.db.commit()
                                friend_request_recieve_check_query = f"SELECT TRUE FROM {str(self.id)}_friends_request_notifications WHERE userid = %s"
                                friend_request_recieve_check_username = (userid,)
                                self.mycursor.execute(friend_request_recieve_check_query, friend_request_recieve_check_username)
                                friend_request_recieve_check_answer = self.mycursor.fetchone()
                                self.db.commit()
                                # print(friend_request_recieve_check_answer,friend_request_send_check_answer,999999999)
                            except:
                                pass
                            # send_friend_request_query = 
                            if friend_request_send_check_answer ==None and friend_request_recieve_check_answer ==None:
                                self.mycursor.execute("INSERT INTO "+str(table_name)+" (userid,seen_status) VALUES(%s,%s)",(self.id,False))
                                self.db.commit()
                            elif friend_request_recieve_check_answer ==(1,):
                                print(i,'already sent you request\nYou want to accept it?\npress Y for YES or N for No')
                                task = input('')
                                if task == 'Y' or task == 'y':
                                    try:
                                        self.add_users_in_friends_tabe_of_each_other(userid,self.id)			# copy acceptin request addin in friends table and removin request from notification table.
                                        self.delete_request_from_table(str(self.id)+"_friends_request_notifications",userid)
                                        self.friends_list.root = self.friends_list.add(self.user_node_creator(userid))
                                        self.display_friends()
                                        print("Successfully made your friend")
                                    except:
                                        print("Error ")
                                elif task == 'n' or task == 'N':
                                    pass
                                else:
                                    print('incorrect input')
                            elif friend_request_send_check_answer == (1,):
                                print("Friend Request already sent")
                            self.mycursor.execute("SELECT * FROM "+str(table_name))
                            for i in self.mycursor:
                                print(i)
                            self.db.commit()
                        elif task == "2":
                            pass
                        elif task == "3":
                            return
                    else:
                        print(i," is already your friend")
        elif task == 2:
            # query_for_old_messages = f"SELECT message FROM messages WHERE (senderid = {str(userid)} AND recieverid ={str(self.id)} ) OR (senderid = {str(self.id)} AND recieverid = {str(userid)}) ORDER BY time ASC"
            self.send_message(account_id)
            self.print_chat(account_id,True)
            self.mark_messages_as_read(account_id)
        elif task == 3:
            while True:
                print("What do you think?Type here....")
                post_content= input()
                if post_content == '':
                    print('Post can be Empty..')
                else:
                    postid = self.creat_post(post_content)
                    print(postid,999999999999)
                    self.add_post_to_friends_newsfeed(postid)
                    break
        elif  task == 4:
            print(3242334)
            table_name = str(self.id) + '_newsfeed'
            query = "SELECT post_id FROM `{}`".format(table_name)
            self.mycursor.execute(query)
            results = self.mycursor.fetchall()
            for post_id in results:
                print(post_id)
                query = "SELECT user_id,post_content,likes_count,comments_count,time FROM posts WHERE post_id = "+str(post_id[0])
                self.mycursor.execute(query)
                result = self.mycursor.fetchall()
                for result in result:
                    print(result)
    def send_message(self,account_id):
        message= input("Enter your message")
        # query = "INSERT INTO messages(sender_id,reciever_id,message,time,deleted,seen_status) VALUES(%s,%s,%s,%s,%s,%s)"
        self.mycursor.execute("INSERT INTO messages(sender_id,reciever_id,message,time,deleted,seen_status) VALUES(%s,%s,%s,%s,%s,%s)",(self.id,account_id,message,datetime.datetime.now(),0,0));
        self.db.commit()
    def remove_from_friends(self,userid):
        table_name1= str(self.id)+"_friendships"
        table_name2 = str(userid)+"_friendships"
        query1 = f"DELETE FROM {table_name1} WHERE userid= {str(userid)}"
        query2 = f"DELETE  FROM {table_name2} WHERE userid= {str(self.id)}"
        self.mycursor.execute(query1)
        self.mycursor.execute(query2)
        self.my.commit()
        self.friends_listroot = self.friends_list.delete(userid)
        return 
    def mark_messages_as_read(self,userid):
        # query ="UPDATE TABLE messages SET seen_status = 1 where sender_id = %s"
        # self.mycursor.execute(query,(userid,))
        # self.db.commit()
        query_for_updating_seen_status = f"UPDATE messages SET seen_status = 1 WHERE seen_status = 0 AND sender_id = {str(userid)} AND reciever_id = {str(self.id)}"
        self.mycursor.execute(query_for_updating_seen_status)
        self.db.commit()
    def print_chat(self,userid,flag):
        sender_query = f"SELECT sender_id FROM messages WHERE  (sender_id = {str(userid)} AND reciever_id ={str(self.id)} ) OR (sender_id = {str(self.id)} AND reciever_id = {str(userid)}) ORDER BY time DESC"
        messages_query = f"SELECT message FROM messages WHERE  (sender_id = {str(userid)} AND reciever_id ={str(self.id)} ) OR (sender_id = {str(self.id)} AND reciever_id = {str(userid)}) ORDER BY time DESC"
        seen_status_query = f"SELECT seen_status FROM messages WHERE  (sender_id = {str(userid)} AND reciever_id ={str(self.id)} ) OR (sender_id = {str(self.id)} AND reciever_id = {str(userid)}) ORDER BY time DESC"
        deleted_status_query = f"SELECT deleted FROM messages WHERE  (sender_id = {str(userid)} AND reciever_id ={str(self.id)} ) OR (sender_id = {str(self.id)} AND reciever_id = {str(userid)}) ORDER BY time DESC"
        time_query = f"SELECT time FROM messages WHERE  (sender_id = {str(userid)} AND reciever_id ={str(self.id)} ) OR (sender_id = {str(self.id)} AND reciever_id = {str(userid)}) ORDER BY time DESC"

        # self.mycursor = self.db.cursor(buffered=True)
        self.mycursor.execute(sender_query)
        sender = self.mycursor.fetchall()
        self.mycursor.execute(messages_query)
        message = self.mycursor.fetchall()
        self.mycursor.execute(seen_status_query)
        seen_status = self.mycursor.fetchall()
        self.mycursor.execute(deleted_status_query)
        deleted_status = self.mycursor.fetchall()
        self.mycursor.execute(time_query)
        time = self.mycursor.fetchall()
        # print(self.mycursor)
        # self.mycursor.fetchall()
        # print(self.mycursor.rowcount,1111111111,)
        messages_history_stack = stack()
        # print(self.mycursor)
        i = 0
        for i in range(self.mycursor.rowcount):
            try :
                # print(self.mycursor.rowcount)
                temp_message_node = messages_node(sender[i][0],message[i][0],seen_status[i][0],deleted_status[i][0],time[i][0])
                # print(temp_message_node.message,temp_message_node.sender)
                messages_history_stack.push(temp_message_node)
                # print(messages_history_stack.peek())
                # print(messages_history_stack.container.top.message)
            except Exception as e:
                print(e)
                break
        # flag = False
        if messages_history_stack.isNull():
            print("No sms")
        else:
            while messages_history_stack.isNull() !=True:
                temp = messages_history_stack.pop()
                # print(temp.delete_status,type(temp.delete_status))
                # print(temp.sender,type(temp.sender))
                if temp.seen_status == 0 and flag == False :
                        print("---------------new message---------------------")
                        flag = True
                if temp.sender == self.id:
                    if temp.delete_status == 0 :
                        print("YOU: "+temp.message)
                    else: 
                        print(self.delete_status,type(self.delete_status))
                        print("YOU: " +"\033[3m\This message was deleted.033[0m")
                else:
                    query_for_account_name = "SELECT name FROM accounts_data WHERE userid = %s"
                    self.mycursor.execute(query_for_account_name,(temp.sender,))
                    username = self.mycursor.fetchone()[0]
                    self.db.commit()
                    if temp.delete_status == 0 :
                        print(f"{str(username)}: {temp.message}")
                    else: 
                        print(f"{str(username)}:" +"\033[3m\This message was deleted.033[0m")
                    # print(f"{str(username)}: {temp.message}")
        self.mark_messages_as_read(temp.sender)


        self.db.commit()
    def input_of_date_of_birt(self): #To take and match date input.If true return it
        while True:
            date_of_birt = input("Enter Your Date Of Birt:(in format --- day/mont/year")
            flag = re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}',date_of_birt)
            if flag:
                return date_of_birt
            else:
                print("Incorrect format")
                continue
    def set_date_of_birt(self):	# set dob and age according to it
        date_of_birth = self.input_of_date_of_birt()
        self.age = self.calculate_age(date_of_birth)
        return date_of_birth
    def calculate_age(self,date_of_birt): #Calculate age
        print(date_of_birt,99)
        todays_date = datetime.datetime.today().strftime('%d/%m/%Y')
        if int(date_of_birt[3:5])< int(todays_date[3:5]) and int(date_of_birt[0:2])>= int(todays_date[0:2]):
            return int(todays_date[6:10]) -int(date_of_birt[6:10])
        else:
            return int(todays_date[6:10]) -int(date_of_birt[6:10])-1
    def set_username(self):
        while True:
            username = input("Enter username:")
            usernnames_list = self.mycursor.execute("SELECT username FROM accounts_data ")
            if usernnames_list == None:
                usernnames_list = []
            else:
                usernnames_list = list(usernnames_list)
            if username != usernnames_list:
                return  username
                # Account.usernames_list.append(self.username)
                # break
            else:
                print("username already exists!")
    def set_password(self):
        while True:
            _password = getpass.getpass(prompt="Enter password:") #display * problem1
            print(_password)
            _temp = getpass.getpass(prompt="Again enter password:")
            print(_temp)
            if len(_password) >=4 and str(_password)== str(_temp):
                
                # Account._passwords_list.append(_password)
                return _password
            else:
                print("try again")
    def information_display(self):
        print("Name = ",self.name)
        print("Dob = ",self.date_of_birth)
        print("Age = ",self.age,"Years")
    def set_name(self):
        name = input("Enter Name:")
        return name
    def set_bio(self):
        bio = input("Enter Your bio:")
        return bio
    def set_location(self):
        location = input("Enter Your City:")
        return location
a = Account()
# a.information_display()
# connection = connection_creator("localhost","root","imranfrommoradabad231321")
# create_database_query = "CREATE DATABASE FacebookDatabase"
# create_database(connection, create_database_query)
db = mysql.connector.connect(host="localhost" ,username="root" ,passwd="imranfrommoradabad231321", db = "FacebookDatabase")
mycursor = db.cursor(buffered=True)

# mycursor.execute("ALTER TABLE accounts_data	RENAME dob to  dob VALUES('01/06/1999')") #used to delete table
# mycursor.execute("DROP TABLE accounts_data")
# db.commit()
# mycursor.execute("DROP TABLE none_friends_request_notifications")
# db.commit()
# mycursor.execute(" CREATE TABLE accounts_data (userid int AUTO_INCREMENT PRIMARY KEY ,username varchar(50) NOT NULL,name varchar(50) NOT NULL,password varchar(50) NOT NULL,dob varchar(25),age int(4),bio varchar(50),location char(25))" )
# mycursor.execute("ALTER TABLE accounts_data MODIFY COLUMN dob  , MODIFY dob varchar(25)")
# mycursor.execute("DROP TABLE messages")
# mycursor.execute(" CREATE TABLE messages (sender_id int NOT NULL,reciever_id int NOT NULL,message varchar(500),time DATETIME,deleted  BOOLEAN NOT NULL,seen_status BOOLEAN NOT NULL )" )
# mycursor.execute("CREATE TABLE posts (post_id int  AUTO_INCREMENT PRIMARY KEY ,user_id int NOT NULL,post_content varchar(500) NOT NULL,likes_count int NOT NULL,comments_count int NOT NULL,time DATETIME NOT NULL)")
mycursor.execute("SELECT * FROM  posts")
for i in mycursor:
    print(i)
# tables = mycursor.fetchall()

# # Drop each table in the list
# for table in tables:
#     mycursor.execute(f"DROP TABLE {table[0]}")
#     print(f"Dropped table {table[0]}")

# # Commit the changes
# db.commit()

# Close the database connection
# db.close()
# db.commit()
# mycursor.execute("SELECT userid FROM  accounts_data WHERE userid > 0")
# db.connect(buffered =False)
# mycursor.fetchall()
# print(mycursor)
# for i in mycursor:
    # try:
        # print(i)
        # newsfeed_table_creation_query = "CREATE TABLE "+str(i[0])+"_newsfeed (post_id int,user_id int)";
        # mycursor.execute(newsfeed_table_creation_query)
        # db.commit()
    # except Exception as a:
    #     print(a)
# newsfeed_table_creation_query = "CREATE TABLE 5_newsfeed (post_id int,user_id int)";
# mycursor.execute(newsfeed_table_creation_query)
# db.commit()
# mycursor.execute("TRUNCATE TABLE  messages")
# mycursor.execute("DELETE FROM  1_friends_request_notifications WHERE userid = 3")
# mycursor.execute("SELECT * FROM  1_friends_request_notifications")
# for i in mycursor:
#     print(i)
mycursor.execute("DESCRIBE posts")

# fetch all the table names
tables = mycursor.fetchall()

# print the table names
for table in tables:
    print(table)