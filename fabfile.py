# Might have to execute "ssh-add ~/.ssh/id_rsa" in local machine if getting ssh
# identity errors.

# fab deploy:development,8080 (target-environment,port)

import os
import errno
import yaml
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
  set_env_config_vars(environment_name)

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
  local('git commit -m "Deploying app. Updated environment.yaml"')

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

def set_env_config_vars(environment_name):
  """ Set the secret config settings
  
  Keep all secret config setting variables in a separate secret.yaml file. Then,
  depending on the environment, save these settings as environment variables or
  heroku config variables. Remember: NEVER track the secret.yaml file in a VCS.
  """
  f = open('poolapp/deploy/secret.yaml')
  secret_settings = yaml.safe_load(f)
  f.close()
  secret_key = secret_settings['secret_key']
  aws_storage_bucket_name = secret_settings['aws_storage_bucket_name']
  aws_access_key_id = secret_settings['aws_access_key_id']
  aws_secret_access_key = secret_settings['aws_secret_access_key']
  print(yellow('Setting environment config settings for %s environment...' %
    environment_name, bold=True))
  local('export SECRET_KEY=%s' % secret_key)
  if environment_name == 'development':
    local('export AWS_STORAGE_BUCKET_NAME=%s' % aws_storage_bucket_name)
    local('export AWS_ACCESS_KEY_ID=%s' % aws_access_key_id)
    local('export AWS_SECRET_ACCESS_KEY=%s' % aws_secret_access_key)
  else:
    local('heroku config:set AWS_STORAGE_BUCKET_NAME=%s' % aws_storage_bucket_name)
    local('heroku config:set AWS_ACCESS_KEY_ID=%s' % aws_access_key_id)
    local('heroku config:set AWS_SECRET_ACCESS_KEY=%s' % aws_secret_access_key)
