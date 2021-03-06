install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

brain-gcd:
	poetry run brain-gcd

build:
	poetry build

publish:
	poetry publish -r TestPyPI

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

black:
	poetry run black brain_games
