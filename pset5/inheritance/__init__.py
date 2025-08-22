import check50
import check50_rs
import re
import os

@check50.check()
def exists():
    """src/main.rs exists"""
    check50.exists("src/main.rs")


@check50.check(exists)
def compiles():
    """src/main.rs compiles"""
    check50_rs.compile("src/main.rs")

@check50.check(compiles_test)
def correct_size():
    """create_family creates correct size of family"""
    check50.run("./inheritance_test").stdout("size_true.*").exit(0)


@check50.check(compiles_test)
def inheritance_rules_1():
    """create_family follows inheritance rules 1"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compiles_test)
def inheritance_rules_2():
    """create_family follows inheritance rules 2"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compiles_test)
def inheritance_rules_3():
    """create_family follows inheritance rules 3"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compiles_test)
def inheritance_rules_4():
    """create_family follows inheritance rules 4"""
    check50.run("export CHECK50_STATIC_INHERITANCE_ENABLED=1 && ./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compiles_test)
def frees_memory():
    """free_family results in no memory leakages"""
    check50_rs.valgrind("./inheritance").exit(0)
