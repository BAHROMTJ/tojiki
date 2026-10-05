# tojiki

[![CI](https://github.com/BAHROMTJ/tojiki/actions/workflows/ci.yml/badge.svg)](https://github.com/BAHROMTJ/tojiki/actions/workflows/ci.yml)

Open-source tools for the **Tajik language** (забони тоҷикӣ), written in pure Python with no dependencies.

Tajik is spoken by about 10 million people, yet developers building apps, search, chat bots and AI products for Tajik speakers have almost no open tooling. `tojiki` is a small, well-tested foundation for that work.

## Features

| Feature | Example |
|---|---|
| Cyrillic → Latin | `Тоҷикистон` → `Tojikiston` |
| Latin → Cyrillic | `Dushanbe` → `Душанбе` |
| Numbers → words | `2026` → `ду ҳазору бисту шаш` |
| Ordinals | `2` → `дуюм`, `30` → `сиюм` |
| Text normalization | fixes Latin `o` hidden in `Тoҷик`, Kazakh `һ` → `ҳ`, combining macrons → `ӣ` |

## Install

```bash
pip install git+https://github.com/BAHROMTJ/tojiki.git
```

## Usage

```python
from tojiki import to_latin, to_cyrillic, to_words, to_ordinal, normalize

to_latin("Хуҷанд")                 # 'Khujand'
to_latin("Кӯлоб", ascii_only=True)  # 'Kulob'
to_cyrillic("Ghafurov")            # 'Ғафуров'
to_words(125)                      # 'саду бисту панҷ'
to_ordinal(21)                     # 'бисту якум'
normalize("Тoҷик")                 # 'Тоҷик'  (the "o" was Latin)
```

Command line:

```bash
tojiki latin "Забони тоҷикӣ"
tojiki number 2026
tojiki number --ordinal 3
echo "һафта" | tojiki normalize
```

## Why normalization matters

Tajik text on the web is often typed on Russian or Kazakh keyboards, so words contain characters that look identical but are different Unicode letters. Two strings that look the same then fail to match in search, databases and AI pipelines. `normalize()` fixes the most common cases without touching words that are genuinely written in Latin script.

## Roadmap

- [ ] Tajik Cyrillic ↔ Perso-Arabic script
- [ ] Restore Tajik letters typed on a Russian keyboard (`х` → `ҳ`, `к` → `қ`) using a word list
- [ ] Tokenizer and stop-word list
- [ ] Number words → integers
- [ ] JavaScript port

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Development

```bash
python -m unittest discover -s tests
```

---

## Бо забони тоҷикӣ

`tojiki` — китобхонаи кушода (open source) барои кор бо забони тоҷикӣ: табдили хат (кириллӣ ↔ лотинӣ), навиштани рақамҳо бо калима ва тоза кардани матн аз ҳарфҳои ба ҳам монанд. Ҳар кас метавонад бепул истифода барад ва дар рушди он саҳм гузорад.

## License

MIT
