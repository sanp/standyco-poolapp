# Might have to execute "ssh-add ~/.ssh/id_rsa" in local machine if getting ssh
# identity errors.

# fab deploy:production (target environment -- production, development, or staging)

from fabric.api import local
from fabric.colors import green, red, yellow
# Style guide: use green for user input, yellow for printing messages to the
# console, and red for errors/exceptions

def deploy(environment_name = 'development'):
  if environment_name not in ('production', 'development', 'staging'):
    raise ValueError(
        'Environment must be either production, development, or staging')

  local('pip freeze > requirements/common.txt')
  local('git add -A')
  print(green("Enter your git commit comment: ", bold=True))
  comment = raw_input()
  local('git commit -m "%s"' % comment)
  if environment_name == 'production':
    deploy_remote()
  else:
    deploy_local()

def deploy_local(port=8080):
  print(yellow('Starting development server on port %d...' % (port), bold=True))
  local('python manage.py runserver %d' % (port))

def deploy_remote():
  print(yellow('Pushing the latest snapshot to Heroku...', bold=True))
  # Display a site-maintenanze message if people visit the site during
  # deployment
  local('heroku maintenance:on')
  local('git push heroku master')
  local('heroku maintenance:off')
