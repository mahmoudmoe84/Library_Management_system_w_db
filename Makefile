install-ruff:
	uv add ruff --dev

lint:
	ruff check .

lint-fix:
	ruff check . --fix