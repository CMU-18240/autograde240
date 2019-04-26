from sys import stdout

class TextColorError(Exception):
    pass

COLOR_DICT = {
    'magenta':  "\033[95m",
    'blue':     "\033[94m",
    'green':    "\033[92m",
    'yellow':   "\033[33m",
    'red':      "\033[91m",
    'bold':     "\033[1m",
    'line':     "\033[4m",
    'endc':     "\033[0m"
}

def what_colors():
    for (key, val) in COLOR_DICT.iteritems():
        print('{}{}{}'.format(val, key, COLOR_DICT['endc']))

def check_op(op):
    op = op.lower()
    if op not in COLOR_DICT:
        raise TextColorError('ERROR: not a valid option for formatting')

def get_op_from_str(op):
    op = op.lower()
    check_op(op)

    return COLOR_DICT[op]

def format_str(s, op):
    clr = get_op_from_str(op)
    return '{}{}{}'.format(clr, s, COLOR_DICT['endc'])

def stdout_turnon(op):
    clr = get_op_from_str(op)
    stdout.write(clr)

def stdout_turnoff():
    stdout.write(COLOR_DICT['endc'])

def stdout_write(s):
    stdout.write(s)
    stdout.flush()

def stdout_flush():
    stdout.flush()
