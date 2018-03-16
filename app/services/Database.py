import psycopg2


class Database(object):

    def __init__(self):
        self.conn = psycopg2.connect(database="postgres",
                user="postgres",
                password="Shadyridge11$%",
                host="127.0.0.1",
                port="5432")
        self.cur = self.conn.cursor()

    def get_users(self):
        self.cur.execute('''SELECT * FROM users;''')
        return (self.cur.fetchall())

    def add_user(self, name, email, password, group):

        self.cur.execute('''INSERT INTO users
        (name, email, password, group)
        VALUES('{}', '{}', '{}' ,'{}');
        '''.format(name, email, password, group))

        self.conn.commit()

    def get_group(self, group):
        self.cur.execute('''SELECT name FROM users
                        WHERE team='{}' '''.format(group))
        return(self.cur.fetchall())





