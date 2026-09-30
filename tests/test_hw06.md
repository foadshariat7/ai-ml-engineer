# Tests for Homework 06

This document explains what [`test_hw06.py`](test_hw06.py) needs to verify.
That file currently holds one stub per case — replace each `...` with real
assertions against the five functions imported from `notes/hw06.py`.

Write at least 25 meaningful test cases.

<div dir="rtl" align="right">

## تست‌های تمرین 6

این سند توضیح می‌دهد که فایل [`test_hw06.py`](test_hw06.py) باید چه چیزی را
بررسی کند. آن فایل در حال حاضر برای هر حالت یک تابع خالی (stub) دارد —
به‌جای هر `...` تست واقعی بنویسید که پنج تابعِ وارد‌شده (import) از
`notes/hw06.py` را بررسی می‌کند.

حداقل ۲۵ تست معنادار بنویسید.

</div>

## What each test should check

### `square_positive`

- `test_square_positive_squares_positive_values_case`: `[1, 2, 3]` returns
  `[1, 4, 9]`.
- `test_square_positive_excludes_negative_values_case`: `[-1, -2, -3]`
  returns `[]` — negative values must not appear squared either (a common
  bug is squaring first and forgetting the sign flips positive).
- `test_square_positive_excludes_zero_case`: `[0]` returns `[]`, not `[0]`.
- `test_square_positive_preserves_order_case`: a mixed input such as
  `[3, -1, 1, -2, 2]` returns `[9, 1, 4]` — the surviving values keep their
  original relative order.
- `test_square_positive_empty_input_case`: `square_positive([])` returns
  `[]`.
- `test_square_positive_does_not_mutate_input_case`: keep a copy of the
  input list before the call and assert the original is unchanged
  afterward.

<div dir="rtl" align="right">

- `test_square_positive_squares_positive_values_case`: ورودی `[1, 2, 3]`
  باید `[1, 4, 9]` برگرداند.
- `test_square_positive_excludes_negative_values_case`: ورودی
  `[-1, -2, -3]` باید `[]` برگرداند — مقادیر منفی نباید حتی به‌صورت مجذورشده
  هم ظاهر شوند (یک اشتباه رایج این است که ابتدا مجذور گرفته شود و فراموش شود
  که علامت منفی، مقدار را مثبت می‌کند).
- `test_square_positive_excludes_zero_case`: ورودی `[0]` باید `[]` برگرداند،
  نه `[0]`.
- `test_square_positive_preserves_order_case`: ورودی ترکیبی مانند
  `[3, -1, 1, -2, 2]` باید `[9, 1, 4]` برگرداند — مقادیر باقی‌مانده باید
  ترتیب نسبی اصلی خود را حفظ کنند.
- `test_square_positive_empty_input_case`: `square_positive([])` باید `[]`
  برگرداند.
- `test_square_positive_does_not_mutate_input_case`: پیش از فراخوانی یک کپی
  از لیست ورودی نگه دارید و بررسی کنید که لیست اصلی بعد از آن تغییر نکرده
  است.

</div>

### `normalize_names`

- `test_normalize_names_strips_whitespace_case`: `["  Alice  "]` returns
  `["alice"]`.
- `test_normalize_names_lowercases_case`: `["ALICE"]` returns `["alice"]`.
- `test_normalize_names_removes_blank_names_case`: parametrize over
  `["   "]`, `["\t\n"]`, and `[""]` — each returns `[]`, since the name is
  blank once stripped.
- `test_normalize_names_already_normalized_case`: `["alice"]` returns
  `["alice"]` unchanged.
- `test_normalize_names_empty_input_case`: `normalize_names([])` returns
  `[]`.
- `test_normalize_names_mixed_batch_case`: `["  Bob ", "ALICE", "   ",
  "charlie"]` returns `["bob", "alice", "charlie"]` — whitespace, casing,
  and a blank entry are all handled correctly in the same call.
- `test_normalize_names_does_not_mutate_input_case`: keep a copy of the
  input list before the call and assert the original is unchanged
  afterward.

<div dir="rtl" align="right">

- `test_normalize_names_strips_whitespace_case`: ورودی `["  Alice  "]`
  باید `["alice"]` برگرداند.
- `test_normalize_names_lowercases_case`: ورودی `["ALICE"]` باید `["alice"]`
  برگرداند.
- `test_normalize_names_removes_blank_names_case`: با پارامترهای
  `["   "]`، `["\t\n"]` و `[""]` — هرکدام باید `[]` برگردانند، چون نام پس از
  حذف فاصله‌ها خالی است.
- `test_normalize_names_already_normalized_case`: ورودی `["alice"]` باید
  بدون تغییر `["alice"]` برگرداند.
- `test_normalize_names_empty_input_case`: `normalize_names([])` باید `[]`
  برگرداند.
- `test_normalize_names_mixed_batch_case`: ورودی
  `["  Bob ", "ALICE", "   ", "charlie"]` باید
  `["bob", "alice", "charlie"]` برگرداند — فاصله، حروف بزرگ/کوچک و یک
  ورودی خالی همگی باید در یک فراخوانی درست مدیریت شوند.
- `test_normalize_names_does_not_mutate_input_case`: پیش از فراخوانی یک کپی
  از لیست ورودی نگه دارید و بررسی کنید که لیست اصلی بعد از آن تغییر نکرده
  است.

</div>

### `unique_lengths`

