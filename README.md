# graphs-project

 In this project I worked with the [Stanford web graph](https://snap.stanford.edu/data/web-Stanford.html), which represents pages from Stanford University and their hyperlink connections, which offers an opportunity to explore various aspects of graph theory and network analysis.

 My main idea is to display how pages are related and implement the HITS (Hyperlink-Induced Topic Search) algorithm to identify both hubs and authorities within the Stanford web graph. Hubs are nodes that link to many other nodes, while authorities are nodes that are linked by many nodes. This analysis can help to uncover the most influential or referenced pages in the network.

- In this project:
  - authorities are demonstrated with the blue color
  - hubs are demonstrated with the red color

- This project is on [GitHub](https://github.com/dantas15/stanford-graphs-project)!

## Build project

```shell
make
```

This will create a local environment at `venv` and install versioned dependencies from `requirements.txt`.

## Run project `main.py` with default arguments

- Preferably, run the complete graph (the .txt file is about 32MB)

```shell
make run-complete
```

- But, you might want to run the shorter sample of the graph with

```shell
make run-short
```

- check ```makefile``` for default arguments and change it accordingly.

## Important Libs

Even though `requirements.txt` is quite big, it's only because I used more important libs that require them:

- `networkx`
- `matplotlib`

## Credits

This is a project I made during my studies at GCC218 - Algorithms in Graphs at [UFLA](https://ufla.br), taught by [Vinícius Dias](https://github.com/viniciusvdias)
