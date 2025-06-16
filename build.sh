set -o errexit

pip install -r requirements.txt

cd skillhive 
gunicorn skillhive.wsgi:application --bind 0.0.0.0:$PORT 
python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate

exit 0