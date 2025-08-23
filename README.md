# check50-rust-checks
A project that aims to recreate all the checks for cs50x's c problems (weeks 1-5) but for rust.\
Created when I challenged myself to recreate cs50's problems in Rust and needed some way to check the validity of the solutions.

These checks use my own check50 extension for running rust programs:\
https://github.com/Greenfire44Official/check50_rs \
If you want to use a different extension or create your own you can modify the dependencies on each test's .cs50.yaml file and modify the imports and the functions on each test's \_\_init__.py file (you can do this easily by using the find and replace function in your preferred text editor to replace any reference to check50_rs with your own extension).

**WORK IN PROGRESS**\
[Current Progress](#progress)

## How to use

Since check50's remote server does not come with cargo (and I doubt there's a way to add it as a requirement) it is not possible to use this for online checks.\
I haven't tested compiling with rustc, but if cargo is not installed on the server, I doubt rustc is either.\
In order to use this extension you have to run it locally.

### Pre-requisites
Install check50:\
https://cs50.readthedocs.io/projects/check50/en/latest/#installation 

Since you are going to be running the tests locally make sure that you have everything you need to compile your rust code and packages:\
https://www.rust-lang.org/tools/install 

### Installing and using
First clone the repository `git clone https://github.com/Greenfire44Official/check50-rust-checks.git` or download the code.\
Then cd into the root directory of the project/package where Cargo.toml is located **not the src folder.** and also **not the root folder of the cargo workspace** (if you are working on a cargo workspace).

By default, the checks requires that the packages are created using the default cargo folder structure.\
That is:
```bash
└── [package name]
    ├── src
    │   ├── main.rs <-- Required. Important: do not change the name of the source file. It **must** be main.rs
    ├── Cargo.lock <-- Will be included if it exists, but it's not required.
    ├── Cargo.toml <-- Required.
    └── * <-- Any other file will be excluded.
```
If your package does not follow this folder structure the check will fail.\
However, you **are** running this locally, so there's nobody stopping you from modifying the check's .cs50.yaml and \_\_init__.py to support your custom folder structure.

Now run check50 using the --dev flag. (If you run it without the --dev flag, even if you are using the --local or --offline flags, the test won't work. I haven't figured out why)\
`cs50 --dev [path to the **folder** of the test you want to run]` (the path **must** be of the folder, not to the \_\_init__.py, nor the .cs50.yaml files. It **must** be the folder.

For example, running the test for mario-more the command would look like:\
`cs50 --dev [path to check50-rust-checks's root folder]/pset1/mario/more`

The test should now run. If the test doesn't run or you encounter a different problem you can create an issue if **(and only if)**:\
+ Your issue is not described in [Basic troubleshooting](#basic-troubleshooting).
+ You've installed all the pre-requisites.
+ You're sure you followed the instructions correctly.
+ You're sure that the code you are testing compiles correctly using `cargo build` or `cargo run`.
+ Your cargo project follows the default folder file structure described in [Installing and using](#installing-and-using).

Once you've made sure of those points, if you still have problems you can submit an issue and I'll attempt to help you. Just take into consideration that I'm still learning to code and won't be able to provide advanced troubleshooting.\
If you open an issue please make sure that you open it here in check50-rust-checks, **NOT** on cs50/problems.

## Basic troubleshooting
If you get the following error: `ModuleNotFoundError: No module named 'check50_rs'` It likely means that check50 did not automatically install the check50_rs extension. You can manually install it using pip:\
`pip install git+https://github.com/Greenfire44Official/check50_rs.git` \
If you are using WSL you will likely encounter an error like: `error: externally-managed-environment` To fix this add the `--break-system-packages` flag like so:\
`pip install git+https://github.com/Greenfire44Official/check50_rs.git --break-system-packages` \
Additionally if you get a message about the package already being installed and you still get the same package not found error you can force a reinstallation of the package adding the `--force` flag.


## Progress
✅ Problem checks that have been tested to work.
⛔️ Partial completion
❌ Not tested
```bash
├── pset1✅
│   ├── cash✅
│   ├── credit✅
│   ├── hello✅
│   ├── mario✅
│   │   ├── less✅
│   │   └── more✅
│   ├── me✅
│   └── world✅
├── pset2✅
│   ├── caesar✅
│   ├── readability✅
│   ├── scrabble✅
│   └── substitution✅
├── pset3⛔️
│   ├── plurality⛔️
│   ├── runoff⛔️
│   └── tideman⛔️
├── pset4⛔️
│   ├── filter❌
│   │   ├── less❌
│   │   └── more❌
│   ├── recover⛔️
│   └── volume⛔️
├── pset5⛔️
│   ├── inheritance⛔️
│   └── speller❌
└── pset6❌
    └── dna
```
