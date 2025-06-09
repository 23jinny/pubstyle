# Packaging Guide for pubstyle

## Quick Summary

- This project uses `pyproject.toml` to define build system requirements and project metadata, adhering to modern Python packaging standards (PEP 517/518).
- Package discovery is configured in `pyproject.toml` using the `[tool.setuptools.packages.find]` table.
- Python version compatibility is declared in `pyproject.toml` via `requires-python` and `classifiers`.

## `pyproject.toml`

The `pyproject.toml` file is the cornerstone of the modern Python packaging system. It specifies the build system (in this case, `setuptools` and `wheel`) and contains most of the project's metadata.

### Understanding `pyproject.toml` Content

The `pyproject.toml` file is organized into several tables (sections denoted by `[]` headers). These tables define how your project is built and declare its metadata. Here's a breakdown of the key parts used in this project:

#### `[build-system]` Table

This section is crucial as it tells build tools (like `pip`) what other tools are needed to build your package and how to drive the build process.

- `requires`: An array of strings specifying the build dependencies. For `pubstyle`, this includes `setuptools>=64` (the package builder) and `wheel` (for creating wheel distributions).
- `build-backend`: A string indicating the Python object (the "backend") that build frontends will use to perform the build. `setuptools.build_meta` is the standard backend for `setuptools`-based projects.

#### `[project]` Table

This is the primary table for declaring static project metadata, as defined by PEP 621.

- `name`: (String) The official name of your package on PyPI (e.g., `"pubstyle"`).
- `version`: (String) The current version of your package (e.g., `"1.0.1"`). It's important to keep this updated for new releases.
- `description`: (String) A short, one-sentence summary of what your project does.
- `readme`: (String or Table) Specifies the file(s) containing the long description for your package, which is shown on PyPI. For `pubstyle`, it's `"README.md"`.
- `requires-python`: (String) A version specifier for the Python versions your project supports (e.g., `">=3.7"`). `pip` will enforce this.
- `license`: (Table) Specifies the license for your project. Common practice is to provide the license text directly or a path to a license file (e.g., `{text = "MIT License"}`).
- `authors`: (Array of Tables) Lists the authors of the project. Each author can have a `name` and `email`.
- `classifiers`: (Array of Strings) A list of Trove classifiers that categorize your project. These help users find your package on PyPI based on its status, audience, supported Python versions, topic, etc.
- `dependencies`: (Array of Strings) A list of packages that your project needs to run. These are the runtime dependencies (e.g., `["matplotlib>=3.3"]`).

#### `[project.urls]` Table

This optional table allows you to list relevant URLs associated with your project.

- Example: `Homepage = "https://github.com/23jinny/pubstyle"`. Other common keys include `Documentation`, `Repository`, `Changelog`, etc.

#### `[project.scripts]` Table

This table defines console scripts that should be created when your package is installed, allowing users to run parts of your package from the command line.

- Each entry maps a script name to a Python entry point (e.g., `"pubstyle-cli" = "pubstyle.cli:main"` creates a command `pubstyle-cli` that runs the `main` function in `pubstyle/cli.py`).

#### `[tool.setuptools.packages.find]` Table

This section is specific to `setuptools` and configures how it discovers your actual Python packages (the directories containing your code).

- `where`: (Array of Strings) Specifies the parent directory (or directories) where `setuptools` should look for packages. `["."]` means it will look in the project root.
- `namespaces`: (Boolean) Typically set to `false`. Set to `true` if you are using PEP 420 namespace packages.

### Package Discovery

Package discovery is now handled entirely by `pyproject.toml` using the `[tool.setuptools.packages.find]` table. This table specifies where `setuptools` should look for your package(s). For this project, it's configured as:

```toml
[tool.setuptools.packages.find]
where = ["."]  # Look for packages in the current directory
namespaces = false
```

This change has allowed for the removal of the `setup.py` file, streamlining the project structure.

## Python Version Compatibility

Python version compatibility is specified in `pyproject.toml`:

- **`requires-python = ">=3.7"`**: This line enforces that the package can only be installed on Python 3.7 or newer. `pip` will prevent installation on older versions.
- **`classifiers`**: The list under `project.classifiers` (e.g., `'Programming Language :: Python :: 3.7'`, `'Programming Language :: Python :: 3.8'`, etc.) informs users and PyPI about the specific Python versions the package is intended to support and has been tested with.

