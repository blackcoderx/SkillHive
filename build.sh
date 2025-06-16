set -o errexit


pip install -r requirements.txt

cd skillhive
python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate