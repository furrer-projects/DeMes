<?php
    class DeMes{
        public static function newAccount($seed=null){
            if(!$seed) $seed = hash('sha256', uniqid().uniqid().uniqid());
            return (object)[
                "private_key"   => "",
                "public_key"    => "",
                "phrases"       => [],
                "addresses"     => [],
                "alias"         => [],
                "flag"          => 0,
                "version"       => 1,
                "type"          => "ACNT"
            ];
        }
        public static function newNode(){
            return (object)[
                "id"            => uniqid().uniqid(),
                "chain_id"      => "",
                "account"       => DeMes::newAccount(),
                "parent"        => "",
                "children"      => [],
                "ip"            => "0.0.0.0",
                "url"           => "https://path-to-json-rpc-url",
                "flag"          => 0,
                "version"       => 1,
                "type"          => "ND"
            ];
        }
        public static function newChain(){
            return (object)[
                "name"          => uniqid("chAIN."),
                "id"            => uniqid(),
                "epoch"         => "",
                "token"         => "CHAIN MAIN TOKEN NAME",
                "nodes"         => "",
                "grand_parent"  => null,
                "flag"          => 0,
                "version"       => 1,
                "type"          => "CHN"
            ];
        }
        public static function newBlock(){
            return (object)[
                "chain_id"      => "",
                "epoch"         => 0,
                "hash"          => "DMx",
                "previous"      => "DMx-1",
                "height"        => 0,
                "time"          => 0,
                "data"          => [],
                "flag"          => 0,
                "version"       => 1,
                "type"          => "BLK"
            ];
        }
        public static function newMessage(){
            return (object)[
                "hash"          => "DMFx",
                "sender"        => null,
                "target"        => null,
                "created"       => time(),
                "modified"      => time(),
                "data"          => "",
                "format"        => "",
                "signature"     => "",
                "expiry"        => time()+(86400*31),
                "flag"          => 0,
                "version"       => 1,
                "type"          => "MSG"
            ];
        }
        public static function newTx(){
            return (object)[
                "hash"          => "DMTx",
                "block"         => "DMx",
                "time"          => time(),
                "senders"       => [],
                "receivers"     => [],
                "fee"           => 0,
                "value"         => 0,
                "version"       => 1,
                "type"          => "TX"
            ];
        }
        public static function newResource(){
            return (object)[
                "hash"          => "rHash",
                "endpoint"      => "https://",
                "created"       => time(),
                "modified"      => time(),
                "format"        => "",
                "data"          => "",
                "expiry"        => 0,
                "flag"          => 0,
                "version"       => 1,
                "type"          => "RSRC"
            ];
        }
    }
?>