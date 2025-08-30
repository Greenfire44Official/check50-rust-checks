import check50
import check50_rs
from PIL import Image

EXEC = "target/debug/filter"

FILES = files = [
    "3x3.bmp",
    "4x4.bmp",
    "19x19.bmp",
]


class Tests:
    input = "test_images/input/"

    class output:
        base = "test_images/output/"
        reflect = base + "reflect/"
        grayscale = base + "grayscale/"
        blur = base + "blur/"
        sepia = base + "sepia/"
        edge = base + "edge/"


@check50.check()
def exists():
    """src/main.rs exists"""
    check50.exists("src/main.rs")
    check50.include("../test_images")


@check50.check(exists)
def compiles():
    """src/main.rs compiles"""
    check50_rs.compile("src/main.rs")


@check50.check(compiles)
def reflect_3x3():
    check50.log("testing 3x3...")
    run_test(Tests.input + FILES[0], Tests.output.reflect + FILES[0], "r")


@check50.check(compiles)
def reflect_4x4():
    check50.log("testing 4x4...")
    run_test(Tests.input + FILES[1], Tests.output.reflect + FILES[1], "r")


@check50.check(compiles)
def grayscale_3x3():
    check50.log("testing 3x3...")
    run_test(Tests.input + FILES[0], Tests.output.grayscale + FILES[0], "g")


@check50.check(compiles)
def grayscale_4x4():
    check50.log("testing 4x4...")
    run_test(Tests.input + FILES[1], Tests.output.grayscale + FILES[1], "g")


@check50.check(compiles)
def grayscale_19x19():
    check50.log("testing 19x19...")
    run_test(Tests.input + FILES[2], Tests.output.grayscale + FILES[2], "g")


@check50.check(compiles)
def blur_3x3():
    check50.log("testing 3x3...")
    run_test(Tests.input + FILES[0], Tests.output.blur + FILES[0], "b")


@check50.check(compiles)
def blur_4x4():
    check50.log("testing 4x4...")
    run_test(Tests.input + FILES[1], Tests.output.blur + FILES[1], "b")


@check50.check(compiles)
def blur_19x19():
    check50.log("testing 19x19...")
    run_test(Tests.input + FILES[2], Tests.output.blur + FILES[2], "b")


@check50.check(compiles)
def edge_3x3():
    check50.log("testing 3x3...")
    run_test(Tests.input + FILES[0], Tests.output.edge + FILES[0], "e")


@check50.check(compiles)
def edge_4x4():
    check50.log("testing 4x4...")
    run_test(Tests.input + FILES[1], Tests.output.edge + FILES[1], "e")


@check50.check(compiles)
def edge_19x19():
    check50.log("testing 19x19...")
    run_test(Tests.input + FILES[2], Tests.output.edge + FILES[2], "e")


def open_image(path: str) -> list[list]:
    try:
        pixels = None
        with Image.open(path) as img:
            width = img.size[0]
            pixels = list(img.getdata())

        if pixels == None:
            raise check50.Failure("Could not get image pixel data.")

        return pixels
    except FileNotFoundError:
        raise check50.Failure(f"Error: The specified BMP file was not found: {path}")
    except Exception as e:
        raise check50.Failure(f"An error occurred: {e}")


def run_test(test_image_path, expected_output_path, filter):
    expected_output_pixels = open_image(expected_output_path)
    check50.run(f"{EXEC} -{filter} {test_image_path} output.bmp").exit(0)
    output_pixels = open_image("output.bmp")
    check50.log("checking output...")
    if output_pixels != expected_output_pixels:
        raise check50.Failure("Output did not match expected output.")
