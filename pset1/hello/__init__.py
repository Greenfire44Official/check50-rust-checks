import check50
import check50_rs


@check50.check()
def exists():
    """src/main.rs exists"""
    check50.exists("src/main.rs")


@check50.check(exists)
def compiles():
    """src/main.rs compiles"""
    check50_rs.compile("src/main.rs")

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./target/debug/hello").stdin("Emma").stdout("Emma").exit()


@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./target/debug/hello").stdin("Rodrigo").stdout("Rodrigo").exit()
