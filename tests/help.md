# Running Tests, Lint, and Type Checks

To run tests, lint, and type checks, use the commands below.

<div dir="rtl" align="right">

برای اجرای تست‌ها، بررسی lint و بررسی type، از دستورات زیر استفاده کنید.

</div>

## Run a test file

Run this project's test suite (or a single file) with `pytest`:

```bash
uv run pytest tests/test_semantics.py
```

<div dir="rtl" align="right">

مجموعه تست‌های پروژه (یا یک فایل مشخص) را با `pytest` اجرا کنید:

</div>

## Lint check

Check for style and lint issues with `ruff`:

```bash
uv run ruff check tests/test_semantics.py
```

<div dir="rtl" align="right">

بررسی مشکلات سبک نوشتاری (style) و lint را با `ruff` انجام دهید:

</div>

## Type check

Verify type correctness with `pyright`:

```bash
uv run pyright tests/test_semantics.py
```

<div dir="rtl" align="right">

صحت type‌ها را با `pyright` بررسی کنید:

</div>

## Notes

- Replace `tests/test_semantics.py` with any other file or directory path to target it instead.
- Running these against the whole `tests/` directory (or the whole project) is also valid, e.g. `uv run pytest tests/`.

<div dir="rtl" align="right">

**نکات**

- به‌جای `tests/test_semantics.py` می‌توانید مسیر هر فایل یا پوشه‌ی دیگری را قرار دهید.
- اجرای این دستورات روی کل پوشه‌ی `tests/` (یا کل پروژه) نیز معتبر است، مثلاً: `uv run pytest tests/`.

</div>
