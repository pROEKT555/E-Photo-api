# E-Photo-api

```bash
pip install requirements.txt`

python manage.py runserver
```

or

```bash
pip install uv

uv run manage.py runserver
```


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

in `http://127.0.0.1:8000/register/` only **POST**:
```json
{
    "username": "zxc",
    "password": "zxc"
}   // має відправляти cookies
```

