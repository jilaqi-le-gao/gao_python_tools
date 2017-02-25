import poplib
import os

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

default_path = './data'

def download_attaches(msg):
    for part in msg.walk():
        if not (part.is_multipart()) and not(part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html'):
            open(os.path.join(default_path, part.get_filename()), 'wb').write(part.get_payload(decode=True))


def check_dir():
    if os.path.exists(default_path):
        return True
    else:
        os.mkdir(default_path)
        return True


if __name__ == "__main__":
    email = input('Username:')
    password = input('Password:')
    pop3_server = input('Pop3 server:')
    pop3_port = input('Pop3 port:')
    pop3_port = int(pop3_port)
    
    check_dir()

    server =poplib.POP3_SSL(pop3_server, port=pop3_port)

    server.set_debuglevel(1)

    print(server.getwelcome())

    server.user(email)
    server.pass_(password)

    print('Messages: %s. Size: %s' % server.stat())

    numMessages = len(server.list()[1])
    for i in range(numMessages):
        try:
            resp, lines, octets = server.retr(i+1)
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            msg = Parser().parsestr(msg_content)
            download_attaches(msg)
        except Exception:
            pass

    server.quit()
