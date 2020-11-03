import sys

# START Constant variables
my_errno = {
    0: "Error: the program takes only one argument.",
    1: "Error: argument must be an int.",
    2: "EOF",
    3: "Error: argument must be a positive int.",
}

sign = True
# END

def print_help():
    print ("SYNOPSIS\n" \
           "\t./groundhog period\n\n" \
           "DESCRIPTION\n" \
           "\tperiod the number of days defining a period")
    exit(0)

def print_and_quit(err_msg):
    sys.stderr.write(err_msg);
    exit(84)