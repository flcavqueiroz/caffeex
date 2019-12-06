# Caffeex | Estoque

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
cd caffeex_estoque
python3 -m venv .venv
source .venv/bin/activate (Windows: .venv\Scripts\activate.bat)
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py runserver
```
* Para acessar area de gerente, basta acessar /admin

