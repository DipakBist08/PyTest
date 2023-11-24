import pytest
import StringSourcePaclage.Source_String_File as My_File


def UserInfo():
    First_Name = 'Rahul'
    User_Age = 25
    assert First_Name == 'Rahul' and User_Age == 25
