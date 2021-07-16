import unittest
import pytest

from mypackage.CRUD import *

userName=os.environ['MYSQL_USER']
pswd=os.environ['MYSQL_PASSWORD']
hostName=os.environ['MYSQL_HOST'] 
portSel= os.environ['MYSQL_PORT']
databaseName='users'
values=["a","b","c","testing3@testing.testing"]
user_name="a"
def test_create_table():
    current_value = create_table(hostName, userName, pswd, portSel)
    expected_value = True

    assert expected_value == current_value

def test_create_table_wrong():
    current_value = create_table(hostName, userName, pswd, "s")
    expected_value = False

    assert expected_value == current_value

def test_insert_user():
    current_value = insert_user(hostName, userName, pswd, databaseName, portSel, values)
    expected_value = True

    assert expected_value == current_value

def test_insert_user_wrong():
    current_value = insert_user("hostName", userName, pswd, databaseName, portSel, values)
    expected_value = False

    assert expected_value == current_value

def test_select_user():
    current_value = select_user(hostName, userName, pswd, databaseName, portSel, user_name)
    expected_value = None

    assert expected_value != current_value

def test_select_user_wrong():
    current_value = select_user(hostName, "userName", pswd, databaseName, portSel, user_name)
    expected_value = False

    assert expected_value == current_value