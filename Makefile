all:
	@echo "please enter a command"

clean:
	find . -type -f -name "*.py[co]" | xargs rm -f
	rm -rf dist *egg-info

dist: clean
	python -m build -n

install: dist
	pip uninstall -y simplegen
	pip install dist/simplegen-0.0.1-py3-none-any.whl

.PHONY : all clean
