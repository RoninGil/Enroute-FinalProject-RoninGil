from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

load_dotenv() #loaded

userName=os.environ['MYSQL_USER']
pswd=os.environ['MYSQL_PASSWORD']
hostName=os.environ['MYSQL_HOST'] 
portSel= os.environ['MYSQL_PORT']
databaseName='users'


# def create_db(hostName, userName, pswd, databaseName, portSel):
#     """This function creates database if inexistent.

#     :param hostname: Host name of DataBase.
#     :type hostname: string
#     :param userName: User name to access DataBase.
#     :type userName: string
#     :param pswd: Password to access DataBase.
#     :type pswd: string
#     :param databaseName: Database name.
#     :type databaseName: string
#     :param portSel: Port active to access DataBase.
#     :type portSel: int

#     """

#     create_db_query=f"CREATE DATABASE IF NOT EXISTS {databaseName}"
#     # Create database
#     try:
#         with connect(host=hostName,user=userName,password=pswd, port=portSel) as connection:
#             with connection.cursor() as cursor:
#                 cursor.execute(create_db_query)
#                 print("Connected 1!")
#                 return True

#     except Error as e:
#         print(e)
#         return False

def create_table(hostName, userName, pswd, portSel):
    """This function creates a user table if inexistent.

    :param hostname: Host name of DataBase.
    :type hostname: string
    :param userName: User name to access DataBase.
    :type userName: string
    :param pswd: Password to access DataBase.
    :type pswd: string
    :param portSel: Port active to access DataBase.
    :type portSel: int

    """


    create_db_query=f"""
    CREATE TABLE IF NOT EXISTS users.user (
        `iduser` INT NOT NULL AUTO_INCREMENT,
        `user_name` VARCHAR(45) NOT NULL,
        `user_address` VARCHAR(45) NOT NULL,
        `user_tel` VARCHAR(45) NOT NULL,
        `user_email` VARCHAR(45) NOT NULL,
        PRIMARY KEY (`iduser`),
        UNIQUE INDEX `iduser_UNIQUE` (`iduser` ASC) VISIBLE,
        UNIQUE INDEX `user_email_UNIQUE` (`user_email` ASC) VISIBLE);
    """
    # Create database
    try:
        with connect(host=hostName,user=userName,password=pswd, port=portSel) as connection:
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
                print("Connected 2!")
                return True

    except Error as e:
        print(e)
        return False

def insert_user(hostName, userName, pswd, databaseName, portSel, values):
    """This function inserts user's data to user table.

    :param hostname: Host name of DataBase.
    :type hostname: string
    :param userName: User name to access DataBase.
    :type userName: string
    :param pswd: Password to access DataBase.
    :type pswd: string
    :param databaseName: DataBase name.
    :type databaseName: string
    :param portSel: Port active to access DataBase.
    :type portSel: int
    :param values: Values to insert on DataBase.
    :type values: array

    """

    insert_data_query="""
    INSERT INTO user (
        user_name,
        user_address,
        user_tel,
        user_email
    ) VALUES (%s, %s, %s, %s)
    """

    print(values)
    try:
        with connect(host=hostName,user=userName,password=pswd,database=databaseName, port=portSel) as connection:
            with connection.cursor() as cursor:
                cursor.execute(insert_data_query, values)
                connection.commit()
                print('CONNECTED 3')
            return True

    except Error as e:
        print(e)
        return False

def select_user(hostName, userName, pswd, databaseName, portSel, user_name):
    """This function selects username obtained from facial recognition.

    :param hostname: Host name of DataBase.
    :type hostname: string
    :param userName: User name to access DataBase.
    :type userName: string
    :param pswd: Password to access DataBase.
    :type pswd: string
    :param databaseName: DataBase name.
    :type databaseName: string
    :param portSel: Port active to access DataBase.
    :type portSel: int
    :param user_name: Name of the person's face recognized by the script.
    :type user_name: string
    

    """


    select_table_query = """
    SELECT *
    FROM user
    WHERE user_name = %s;
    """
    print("USER NAME EN EL SELECT QUERY",user_name)
    try:
        with connect(host=hostName,user=userName,password=pswd,database=databaseName, port=portSel) as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_table_query, (user_name,))
                result = cursor.fetchall()
                for row in result:
                    print('CONNECTED 4')
                    print(row)
                return row

    except Error as e:
        print(e)
        return False
