JOB_TITLE_FILE='domain_classification/data/Titres_profils.csv'
OUTPUT_FILENAME='job_title_classification_result.csv'

clean:
	rm -Rf *.egg-info
	rm -Rf build
	rm -Rf dist
	rm -Rf .pytest_cache
	rm -f .coverage

build: clean
	python3 setup.py sdist

run: build
	python3 -m domain_classification.main \
	--input_file ${JOB_TITLE_FILE} \
	--output_filename ${OUTPUT_FILENAME}

linter:
	pylint domain_classification

test:
	pytest -vv
	coverage run --source=domain_classification -m pytest
