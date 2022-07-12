# BEGIN_IMPORTS
from argparse import ArgumentParser, Namespace
from json import load
from os import getcwd, listdir, mkdir
from os.path import exists
from pathlib import Path
from shutil import copy
from typing import Any, Dict, Iterable, List, Tuple

JSON_VALIDATE: bool

try:
    from jsonschema import validate
    JSON_VALIDATE = True
except (ImportError,):
    JSON_VALIDATE = False
# END_IMPORTS

# BEGIN_CONSTANTS
CWD: str = str(Path(__file__).parents[0]).replace("\\", "/")
USER_CWD: str = getcwd().replace("\\", "/")
PATH_TO_DIR_SCHEMAS: str = CWD + "/schemas/"
PATH_TO_DIR_TEMPLATES: str = CWD + "/templates/"
THIS_REPOSITORY: str = "https://github.com/nicdgonzalez/Templates"
# END_CONSTANTS

# BEGIN_GLOBALS
parser: ArgumentParser = ArgumentParser()
fmt: Dict[str, Any]
# END_GLOBALS

# BEGIN_SCHEMAS
schemas: Dict[str, Dict[str, Any]] = {}

if (JSON_VALIDATE):
    schemas["argument"] = {}

for (file) in listdir(PATH_TO_DIR_SCHEMAS):
    # Split into ['name', 'schema.json'] then use 'name' for the key.
    key: str = file.split(".", maxsplit=1)[0]
    schemas[key] = load(open((PATH_TO_DIR_SCHEMAS + file), "r"))
# END_SCHEMAS


# BEGIN_FLAGS
def add_arguments(flags: Iterable[Dict[str, Any]]) -> None:
    global schemas, parser

    for (options) in tuple(flags):
        options[""] = list(options[""])

        if (JSON_VALIDATE):
            assert (schemas["argument"] != {}), (
                "Missing schema for 'Argument' object. Go to '%s' for a copy."
                % (THIS_REPOSITORY)
            )
            validate(options, schemas["argument"])

        name_or_flags: Tuple[str, ...] = tuple(options.pop(""))
        parser.add_argument(*name_or_flags, **options)

    return None


args: Namespace = None

with open(CWD + "/flags.json", "r") as f:
    add_arguments(load(f)["flags"])
    args = parser.parse_args()
    fmt = {**{k: v for k, v in args._get_kwargs()}}
# END_FLAGS

# BEGIN_FILES
files: List[Tuple[str, str]] = []  # [(dest, source), ...]

assert (args.directory), (
    "Either the definition for '-d/--directory' flag is missing in "
    "'flags.json' or the 'required' option is not set to ``true``."
)

fmt["directory"] = args.directory.replace(".", USER_CWD)
buffer: str = fmt["directory"]
buffer_copy: str = buffer


def read_template_map(template_map: Dict[str, Any]) -> None:
    global buffer, files

    for (dir_name, dir_content) in template_map.items():
        if (isinstance(dir_content, dict)):
            buffer += dir_name
            read_template_map(dir_content)
            # TODO: All directories should eventually be created whether
            # there is a default file in it or not.

            # Move all code block from `for f in files` to here and
            # create dirs from here.
        elif (isinstance(dir_content, list)):
            for (file_map) in dir_content:
                d, s = file_map.split("::", maxsplit=1)
                dest: str = buffer + "/" + d
                source: str = PATH_TO_DIR_TEMPLATES + s
                files.append((dest, source))

    global buffer_copy
    buffer = buffer_copy

    return None


names: Dict[str, str] = {
    "Project": args.name,
    "project": args.name.lower(),
    "PROJECT": args.name.upper()
}

fmt = {**fmt, **names}

with open(CWD + "/template_map.json", "r") as f:
    data: Dict[str, Any] = load(f)
    read_template_map(data["all"])
    if args.language != "null":
        read_template_map(data[args.language])

for (target, template) in files:
    target = target.format(**fmt)
    template = template.format(**fmt)

    directories: List[str] = (
        target[target.index(":") + 1:]
        .replace(USER_CWD[USER_CWD.index(":") + 1:], "")
        .rsplit("/", maxsplit=1)[0]
        .split("/")
    )

    buffer = USER_CWD

    for d in directories:
        buffer += ("/" + d) * (not not d)
        if not exists(buffer):
            mkdir(buffer)

    # try except else block instead of if png

    if (target.rsplit(".", maxsplit=1)[1]) in ("png", "jpeg", "gif"):
        copy(template, target)
    else:
        with open(template, "r") as f:
            template_content: str = (
                "\n"
                .join(
                    line.strip("\n").format(**fmt)
                    for line
                    in f.readlines()
                )
            )

        with open(target, 'w+') as f:
            f.write(template_content)

    # Also make a fallback to atleast copy the files if it can't format it
# END_FILES
