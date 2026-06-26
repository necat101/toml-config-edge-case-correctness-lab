# VERIFY.md — Fresh-clone verification

## Commit 0005bf7 (HEAD)

Verified 2026-06-26.

```bash
$ git clone https://github.com/necat101/toml-config-edge-case-correctness-lab.git toml-verify
Cloning into 'toml-verify'...

$ cd toml-verify
$ python3 -m py_compile generate_cases.py run_lab.py
$ python3 generate_cases.py
Wrote 50 cases to cases/cases.jsonl (26187 bytes), tomllib_available=True

$ python3 run_lab.py
Results: results/results.jsonl (108926 bytes)
Report: RESULTS.md
  tomllib_loads_baseline: pass=46 fail=0 skip=4 time=10.28ms
  tomllib_parse_float_decimal: pass=46 fail=0 skip=4 time=10.88ms
  json_loads_config_baseline: pass=2 fail=0 skip=48 time=2.56ms
  configparser_ini_baseline: pass=2 fail=0 skip=48 time=39.11ms
  naive_key_value_split: pass=1 fail=40 skip=9 time=1.15ms
  naive_comment_strip_then_split: pass=1 fail=40 skip=9 time=1.12ms
  naive_type_guess_parser: pass=16 fail=25 skip=9 time=2.84ms
```

All 50 cases generated deterministically (seed 42).
- `tomllib_loads_baseline`, `tomllib_parse_float_decimal`: **46/46 pass, 0 fail, 4 skip** (4 non-TOML format cases skipped by design).
- `json_loads_config_baseline`: **2/2 pass, 0 fail, 48 skip** (TOML/INI cases skipped by design).
- `configparser_ini_baseline`: **2/2 pass, 0 fail, 48 skip** (TOML/JSON cases skipped by design).
- `naive_key_value_split`: 1 pass, 40 fail, 9 skip — all failures expected.
- `naive_comment_strip_then_split`: 1 pass, 40 fail, 9 skip — all failures expected.
- `naive_type_guess_parser`: 16 pass, 25 fail, 9 skip — all failures expected.

Python: CPython 3.12.3 on Linux-6.17.0-1009-aws-x86_64-with-glibc2.39
tomllib available: True
