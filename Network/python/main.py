from CLI import *
CLI.load()
cmd = ""
while cmd!="exit":
    cmd = input("DeMes >>>")
    if CLI.parse(cmd):
        print("[Done]")
    else:
        if len(cmd)!=0:
            print("[Invalid Command]")