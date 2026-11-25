# Tell a Whole Story in 32 Characters

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/stevewhy404/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/rank.svg)](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/leaderboard)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/stevewhy404/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/reward.svg)](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

A Wi-Fi network name that tells a whole story in 25 characters:

> I changed the locks, Dave

The network name is a breakup note left for Dave — the locks are
changed and Dave is the one locked out. A situation, a named
character, and something that happened, in one line a passer-by
reads in a phone's network list.

## How it works

`main.py` writes the name to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(UTF-8, 1–32 characters, not whitespace-only, enforced by `verify()`).

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
