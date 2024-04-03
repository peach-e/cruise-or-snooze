.PHONY: format
format:
	black .

.PHONY: clean-notebooks
clean-notebooks:
	jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebooks/*.ipynb
