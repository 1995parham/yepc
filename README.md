# Yet Another El Project - Compiler

[![Travis branch](https://img.shields.io/travis/com/1995parham/yepc/master.svg?style=flat-square&logo=travis)](https://travis-ci.com/1995parham/yepc)

## Introduction

Another compiler project, nothing else. every year students of
Amirkabir University of Technology write a simple compiler and
nothing change, we are just two of them.

The onlu difference is that we are using [ply](https://github.com/dabeaz/ply) and python for the first time :dancer:

-- Fall 2016, Prof. Razzazi Compiler Course

## How To Run

### Backend
The backend is the core of the project that parses the grammer and generates C code.

```
python3 -mpip pipenv
pipenv install
pipenv shell
./yepc-serve.py
```

### Frontend
We have planty of time, so we have created the an Angular Frontend for our project.
The frontend project is outdated but with the help from [here](https://stackoverflow.com/questions/55921442/how-to-fix-referenceerror-primordials-is-not-defined-in-node),
it works now.

```sh
cd yepc-UI
npm install
npx bower install
npx grunt --force
```

## Contributors

- [Parham Alvani](https://github.com/1995parham)
- [Saman Fekri](https://github.com/samanfekri)
