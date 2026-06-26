#!/usr/bin/env python3
"""
generate_cases.py — deterministic TOML config parsing edge-case corpus.

Uses Python stdlib (tomllib, json, configparser, decimal, datetime) as source of truth.
Seed: 42
"""
import json
import decimal
import datetime
from pathlib import Path

try:
    import tomllib
    HAS_TOMLLIB = True
except ImportError:
    HAS_TOMLLIB = False
    tomllib = None

SEED = 42
OUT_DIR = Path("cases")
OUT_FILE = OUT_DIR / "cases.jsonl"

# Each case: id, category, format_hint, raw_input, notes
RAW_CASES = [
    ("T001", "normal", "toml", 'title = "Example"\ncount = 42\n', "plain key/value"),
    ("T002", "normal", "toml", 'debug = true\nenabled = false\n', "booleans"),
    ("T003", "normal", "toml", 'pi = 3.14159\nlarge = 1_000_000\n', "float + numeric underscore"),
    ("T004", "string_escape", "toml", 'msg = "a # b = c"\n', 'string containing # and ='),
    ("T005", "string_escape", "toml", 's1 = "quoted"\ns2 = \'literal\'\n', "quoted vs literal"),
    ("T006", "string_escape", "toml", 'emoji = "🦀 café"\n', "unicode + emoji"),
    ("T007", "comments", "toml", 'x = 1  # comment\ny = 2\n', "inline comment"),
    ("T008", "arrays", "toml", 'nums = [1, 2, 3]\n', "simple array"),
    ("T009", "nested_table", "toml", '[server]\nhost = "localhost"\nport = 8080\n', "nested table"),
    ("T010", "dotted_key", "toml", 'a.b.c = 123\n', "dotted keys"),
    ("T011", "inline_table", "toml", 'point = { x = 1, y = 2 }\n', "inline table"),
    ("T012", "array_of_tables", "toml", '[[plugins]]\nname = "a"\n[[plugins]]\nname = "b"\n', "array of tables"),
    ("T013", "multiline", "toml", 's = """\nline1\nline2\n"""\n', "multiline basic string"),
    ("T014", "multiline", "toml", "s = '''\nraw\\nno\\escape\n'''\n", "multiline literal string"),
    ("T015", "date_time", "toml", 'd = 2023-05-17\nt = 12:34:56\nz = 2023-05-17T12:34:56Z\n', "dates/times"),
    ("T016", "pyproject_like", "toml", '[tool.myapp]\nversion = "1.0"\ndebug = true\n', "pyproject-like tool section"),
    ("T017", "null_missing", "toml", 'x = 1\n# no y key\n', "missing key / no null in TOML"),
    ("T018", "duplicate_key", "toml", 'x = 1\nx = 2\n', "duplicate key — should error"),
    ("T019", "malformed", "toml", 'x = "unterminated\n', "malformed quote — should error"),
    ("T020", "arrays", "toml", 'mixed = [1, "two", true, 3.14]\n', "mixed type array"),
    ("T021", "normal", "toml", 'neg = -42\nzero = 0\n', "negative / zero"),
    ("T022", "string_escape", "toml", 'path = "C:\\\\Users\\\\test"\n', "escaped backslash"),
    ("T023", "comments", "toml", '# full line comment\nx = 5\n', "full line comment"),
    ("T024", "nested_table", "toml", '[a.b.c]\nx = 1\n', "deeply nested table"),
    ("T025", "array_of_tables", "toml", '[[servers]]\nip = "1.1.1.1"\n[[servers]]\nip = "2.2.2.2"\n', "servers array of tables"),
    ("T026", "date_time", "toml", 'odt = 2023-05-17T12:34:56+02:00\n', "datetime with offset"),
    ("T027", "pyproject_like", "toml", '[project]\nname = "demo"\nversion = "0.1.0"\n', "project section"),
    ("T028", "null_missing", "toml", 'x = 1\n', "explicit missing/null test — y is absent"),
    ("T029", "malformed", "toml", 'x = [1, 2,\n', "trailing comma unclosed — should error"),
    ("T030", "json_confusion", "json", '{"x": 1, "y": true, "z": null}\n', "JSON with null"),
    ("T031", "json_confusion", "toml", 'x = 1\ny = true\n# no null in TOML\n', "TOML no null"),
    ("T032", "ini_confusion", "ini", '[section]\nkey = value\n', "INI-style"),
    ("T033", "ini_confusion", "toml", '[section]\nkey = "value"\nnum = 42\nflag = true\n', "TOML that looks like INI but has types"),
    ("T034", "naive_negative", "toml", 'url = "http://x.com?a=1#frag"\n', "string with # and = that breaks naive parsers"),
    ("T035", "naive_negative", "toml", 'msg = "foo = bar # not a comment"\n', "fake comment inside string"),
    ("T036", "string_escape", "toml", 's = "line1\\nline2"\n', "escaped newline"),
    ("T037", "arrays", "toml", 'empty = []\n', "empty array"),
    ("T038", "inline_table", "toml", 't = {a = 1, b = "x"}\n', "inline table 2"),
    ("T039", "dotted_key", "toml", 'x.y = 1\nx.z = 2\n', "multiple dotted keys"),
    ("T040", "duplicate_key", "toml", 'a.b = 1\n[a]\nb = 2\n', "dotted key then table — duplicate, should error"),
    ("T041", "null_missing", "toml", 'x = 1\n', "missing key test"),
    ("T042", "pyproject_like", "toml", '[tool.ruff]\nline-length = 88\n', "tool.ruff style"),
    ("T043", "string_escape", "toml", 'q = "He said \\"hi\\""\n', "escaped quotes"),
    ("T044", "arrays", "toml", 'nested = [[1,2],[3,4]]\n', "nested arrays"),
    ("T045", "date_time", "toml", 'local = 12:34:56.789\n', "time with fractional seconds"),
    ("T046", "naive_negative", "toml", 'x = true  # real comment\n', "bool with trailing comment"),
    ("T047", "json_confusion", "json", '{"a": 1, "b": [2,3]}\n', "JSON baseline"),
    ("T048", "ini_confusion", "ini", '[sec]\na=1\nb=true\n', "INI baseline — all values are strings"),
    ("T049", "malformed", "toml", 'x = true\ny = \n', "missing value — should error"),
    ("T050", "normal", "toml", 's = "ok"\nn = 123\nf = 4.5\nb = false\n', "all basic types"),
]

