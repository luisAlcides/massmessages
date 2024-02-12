

class NewUserController():
    def __init__(self, user):
        sql_insert_new_user = '''
            INSERT INTO users(name, last_name,username,password,phone, role) 
            VALUES(?,?,?,?,?,?)
        '''