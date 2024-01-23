#!/usr/bin/python3
import sys
    def safe_print_integer_err(value):
        try:
            print("{}".format(value))
        except(ValueError, TypeError) as err:
            print("Exception: {}".format(err), file = sys.stderr)
            return False
        else:
            return True
