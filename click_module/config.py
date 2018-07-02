#-*-coding:utf-8-*-
import logging

LOGGING = {
    "version":1,
    "disable_existing_loggers":False,
    "formatters":{
        "standard":{
            "format":'[%(asctime)s][%(threadName)s][%(message)s]'
        }
    },
    "handlers":{
        "console":{
            "level":"DEBUG",
            "class":'logging.StreamHandler',
            'formatter':'standard',
        }
    },
    "loggers":{
        "main":{
            "handlers":['console'],
            'level':'DEBUG',
            'propagate':True
        }
    }

}