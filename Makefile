.DEFAULT_GOAL: run

VENV = venv
activate_venv = . $(VENV)/bin/activate

# Define targets
.PHONY: run
run:
	@echo "Activating virtual environment..." && \
	$(activate_venv) && \
	echo "Virtual environment activated." && \
	echo "Running Django development server..." && \
	python manage.py runserver

.PHONY: migrate
migrate:
	$(activate_venv) && \
	python manage.py migrate
	

.PHONY: migrations
migrations:
	$(activate_venv) && \
	python manage.py makemigrations


.PHONY: superuser
superuser:
	$(activate_venv) && \
	python manage.py createsuperuser
