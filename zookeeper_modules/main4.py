from kazoo.client import KazooClient
import time
zk = KazooClient(hosts="192.168.31.144:2181,192.168.31.20:2181,192.168.31.223:2181")
zk.start()

# 监听节点
@zk.DataWatch("/mproxy/aa/validators")
def watch_node(data, stat):
    print("Version: %s, data: %s" % (stat, data.decode("utf-8")))
    with open('conf2.txt','wb')as f:
        f.write(data)

@zk.ChildrenWatch("/mproxy/aa")
def children_node(children):
    print("The children now are:", children[0])
   
