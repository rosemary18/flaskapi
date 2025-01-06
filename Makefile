VENV_DIR = .env
PYTHON = python

create_venv:
	@$(PYTHON) -m venv $(VENV_DIR)

db:
	@$(PYTHON) init_db.py

install_requirements:
	@pip install -r requirements.txt

run:
	@$(PYTHON) main.py

requirements:
	@pip freeze > requirements.txt
