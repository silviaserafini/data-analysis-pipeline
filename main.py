import random
import os 
import sys
from argparse import ArgumentParser
import subprocess
from reportL4 import CreateReport
import pandas as pd

def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])
    #return proc.stdout.read()


parser = ArgumentParser(description="This program shows the avarage US airlanes delays"
"--depDelay shows departure-only delay, --arrDelay shows arrival-only delay ), filtering per Airline, air route, period of time ")

#optional flags arguments
parser.add_argument("-b","--best",help="flag: show the data related to the fastest operators (if false, show the slowest operators)",action="store_true")
parser.add_argument("-y","--depDelay",help="flag: show the data related to departure delays (if False, show arrival delays)",action="store_true")

parser.add_argument("-a","--arrAirport",help="landing airport [IATA code]",default=None)
parser.add_argument("-d","--depAirport",help="departure airport [IATA code]",default=None)
#parser.add_argument("--country",help="IATA code for departure airport",default="None")

parser.add_argument("-c","--airlineCode",help="airline [2 characters IATA code]",default=None)
parser.add_argument("-t","--time",help="show the results for last month [1], year [0]",default="0",type=int,choices=[0, 1])

args = parser.parse_args()
#print(args)

if args.depDelay:
    depDelay=args.depDelay
else:
    depDelay=False

if args.best:
    print(CreateReport(args.airlineCode,args.time,args.depAirport,args.arrAirport,depDelay=depDelay, best=args.best))
else:
    print(CreateReport(args.airlineCode,args.time,args.depAirport,args.arrAirport))