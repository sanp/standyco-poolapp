# Might have to execute "ssh-add ~/.ssh/id_rsa" in local machine if getting ssh
# identity errors.

# fab deploy:development,8080 (target-environment,port)

import os
import errno
from fabric.api import *
from fabric.colors import green, red, yellow
# Style guide: use green for user input, yellow for printing messages to the
# console, and red for errors/exceptions

def deploy(environment_name='development', port='8080'):
  if environment_name not in ('production', 'development', 'staging'):
    raise ValueError(
        'Environment must be either production, development, or staging')

  set_env(environment_name)
  commit_environment_yaml()

  local('pip freeze > requirements/common.txt')
  if environment_name == 'production':
    deploy_remote()
  else:
    deploy_local(port)

def deploy_local(port='8080'):
  print(yellow('Starting development server on port %s...' % (port), bold=True))
  local('python manage.py runserver %s' % (port))

def deploy_remote():
  print(yellow('Pushing the latest snapshot to Heroku...', bold=True))
  # Display a site-maintenanze message if people visit the site during
  # deployment
  local('heroku maintenance:on')
  local('git push heroku master')
  local('heroku maintenance:off')

def set_env(environment_name):
  env_yaml_file = 'poolapp/deploy/environment.yaml'
  env_setting = 'environment: %s' % (environment_name)
  write_file(env_setting, env_yaml_file)

def commit_environment_yaml():
  """ Only commit the changes to environment.yaml
  
  I don't like adding and committing the entire repo's changes in a fabfile,
  because I want to see/know what I'm committing rather than have it done
  automatically.  Possibly in the future I might change my mind and commit
  everything in fab, though. For now, just commit the changes made to the
  environment.yaml file when deploying.
  """
  print(yellow('Committing changes to environment.yaml file...', bold=True))
  local('git add poolapp/deploy/environment.yaml')
  try:
    local('git commit -m "Deploying app. Updated environment.yaml"')
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
