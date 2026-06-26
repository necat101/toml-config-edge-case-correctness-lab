# TOML Config Edge-Case Correctness Lab

A tiny, reproducible Python-only lab testing the Hacker News debate around TOML config parsing.

**HN thread:** https://news.ycombinator.com/item?id=36018817
**TOML spec:** https://toml.io/en/

## What HN was debating

- TOML is attractive for human-written config and pyproject-style files.
- TOML is NOT meant to be a JSON replacement for arbitrary data transfer.
- Comments and readable key/value syntax are useful.
- "Looks like INI" does NOT mean it has INI semantics.
- YAML / JSON / JSON5 / INI / TOML have different tradeoffs.
- Missing values and the lack of null are a real design choice, not just an omission.
- Multiline strings, arrays of tables, dotted keys, and inline tables can surprise people.
- A real parser matters more than naive `split("=")`.
- TOML versioning (0.4 / 0.5 / 1.0 / 1.1) — parsers need to be explicit about which version they support.
- JSON number precision debates — JSON numbers are not IEEE-754, parser-dependent.
- Python `tomllib` is a parser, not a writer.

## What this lab does

Tests 50 deterministic config parsing edge cases across 7 stdlib-only methods:

| Method | Description |
|---|---|
| `tomllib_loads_baseline` | `tomllib.loads` — stdlib TOML parser, correctness oracle |
| `tomllib_parse_float_decimal` | `tomllib.loads` with `parse_float=Decimal` |
| `json_loads_config_baseline` | `json.loads` — JSON-equivalent cases only, skip others |
| `configparser_ini_baseline` | `configparser` — INI-style cases only, skip others |
| `naive_key_value_split` | intentionally unsafe line-based `key=value` parser — expected to fail |
| `naive_comment_strip_then_split` | intentionally unsafe "strip after # then split on =" — expected to fail |
| `naive_type_guess_parser` | intentionally unsafe type guesser (bool/int/float/null) — expected to fail |

**Categories covered:** normal, string_escape, comments, arrays, nested_table, dotted_key, inline_table, array_of_tables, multiline, date_time, pyproject_like, null_missing, duplicate_key, malformed, ini_confusion, json_confusion, naive_negative

No compilers, no package managers, no Docker, no external corpora, no network calls during the benchmark. Python stdlib only.

## Running

```bash
python3 -m py_compile generate_cases.py run_lab.py
python3 generate_cases.py
python3 run_lab.py
```

Output:
- `cases/cases.jsonl` — 50 deterministic cases (seed 42)
- `results/results.jsonl` — per-method results
- `RESULTS.md` — summary table, skip matrix, failure list, conclusions

## Results (CPython 3.12.3, tomllib available)

| Method | Pass | Fail | Skip |
|---|---|---:|---:|
| tomllib_loads_baseline | 46 | 0 | 4 |
| tomllib_parse_float_decimal | 46 | 0 | 4 |
| json_loads_config_baseline | 2 | 0 | 48 |
| configparser_ini_baseline | 2 | 0 | 48 |
| naive_key_value_split | 1 | 40 | 9 |
| naive_comment_strip_then_split | 1 | 40 | 9 |
| naive_type_guess_parser | 16 | 25 | 9 |

tomllib/json/configparser skip non-applicable formats by design (46 TOML cases, 2 JSON cases, 2 INI cases). All naive failures are **expected** — that's the point.

See [RESULTS.md](RESULTS.md) for full details.

## Key findings

- `tomllib` correctly parses TOML, rejects duplicate keys and malformed input.
- TOML has **no null** — missing keys are the design choice.
- `json.loads` correctly parses JSON; skips TOML/INI cases.
- `configparser` correctly parses INI; skips TOML/JSON cases.
- Naive key=value parsing breaks on: quoted strings, `#`/`=` inside strings, arrays, nested tables, dotted keys, inline tables, arrays of tables, multiline strings, date/time types, comments.
- Type-guessing helps a little (16/25 vs 1/40 pass rate) but still breaks on complex structures.
- Format confusion (TOML vs INI vs JSON) is a real footgun.
- Python `tomllib` is read-only — parser, not writer.

## Scope

This lab is intentionally tiny. It does **not** claim TOML is globally better than JSON, INI, YAML, or anything else. It tests the HN debate in a reproducible way: TOML can be nice for human-written config, but naive parsing and format confusion break quickly.

No external parsers (tomli, tomlkit, ruamel, yaml, json5, jq, yq, node, cargo) were used.

## Verify

See [VERIFY.md](VERIFY.md) for a fresh-clone verification transcript.
