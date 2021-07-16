
CRUD
==================================================

Params
------------------------------

The following params are the ones used in this python file so every function can be connected succesfully to the DB.

* hostName: Host name of the DB. (str)
* userName: User name to access the DB. (str)
* pswd: Password of the DB connection. (str)
* portSel: Number of port selected to access the DB. (int)
* databaseName: Name of the DB to be accessed. This is the DB where the info will be stored. (str)

Special params
------------------------------
* values: Only used in the "insert" query. These are the values retrieved from the GUI, the ones the user registered with. (Array)
* user_name: Only used in the "select" query. This value is the name of the person recognized by the algorithm, it grants access to the info stored in the DB. (str)

Create 'users' table
------------------------------

With this function you create the table inside your selected DB, in case it already exists, this doesn't overwrite your table or create a new one.

.. code-block:: py

    def create_table(hostName, userName, pswd, portSel):
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

First, we find the query, which is a straight mysql query to create a table if inexistent on DB.
There are five columns created with this table: iduser, user_name, user_address, user_tel, user_email.
These are the values that will be used to INSERT and SELECT data from the specified user.

.. code-block:: py

    try:
        with connect(host=hostName,user=userName,password=pswd, port=portSel) as connection:
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
                print("Connected 2!")
                return True

    except Error as e:
        print(e)
        return False
    
With this 'try' block we can be sure that the code won't "break" if the connection fails either because a wrong input was given or any other reason.

Insert data into 'users' table
-----------------------------------

With this function you can insert the data given by the user when registering before the face recognition.

.. code-block:: py

    def insert_user(hostName, userName, pswd, databaseName, portSel, values):
    insert_data_query="""
    INSERT INTO user (
        user_name,
        user_address,
        user_tel,
        user_email
    ) VALUES (%s, %s, %s, %s)
    """
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

This query is used to insert the data gatheres (from the user in the GUI) inside the DB.

Select data from 'users' table
-----------------------------------

Once the info is stored, if the person registered wants to access again, the info provided by him/her will be displayed inside the GUI.

.. code-block:: py

    def select_user(hostName, userName, pswd, databaseName, portSel, user_name):
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

When the facial recognition algorithm gives the name of the person back succesfully, the info gathered in the DB will be displayed.