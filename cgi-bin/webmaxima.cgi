#!/usr/bin/env python

from __future__ import print_function

import cgi, cgitb

import subprocess

def main():
    cgitb.enable()
    print("Content-type:text/html\n")

    form = cgi.FieldStorage()
    maxima_input = form.getvalue('maxima_input') or ""

    maxima_output = subprocess.Popen(["maxima", "--very-quiet", "--init-mac=init.mac"],
                                     stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE).communicate(maxima_input.encode())[0].decode()
    # ignore the warning in the first line (about the system() function redefinition)
    print("\n".join(maxima_output.split("\n")[1:]))

if __name__ == "__main__":
    main()
