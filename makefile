VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# default arguments
inputgraph = "./data/web-stanford-complete.txt"
shortgraph = "./data/web-stanford-short.txt"

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run-short: $(VENV)/bin/activate
	$(PYTHON) main.py $(shortgraph)

run-complete: $(VENV)/bin/activate
	$(PYTHON) main.py $(inputgraph)

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
