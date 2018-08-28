clean:
	@rm -rf `find . -name __pycache__`
	@git clean -dXf

.venv:
	python3 -m venv .venv
	.venv/bin/pip3 install --upgrade pip wheel setuptools
	@echo "To activate the venv, execute 'source ~/sandbox/.venv/bin/activate'"

.PHONY: clean
