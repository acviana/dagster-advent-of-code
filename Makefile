export-requirements:
	poetry export -f requirements.txt -o requirements.txt
	poetry export -f requirements.txt -o requirements_dev.txt --dev

_update:
	poetry update

update: _update export-requirements

update-diff:
	poetry update --dry-run | grep -i updat