- `test_unique_lengths_collapses_duplicates_case`:
  `["AI", "ML", "AI", "Python", "ML"]` returns `{2, 6}` — five words in,
  two unique lengths out.
- `test_unique_lengths_empty_input_case`: `unique_lengths([])` returns
  `set()`.

<div dir="rtl" align="right">

- `test_unique_lengths_collapses_duplicates_case`: ورودی
  `["AI", "ML", "AI", "Python", "ML"]` باید `{2, 6}` برگرداند — پنج واژه
  ورودی، دو طول یکتا خروجی.
- `test_unique_lengths_empty_input_case`: `unique_lengths([])` باید
  `set()` برگرداند.

</div>

### `score_labels`

- `test_score_labels_high_case`: `{"alice": 0.9}` returns
  `{"alice": "high"}`.
- `test_score_labels_low_case`: `{"bob": 0.5}` returns `{"bob": "low"}`.
- `test_score_labels_boundary_case`: `{"charlie": 0.8}` returns
  `{"charlie": "high"}` — the threshold is inclusive (`>=`, not `>`).
- `test_score_labels_empty_input_case`: `score_labels({})` returns `{}`.

<div dir="rtl" align="right">

- `test_score_labels_high_case`: ورودی `{"alice": 0.9}` باید
  `{"alice": "high"}` برگرداند.
- `test_score_labels_low_case`: ورودی `{"bob": 0.5}` باید `{"bob": "low"}`
  برگرداند.
- `test_score_labels_boundary_case`: ورودی `{"charlie": 0.8}` باید
  `{"charlie": "high"}` برگرداند — آستانه شامل خودش است (`>=`، نه `>`).
- `test_score_labels_empty_input_case`: `score_labels({})` باید `{}`
  برگرداند.

</div>

### `keep_valid_scores`

- `test_keep_valid_scores_removes_none_case`:
  `{"alice": 0.5, "bob": None}` returns `{"alice": 0.5}`.
- `test_keep_valid_scores_keeps_zero_case`: `{"alice": 0.0}` returns
  `{"alice": 0.0}` — this is the truthiness trap: filtering must use
  `is not None`, not `if score`, or a zero score would be dropped.
- `test_keep_valid_scores_keeps_negative_case`: `{"alice": -0.3}` returns
  `{"alice": -0.3}` — the function only filters `None`, it does not
  validate the sign.
- `test_keep_valid_scores_empty_input_case`: `keep_valid_scores({})`
  returns `{}`.
- `test_keep_valid_scores_mixed_batch_case`:
  `{"alice": 0.0, "bob": None, "charlie": 0.7, "dave": -1.2}` returns
  `{"alice": 0.0, "charlie": 0.7, "dave": -1.2}`.
- `test_keep_valid_scores_does_not_mutate_input_case`: keep a copy of the
  input dict before the call and assert the original is unchanged
  afterward.

<div dir="rtl" align="right">

- `test_keep_valid_scores_removes_none_case`: ورودی
  `{"alice": 0.5, "bob": None}` باید `{"alice": 0.5}` برگرداند.
- `test_keep_valid_scores_keeps_zero_case`: ورودی `{"alice": 0.0}` باید
  `{"alice": 0.0}` برگرداند — این همان تله‌ی truthiness است: فیلتر کردن
  باید با `is not None` انجام شود، نه `if score`، وگرنه امتیاز صفر حذف
  می‌شود.
- `test_keep_valid_scores_keeps_negative_case`: ورودی `{"alice": -0.3}`
  باید `{"alice": -0.3}` برگرداند — تابع فقط `None` را فیلتر می‌کند و
  علامت را بررسی نمی‌کند.
- `test_keep_valid_scores_empty_input_case`: `keep_valid_scores({})` باید
  `{}` برگرداند.
- `test_keep_valid_scores_mixed_batch_case`: ورودی
  `{"alice": 0.0, "bob": None, "charlie": 0.7, "dave": -1.2}` باید
  `{"alice": 0.0, "charlie": 0.7, "dave": -1.2}` برگرداند.
- `test_keep_valid_scores_does_not_mutate_input_case`: پیش از فراخوانی یک
  کپی از دیکشنری ورودی نگه دارید و بررسی کنید که ورودی اصلی بعد از آن
  تغییر نکرده است.

</div>

## Notes

- Use `pytest` (`uv run pytest tests/test_hw06.py`) — see
  [`help.md`](help.md) for the full set of commands.
- Keep one test function per behavior, following the existing
  `test_<description>_case` naming.
- All five functions must be implemented as comprehensions (per
  [`hw06.md`](../notes/hw06.md)), but these tests only check behavior —
  they cannot verify *how* a function is written, only *what* it returns.

<div dir="rtl" align="right">

## نکات

- از `pytest` استفاده کنید (`uv run pytest tests/test_hw06.py`) — برای
  مجموعه کامل دستورات به [`help.md`](help.md) مراجعه کنید.
- برای هر رفتار یک تابع تست جداگانه بنویسید و از الگوی نام‌گذاری موجود
  یعنی `test_<description>_case` پیروی کنید.
- هر پنج تابع باید به‌صورت comprehension پیاده‌سازی شوند (طبق
  [`hw06.md`](../notes/hw06.md))، اما این تست‌ها فقط رفتار را بررسی
  می‌کنند — نمی‌توانند بررسی کنند که تابع *چگونه* نوشته شده، فقط اینکه
  *چه چیزی* برمی‌گرداند.

</div>
