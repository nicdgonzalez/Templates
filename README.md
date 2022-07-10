<div align="center">
    <h1>Templates</h1>
    <img src="./templates/images/py.png" alt="template_banner" />
</div>

## Table of Contents

* [Introduction](#introduction)
* [Technologies Used](#technologies-used)
* [Project Status](#project-status)
* [Version Naming](#version-naming)
* [Setup](#setup)
* [Usage](#usage)
* [Contributing](#contributing)
* [Bug / Feature Request](#bug--feature-request)
* [Room for Improvement](#room-for-improvement)
* [Additional Information](#additional-information)

## Introduction

<!-- Buttons -->

**Templates** is a utility for creating dynamic project templates.

Instead of having a generic copy/paste-able directory for starting new
projects, where after copying you still have to go in and continue setting
up, this library allows you to create organized template files with
{variable names} which can be defined later on when you are actually using
the template. 

## Technologies Used

* Windows OS (x64)
* Python 3.10.5

## Project Status

This project is currently *in development*.

## Version Naming

This library uses semantic versioning:

```
MAJOR.MINOR.PATCH
```

Where an increment in:

* `MAJOR` = Incompatible changes (may require code to be updated).
* `MINOR` = Backwards compatible feature changes.
* `PATCH` = Backwards compatible bug fixes.

## Setup

Getting started...

* Download the [latest version](https://github.com/nicdgonzalez/Templates)
  of this project from GitHub.

* From the command line, find the root directory of the project.
  To install the project, run:

```powershell
# This should automatically put the library into PYTHONPATH.
# This way it can be called by name (templates) instead of by absolute path.
> pip install "."
```

* Now for demonstration purposes, we will create a dummy project using
  one of the templates I created:

```powershell
# Go to a different directory (to showcase that this works from anywhere):
cd ../../

# Make a new directory named 'Testing':
mkdir "Testing"

# Run 'templates' to set up a new Python project named 'TestLib' in 'Testing':
python -m "templates" --directory ./"Testing" --language py --name "TestLib" --repository "https://github.com/nicdgonzalez/TemplatesExample"
```

> **Note**
> Run `python -m "templates" -h` to open the help menu and see all of the
> available arguments/flags.

## Usage

Provide use cases and real world code examples here.

### Adding/Editing the Standard Templates

* Step 1:

```
```

* Step 2:

```
```

> **Warning**
> A warning message.

### Adding/Editing Argument Flags

* Step 1:

```
```

* Step 2:

```
```

> **Note**
> The values from the argument flags are automatically added to the Format
> parameters and ready to use in your templates.

> **Warning**
> A warning message.

## Contributing

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

* Fork the repository.

* Create a new branch

```powershell
> git checkout -b "improve-feature"
```

* Make the appropriate changes in the files.

* Stage the modified files.

```powershell
> git add <file(s)>
```

* Commit changes.

```powershell
> git commit -m "Improve feature."
```

* Push to the branch.

```powershell
> git push "origin" "improve-feature"
```

* Create a [Pull Request](https://github.com/nicdgonzalez/Templates/pulls).

## Bug / Feature Request

If you find a bug (program failed to run and/or gave undesired results)
or you just want to request a feature, kindly open a new issue
[here](https://github.com/nicdgonzalez/Templates/issues).

## Room for Improvement

Areas that could use improvement:

- [ ] Code organization.

Unimplemented features:

- [ ] (?) Rewrite and/or make it class-based instead of a script.

> **Note**
> Features marked with *(?)* indicate that it is unconfirmed whether the feature
> will/will not undergo development.

## Additional Information

* Created by [Nicolas Gonzalez](https://github.com/nicdgonzalez)
  -- feel free to contact me!
