import check50
import check50_rs
import re
import os

EXEC = "./target/debug/inheritance"


@check50.check()
def exists():
    """src/main.rs exists"""
    check50.exists("src/main.rs")


@check50.check(exists)
def compiles():
    """src/main.rs compiles"""
    check50_rs.compile("src/main.rs")


@check50.check(compiles)
def correct_size():
    """create_family creates correct size of family"""
    process = check50.run(f"{EXEC}")
    out = process.stdout()
    lines: list = out.rstrip().lstrip().split("\n")  # type: ignore
    if len(lines) != 7:
        raise check50.Failure(
            f"Incorrect family lenght or formatting. Expected 7 lines, got {len(lines)}"
        )


@check50.check(compiles)
def inheritance_rules_1():
    """create_family follows inheritance rules 1"""
    process = check50.run(f"{EXEC}")
    out = process.stdout()
    check_output(out)


@check50.check(compiles)
def inheritance_rules_2():
    """create_family follows inheritance rules 2"""
    process = check50.run(f"{EXEC}")
    out = process.stdout()
    check_output(out)


@check50.check(compiles)
def inheritance_rules_3():
    """create_family follows inheritance rules 3"""
    process = check50.run(f"{EXEC}")
    out = process.stdout()
    check_output(out)


@check50.check(compiles)
def inheritance_rules_4():
    """create_family follows inheritance rules 4"""
    process = check50.run(f"{EXEC}")
    out = process.stdout()
    check_output(out)


@check50.check(compiles)
def output_is_random():
    """output is random"""
    out1 = check50.run(f"{EXEC}").stdout()
    out2 = check50.run(f"{EXEC}").stdout()
    out3 = check50.run(f"{EXEC}").stdout()
    # The chances of 3 outputs to match are about 0.0000000001601794%
    # (accounting for the restrictions of a valid output which reduce the number of possible outputs).
    if out1 == out2 and out2 == out3:
        raise check50.Failure("Output is not randomized.")


def check_output(output):
    lines = output.rstrip().lstrip().split("\n")
    people: list[Person] = []
    child = None

    for line in lines:
        check50.log(f"{line}")
        words = line.split()
        current = Person(words[0], words[-1])
        match words[0]:
            case "Child":
                if child:
                    raise check50.Failure(
                        "Too many childs. Only one Child is expected."
                    )
                people.append(current)
            case "Parent":
                if not people[0].add_parent(current):
                    raise check50.Failure(
                        f"Could not add {line} as a parent. Make sure only 2 parents are output."
                    )
                people.append(current)
            case "Grandparent":
                for person in people:
                    if person.generation == "Parent" and not person.has_both_parents():
                        if not person.add_parent(current):
                            raise check50.Failure(
                                f"Could not add {line} as a parent. Make sure only 2 parents are output."
                            )
                people.append(current)
            case _:
                raise check50.Failure(f"Invalid person generation: {words[0]}")
    for person in people:
        if not person.alleles_are_valid():
            raise check50.Failure(
                f"Invalid alleles {person.alleles} on person of generation {person.generation}.\n    {person.generation}'s parents' alleles: {person.parents[0].alleles}, {person.parents[1].alleles}"
            )


class Person:
    def __init__(self, generation, alleles) -> None:
        self.generation = generation
        self.alleles: str = alleles
        self.parents: list[Person] = []

    def alleles_are_valid(self) -> bool:
        if len(self.parents) == 0:
            return True

        if not len(self.parents) == 2:
            return False

        for allele in self.alleles:
            valid = False
            for parent in self.parents:
                if allele in parent.alleles:
                    valid = True
            if not valid:
                return False
        return True

    def add_parent(self, parent):
        if not len(self.parents) < 2:
            return False
        self.parents.append(parent)
        return True

    def has_both_parents(self) -> bool:
        if len(self.parents) == 2:
            return True
        return False
