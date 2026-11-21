import csv, json, re, sys, pathlib

NUM = re.compile(r"^-?\d+(\.\d+)?$")
POUR = re.compile(r"^(\d+):(\d+(\.\d+)?)$")


def coerce(v):
    if v == "":
        return None
    return float(v) if NUM.match(v) and "." in v else (int(v) if NUM.match(v) else v)


def parse_pours(raw):
    if not raw:
        return None
    out = []
    for part in raw.split(";"):
        m = POUR.match(part.strip())
        if not m:
            return None
        out.append({"t_s": int(m.group(1)), "cum_g": float(m.group(2))})
    return out


def convert(path):
    errors = []
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for i, row in enumerate(reader, start=2):
            if not any(c.strip() for c in row):
                continue
            if len(row) != len(header):
                errors.append(f"line {i}: {len(row)} fields, expected {len(header)} (id={row[0] if row else '?'})")
                continue
            rec = {}
            for k, v in zip(header, row):
                rec[k] = coerce(v.strip())
            if "pours" in rec:
                rec["pours_raw"] = rec.pop("pours")
                rec["pours"] = parse_pours(rec["pours_raw"]) if rec["pours_raw"] else None
            rows.append(rec)
    return header, rows, errors


if __name__ == "__main__":
    folder = pathlib.Path(sys.argv[1])
    bad = 0
    for csv_path in sorted(folder.glob("*.csv")):
        header, rows, errors = convert(csv_path)
        for e in errors:
            print(f"{csv_path.name}: {e}")
        bad += len(errors)
        out = csv_path.with_suffix(".json")
        out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{csv_path.name}: {len(rows)} rows -> {out.name}")
    sys.exit(1 if bad else 0)
