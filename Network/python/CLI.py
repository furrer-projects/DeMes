from model import *
import os
import pickle
from Server import *

class CLI:
    @staticmethod
    def parse(cmd:str):
        parts = cmd.split(' ')
        if parts[0].lower()=="create" or parts[0].lower()=="new":
            if parts[1]=="account":
                ret = DeMes.newAccount()
                ret['phrases'] = " ".join(DeMes.generatePhrases())
                # ret['private_key'] = DeMes.generatePrivateKeyBySeed(DeMes.generateSeedByPhrases(ret['phrases']))
                # ret['public_key'] = ret['private_key'].get_public_key()
                CLI.temp = ret
                return True
            elif "phrases":
                ret = " ".join(DeMes.generatePhrases())
                print(ret)
                return True
            elif parts[1]=="node":
                ret = DeMes.newNode()
                CLI.temp = ret
                return True
        elif parts[0].lower()=="import" or parts[0].lower()=="recover":
            if parts[1]=="account":
                phrases = " ".join(parts[2:])
                ret = DeMes.newAccount()
                ret['phrases'] = phrases
                # ret['private_key'] = DeMes.generatePrivateKeyBySeed(DeMes.generateSeedByPhrases(ret['phrases']))
                # ret['public_key'] = ret['private_key'].get_public_key()
                CLI.temp = ret
                return True
        elif parts[0].lower()=="show":
            if len(parts)>1:
                if parts[1] in CLI.variables:
                    print(CLI.variables[parts[1]])
                    return True
                else:
                    print("[Undefined variable]")
                    return True
            print(CLI.temp)
            return True
        elif parts[0].lower()=="define":
            if len(parts)>1:
                CLI.variables[parts[1]] = CLI.temp
                return True
            return False
        elif parts[0].lower()=="undefine":
            if len(parts)>1:
                del(CLI.variables[parts[1]])
                return True
            CLI.temp = None
            return True
        elif parts[0].lower()=="select":
            if len(parts)>1:
                if parts[1]=="account":
                    if len(parts)>2:
                        if parts[2] in CLI.variables:
                            if CLI.variables[parts[2]]['type']=="ACNT":
                                CLI.activateAccount(CLI.variables[parts[2]])
                                print("Account Activated.")
                                return True
                        elif CLI.temp['type']=="account":
                            CLI.activateAccount(CLI.temp)
                            print("Temp Account Activated.")
                            return True
                if parts[1] in CLI.variables:
                    CLI.temp = CLI.variables[parts[1]]
                else:
                    print("[Undefined Variable -> "+parts[1]+"]")
                return True
            return False
        elif parts[0].lower()=="sign":
            if CLI.activateAccount!=None:
                if len(parts)>1:
                    return
                txt = input("Enter text to sign >>>")
                sign = DeMes.sign(txt, CLI.active_account['private_key'])
                print(sign)
            else:
                print("[Please activate an account]")
                pass
            return True
        elif parts[0].lower()=="verify":
            if CLI.activateAccount!=None:
                if len(parts)>1:
                    return
                txt = input("Enter text to verify >>>")
                sign = input("Enter signature to verify >>>")
                result = DeMes.verify(txt, sign, CLI.active_account['public_key'])
                if result:
                    print("[Verified]")
                else:
                    print("[Unverified]")
            else:
                print("[Please activate an account]")
                pass
            return True
        elif parts[0].lower()=="version":
            print("+----------------------------------------------------+")
            print("| DeMes Network Command Line Interface Version 0.0.1 |")
            print("+----------------------------------------------------+")
            return True
        elif parts[0].lower()=="save":
            CLI.save()
            return True
        elif parts[0].lower()=="reset":
            answer = input("All settings and data will clean and they are not recoverable by CLI itself.\nAre you sure to reset the CLI (y/n)? ")
            if answer.lower()[0]=="y":
                CLI.temp = None
                CLI.variables = {}
                CLI.save()
                return True
        elif parts[0].lower()=="server":
            if len(parts)>1:
                if parts[1].lower()=="start":
                    if CLI.server_object is None:
                        CLI.server_object = DeMesServer()
                        print('starting...')
                        CLI.server_object.start()
                elif parts[1].lower()=="stop":
                    CLI.server_object.stop()
                    CLI.server_object = None
                    pass
                else:
                    print('invalid server comands')
            return True
        elif parts[0]=="exit":
            exit()
        return False
    @staticmethod
    def save():
        print("saving CLI Profile...")
        out = {
            "temp" : CLI.temp,
            "vars" : CLI.variables
        }
        f = open("profile", "wb")
        pickle.dump(out, f)
        f.close()
    @staticmethod
    def load():
        if os.path.exists("profile"):
            print("Loading CLI Profile...")
            f = open("profile", "rb")
            inp = pickle.load(f)
            CLI.temp = inp['temp']
            CLI.variables = inp['vars']
            f.close()
            if "__ACTIVE_ACCOUNT__" in CLI.variables:
                CLI.activateAccount(CLI.variables['__ACTIVE_ACCOUNT__'])
            print("[Done]")
    def activateAccount(acc):
        if acc['type']=="ACNT":
            CLI.variables['__ACTIVE_ACCOUNT__'] = acc
            cp = acc.copy()
            cp['private_key'] = DeMes.generatePrivateKeyBySeed(DeMes.generateSeedByPhrases(cp['phrases']))
            cp['public_key'] = cp['private_key'].get_public_key()
            CLI.active_account = cp
            print(cp)

            

CLI.temp = None
CLI.variables = {}
CLI.active_account = None
CLI.server_object = None
