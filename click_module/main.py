#!/usr/bin/env python
#-*- coding:utf-8 -*-

import click
import os 
import os.path
import logging
import logging.config
from config import LOGGING
logging.config.dictConfig(LOGGING)
logger = logging.getLogger("main")


@click.command()
@click.option('--env','-env',default=None,help='the env of scripts')
@click.option('--filename','-filename',default=None,help="the group of scripts")
@click.option('--thread_nums','-thread_nums',type=int,default=1,help="the number of threads")
def main(env,filename,thread_nums):
    print("the environment is {}".format(env))
    print("the num of threads is {}".format(thread_nums))
    if env == None:
        logger.error("Must set an environment.")
        return
    else:
        pass



if "__main__" == __name__:
    main()