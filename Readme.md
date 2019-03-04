It is a simple Post api, which take data as POST param. "data" param must contain json


Project Setup:
    
    pipenv shell #open python shell
    pipenv install # install all requirements


Start Project:

    python manage.py runserver


We have used three variable in settings file

    ENCRYPT_KEY => Secret key for encryption and decryption
    ENCRYPT => Enryping returning data
    DECRYPT => Decrypt data send in post

Test1:

    ENCRYPT = False
    DECRYPT = False
    
    POST param:
        data = {"data":"hers is some data"}
        
    Response:
        {"data": "hers is some data"}

Test2:

    ENCRYPT = True
    DECRYPT = False
    POST param:
        data = {"data":"hers is some data"}
        
    Response:
        "Z0FBQUFBQmNmTlZOUC1XT3VnbzBtcWtvQmhUbWo2ODZGU2JNMHdOaXoyR3QyTTU1QVJqMndOZ2RDS09uaF9iSndBUjJBUDcwTWY0M05SUnJxUDB3MTZKRy11Yk9RVnBGSWhNUHBSQ3Ffd2FsdDZ6OWQzall2RWs9"
        
Test3:

    ENCRYPT = False
    DECRYPT = True
    POST param:
        data = Z0FBQUFBQmNmTlZOUC1XT3VnbzBtcWtvQmhUbWo2ODZGU2JNMHdOaXoyR3QyTTU1QVJqMndOZ2RDS09uaF9iSndBUjJBUDcwTWY0M05SUnJxUDB3MTZKRy11Yk9RVnBGSWhNUHBSQ3Ffd2FsdDZ6OWQzall2RWs9
        
    Response:
        {"data":"hers is some data"}



Test4:

    ENCRYPT = True
    DECRYPT = True
    POST param:
        data = Z0FBQUFBQmNmTlZOUC1XT3VnbzBtcWtvQmhUbWo2ODZGU2JNMHdOaXoyR3QyTTU1QVJqMndOZ2RDS09uaF9iSndBUjJBUDcwTWY0M05SUnJxUDB3MTZKRy11Yk9RVnBGSWhNUHBSQ3Ffd2FsdDZ6OWQzall2RWs9
        
    Response:
        Z0FBQUFBQmNmTlhQU250U0x5alRlYk9fLU5OWVhOQXN4WTFPWm5YQUd0MlFqNHZ2M0I1LWJFZW1YN2hlRDRzRjJjbVZZU0g1SERPYXJwQ1QtVktUOWFtM3VnVWdLYVpoSzMzS0gxc1NUZl8zTVV0YTdPQktRSUE9
