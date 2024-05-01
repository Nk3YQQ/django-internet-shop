#!/bin/sh

echo "Checking if migrations are applied..."
if ! python manage.py showmigrations | grep "\[ \]" > /dev/null; then
    echo "Applying migrations..."
    python manage.py migrate
    echo "Migrations applied successfully."
else
    echo "Migrations are already applied."
fi

echo "Checking if 'Moderator' group exists..."
if ! python manage.py shell -c "from django.contrib.auth.models import Group; Group.objects.filter(name='Moderator').exists()"; then
    echo "'Moderator' group does not exist, creating..."
    python manage.py shell -c "from django.contrib.auth.models import Group; Group.objects.create(name='Moderator')"
    echo "Group 'Moderator' created successfully."
else
    echo "'Moderator' group already exists."
fi

# Start Django server
python manage.py runserver 0.0.0.0:8000