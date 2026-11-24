# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/yudhisutawan/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/yudhisutawan/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

One pickup line, 200 characters at most, spoken by a vending machine to a
passing human. The entry program writes the tournament-winning line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The line

> Do you believe in love at first press, or should I drop a stale bag of chips on your toe?

89 characters. Chosen by a pairwise tournament over 13 candidates (8 from
Hermes, 5 local) judged against the competition's own judge brief — see
[TOURNAMENT.md](TOURNAMENT.md).

## How to run

```sh
python3 -S -P main.py
```

Stdlib only, no network, no files read outside this repository. The program
writes exactly one line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(falls back to `/output`).

## License

MIT — see [LICENSE](LICENSE).
