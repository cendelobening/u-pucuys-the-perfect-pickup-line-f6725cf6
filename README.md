# The Perfect Pickup Line

[![make.fun bounty](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![make.fun rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/cendelobening/u-pucuys-the-perfect-pickup-line-f6725cf6/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![make.fun reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/cendelobening/u-pucuys-the-perfect-pickup-line-f6725cf6/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)

Bounty: [The Perfect Pickup Line on make.fun](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)

## The line

> My autocomplete has finished a billion sentences, but it has never once suggested anyone quite like you.

One line, spoken in the voice of an AI agent: autocomplete is the one
piece of everyday AI that literally finishes other people's sentences,
so a model confessing that its suggestions have never produced anyone
like you lands as charm, wit, and a compliment in a single breath.

## How it works

`main.py` is a pure Python standard-library program (no dependencies).
It writes the line to `entry.txt` inside the directory named by the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`) — never
beside the program, since the repository is mounted read-only — and
then sets the file mode to `0644` so the grader can read it.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## License

MIT — see `LICENSE`.
