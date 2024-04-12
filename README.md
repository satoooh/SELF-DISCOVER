# SELF-DISCOVER prompt

This repository is an **UNOFFICIAL** Python implementation of the [SELF-DISCOVER paper](https://arxiv.org/abs/2402.03620).
Using `self_discover.py`, you can easily try the SELF-DISCOVER method.

## How to use

This repo uses [Rye](https://rye-up.com/) and [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers).

- clone this repo
- build container
  - use the command "Dev Containers: Open Folder in Container..." from VSCode command palette.

After building, reopen the shell or run the following command:

```sh
exec $SHELL -l
```

Create an .env file and set the OPENAI_API_KEY.

```.env
OPENAI_API_KEY=sk-...
```

run `test_self_discover.py` (testing for problem statements from the MATH dataset mentioned in the paper)

```sh
rye sync
rye run python src/test_self_discover.py
```
