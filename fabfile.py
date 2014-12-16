from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = '.html'
DEPLOY_PATH = env.deploy_path
env.py2sc = 'wiki/chaos2py4scientist/'
env.book = '_book'
env.cafe_pages = '../../../42chaos2py4scientist/cafe_OpenMind/'

def pub2all():
    p2cafe()
    gitbook()

def serve():
    local('markdoc serve')
def reserve():
    build()
    serve()

def build():
    local('markdoc build')
def p2cafe():
    build()
    local('cd {deploy_path} && '
            'pwd && '
            #'git pu && '
            'git add --all . && '
            #'git st && '
            'git ci -am "re-build from local by markdoc @MBP111216ZQ" && '
            #'git pu cafe gitcafe-page '
            'git pu && '
            'pwd '.format(**env)
          )

def gitbook():
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
            'pwd '.format(**env)
          )

