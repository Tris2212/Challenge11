string_input = input('Input String: ')
validate = ['SELECT', 'UPDATE', 'DELETE', 'INSERT INTO', 'CREATE DATABASE', 'ALTER DATABASE', 'CREATE TABLE', 'ALTER TABLE', 'DROP TABLE', 'CREATE INDEX', 'DROP INDEX']
if any(ext in string_input for ext in validate):
    print('Invalid string. It contains MYSQL commands. ' + string_input)
else:
    print('Valid string.')