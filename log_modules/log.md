# 工作流
理解log模块，首先应该理解其工作流，下面通过例子来说明其工作流
首先是main.py
```
import sub
import sub2
import logging
import logging.config
from config import LOGGING
logging.config.dictConfig(LOGGING)
logger = logging.getLogger("main")

def main():
    sub.sub1()
    logger.error("main debug")


if "__main__" == __name__:
    main() 
```

在这里我们引入了sub 和sub2，先不理会其配置文件，假设已经写好配置文件了。
其次是sub.py 文件
```
import logging
sub_logger = logging.getLogger("main.sub")
def sub1():
    print("Hello This is sub1")
    sub_logger.debug("This is sub1")
```
我们可以看到，如果是多模块引入log机制，可以直接写成 如上面的形式。这种继承机制，让我们可以很方便的复用log.
# 理解配置文件
配置文件一般有两种：
字典形式
配置文件形式
至于哪种形式更好，就众说纷坛，有说字典形式比较好，因为都是python文件，我们写代码自定义程度更高，一种说配置文件形式其可读性更好。这里没有一个决断，我们首先使用字典形式，用代码来定义配置文件。
在配置文件里面，log有四个类，分别是
1. formatters
2. handlers
3. filters
4. loggers
## formatters
首先我们来看一下formatters
```
"formatters":{
  # 标准模式
  "standard":{
     'format':'[%(asctime)s][%(threadName)s:%(thread)d][%(name)s:%(levelname)s(%(lineno)d)]\n[%(module)s:%(funcName)s]:%(message)s'
  }
  # 简单模式
  "brief":{
    "format":'[%(message)s]'
  }
}
```
其中 standard 和 brief 都是我们可以自定义的名字 
接下来我们看一下formatters的格式化字符串有哪些，并且分别是什么含义：
```
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s 用户输出的消息
```
## handlers
handlers模块，顾名思义，就是处理log的模块，在这里我们要定义，log的输出是文件形式还是命令行输出形式，文件形式的话，其文件的存储路径，文件大小改如何分割等问题
```
"handlers":{
  "console":{
     'level':'DEBUG',    #输出信息的最低级别
     'class':'logging.StreamHandler',
     'formatter':'standard', #使用standard格式
      'filters': ['require_debug_true',], #仅当 DEBUG = True 该处理器才生效,一般没用。
  },
  'log':{
      'level':'DEBUG',
      'class':'logging.handlers.RotatingFileHandler',
      'formatter':'standard',
      'filename':os.path.join(BASE_DIR, 'debug.log'), #输出位置
      'maxBytes':1024*1024*5, #文件大小 5M
      'backupCount': 5, #备份份数
       'encoding': 'utf8', #文件编码
    },
}
```
同理，这里的console和log也是我们自定义的名字，我们还可以定义其他的，然后选择日志的输出位置，或者设置变量为日志的输出位置
## loggers
loggers是日志的全局管理器，我们会在这里定义一个管理器，在后面调用的时候，我们要获得这个管理器的名字。
```
# 日志管理器集合
    'loggers':{
        #管理器
        "main":{
            'handlers':['console', 'main_log'],
            'level':'DEBUG',
            'propagate':True, #是否传递给父记录器
        },
    }
```
其中 main 是我们自己定义的名字，需要注意的是，如果使用的logger没有在这里定义名字，那么这些配置将无用。
# 调用logger
这里其实也是前面有提到的东西，我们要引入logging和logging.config。（注意，不能只单纯引入logging，会报错）
在main.py中我们 这么引用
```
import logging
import logging.config
from config import LOGGING
logging.config.dictConfig(LOGGING)
logger = logging.getLogger("main"
```
其中这个main 就是我们定义在配置文件中管理器的main
根据其工作流原理，其自模块也需要进行log记录，这个时候我们就不需要写配置文件了，直接使用这个配置文件即可
在sub.py中
```
import logging
sub_logger = logging.getLogger("main.sub")
def sub1():
    print("Hello This is sub1")
    sub_logger.debug("This is sub1")
```
# 总结
就这样，我们模拟了如何在python中使用日志记录，这对于开发来说是一件提高效率和产品质量很重要的事情

# 代码地址
https://github.com/TheFifthMan/python_modules 

# reference
http://yshblog.com/blog/125

https://segmentfault.com/a/1190000015143449