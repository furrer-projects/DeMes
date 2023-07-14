<?php
class Node{
    public static function main(){
        $body = file_get_contents("php://");
        $body = json_decode($body);
        if($body){
            if($body->type!="PKT") return;
        }
    }
}
?>