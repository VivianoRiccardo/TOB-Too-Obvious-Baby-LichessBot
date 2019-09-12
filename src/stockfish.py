import time
from subprocess import Popen, PIPE

def put(p, msg):
    p.stdin.write(msg+'\n')
    p.stdin.flush()

def get(p, verbose=False):
    put(p, 'isready')
    lines = []
    while True:
        s = p.stdout.readline().strip()
        if s == 'readyok':
            break
        if verbose:
            print(s)
        lines.append(s)
    return lines

def putget(p, msg, verbose=False):
    put(p, msg)
    get(p, verbose)

def go(p, depth=None, t=1.0, dt=0.05, verbose=False):
    depth = 'infinite' if depth is None else 'depth %d' % depth
    put(p, "go %s" % depth)
    t0 = time.time()
    stopped = False
    while True:
        time.sleep(dt)
        lines = get(p, verbose=verbose)
        for line in lines:
            if line.startswith('bestmove'):
                return line
        if not stopped and time.time() - t0 > t:
            put(p, "stop")
            stopped = True

p = Popen("../bin/stockfish_10_x64_modern", stdout=PIPE, stdin=PIPE, universal_newlines=True)
get(p, verbose=True)
putget(p, 'uci')
putget(p, 'position startpos')
bestmove = go(p, depth=20, t=0.5)
print(bestmove)
put(p,'position startpos moves e2e4 e7e6')
bestmove = go(p, depth=20, t=0.5)
print(bestmove)

