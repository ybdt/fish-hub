#!/usr/bin/env python

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer();
authorizer.add_user("user", "12345", "/home/giampaolo", perm="elradfmwMT");
authorizer.add_anonymous("/home/nobody");

handler = FTPHandler;
handler.authorizer = authorizer;

server = FTPServer( ("192.168.1.128", 21), handler );
server.serve_forever();