def default_json_serializer(o):
    if isinstance(o, decimal.Decimal):
        return float(o)
    if isinstance(o, (datetime.date, datetime.datetime, datetime.time)):
        return o.isoformat()
    raise TypeError(repr(o))

def normalize_value(v):
    """JSON-serializable normalized form."""
    try:
        json.dumps(v, default=default_json_serializer)
        return json.loads(json.dumps(v, default=default_json_serializer))
    except Exception:
        return str(v)

def build_expected(raw: str, fmt: str, category: str):
    result = {"format": fmt, "category": category}
    # Try tomllib
    toml_ok = False
    toml_val = None
    toml_err = None
    if HAS_TOMLLIB and fmt == "toml":
        try:
            toml_val = tomllib.loads(raw)
            toml_ok = True
        except Exception as e:
            toml_err = str(e)
    result["toml_parse_ok"] = toml_ok
    if toml_ok:
        result["toml_value"] = normalize_value(toml_val)
    if toml_err:
        result["toml_error"] = toml_err

    # Try json
    json_ok = False
    json_val = None
    try:
        json_val = json.loads(raw)
        json_ok = True
    except Exception as e:
        json_err = str(e)
        result["json_error"] = json_err
    result["json_parse_ok"] = json_ok
    if json_ok:
        result["json_value"] = normalize_value(json_val)

    # Try configparser for INI
    ini_ok = False
    ini_val = None
    if fmt in ("ini", "toml"):
        try:
            import configparser
            cp = configparser.ConfigParser()
            cp.read_string(raw)
            ini_val = {s: dict(cp[s]) for s in cp.sections()}
            # configparser also puts defaults; include if non-empty
            if not ini_val and cp.defaults():
                ini_val = {"DEFAULT": dict(cp.defaults())}
            ini_ok = True
        except Exception as e:
            result["ini_error"] = str(e)
    result["ini_parse_ok"] = ini_ok
    if ini_ok:
        result["ini_value"] = ini_val

    # Type observations from toml if available
    if toml_ok and isinstance(toml_val, dict):
        def collect_types(d, prefix=""):
            out = {}
            if isinstance(d, dict):
                for k, v in d.items():
                    pk = f"{prefix}.{k}" if prefix else k
                    if isinstance(v, dict):
                        out.update(collect_types(v, pk))
                    elif isinstance(v, list):
                        out[pk] = f"list[{type(v[0]).__name__ if v else 'empty'}]"
                    else:
                        out[pk] = type(v).__name__
            return out
        result["type_map"] = collect_types(toml_val)

    # Expected outcome classification
    expect_error = category in {"duplicate_key", "malformed"}
    result["expect_parse_error_toml"] = expect_error

    return result

def main():
    OUT_DIR.mkdir(exist_ok=True)
    seen = set()
    with OUT_FILE.open("w", encoding="utf-8") as f:
        for case in RAW_CASES:
            case_id, category, fmt, raw = case[:4]
            notes = case[4] if len(case) > 4 else ""
            if case_id in seen:
                raise ValueError(f"duplicate {case_id}")
            seen.add(case_id)
            expected = build_expected(raw, fmt, category)
            rec = {
                "case_id": case_id,
                "category": category,
                "format": fmt,
                "raw": raw,
                "notes": notes,
                "expected": expected,
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    size = OUT_FILE.stat().st_size
    print(f"Wrote {len(RAW_CASES)} cases to {OUT_FILE} ({size} bytes), tomllib_available={HAS_TOMLLIB}")

if __name__ == "__main__":
    main()
