import check50
import check50_rs
import os

EXEC = "./target/debug/speller"

@check50.check()
def exists():
    """src/main.rs exists"""
    check50.exists("src/main.rs")


@check50.check(exists)
def compiles():
    """src/main.rs compiles"""
    check50_rs.compile("src/main.rs")


@check50.check(compiles)
def basic():
    """handles most basic words properly"""
    check50.include("basic")
    check50.run(f"{EXEC} basic/dict basic/text").stdout(open("basic/out")).exit(0)


@check50.check(compiles)
def min_length():
    """handles min length (1-char) words"""
    check50.include("min_length")
    check50.run(f"{EXEC} min_length/dict min_length/text").stdout(
        open("min_length/out")
    ).exit(0)


@check50.check(compiles)
def max_length():
    """handles max length (45-char) words"""
    check50.include("max_length")
    check50.run(f"{EXEC} max_length/dict max_length/text").stdout(
        open("max_length/out")
    ).exit(0)


@check50.check(compiles)
def apostrophe():
    """handles words with apostrophes properly"""
    check50.include("apostrophe")
    check50.run(f"{EXEC} apostrophe/without/dict apostrophe/with/text").stdout(
        open("apostrophe/outs/without-with")
    ).exit(0)
    check50.run(f"{EXEC} apostrophe/with/dict apostrophe/without/text").stdout(
        open("apostrophe/outs/with-without")
    ).exit(0)
    check50.run(f"{EXEC} apostrophe/with/dict apostrophe/with/text").stdout(
        open("apostrophe/outs/with-with")
    ).exit(0)


@check50.check(compiles)
def case():
    """spell-checking is case-insensitive"""
    check50.include("case")
    check50.run(f"{EXEC} case/dict case/text").stdout(open("case/out")).exit(0)


@check50.check(compiles)
def substring():
    """handles substrings properly"""
    check50.include("substring")
    check50.run(f"{EXEC} substring/dict substring/text").stdout(
        open("substring/out")
    ).exit(0)


@check50.check(compiles)
def large_dict():
    """handles large dictionary (hash collisions) properly"""
    check50.include("large")
    check50.run(f"{EXEC} large/dict large/text").stdout(open("large/out")).exit(0)
