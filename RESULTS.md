# TOML Config Edge-Case Correctness Lab — Results

**Python:** 3.12.3 (CPython)

**tomllib available:** True

**Platform:** Linux-6.17.0-1009-aws-x86_64-with-glibc2.39

**Cases:** 50 (26187 bytes)

**Seed:** 42 (deterministic)

**Timing:** time.perf_counter()

**Memory:** tracemalloc — current 480.2 KiB, peak 493.1 KiB

**Total wall time:** 0.0786s

**Subprocess count:** 0

## Summary

| Method | Kind | Pass | Fail | Skip | Expected-Fail | Time (ms) |
|---|---|---:|---:|---:|---:|---:|
| tomllib_loads_baseline | toml-parse | 46 | 0 | 4 | 0 | 6.337 |
| tomllib_parse_float_decimal | toml-parse | 46 | 0 | 4 | 0 | 6.928 |
| json_loads_config_baseline | json-parse | 2 | 0 | 48 | 0 | 1.597 |
| configparser_ini_baseline | ini-parse | 2 | 0 | 48 | 0 | 24.026 |
| naive_key_value_split | naive-parse | 1 | 40 | 9 | 40 | 0.681 |
| naive_comment_strip_then_split | naive-parse | 1 | 40 | 9 | 40 | 0.665 |
| naive_type_guess_parser | naive-parse | 16 | 25 | 9 | 25 | 1.932 |

## Skip Matrix

| Method | Total | Passed | Failed | Skipped |
|---|---:|---:|---:|---:|
| tomllib_loads_baseline | 50 | 46 | 0 | 4 |
| tomllib_parse_float_decimal | 50 | 46 | 0 | 4 |
| json_loads_config_baseline | 50 | 2 | 0 | 48 |
| configparser_ini_baseline | 50 | 2 | 0 | 48 |
| naive_key_value_split | 50 | 1 | 40 | 9 |
| naive_comment_strip_then_split | 50 | 1 | 40 | 9 |
| naive_type_guess_parser | 50 | 16 | 25 | 9 |

## Failures (grouped by method)

### naive_key_value_split

- **T001** [normal] — naive parse mismatch (expected)
- **T002** [normal] — naive parse mismatch (expected)
- **T003** [normal] — naive parse mismatch (expected)
- **T004** [string_escape] — naive parse mismatch (expected)
- **T005** [string_escape] — naive parse mismatch (expected)
- **T006** [string_escape] — naive parse mismatch (expected)
- **T007** [comments] — naive parse mismatch (expected)
- **T008** [arrays] — naive parse mismatch (expected)
- **T009** [nested_table] — naive parse mismatch (expected)
- **T010** [dotted_key] — naive parse mismatch (expected)
- **T011** [inline_table] — naive parse mismatch (expected)
- **T012** [array_of_tables] — naive parse mismatch (expected)
- **T013** [multiline] — naive parse mismatch (expected)
- **T014** [multiline] — naive parse mismatch (expected)
- **T015** [date_time] — naive parse mismatch (expected)
- **T016** [pyproject_like] — naive parse mismatch (expected)
- **T017** [null_missing] — naive parse mismatch (expected)
- **T020** [arrays] — naive parse mismatch (expected)
- **T021** [normal] — naive parse mismatch (expected)
- **T022** [string_escape] — naive parse mismatch (expected)
- **T023** [comments] — naive parse mismatch (expected)
- **T024** [nested_table] — naive parse mismatch (expected)
- **T025** [array_of_tables] — naive parse mismatch (expected)
- **T027** [pyproject_like] — naive parse mismatch (expected)
- **T028** [null_missing] — naive parse mismatch (expected)
- **T031** [json_confusion] — naive parse mismatch (expected)
- **T033** [ini_confusion] — naive parse mismatch (expected)
- **T034** [naive_negative] — naive parse mismatch (expected)
- **T035** [naive_negative] — naive parse mismatch (expected)
- **T036** [string_escape] — naive parse mismatch (expected)
- **T037** [arrays] — naive parse mismatch (expected)
- **T038** [inline_table] — naive parse mismatch (expected)
- **T039** [dotted_key] — naive parse mismatch (expected)
- **T041** [null_missing] — naive parse mismatch (expected)
- **T042** [pyproject_like] — naive parse mismatch (expected)
- **T043** [string_escape] — naive parse mismatch (expected)
- **T044** [arrays] — naive parse mismatch (expected)
- **T045** [date_time] — naive parse mismatch (expected)
- **T046** [naive_negative] — naive parse mismatch (expected)
- **T050** [normal] — naive parse mismatch (expected)

### naive_comment_strip_then_split

