import datetime

f = open('lastest.log', 'wt', encoding='UTF-8')
f.close()


def time():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    return(f'[{time}]')


def info(text, func='root'):
    f = open('lastest.log', 'at', encoding='UTF-8')
    data = time() + ' [' + func + ']' + " [?] " + text
    print(data)
    f.write(data + '\n')
    f.close()


def warn(text, func='root'):
    f = open('lastest.log', 'at', encoding='UTF-8')
    data = time() + ' [' + func + ']' + " [!] " + text
    print(data)
    f.write(data + '\n')
    f.close()


def cmd(command, user, guild):
    f = open('lastest.log', 'at', encoding='UTF-8')
    data = '{0} @{1} used the command "{2}" on the server "{3}"'.format(
        time(), user, command, guild)
    print(data)
    f.write(data + '\n')
    f.close()
