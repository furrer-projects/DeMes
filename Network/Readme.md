DeMes Network has following object:

-   Account
-   Chain
-   Node
-   Packet
-   Block
-   Message
-   Transaction
-   Resource

**Account** : Account objects are defined to store public/private key + some extra indexing information. 
**Node** : Nodes are key part of the network and information will iterate and store over theme. the node object a lot of information about nodes.
    - *id* : node id,
    - *path* : node path shows the node hirachy and data path

*to avoid extra iterations every node will propagate data to its parent and its children. **Note:** Nodes can change their parents. the can block any of childrens but not able to select their children. also nodes unable to select their children as parent.


words.txt words are used to generate account phrases