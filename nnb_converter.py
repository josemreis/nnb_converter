import json
import re
import argparse
import sys
import os


def parse_args() -> argparse.Namespace:
    """argument parser"""

    ## parse CLI args
    parser = argparse.ArgumentParser(
        prog="nnb_converter.py",
        description="Convert node.js notebook to Markdown or js scripts.",
    )

    parser.add_argument(
        "-f",
        "--file-to-convert",
        dest="file_to_convert",
        type=str,
        help="Node.js notebook file to convert",
    )

    parser.add_argument(
        "-o",
        "--convert-to",
        type=str,
        dest="convert_to",
        default=None,
        help="Convert the nnb file to 'md' or 'js'.",
    )

    # parser.add_argument(
    #         "-f",
    #         "--force-creation",
    #         dest="force_creation",
    #         action="store_true",
    #         default=False,
    #         help="Should it create the annotation projects?",
    #     )

    # parse. If no args display the "help menu"
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    return parser.parse_args()


def parse_nnb(nnb_path: str = "resources/sample.nnb") -> dict:
    """parse a node.js notebook"""
    with open(nnb_path, encoding="utf-8") as fp:
        return json.load(fp).get("cells")


def as_code_block(code: str, language: str = "bash") -> str:
    """create a code block"""
    return "\n".join(["```" + language, code, "```"])


def remove_ansi_escape(text: str) -> str:
    # 7-bit C1 ANSI sequences
    ansi_escape = re.compile(
        r"""
        \x1B  # ESC
        (?:   # 7-bit C1 Fe (except CSI)
            [@-Z\\-_]
        |     # or [ for CSI, followed by a control sequence
            \[
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
    """,
        re.VERBOSE,
    )
    return ansi_escape.sub("", text)


def code_cell_to_md(cell: dict) -> str:
    """covert a code cell to markdown"""
    code_list = cell.get("source")
    output_list = cell.get("outputs")
    out = ""
    for code, output in zip(code_list, output_list):
        code_block = as_code_block(code=code, language=cell.get("language"))
        md_output = ""
        for cur_output in output.get("items"):
            md_output += as_code_block(
                "\n".join(
                    [
                        "## " + remove_ansi_escape(_)
                        for _ in cur_output.get("value")
                        if len(_) > 0
                    ]
                ),
                language="bash",
            )
        out += "\n".join([code_block, md_output])
    return out


def string_to_multiline(text: str, every_n_character: int = 79) -> str:
    """add line breaks every n character"""
    return re.sub("(.{every_n_character})", "\\1\n", text, 0, re.DOTALL)


def markdown_cell_to_comment(cell: dict, **kwargs) -> str:
    """Convert markdown cell to a javascript comment"""
    text = "\n".join([_ for _ in cell.get("source")[0].split("\n") if len(_) > 0])
    return "\n".join(["/*", string_to_multiline(text=text), "*/"])


def nnb_to_script(nnb_parsed: dict, n_vspaces: int = 2) -> str:
    """Parse a nnb_parsed dict into a js script"""
    out = []
    for cell in nnb_parsed:
        lang = cell.get("language")
        if lang == "markdown":
            out.append(markdown_cell_to_comment(cell=cell))
        else:
            out.append("\n".join([_ for _ in cell["source"]]))
    return (n_vspaces * "\n").join(out)


def nnb_to_markdown(nnb_parsed: dict, n_vspaces: int = 2) -> str:
    """Parse a nnb_parsed dict into a js script"""
    out = []
    for cell in nnb_parsed:
        lang = cell.get("language")
        if lang == "markdown":
            out.append("\n".join([_ for _ in cell["source"]]))
        else:
            out.append(code_cell_to_md(cell=cell))
    return (n_vspaces * "\n").join(out)


def main() -> None:
    """main program"""
    args = parse_args()
    nnb_path = args.file_to_convert
    assert args.convert_to in ["md", "js"], '-o/--convert-to only accepts "md" or "js"'
    assert ".nnb" in nnb_path, "input file must be a node.js notebook file(.nnb)"
    # prepare the output path for the converted file
    new_filename = nnb_path.split("/")[-1].replace(".nnb", "." + args.convert_to)
    output_file = os.path.join("/".join(nnb_path.split("/")[0:-1]), new_filename)
    # parse the nnb file
    nnb_parsed = parse_nnb(nnb_path=nnb_path)
    if args.convert_to == "md":
        converted = nnb_to_markdown(nnb_parsed=nnb_parsed)
    else:
        converted = nnb_to_script(nnb_parsed=nnb_parsed)
    # write it
    with open(output_file, "w+") as fp:
        fp.write(converted)
    print(f"[+] The converted file can be found in {output_file}")


if __name__ == "__main__":
    main()
