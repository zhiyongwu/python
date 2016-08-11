from socket import AF_INET,socket,SOCK_STREAM

class LazyConnection:
    def __init__(self,address,family=AF_INET,type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family,self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self,exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

if __name__ == '__main__':
    from functools import partial
    conn = LazyConnection(('www.python.org',80))
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)