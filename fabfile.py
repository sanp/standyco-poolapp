# Might have to execute "ssh-add ~/.ssh/id_rsa" in local machine if getting ssh
# identity errors.  Also, make sure your remote branches are called staging and
# production.

# fab deploy:production,master (environment,branch)

import os
import errno
import yaml
from subprocess import call
from fabric.api import *
from fabric.colors import green, red, yellow
# Style guide: use green for user input, yellow for printing messages to the
# console, and red for errors/exceptions

def deploy(environment_name='development', branch='master', port='8080'):
  if environment_name not in ('production', 'development', 'staging'):
    raise ValueError(
        'Environment must be either production, development, or staging')

  set_env(environment_name)
  local('pip freeze > requirements/common.txt')
  commit_environment_yaml(environment_name)

  if environment_name == 'development':
    deploy_local(port)
  else:
    deploy_remote(environment_name, branch)

def deploy_local(port='8080'):
  print(yellow('Starting development server on port %s...' % (port), bold=True))
  local('python manage.py runserver %s' % (port))

def deploy_remote(environment, branch):

  # Each environment has a different heroku app associated wit it.
  app_name = {
      'production': 'standyco-poolapp',
      'staging': 'standyco-poolapp-staging'
      }

  print(yellow('Now deploying the %s branch to the %s environment...' 
    % (branch, environment), bold=True))
  # Push to github
  print(yellow('Pushing the latest snapshot to Github...', bold=True))
  local('git push github %s' % (branch))
  print(yellow('Pushing the latest snapshot to Heroku...', bold=True))
  # Display a site-maintenanze message if people visit the site during
  # deployment
  local('heroku maintenance:on --app %s' % app_name[environment])
  # Make sure that the staging and production remotes are named 'staging' and
  # 'production' respectively.
  local('git push %s %s' % (environment, branch))
  local('heroku maintenance:off --app %s' % app_name[environment])

def set_env(environment_name):
  env_yaml_file = 'poolapp/deploy/environment.yaml'
  env_setting = 'environment: %s' % (environment_name)
  write_file(env_setting, env_yaml_file)

def commit_environment_yaml(environment_name):
  """ Only commit the changes to environment.yaml
  
  I don't like adding and committing the entire repo's changes in a fabfile,
  because I want to see/know what I'm committing rather than have it done
  automatically.  Possibly in the future I might change my mind and commit
  everything in fab, though. For now, just commit the changes made to the
  environment.yaml file when deploying.
  """
  print(yellow('Committing changes to environment.yaml file...', bold=True))
  # The requirements files and the environment.yaml files are sometimes
  # automatically changed by this fabfile script, so add them before commit just
  # in case.  All other files should not be automatically added/committed on a
  # deploy -- I want to manyally add/commit those because i want to know what
  # I'm committing.
  local('git add poolapp/deploy/environment.yaml')
  local('git add poolapp/requirements/*')
  # Fab will throw an error if you try to commit a repo with no new changes, so
  # wrap in a try-catch to avoid this.
  try:
    local('git commit -m "Deploying app to %s."' % environment_name)
  except:
    print(green('Nothing new to commit.', bold=True))
      

def write_file(data, path):
  """ Writes some object (data) to a file safely - first makes sure the path
  exists
  """

  def mkdir_p(path):
    # Taken from http://stackoverflow.com/a/600612/119527
    try:
      os.makedirs(path)
    except OSError as exc: # Python >2.5
      if exc.errno == errno.EEXIST and os.path.isdir(path):
        pass
      else: raise

  def safe_open_w(path):
    """ Open "path" for writing, creating any parent directories as needed.
    """
    mkdir_p(os.path.dirname(path))
    return open(path, 'wb')

  with safe_open_w(path) as f:
    f.write(data)
    f.close()
