# This is the Twisted Fast Poetry Server, version 1.0

import argparse, os, sys

from twisted.internet.protocol import ServerFactory, Protocol


def parse_args():
    usage = """usage: %prog [options] poetry-file
This is the Slow Poetry Server, blocking edition.
Run it like this:
  python slowpoetry.py <path-to-poetry-file>
If you are in the base directory of the twisted-intro package,
you could run it like this:
  python blocking-server/slowpoetry.py poetry/ecstasy.txt
to serve up John Donne's Ecstasy, which I know you want to do.
"""

    parser = argparse.ArgumentParser(description=usage)

    help = "The poetry file."
    parser.add_argument('--filename', help=help)  # type=argparse.FileType('r'),

    help = "The port to listen on. Default to a random available port."
    parser.add_argument('--port', type=int, help=help)

    help = "The interface to listen on. Default is localhost."
    parser.add_argument('--iface', help=help, default='localhost')

    help = "The number of seconds between sending bytes."
    parser.add_argument('--delay', type=float, help=help, default=.7)

    help = "The number of bytes to send at a time."
    parser.add_argument('--num-bytes', type=int, help=help, default=10)

    return parser.parse_args()


class PoetryProtocol(Protocol):

    def connectionMade(self):
        self.transport.write(self.factory.poem)
        self.transport.loseConnection()


class PoetryFactory(ServerFactory):
    protocol = PoetryProtocol

    def __init__(self, poem):
        self.poem = poem


def main():
    options = parse_args()
    if options.filename:
        poetry_file = options.filename
    else:
        poetry_file = None

    # print 'Poetry file:',poetry_file
    # print 'Options:',options.iface, options.port, options.num_bytes, options.delay

    # poem = open(poetry_file).read()

    poem = 'This is a poem, a beautiful poem, but not beautiful AT ALL!'

    factory = PoetryFactory(poem)

    from twisted.internet import reactor

    port = reactor.listenTCP(options.port or 0, factory,
                             interface=options.iface)

    print 'Serving %s on %s.' % (poetry_file, port.getHost())

    reactor.run()


if __name__ == '__main__':
    main()