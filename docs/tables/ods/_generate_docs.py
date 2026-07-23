#!/usr/bin/env python3
"""
Генерирует шаблоны документации таблиц (docs/tables/ods/dbo_<Table>.md)
из markdown-таблицы метаданных MS SQL (см. _mssql_metadata_temp.md).

Использование:
    python3 _generate_docs.py [--source _mssql_metadata_temp.md] [--schema dbo] [--out .]
"""
import argparse
import datetime
from collections import OrderedDict
from pathlib import Path

CHAR_TYPES = {"nvarchar", "varchar", "nchar", "char", "varbinary", "binary"}
DECIMAL_TYPES = {"decimal", "numeric"}


def parse_metadata(source: Path):
    lines = source.read_text(encoding="utf-8").splitlines()
    rows = []
    for line in lines[2:]:  # skip header + separator row
        if not line.strip():
            continue
        parts = line.split("|")
        if len(parts) < 12:
            continue
        (_, schema, table, column, pos, dtype, maxlen, prec, scale,
         nullable, default, samples) = parts[:12]
        rows.append(dict(
            schema=schema, table=table, column=column, pos=int(pos) if pos else 0,
            dtype=dtype, maxlen=maxlen, prec=prec, scale=scale,
            nullable=nullable, default=default, samples=samples,
        ))

    tables = OrderedDict()
    for r in rows:
        tables.setdefault((r["schema"], r["table"]), []).append(r)
    return tables


def format_type(r):
    dtype = r["dtype"]
    maxlen = r["maxlen"]
    prec = r["prec"]
    scale = r["scale"]
    if dtype in CHAR_TYPES:
        if maxlen == "-1":
            return f"{dtype}(max)"
        if maxlen:
            return f"{dtype}({maxlen})"
        return dtype
    if dtype in DECIMAL_TYPES:
        if prec and scale:
            return f"{dtype}({prec},{scale})"
        if prec:
            return f"{dtype}({prec})"
        return dtype
    return dtype


def escape_md(s):
    return s.replace("|", "\\|").strip()


def render_table_doc(schema: str, table: str, cols, doc_schema: str, today: str) -> str:
    cols_sorted = sorted(cols, key=lambda r: r["pos"])
    out = [
        f"# {doc_schema}.{table}",
        "",
        "## Система-источник",
        "",
        "_TODO: указать систему-источник_",
        "",
        "## Описание таблицы",
        "",
        "_TODO: заполнить описание таблицы_",
        "",
        "## Описание колонок",
        "",
        "| Колонка | Тип | Описание | Пример данных |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for r in cols_sorted:
        col = escape_md(r["column"])
        typ = escape_md(format_type(r))
        sample = escape_md(r["samples"])
        out.append(f"| `{col}` | {typ} | _TODO_ | {sample} |")
    out += [
        "",
        "## Дата создания документа",
        "",
        today,
        "",
        "## Кем создан",
        "",
        "_TODO_",
        "",
    ]
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", type=Path, default=Path(__file__).parent / "_mssql_metadata_temp.md",
        help="Путь к markdown-файлу с метаданными таблиц (результат SQL-скрипта выгрузки метаданных)",
    )
    parser.add_argument(
        "--schema", default="dbo",
        help="Заголовок/имя схемы, используемое в заголовке документа и в имени файла (по умолчанию: dbo)",
    )
    parser.add_argument(
        "--out", type=Path, default=Path(__file__).parent,
        help="Папка, куда сохранять сгенерированные .md файлы (по умолчанию: папка скрипта)",
    )
    args = parser.parse_args()

    tables = parse_metadata(args.source)
    today = datetime.date.today().strftime("%d.%m.%Y")
    args.out.mkdir(parents=True, exist_ok=True)

    for (schema, table), cols in tables.items():
        file_path = args.out / f"{args.schema}_{table}.md"
        file_path.write_text(render_table_doc(schema, table, cols, args.schema, today), encoding="utf-8")

    print(f"Сгенерировано файлов: {len(tables)} -> {args.out}")


if __name__ == "__main__":
    main()
