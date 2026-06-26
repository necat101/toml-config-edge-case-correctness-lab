# VERIFY.md — Fresh-clone verification

## Commit 1c1c7bc (HEAD)

Verified 2026-06-26.

```bash
$ git clone https://github.com/necat101/toml-config-edge-case-correctness-lab.git toml-verify
Cloning into 'toml-verify'...

$ cd toml-verify
$ python3 -m py_compile generate_cases.py run_lab.py
$ python3 generate_cases.py
Wrote 50 cases to cases/cases.jsonl (26187 bytes), tomllib_available=True

$ python3 run_lab.py
Results: results/results.jsonl (108968 bytes)
Report: RESULTS.md
  tomllib_loads_baseline: pass=46 fail=0 skip=4 time=6.07ms
  tomllib_parse_float_decimal: pass=46 fail=0 skip=4 time=6.59ms
  json_loads_config_baseline: pass=2 fail=0 skip=48 time=1.53ms
  configparser_ini_baseline: pass=2 fail=0 skip=48 time=23.35ms
  naive_key_value_split: pass=1 fail=40 skip=9 time=0.66ms
  naive_comment_strip_then_split: pass=1 fail=40 skip=9 time=0.76ms
  naive_type_guess_parser: pass=16 fail=25 skip=9 time=1.57ms
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

---

## Prior verifications

- Commit `942be05` — also fresh-clone verified with identical results.
- Commit `5ec10fc` — also fresh-clone verified with identical results.
- Commit `0005bf7` — initial results commit; also fresh-clone verified with identical results.
