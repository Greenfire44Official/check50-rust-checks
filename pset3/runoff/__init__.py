import check50
import check50_rs
import re

exec = "./target/debug/runoff"
a, b, c, d = "Alice", "Bob", "Charlie", "David"


@check50.check()
def exists():
    """src/main.rs exists"""
    check50.exists("src/main.rs")


@check50.check(exists)
def compiles():
    """src/main.rs compiles"""
    check50_rs.compile("src/main.rs")


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
            raise check50.Failure("Rejected MAX candidates (MAX=9)")


@check50.check(compiles)
@check50.hidden("Rejected MAX candidates (MAX=9)")
def accepts_max_candidates():
    """Accepts MAX candidates"""
    process = check50.run(f"{exec} 1 2 3 4 5 6 7 8 9")
    try:
        process.exit(0, timeout=5)
    except check50.Failure as e:
        if str(e) != "timed out while waiting for program to exit":
            raise check50.Failure("Rejected MAX candidates (MAX=9)")


@check50.check(compiles)
@check50.hidden("Did not reject too many candidates (MAX=9)")
def handles_too_many_candidates():
    """Rejects too many candidates"""
    code = check50.run(f"{exec} 1 2 3 4 5 6 7 8 9 10").exit()
    if not code != 0:
        raise check50.Failure("Did not reject too many candidates (MAX=9)")


@check50.check(compiles)
@check50.hidden("Did not reject invalid candidate")
def handles_invalid_candidates():
    """Rejects invalid candidate"""
    code = check50.run(f"{exec} {a} {b}").stdin("1").stdin(c).exit(1)


@check50.check(compiles)
# @check50.hidden("Did not identify Alice as winner of election")
def print_winner0():
    """Identifies Alice as winner of election"""
    votes: list[list[str]] = [[a, b, c]] * 3 + [[b, c, a]] * 2 + [[c, a, b]]
    result = test(number_of_votes=6, votes=votes)
    check_winner(result, "Alice\n")


@check50.check(compiles)
# @check50.hidden("Did not identify Alice as winner of election")
def print_winner1():
    """Identifies Bob as winner of election"""
    votes: list[list[str]] = [[b, a, c]] * 3 + [[a, c, b]] * 2 + [[c, a, b]]
    result = test(number_of_votes=6, votes=votes)
    check_winner(result, "Bob\n")


@check50.check(compiles)
# @check50.hidden("Did not identify Alice as winner of election")
def print_winner2():
    """Identifies Charlie as winner of election"""
    votes: list[list[str]] = [[c, b, a]] * 3 + [[b, c, a]] * 2 + [[a, a, c]]
    result = test(number_of_votes=6, votes=votes)
    check_winner(result, "Charlie\n")


@check50.check(compiles)
@check50.hidden("Did not identify Alice as winner of election")
def print_winner_complex():
    """Handles complex vote"""
    votes: list[list[str]] = (
        [[a, b, c, d]] * 9
        + [[b, a, c, d]] * 6
        + [[c, a, b, d]] * 3
        + [[c, b, a, d]] * 2
        + [[d, a, b, c]] * 2
        + [[d, b, a, c]] * 2
    )
    result = test(number_of_votes=24, votes=votes, candidates=[a, b, c, d])
    check_winner(result, "Alice\n")


@check50.check(compiles)
@check50.hidden("Did not print both winners of election")
def print_winner3():
    """Prints multiple winners in case of tie"""
    votes: list[list[str]] = [[a, b, c], [b, c, a]]
    result = test(number_of_votes=2, votes=votes, number_of_winners=2)
    if set(result.split("\n")) - {""} != {a, b}:  # type: ignore
        raise check50.Mismatch(f"{a}\n{b}\n", result)


@check50.check(compiles)
@check50.hidden("Did not print all three winners of election")
def print_winner4():
    """Prints all names when all candidates are tied"""
    votes: list[list[str]] = [[a, b, c], [b, c, a], [c, a, b]]
    result = test(number_of_votes=3, votes=votes, number_of_winners=3)
    if set(result.split("\n")) - {""} != {a, b, c}:  # type: ignore
        raise check50.Mismatch(f"{a}\n{b}\n{c}\n", result)


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
    number_of_votes: int,
    votes: list[list[str]],
    candidates=["Alice", "Bob", "Charlie"],
    number_of_winners=1,
):
    program = check50.run(f"{exec} " + " ".join(candidates)).stdin(
        str(number_of_votes), prompt=False
    )
    for vote in votes:
        for rank in vote:
            program.stdin(rank, prompt=False)
    out: list[str] = program.stdout().split()[-number_of_winners:]  # type: ignore
    result = ""
    for line in out:
        result += line + "\n"
    check50.log(result)
    return result
