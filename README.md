
# check50-rust-checks

A project that aims to recreate all the checks for CS50x's C problems (weeks 1–5) in Rust.

Created when I challenged myself to recreate cs50's problems in Rust and needed some way to check the validity of the solutions.

These checks use my own [check50_rs](https://github.com/Greenfire44Official/check50_rs) extension for running Rust programs with check50.

If you want to use a different extension, you can:
- Modify the dependencies in each test's `.cs50.yaml` file.
- Update the imports and functions in each test's `__init__.py` file.
- Use your editor's find-and-replace to swap references to `check50_rs` with your own extension.

**WORK IN PROGRESS**

[Current Progress](#progress)

## How to Use

> **Note:**  
> check50's remote server does **not** include Cargo or Rust.  
> These checks are intended for **local use only**.

### Prerequisites

- [Install check50](https://cs50.readthedocs.io/projects/check50/en/latest/#installation)
- [Install Rust and Cargo](https://www.rust-lang.org/tools/install)

### Installation & Usage

1. **Clone the repository:**
  ```bash
  git clone https://github.com/Greenfire44Official/check50-rust-checks.git
  ```

2. **Navigate to your Rust package directory** (where `Cargo.toml` is located).  
  **Do not** cd into the `src` folder or the root of a Cargo workspace (If you are using a Cargo workspace).

  Your package should follow the default Cargo structure:
  ```plaintext
  [package name]
  ├── src
  │   └── main.rs      # Required. Must be named main.rs
  ├── Cargo.toml       # Required
  ├── Cargo.lock       # Optional
  └── ...              # Other files ignored
  ```

  If your package structure is different, you can modify the check's `.cs50.yaml` and `__init__.py` files to match.

3. **Run check50 locally with the `--dev` flag:**
  ```bash
  cs50 --dev [path to the folder of the test you want to run]
  ```

  - The path must be to the folder, **not** to `__init__.py` or `.cs50.yaml`.
  - Example for mario-more:
    ```bash
    cs50 --dev [path to check50-rust-checks]/pset1/mario/more
    ```

---


## Troubleshooting

- **ModuleNotFoundError: No module named 'check50_rs'**  
  Install the extension manually:
  ```bash
  pip install git+https://github.com/Greenfire44Official/check50_rs.git
  ```

  - On WSL, add `--break-system-packages`:
    ```bash
    pip install git+https://github.com/Greenfire44Official/check50_rs.git --break-system-packages
    ```

  - To force reinstall (In case of corrupted install):
    ```bash
    pip install --force git+https://github.com/Greenfire44Official/check50_rs.git
    ```

- **Other issues:**  
  Before opening an issue, please ensure:
  - Your issue is not described above.
  - All prerequisites are installed.
  - You've re-read [Installation & Usage](#installation--usage) and made sure you followed the instructions correctly.
  - The code you're testing compiles with `cargo build` or `cargo run`.
  - Your project (package) follows the default folder structure.

  If you still have problems, you can submit an issue here (not on cs50/problems) and I'll try my best to help, just know that I'm still learning, so I may not be able to provide advanced troubleshooting.

---


## Progress

| Status | Meaning |
|--------|---------|
| ✅     | Tested and working |
| ⛔️     | Partial completion / Not tested |
| ❌     | Not tested |

```bash
check50-rust-checks
├── pset1 ✅
│   ├── cash ✅
│   ├── credit ✅
│   ├── hello ✅
│   ├── mario ✅
│   │   ├── less ✅
│   │   └── more ✅
│   ├── me ✅
│   └── world ✅
├── pset2 ✅
│   ├── caesar ✅
│   ├── readability ✅
│   ├── scrabble ✅
│   └── substitution ✅
├── pset3 ✅
│   ├── plurality ✅ 
│   ├── runoff ✅
│   └── tideman ✅
├── pset4 ✅
│   ├── filter ✅
│   │   ├── less ✅
│   │   └── more ✅
│   ├── recover ✅
│   └── volume ✅
├── pset5 ⛔️
│   ├── inheritance ⛔️
│   └── speller ❌
└── pset6 ❌
    └── dna ❌
```
