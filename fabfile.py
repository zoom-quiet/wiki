from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = '.html'
DEPLOY_PATH = env.deploy_path
env.py2sc = 'wiki/chaos2py4scientist/'
env.cafe_pages = '_book'
# Remote server configuration
#production = 'root@localhost:22'
#dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
#env.cloudfiles_username = 'my_rackspace_username'
#env.cloudfiles_api_key = 'my_rackspace_api_key'
#env.cloudfiles_container = 'my_cloudfiles_container'

#def clean():
#    if os.path.isdir(DEPLOY_PATH):
#        local('rm -rf {deploy_path}/*'.format(**env))
#        #local('mkdir {deploy_path}'.format(**env))

def build():
    local('markdoc build')
def serve():
    local('markdoc serve')
def reserve():
    build()
    serve()
#def preview():
#    local('pelican -s publishconf.py')
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
            #'ls -la && '
            'gitbook build && '
            #'pwd && '
            'cd {cafe_pages} && '
            #'git st && '
            'git add --all . && '
            'git ci -am "re-build from local by gitbook @MBP111216ZQ" && '
            'git pu && '
            #'ls -la && '
            'pwd '.format(**env)
          )
