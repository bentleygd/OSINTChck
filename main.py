#!/usr/bin/python
from coreutils import getConfig
import osintchck
import argparse


a_parse = argparse.ArgumentParser(description='Open Threat Intel checker.')
a_parse.add_argument('-I','--ip', action='store_true',
                    help='Check for IP address')
a_parse.add_argument('-D', '--dns', action='store_true',
                    help='Check for DNS Name')
a_parse.add_argument('-U', '--url', action='store_true', 
                    help='Check for URL')
a_parse.add_argument('indicator', type=str, help='Indicator to check for.')
args = a_parse.parse_args()

config = getConfig('config.cnf')
vt_api_key = config.VTPI()
fsb_api_key = config.FSBAPI()
if args.ip:
    ip_chck = osintchck.IPOSINT(args.indicator)
    vt = ip_chck.VTChck(vt_api_key)
    tc = ip_chck.TCChck()
    tm = ip_chck.TMChck()
    fsb = ip_chck.FSBChck(fsb_api_key)
    tbl = ip_chck.TBLChck()
    uh = ip_chck.UHChck()
