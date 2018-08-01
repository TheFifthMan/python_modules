from kazoo.client import KazooClient

zk = KazooClient(hosts="192.168.31.144:2181,192.168.31.20:2181,192.168.31.223:2181")
zk.start()

# 删除节点
zk.delete("/mproxy/aa/validators",recursive=True)

# 创建节点
result = zk.create('/mproxy/aa/validators',b'validator_huabei_1')
print(result)

# 更新节点
with open("conf.txt",'rb') as f:
    zk.set("/mproxy/aa/validators",f.read())

# 获取节点
data,stat = zk.get("/mproxy/aa/validators")
print(data.decode('utf-8'))
print(stat)
#zk.delete("/mproxy/aa/validator",recursive=True)
