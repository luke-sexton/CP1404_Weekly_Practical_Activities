usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
ask_user = input("Please enter your user name: ")
if ask_user in usernames:
    print("Access granted.")
else:
    print("Access denied.")
