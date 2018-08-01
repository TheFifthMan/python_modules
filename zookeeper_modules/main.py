#-*- coding: utf-8 -*-
import time
from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch

class ValidatorDetector:

    def __init__(self):
        self.zk = KazooClient(hosts='192.168.31.20:2181,192.168.31.223:2181,129.168.31.144:2181')
        self.validator_children_watcher = ChildrenWatch(client=self.zk,path='/mproxy/validators',func=self.validator_watcher_fun)
        self.zk.start()

    def validator_watcher_fun(self,children):
        print("The children now are:", children)

    def create_node(self):
        a = self.zk.create('/mproxy/aa/validator',b'validator_huabei_1',ephemeral=True,sequence=True)
        print(a)
    def __del__(self):
        self.zk.close()


if __name__ == '__main__':
    detector = ValidatorDetector()
    detector.create_node()
    time.sleep(10)