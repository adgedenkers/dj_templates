# Imports
import re
import sys

app_name = sys.argv[1]
config_name = app_name + '.apps.' + app_name.capitalize() + 'Config'

print(app_name)
print(config_name)

# Open a file
with open('django_app/settings.py', 'r') as f:
    contents = f.read()

# Search and replace 
contents = re.sub(r'INSTALLED_APPS = [\n', 'INSTALLED_APPS = [\n    "{}",'.format(config_name), contents)

# Write the new content to the file
with open('django_app/settings.py', 'w') as f:
    f.write(contents)