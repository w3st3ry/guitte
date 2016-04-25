# Guitte, the git CLI from France - Guitte, le git de France

![logo](https://raw.githubusercontent.com/pichar-v/guitte/master/guitte_de_france.svg)

## Description

Guitte is a french wrapper, write in Python 3 for the git CLI, intended as a drop-in replacement of classic CLI.
He's inspirated by the Marcel Docker project for the future french sovereign operating system too.

## Usage

Type this command in your shell to use `guitte` anywhere on your linux distribution (root privileges required):

```bash
$ sudo cp guitte guitte.py /usr/bin/.
```

Then, when it's finish, you can run commands using `guitte` prefix:

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
