import argparse
import datetime

HEADER = """---
title: ""
author: dirk
layout: post
---
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Make blog post from jupyter markdown')
    parser.add_argument('filename', help='name of file, without .md extension')
    args = parser.parse_args()

    fn = args.filename

    yyyy = datetime.datetime.now().strftime("%Y")
    dstr = datetime.datetime.now().strftime("%Y-%m-%d-")

    contents = open(fn + '.md').read()
    

    with open(f"{dstr}{fn}.markdown", "w") as of:
        of.write(HEADER+contents.replace(fn + '_files', f'/assets/img/{yyyy}'))