- **T001** [normal] — naive parse mismatch (expected)
- **T002** [normal] — naive parse mismatch (expected)
- **T003** [normal] — naive parse mismatch (expected)
- **T004** [string_escape] — naive parse mismatch (expected)
- **T005** [string_escape] — naive parse mismatch (expected)
- **T006** [string_escape] — naive parse mismatch (expected)
- **T007** [comments] — naive parse mismatch (expected)
- **T008** [arrays] — naive parse mismatch (expected)
- **T009** [nested_table] — naive parse mismatch (expected)
- **T010** [dotted_key] — naive parse mismatch (expected)
- **T011** [inline_table] — naive parse mismatch (expected)
- **T012** [array_of_tables] — naive parse mismatch (expected)
- **T013** [multiline] — naive parse mismatch (expected)
- **T014** [multiline] — naive parse mismatch (expected)
- **T015** [date_time] — naive parse mismatch (expected)
- **T016** [pyproject_like] — naive parse mismatch (expected)
- **T017** [null_missing] — naive parse mismatch (expected)
- **T020** [arrays] — naive parse mismatch (expected)
- **T021** [normal] — naive parse mismatch (expected)
- **T022** [string_escape] — naive parse mismatch (expected)
- **T023** [comments] — naive parse mismatch (expected)
- **T024** [nested_table] — naive parse mismatch (expected)
- **T025** [array_of_tables] — naive parse mismatch (expected)
- **T027** [pyproject_like] — naive parse mismatch (expected)
- **T028** [null_missing] — naive parse mismatch (expected)
- **T031** [json_confusion] — naive parse mismatch (expected)
- **T033** [ini_confusion] — naive parse mismatch (expected)
- **T034** [naive_negative] — naive parse mismatch (expected)
- **T035** [naive_negative] — naive parse mismatch (expected)
- **T036** [string_escape] — naive parse mismatch (expected)
- **T037** [arrays] — naive parse mismatch (expected)
- **T038** [inline_table] — naive parse mismatch (expected)
- **T039** [dotted_key] — naive parse mismatch (expected)
- **T041** [null_missing] — naive parse mismatch (expected)
- **T042** [pyproject_like] — naive parse mismatch (expected)
- **T043** [string_escape] — naive parse mismatch (expected)
- **T044** [arrays] — naive parse mismatch (expected)
- **T045** [date_time] — naive parse mismatch (expected)
- **T046** [naive_negative] — naive parse mismatch (expected)
- **T050** [normal] — naive parse mismatch (expected)

### naive_type_guess_parser

- **T007** [comments] — naive parse mismatch (expected)
- **T008** [arrays] — naive parse mismatch (expected)
- **T009** [nested_table] — naive parse mismatch (expected)
- **T010** [dotted_key] — naive parse mismatch (expected)
- **T011** [inline_table] — naive parse mismatch (expected)
- **T012** [array_of_tables] — naive parse mismatch (expected)
- **T013** [multiline] — naive parse mismatch (expected)
- **T014** [multiline] — naive parse mismatch (expected)
- **T015** [date_time] — naive parse mismatch (expected)
- **T016** [pyproject_like] — naive parse mismatch (expected)
- **T020** [arrays] — naive parse mismatch (expected)
- **T022** [string_escape] — naive parse mismatch (expected)
- **T024** [nested_table] — naive parse mismatch (expected)
- **T025** [array_of_tables] — naive parse mismatch (expected)
- **T027** [pyproject_like] — naive parse mismatch (expected)
- **T033** [ini_confusion] — naive parse mismatch (expected)
- **T036** [string_escape] — naive parse mismatch (expected)
- **T037** [arrays] — naive parse mismatch (expected)
- **T038** [inline_table] — naive parse mismatch (expected)
- **T039** [dotted_key] — naive parse mismatch (expected)
- **T042** [pyproject_like] — naive parse mismatch (expected)
- **T043** [string_escape] — naive parse mismatch (expected)
- **T044** [arrays] — naive parse mismatch (expected)
- **T045** [date_time] — naive parse mismatch (expected)
- **T046** [naive_negative] — naive parse mismatch (expected)

## Notes

- `tomllib_loads_baseline`: validated against stdlib — correctly parses TOML, rejects duplicates/malformed input.
- `tomllib_parse_float_decimal`: same as baseline with Decimal float parsing.
- `json_loads_config_baseline`: correctly parses JSON cases; skips TOML/INI cases.
- `configparser_ini_baseline`: correctly parses INI cases; skips TOML/JSON cases.
- `naive_key_value_split`: fails on comments, strings with #/=, arrays, tables, multiline, dates — as expected.
- `naive_comment_strip_then_split`: mangles strings containing # — as expected.
- `naive_type_guess_parser`: misclassifies strings that look like bools/numbers/null — as expected.
- TOML has no null — missing keys are the design choice.
- Duplicate keys are parse errors in TOML — correctly rejected.
- Python tomllib is read-only (parser, not writer).
- No external parsers (tomli, tomlkit, yaml, json5, etc.) were used — out of scope.

## Conclusion

TOML is nice for human-written config with comments, typed values, and pyproject-style sections. Naive key=value parsing breaks quickly on dotted keys, arrays of tables, quoted strings, comments, multiline strings, and date/time types. A real parser matters — tomllib handles all of these correctly. Format confusion (TOML vs INI vs JSON) is a real footgun. Use the right parser for the format.
