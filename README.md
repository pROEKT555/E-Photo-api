# E-Photo-api

`pip install requirements.txt`

`python manage.py runserver`

in `http://127.0.0.1:8000/register/` only **POST**:
```json
{
    "username": "zxc",
    "password": "zxc",
    "email": "zxc@zxc.com",
    "groups": [
        "role"  // можна тільки одну, це роль
    ]
}
```
