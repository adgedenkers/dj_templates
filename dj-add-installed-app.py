# Imports
import re
import sys

app_name = sys.argv[1]
config_name = app_name + '.apps.' + app_name.capitalize() + 'Config'

print("Adding App Named:", app_name)
print("The Config is Listed as:", config_name)

search_text = 'INSTALLED_APPS = [\n'
replace_text = 'INSTALLED_APPS = [\n    "{}",\n'.format(config_name)

# Open a file
with open('django_app/settings.py', 'r') as f:
    data =f.read()
    data = data.replace(search_text, replace_text)

# Write the new content to the file
with open('django_app/settings.py', 'w') as f:
    f.write(data)

print("Added to `settings.py` file.")