# boolang

Boolang is a language meant for doing boolean algebra. I am making it to help me with my digital logic homework.

Boolang is implemented in python using [PLY](https://www.dabeaz.com/ply/) (Python Lex-Yacc).

Not to be confused with [boo-lang](https://github.com/boo-lang/boo)

## Instructions
### Setup

Clone the repository and cd into it.
```bash
git clone https://github.com/rpshukla/boolang.git
cd boolang
```

Source setup.bash. This will add src to PYTHONPATH and bin to PATH:
```bash
source setup.bash
```

You will have to do this setup every time you open a new bash prompt. If you want to make the changes to your environment variables permanent, add the following line to your .bashrc. Replace PATH\_OF\_BOOLANG\_REPO with the absolute path of ../boolang on your system.
```bash
source PATH_OF_BOOLANG_REPO/setup.bash
```

### Usage
Once you have done the setup. You should be able to type "boolang" from any directory in a bash prompt to be dropped into a boolang REPL. If you want to run some boolang code in a file, run:
```bash
boolang filename
```

## A Tour of the Syntax
Define a function.

Note: spaces and newlines are not significant.
```
\def \my_funct [x, y] {
    x'y + xy'
}
```

Print a truth table for my\_funct:
```
\truth \my_funct
```
