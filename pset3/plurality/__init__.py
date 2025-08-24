import check50
import check50_rs
import re

exec = "./target/debug/plurality"


@check50.check()
def exists():
    """src/main.rs exists"""
    check50.exists("src/main.rs")


@check50.check(exists)
def compiles():
    """src/main.rs compiles"""
    check50_rs.compile("src/main.rs")


check50.check(compiles)


@check50.hidden("Did not handle no candidates")
def handles_no_candidates():
    """Handles no candidates"""
    code = check50.run(f"{exec}").exit()
    if not code != 0:
        raise check50.Failure("Did not handle no candidates")


@check50.check(compiles)
@check50.hidden("Rejected one candidates (MAX=9)")
def accepts_one_candidates():
    """Accepts one candidates"""
    process = check50.run(f"{exec} Alice")
    try:
        process.exit(0, timeout=5)
    except check50.Failure as e:
        if str(e) != "timed out while waiting for program to exit":
            raise check50.Failure("ejected MAX candidates (MAX=9)")


@check50.check(compiles)
@check50.hidden("Rejected MAX candidates (MAX=9)")
def accepts_max_candidates():
    """Accepts MAX candidates"""
    process = check50.run(f"{exec} 1 2 3 4 5 6 7 8 9")
    try:
        process.exit(0, timeout=5)
    except check50.Failure as e:
        if str(e) != "timed out while waiting for program to exit":
            raise check50.Failure("ejected MAX candidates (MAX=9)")


@check50.check(compiles)
@check50.hidden("Did not reject too many candidates (MAX=9)")
def handles_too_many_candidates():
    """Rejects too many candidates"""
    code = check50.run(f"{exec} 1 2 3 4 5 6 7 8 9 10").exit()
    if not code != 0:
        raise check50.Failure("Did not reject too many candidates (MAX=9)")


@check50.check(compiles)
@check50.hidden("Did not identify Alice as winner of election")
def print_winner0():
    """Identifies Alice as winner of election"""
    out = test(number_of_votes=10, votes=["Alice"] * 8 + ["Bob"] * 2)
    check_winner(out, "Alice\n")


@check50.check(compiles)
@check50.hidden("Did not identify Bob as winner of election")
def print_winner1():
    """Identifies Bob as winner of election"""
    out = test(number_of_votes=10, votes=["Alice"] + ["Bob"] * 8 + ["Charlie"])
    check_winner(out, "Bob\n")


@check50.check(compiles)
@check50.hidden("Did not identify Charlie as winner of election")
def print_winner2():
    """Identifies Charlie as winner of election"""
    out = test(number_of_votes=18, votes=["Alice"] + ["Bob"] * 8 + ["Charlie"] * 9)
    check_winner(out, "Charlie\n")


@check50.check(compiles)
@check50.hidden("Did not print both winners of election")
def print_winner3():
    """Prints multiple winners in case of tie"""
    result = test(
        number_of_votes=21, votes=["Alice"] * 8 + ["Bob"] * 8 + ["Charlie"] * 5
    )
    if set(result.split("\n")) - {""} != {"Alice", "Bob"}:  # type: ignore
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)


@check50.check(compiles)
@check50.hidden("Did not print all three winners of election")
def print_winner4():
    """Prints all names when all candidates are tied"""
    result = test(
        number_of_votes=24, votes=["Alice"] * 8 + ["Bob"] * 8 + ["Charlie"] * 8
    )
    if set(result.split("\n")) - {""} != {"Alice", "Bob", "Charlie"}:  # type: ignore
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)


# Note that check needs to be unhidden in order for help to be displayed
def check_winner(result, correct):
    if result == correct:
        return

    help = None
    r = result.rstrip()
    c = correct.rstrip()
    if r == c:
        if result[-1] == "\n":
            if result[-2].isspace():
                help = "did you print an extra space?"
        elif result[-1].isspace():
            help = "did you print a space instead of a newline?"
        else:
            help = "did you forget the newline after the name?"

    raise check50.Mismatch(correct, result, help=help)


def test(
    number_of_votes: int, votes: list[str], candidates=["Alice", "Bob", "Charlie"]
):
    program = check50.run(f"{exec} " + " ".join(candidates)).stdin(str(number_of_votes))
    for vote in votes:
        program.stdin(vote)
    return program.stdout()
