#!/bin/sh
gunicorn --chdir pyreceipt pyreceipt:app -w 2 --threads 2 -b 0.0.0.0:80