#!/bin/sh
socat tcp-l:5007,fork,reuseaddr exec:./entry.py

