# Author: Adge Denkers / https://github.com/adgedenkers
# Created: 2023-02-26 10:14:48
# Description: Creates a new Django app with a urls.py, and a base.html template
# Usage: dj-new-app.sh <app_name>
# Example: dj-new-app.sh myapp
# Note: This script assumes you are in the root of your Django project

python manage.py startapp $1
cd $1
curl -O https://raw.githubusercontent.com/adgedenkers/dj_templates/main/app/urls.py
mkdir templates
cd templates
mkdir $1 
cd $1
curl -O https://raw.githubusercontent.com/adgedenkers/dj_templates/main/app/templates/base.html
cd ../../..
python dj-add-installed-app.py $1
python dj-add-app-urls.py $1