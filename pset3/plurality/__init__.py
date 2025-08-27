import check50
import check50_rs


exec = "./target/debug/plurality"
a, b, c, d, e, f, g, h, i, j = (
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Earl",
    "Frank",
    "Grace",
    "Heidi",
    "Ivan",
    "Judy",
)


@check50.check()
def exists():
    """src/main.rs exists"""
    check50.exists("src/main.rs")


@check50.check(exists)
def compiles():
    """src/main.rs compiles"""
    check50_rs.compile("src/main.rs")


@check50.check(compiles)
def handles_no_candidates():
    """Handles no candidates"""
    code = check50.run(f"{exec}").exit()
    if not code != 0:
        raise check50.Failure("Did not handle no candidates")


@check50.check(handles_no_candidates)
def accepts_one_candidate():
    """Accepts one candidate"""
    check50_rs.run_and_wait(f"{exec} {a}")


@check50.check(accepts_one_candidate)
def accepts_max_candidates():
    """Accepts MAX candidates"""
    check50_rs.run_and_wait(f"{exec} {a} {b} {c} {d} {e} {f} {g} {h} {i}")


@check50.check(accepts_max_candidates)
def handles_too_many_candidates():
    """Rejects too many candidates"""
    code = check50.run(f"{exec} {a} {b} {c} {d} {e} {f} {g} {h} {i} {j}").exit()
    if not code != 0:
        raise check50.Failure("Did not reject too many candidates (MAX=9)")


@check50.check(handles_too_many_candidates)
def handles_duplicate_candidates():
    """Rejects duplicate candidates"""
    code = check50.run(f"{exec} {a} {b} {a}").exit()
    if not code != 0:
        raise check50.Failure("Did not reject duplicate candidates")


# Note: Plurality is expected to skip the vote on invalid input, unlike runoff or tideman
# which are expected to exit with an error code
@check50.check(handles_duplicate_candidates)
def handles_invalid_candidates():
    """Skips invalid candidate vote"""
    # Cast one invalid vote for candidate 'c' (not in the list), expect no votes counted
    result = test(number_of_votes=1, votes=[c], candidates=[a, b], number_of_winners=2)
    # Both candidates should be tied at 0 votes, so both names should be printed
    if set(result.split("\n")) - {""} != {a, b}:
        raise check50.Failure("Did not skip invalid candidate vote")


@check50.check(handles_invalid_candidates)
def print_winner0():
    """Identifies Alice as winner of election"""
    result = test(number_of_votes=3, votes=[a] * 2 + [b] * 1)
    check_winner(result, f"{a}\n")


@check50.check(handles_invalid_candidates)
def print_winner1():
    """Identifies Bob as winner of election"""
    result = test(number_of_votes=4, votes=[a] + [b] * 2 + [c])
    check_winner(result, f"{b}\n")


@check50.check(handles_invalid_candidates)
def print_winner2():
    """Identifies Charlie as winner of election"""
    result = test(number_of_votes=6, votes=[a] + [b] * 2 + [c] * 3)
    check_winner(result, f"{c}\n")


@check50.check(handles_invalid_candidates)
def print_winner_complex():
    """Handles complex vote"""
    votes: list[str] = [a] * 3 + [b] * 2 + [c] + [d] * 2 + [e]
    result = test(number_of_votes=9, votes=votes, candidates=[a, b, c, d, e])
    check_winner(result, f"{a}\n")


@check50.check(handles_invalid_candidates)
def print_winner3():
    """Prints multiple winners in case of tie"""
    votes: list[str] = [a] * 2 + [b] * 2 + [c]
    result = test(
        number_of_votes=5,
        votes=votes,
        number_of_winners=2,
    )
    if set(result.split("\n")) - {""} != {a, b}:  # type: ignore
        raise check50.Mismatch(f"{a}\n{b}\n", result)


@check50.check(handles_invalid_candidates)
def print_winner4():
    """Prints all names when all candidates are tied"""
    votes: list[str] = [a] * 2 + [b] * 2 + [c] * 2
    result = test(
        number_of_votes=6,
        votes=votes,
        number_of_winners=3,
    )
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
    votes: list[str],
    candidates=[a, b, c],
    number_of_winners=1,
):
    program = check50.run(f"{exec} " + " ".join(candidates)).stdin(
        str(number_of_votes), prompt=False
    )
    check50.log("────────────────────────")
    for vote in votes:
        program.stdin(vote, prompt=False)
        check50.log("────────────────────────")
    out: list[str] = program.stdout().split()[-number_of_winners:]  # type: ignore
    result = ""
    for line in out:
        result += line + "\n"
    check50.log(f"Output:")
    check50.log(result)
    return result