This dual approach ensures both enforcement of a minimum version and clear communication of supported versions.

## Building and Installing

- **Editable install (for development):**

  ```bash
  python -m pip install -e .
  ```

- **Standard install:**

  ```bash
  python -m pip install .
  ```

These commands will use the `pyproject.toml` configuration.


## Auxiliary: Understanding `setup.py` and its Evolution

For many years, the `setup.py` script was the heart of Python packaging. If you've worked with older Python projects, you've undoubtedly encountered it. This section provides a brief overview for context and to highlight why `pyproject.toml` is now the preferred standard.

### The Traditional Role of `setup.py`

A `setup.py` file is a Python script, typically using the `setuptools` library. Its primary responsibilities included:

- **Metadata Declaration:** Defining project metadata like name, version, author, license, dependencies, etc., by passing arguments to the `setup()` function.
- **Package Discovery:** Specifying which Python modules and packages to include in the distribution (e.g., using `find_packages()`).
- **Build Process:** Containing logic to build source distributions (`sdist`) and built distributions like wheels (`bdist_wheel`).
- **Extensibility:** Allowing complex build logic, compilation of C extensions, and custom commands.

Commands like `python setup.py sdist`, `python setup.py bdist_wheel`, and `python setup.py install` were common.

### The Shift to `pyproject.toml`

While `setup.py` was powerful, its executable nature and reliance on `setuptools` by default led to some challenges:

1. **Build System Diversity:** It was hard for tools like `pip` to know which build system a project used (e.g., `setuptools`, `flit`, `poetry`) or what dependencies were needed *just to build the package* without first executing `setup.py`.
2. **Static Metadata Access:** Getting basic metadata often required running `setup.py`, which could have side effects or be slow.
3. **Standardization:** There was a desire for a more declarative and standardized way to specify build requirements and project metadata.

To address these, several Python Enhancement Proposals (PEPs) were introduced:

- **PEP 518 (`pyproject.toml` introduction):** Specified `pyproject.toml` as a way to declare build system dependencies. This allows tools like `pip` to install necessary build tools in an isolated environment *before* attempting to build the package.
- **PEP 517 (Build Backend Interface):** Defined a standard interface between build frontends (like `pip`) and build backends (like `setuptools`, `flit`, `poetry`). This decouples the build process from `setuptools` specifically.
- **PEP 621 (Storing project metadata in `pyproject.toml`):** Standardized how project metadata (name, version, dependencies, etc.) should be stored statically in `pyproject.toml`.

### Key Differences: `setup.py` vs. `pyproject.toml`

| Feature             | `setup.py` (Traditional)                                  | `pyproject.toml` (Modern)                                                                 |
|---------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **Nature**          | Executable Python script                                  | Declarative TOML configuration file                                                       |
| **Build System**    | Implicitly `setuptools` (usually); build deps not declared | Explicitly declares build system and its requirements in `[build-system]` table (PEP 518) |
| **Metadata**        | Defined via `setup()` function calls; dynamic             | Statically defined in `[project]` table (PEP 621) and other tool-specific tables          |
| **Package Discovery** | Often via `find_packages()` in `setup.py`                 | Can be configured in `pyproject.toml` (e.g., `[tool.setuptools.packages.find]`)           |
| **Extensibility**   | High (arbitrary Python code)                              | Primarily declarative; complex build logic might still involve a `setup.py` or build scripts called by the backend |

### The Current Landscape

Today, `pyproject.toml` is the central configuration file.

- For many projects (like `pubstyle` now), `pyproject.toml` can completely replace `setup.py` by handling build system specification, metadata, and package discovery.
- For projects with very complex build requirements (e.g., compiling C extensions with custom flags), a `setup.py` might still exist, but `pyproject.toml` will still be present to declare the build system and its dependencies. The build backend specified in `pyproject.toml` would then invoke `setup.py` or other build scripts as needed.

The move to `pyproject.toml` has brought more clarity, standardization, and robustness to the Python packaging ecosystem.
