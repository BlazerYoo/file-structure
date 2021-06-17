# file structure
Generate markdown of file structure

Ideal for generating file structure for repo README's or documentation

Adapted from [StackOverflow](https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python)

[Source](https://github.com/BlazerYoo/file-structure/blob/main/source.py)

## Use
1. `git clone https://github.com/BlazerYoo/file-structure.git fs` or [download](https://github.com/BlazerYoo/file-structure/archive/refs/heads/main.zip) repo
2. `mv ./fs/fs.py ./fs.py`
3. `python fs.py [directory]`

or

3. `mv ./fs/fs.sh ./fs.sh`
4. `chmod +x ./fs.sh`
5. `./fs.sh [directory]`

## Example generated from [this](https://github.com/BlazerYoo/file-structure) repo

```
./
├── .git/
│   ├── info/
│   │   └── exclude
│   ├── hooks/
│   │   ├── fsmonitor-watchman.sample
│   │   ├── pre-applypatch.sample
│   │   ├── update.sample
│   │   ├── pre-push.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-rebase.sample
│   │   ├── applypatch-msg.sample
│   │   ├── post-update.sample
│   │   └── commit-msg.sample
│   ├── description
│   ├── branches/
│   ├── refs/
│   │   ├── heads/
│   │   │   └── main
│   │   ├── tags/
│   │   └── remotes/
│   │       └── origin/
│   │           └── HEAD
│   ├── objects/
│   │   ├── pack/
│   │   ├── info/
│   │   ├── f0/
│   │   │   └── d3977a8be44a17531a6efa4c714b558006a081
│   │   ├── 09/
│   │   │   └── c270bdcc14e26d1c2becd3963a613dd46a9665
│   │   ├── 6c/
│   │   │   └── 3a959ac8450ad1ad0243c520c507d711d04a2d
│   │   ├── ef/
│   │   │   └── a93545bee9939dceb060a29c49103270ada202
│   │   ├── 8d/
│   │   │   └── 90558b8320c6e7859bf78ca98e3e352a44b2db
│   │   ├── f5/
│   │   │   └── 5aa152eeea28d46900d50614f92756771d46dd
│   │   ├── df/
│   │   │   └── e0770424b2a19faf507a501ebfc23be8f54e7b
│   │   ├── c1/
│   │   │   └── 5aa9524d0b0ca746b19fb0550e184b0e215b59
│   │   ├── 29/
│   │   │   └── 014fbc75a84c9b62ed4a290c45376768e86d25
│   │   ├── 24/
│   │   │   └── 2f0706e2b6475afb675e04334d884a4bec34f3
│   │   ├── 63/
│   │   │   └── 8357b50407379d053d97bb6d75a43090189da7
│   │   ├── 01/
│   │   │   └── 3232ad417aa20a3c43ac467408f730fe68a35c
│   │   ├── 7c/
│   │   │   └── 1b5f041406754b0a7a4bca660c52501a89fc1c
│   │   └── 83/
│   │       └── 70423f943a2dc02dabf1fc7c06e8dd9c67d3e8
│   ├── packed-refs
│   ├── logs/
│   │   ├── refs/
│   │   │   ├── remotes/
│   │   │   │   └── origin/
│   │   │   │       └── HEAD
│   │   │   └── heads/
│   │   │       └── main
│   │   └── HEAD
│   ├── HEAD
│   ├── config
│   └── index
├── .gitattributes
├── README.md
├── fs.py
├── fs.sh
└── fileStructure.md
```