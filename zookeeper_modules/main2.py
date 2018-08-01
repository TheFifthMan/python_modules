from kazoo.client import KazooClient

class PyzooConn(object):
    def __init__(self):
        self.zk = KazooClient(hosts='192.168.31.20:2181,192.168.31.223:2181,129.168.31.144:2181')
        self.zk.start()

    def get_data(self,param):
        if self.zk.exists(param):
            data,stat = self.zk.get(param)
            print("data:{},stat:{}".format(data,stat))
        else:
            print("None")
        
    def create_node(self,node,value):
        self.zk.create(node,value)
    
    def close(self):
        self.zk.close()
    
if __name__ == "__main__":
    pz = PyzooConn()
    pz.get_data("/mproxy/aa/validator0000000001")
