class DeMes{
    static newAccount($seed=null){
        return {
            "private_key"   : "",
            "public_key"    : "",
            "phrases"       : [],
            "addresses"     : [],
            "alias"         : [],
            "flag"          : 0,
            "version"       : 1,
            "type"          : "ACNT"
        };
    }
    static newNode(){
        return {
            "id"            : parseInt(Math.random()*Date.now()).toString(36)+parseInt(Math.random()*Date.now()).toString(36),
            "chain_id"      : "",
            "account"       : DeMes.newAccount(),
            "parent"        : "",
            "children"      : [],
            "ip"            : "0.0.0.0",
            "url"           : "https://path-to-json-rpc-url",
            "flag"          : 0,
            "version"       : 1,
            "type"          : "ND"
        };
    }
    static newChain(){
        return {
            "name"          : "chAIN."+parseInt(Math.random()*Date.now()).toString(36),
            "id"            : parseInt(Math.random()*Date.now()).toString(36),
            "epoch"         : 0,
            "token"         : "CHAIN MAIN TOKEN NAME",
            "nodes"         : "",
            "grand_parent"  : null,
            "flag"          : 0,
            "version"       : 1,
            "type"          : "CHN"
        };
    }
    static newPacket(){
        return {
            "data"          : null,
            "history"       : [],
            "version"       : 1,
            "type"          : "PKT"
        };
    }
    static newBlock(){
        return {
            "hash"          : "DMx",
            "previous"      : "DMx-1",
            "height"        : 0,
            "time"          : parseInt(Date.now()/1000),
            "data"          : [],
            "version"       : 1,
            "type"          : "BLK"
        };
    }
    static newMessage(){
        return {
            "hash"          : "DMFx",
            "sender"        : null,
            "target"        : null,
            "created"       : time(),
            "modified"      : time(),
            "data"          : "",
            "signature"     : "",
            "expiry"        : time()+(86400*31),
            "flag"          : 0,
            "version"       : 1,
            "type"          : "MSG"
        };
    }
    static newTx(){
        return {
            "hash"          : "DMTx",
            "block"         : "DMx",
            "time"          : time(),
            "senders"       : [],
            "recipients"    : [],
            "signature"     : "",
            "fee"           : 0,
            "value"         : 0,
            "version"       : 1,
            "type"          : "TX"
        };
    }
}