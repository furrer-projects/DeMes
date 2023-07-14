from uuid import *
from datetime import datetime
import random
import hashlib
from ecpy.curves import Curve, Point
from ecpy.keys import ECPublicKey, ECPrivateKey
from ecpy.ecdsa import ECDSA
model_ecdsa = ECDSA()
class DeMes:
    @staticmethod
    def newAccount():
        return {
            "private_key"   : "",
            "public_key"    : "",
            "phrases"       : [],
            "addresses"     : [],
            "alias"         : [],
            "flag"          : 0,
            "version"       : 1,
            "type"          : "ACNT"
        }
    @staticmethod
    def newNode():
        return {
            "id"            : str(uuid1()),
            "chain_id"      : "",
            "account"       : DeMes.newAccount(),
            "parent"        : "",
            "children"      : [],
            "ip"            : "0.0.0.0",
            "url"           : "https://path-to-json-rpc-url",
            "flag"          : 0,
            "version"       : 1,
            "type"          : "ND"
        }
    @staticmethod
    def newChain():
        return {
            "name"          : "chAIN."+str(uuid1()),
            "id"            : str(uuid1()),
            "epoch"         : 0,
            "token"         : "CHAIN MAIN TOKEN NAME",
            "nodes"         : "",
            "grand_parent"  : None,
            "flag"          : 0,
            "version"       : 1,
            "type"          : "CHN"
        }
    @staticmethod
    def newPacket():
        return {
            "data"          : None,
            "history"       : [],
            "version"       : 1,
            "type"          : "PKT"
        }
    def newBlock():
        return {
            "hash"          : "DMx",
            "previous"      : "DMx-1",
            "height"        : 0,
            "time"          : int(datetime.now().timestamp()),
            "data"          : [],
            "version"       : 1,
            "type"          : "BLK"
        }
    def newMessage():
        return {
            "hash"          : "DMFx",
            "sender"        : None,
            "target"        : None,
            "created"       : int(datetime.now().timestamp()),
            "modified"      : int(datetime.now().timestamp()),
            "data"          : "",
            "signature"     : "",
            "expiry"        : int(datetime.now().timestamp())+(86400*31),
            "flag"          : 0,
            "version"       : 1,
            "type"          : "MSG"
        }
    def newTx():
        {
            "hash"          : "DMTx",
            "block"         : "DMx",
            "time"          : int(datetime.now().timestamp()),
            "senders"       : [],
            "recipients"    : [],
            "signature"     : "",
            "fee"           : 0,
            "value"         : 0,
            "version"       : 1,
            "type"          : "TX"
        }
    @staticmethod
    def generateSeedByPhrases(phrases):
        if type(phrases)==list:
            phrases = " ".join(phrases)
        phrases = bytes(phrases, 'ascii')
        seed = hashlib.sha256(phrases).hexdigest()
        seed = int(seed, 16)
        return seed
    @staticmethod
    def generatePrivateKeyBySeed(seed):
        return ECPrivateKey(seed, Curve.get_curve('secp256k1'))
    @staticmethod
    def sign(msg, private_key):
        msg = bytes(msg, 'utf-8')
        return model_ecdsa.sign(msg, private_key).hex()
    @staticmethod
    def verify(msg, sign, public_key):
        msg = bytes(msg, 'utf-8')
        return model_ecdsa.verify(msg, bytes.fromhex(sign), public_key)
    @staticmethod
    def generatePhrases(count=12):
        f = open('words.txt', 'r+')
        lines = f.readlines()
        ret = []
        while count>0:
            word = lines[random.randint(0, len(lines))]
            word = word.replace("\n", "")
            if (not word in ret) and len(word)>3:
                ret.append(word)
                count-=1
        return ret

