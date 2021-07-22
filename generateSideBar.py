#Quick script to generate a md index file
#Generate a SideBar from the directory structure.

#for every folder
import glob
import pathlib
import re

class MarkDown:

    def link(self, src, text, space):
        indent = " " * spaces
        return f"* [{text}](src)"

    def heading(self):
        pass

def path_to_markdown(path : pathlib.Path) -> str:
    """

    Convert a path to a markdown link

    :param path:
        Pathlib object
    :return str:
        A markdown link.
    """
    stem = path.stem
    rel_path = path.relative_to(pathlib.Path.cwd())
    if path.is_dir():
        return f"* [{stem}](./{rel_path}/index.md)\n"
    else:
        return f"* [{stem}](./{rel_path})\n"


def make_sidebar_markdown_file(dir: pathlib.Path):
    print(f"Operating on {dir.as_posix()}")
    sidebar_path = dir / '_sidebar.md'
    with open(sidebar_path, 'w') as sidebar_file:
        for markdown_file in dir.iterdir():
            if markdown_file.is_file() and not re.match(r'_|/.', markdown_file.stem):
                sidebar_file.write(path_to_markdown(markdown_file))

def make_index_markdown():
    pass

def make_sidebar_file(dir: pathlib.Path = pathlib.Path.cwd()):
    sidebar_path = dir / '_sidebar.md'

    directories = sorted(glob.glob(dir.as_posix() + '/*/'))
    with open(sidebar_path, 'w') as sidebar_file:
        with open(sidebar_path, 'w') as sidebar_file:
            for markdown_file in directories:
                sidebar_file.write(path_to_markdown(pathlib.Path(markdown_file)))

    index_markdown_file = dir / 'index.md'
    for f in dir.iterdirs():
        #generate index.md




def makeSideBars(dir: pathlib.Path = pathlib.Path.cwd()) -> None:
    """

    Recursivly makes a _sidebar.md file.

    :param dir:
        Pathlib object.
    """

    make_sidebar_markdown_file(dir)

    for sub_dir in dir.iterdir():
        if sub_dir.is_dir():
            #make_index_markdown(sub_dir)
            if not sub_dir.stem.startswith("."):
                makeSideBars(sub_dir)


if __name__ == '__main__':
    make_sidebar_file()


