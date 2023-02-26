# Imports
import sys

app_name = sys.argv[1]
#config_name = app_name + '.apps.' + app_name.capitalize() + 'Config'



# Open a file
with open('django_app/urls.py', 'r') as f:
    data =f.read()

    search_text = 'from django.urls import path'
    replace_text = 'from django.urls import include, path'
    data = data.replace(search_text, replace_text)

    search_text = 'urlpatterns = [\n'
    replace_text = 'urlpatterns = [\n    path("{a}/", include("{a}.urls")),\n'.format(a=app_name)
    data = data.replace(search_text, replace_text)

# Write the new content to the file
with open('django_app/urls.py', 'w') as f:
    f.write(data)

print("Added `{}` to the `django_app\urls.py` file.".format(app_name))