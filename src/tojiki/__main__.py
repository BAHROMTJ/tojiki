"""Command-line interface: python -m tojiki <command> [text]"""

import argparse
import sys

from . import __version__, normalize, to_cyrillic, to_latin, to_ordinal, to_words


def _read_text(args):
    if args.text:
        return " ".join(args.text)
    return sys.stdin.read()


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="tojiki", description="Tools for the Tajik language."
    )
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)

    latin = sub.add_parser("latin", help="Cyrillic -> Latin")
    latin.add_argument("--ascii", action="store_true", help="use plain ASCII (ī -> i)")
    latin.add_argument("text", nargs="*")

    cyr = sub.add_parser("cyrillic", help="Latin -> Cyrillic")
    cyr.add_argument("text", nargs="*")

    norm = sub.add_parser("normalize", help="fix look-alike characters")
    norm.add_argument("text", nargs="*")

    num = sub.add_parser("number", help="number to words")
    num.add_argument("--ordinal", action="store_true", help="якум, дуюм, ...")
    num.add_argument("value", type=int)

    args = parser.parse_args(argv)
    if args.command == "latin":
        print(to_latin(_read_text(args), ascii_only=args.ascii))
    elif args.command == "cyrillic":
        print(to_cyrillic(_read_text(args)))
    elif args.command == "normalize":
        print(normalize(_read_text(args)))
    elif args.command == "number":
        print(to_ordinal(args.value) if args.ordinal else to_words(args.value))
    return 0


if __name__ == "__main__":
    sys.exit(main())
