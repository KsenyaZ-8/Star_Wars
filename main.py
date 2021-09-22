from telnetlib import Telnet
 
with Telnet("sw1.dvmn.org", 23) as tn:
    tn.interact()