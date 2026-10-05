"""A small, editable set of common Tajik stop words."""

from importlib.resources import files


STOPWORDS = {
    word.strip()
    for word in files(__package__).joinpath("stopwords.txt").read_text(encoding="utf-8").splitlines()
    if word.strip()
}
