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
def world():
    """main.rs prints \"hello, world\""""
    check50.run("./target/debug/hello").stdout("hello, world").exit()