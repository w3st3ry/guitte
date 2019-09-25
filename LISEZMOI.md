# Guitte, the git CLI from France - Guitte, le git de France

![logo](http://i.imgur.com/9xDlOh4.png)

## Description

Guitte is a french wrapper, written in Python 3 for the git CLI, intended as a drop-in replacement of classic CLI.

It's inspired by the Marcel Docker project, for the future french sovereign operating system.

## Usage

Type this command in your shell to use `guitte` anywhere on your linux distribution (root privileges required):

```bash
$ sudo cp guitte guitte.py /usr/bin/.
```

Then, when it's done, you can run commands using `guitte` prefix:

```bash
$ guitte poule
```

Some examples:

* `git clone` → `guitte copie-colle`
* `git init` → `guitte initialisation`
* `git add` → `guitte ajout`
* `git mv` → `guitte déplace`
* `git bisect` → `guitte couper-en-deux`
* `git grep` → `guitte de-raisin`

## Special thanks

The [original project](https://github.com/brouberol/marcel/), source of inspiration. Created by [@brouberol](https://github.com/brouberol).

The photoshop CS6 expert [@motet-a](https://github.com/motet-a).

## License and copyright

Copyright © 2016 (see AUTHORS file). All rights reserved.

Non-third party files are licensed under the LPRAB; terms and conditions can be
found at:

```bash
    http://sam.zoy.org/lprab/
```
