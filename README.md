# graphs-project

## Build project

```shell
make
```

This will create a local environment at ```venv```, install versioned dependencies from ```requirements.txt```.

## Run project ```main.py``` with default arguments

- Preferably, run the complete graph (the .txt file is about 32MB)

```shell
make run-complete
```

- But, you might want to run the shorter sample of the graph with

```shell
make run-short
```

- check ```Makefile``` for default arguments and change it accordingly.
