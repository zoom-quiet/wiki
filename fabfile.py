# -*- coding: utf-8 -*-

from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
#env.deploy_path = '.html'
env.static_path = '_static'

def build():
    local('markdoc build && '
            #'ls -la && '
            'rsync -avzP4 {static_path}/media/ {deploy_path}/media/ && '
            'pwd '.format(**env)
        )

def serve():
    local('markdoc serve')

def reserve():
    build()
    serve()

def CNAME():
    local('ls -la {deploy_path}/ && '
            'cp -f {static_path}/CNAME {deploy_path}/ && '
            'pwd '.format(**env)
        )

def hg_pahes():
    local('cd {deploy_path} && '
            'pwd && '
            'git st && '
            'git add --all . && '
            'git ci -am "re-build from local by markdoc @MBP111216ZQ" && '
            #'git pu cafe gitcafe-page '
            'git pu && '
            'date '.format(**env)
          )


def pub():
    build()
    CNAME()
    hg_pahes()

'''
env.py2sc = 'wiki/chaos2py4scientist/'
env.book = '_book/'
env.cafe_pages = '../../../7niu_zoomquiet/gitbook/'
#env.cafe_pages = '../../../42chaos2py4scientist/cafe_OpenMind/'
env.qrsync_bin = '/opt/bin/7niu_package_darwin_amd64/qrsync'
env.qrsync_cfg = '../7niu-zoomquiet.json'
def sync7niu():
    local('pwd && '
            '{qrsync_bin} {qrsync_cfg} && '
            'date '.format(**env)
          )
def pub7niu():
    build()
    book7niu()
    sync7niu()
    #cafe4wiki()
    #cafe4gitbook()

def book7niu():
    local('pwd && '
            'cd {py2sc} && '
            'gitbook build && '
            'rsync -avzP4 {book} {cafe_pages} && '
            #'ls -la && '
            'date '.format(**env)
          )

def wiki2cafe():
    build()
    local('cd {deploy_path} && '
            'pwd && '
            #'git pu && '
            'git add --all . && '
            #'git st && '
            'git ci -am "re-build from local by markdoc @MBP111216ZQ" && '
            #'git pu cafe gitcafe-page '
            'git pu && '
            'date '.format(**env)
          )

def cafe4gitbook():
    local('cd {py2sc} && '
            'pwd && '
            'gitbook build && '
            #'pwd && '
            #'cd {book} && '
            'rsync -avzP4 {book} {cafe_pages} && '
            #'ls -la && '
            'cd {cafe_pages} && '
            'git st && '
            'git add --all . && '
            'git ci -am "re-build from local by gitbook @MBP111216ZQ" && '
            'git pu && '
            #'ls -la && '
            'date '.format(**env)
          )
'''
