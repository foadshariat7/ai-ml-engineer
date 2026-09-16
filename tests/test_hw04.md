# Tests for Homework 04

This document explains what [`test_hw04.py`](test_hw04.py) needs to verify.
That file currently holds one stub per case — replace each `...` with real
assertions against `average_scores`, imported from `notes/hw04.py`.

Write at least 14 meaningful test cases.

<div dir="rtl" align="right">

## تست‌های تمرین ۳

این سند توضیح می‌دهد که فایل [`test_hw04.py`](test_hw04.py) باید چه چیزی را
بررسی کند. آن فایل در حال حاضر برای هر حالت یک تابع خالی (stub) دارد —
به‌جای هر `...` تست واقعی بنویسید که تابع `average_scores` را از
`notes/hw04.py` وارد (import) کرده و بررسی می‌کند.

حداقل ۱۴ تست معنادار بنویسید.

</div>

## What each test should check

### Aggregation

- `test_repeated_user_case`: two records for the same user average to that
  user's mean (e.g. `10.0` and `20.0` give `{"Foad": 15.0}`).
- `test_multiple_user_case`: several users are averaged independently of
  one another.
- `test_ignore_none_score_case`: a record with `"score": None` is skipped
  rather than counted as `0` — `10.0` plus a `None` still averages `10.0`.
- `test_user_with_only_none_case`: a user whose every score is `None` is
  absent from the result entirely (assert the key is **not in** the dict).
- `test_zero_score_included_case`: `0` and `0.0` are counted, so `10.0`
  and `0.0` average to `5.0` — not `10.0`.
- `test_integer_score_accepted_case`: integer scores are accepted.
- `test_empty_input_case`: `average_scores([])` returns `{}`.

<div dir="rtl" align="right">

- `test_repeated_user_case`: دو رکورد برای یک کاربر باید میانگین آن کاربر
  را بدهند (مثلاً `10.0` و `20.0` نتیجه‌ی `{"Foad": 15.0}` می‌دهند).
- `test_multiple_user_case`: چند کاربر باید مستقل از یکدیگر میانگین‌گیری
  شوند.
- `test_ignore_none_score_case`: رکوردی با `"score": None` باید نادیده
  گرفته شود، نه اینکه `0` حساب شود — `10.0` به‌همراه یک `None` باز هم
  میانگین `10.0` می‌دهد.
- `test_user_with_only_none_case`: کاربری که همه‌ی امتیازهایش `None` است
  نباید اصلاً در نتیجه باشد (بررسی کنید که کلید در دیکشنری **نیست**).
- `test_zero_score_included_case`: `0` و `0.0` باید شمرده شوند، پس `10.0`
  و `0.0` میانگین `5.0` می‌دهند — نه `10.0`.
- `test_integer_score_accepted_case`: امتیازهای صحیح (int) باید پذیرفته
  شوند.
- `test_empty_input_case`: `average_scores([])` باید `{}` برگرداند.

</div>

### Rejecting invalid scores

Use `pytest.raises(...)` for each of these:

- `test_missing_score_case`: the `score` key is absent → `ValueError`.
- `test_negative_score_case`: a negative score → `ValueError`.
- `test_nan_score_case`: `float("nan")` → `ValueError`.
- `test_positive_infinity_score_case`: `float("inf")` → `ValueError`.
- `test_negative_infinity_score_case`: `float("-inf")` → `ValueError`.
- `test_non_numeric_score_case`: a string such as `"2222"` → `TypeError`.
- `test_boolean_score_case`: `True` → `TypeError`, rather than being
  silently accepted as `1`.

<div dir="rtl" align="right">

برای هرکدام از موارد زیر از `pytest.raises(...)` استفاده کنید:

- `test_missing_score_case`: نبودِ کلید `score` → `ValueError`.
- `test_negative_score_case`: امتیاز منفی → `ValueError`.
- `test_nan_score_case`: مقدار `float("nan")` → `ValueError`.
- `test_positive_infinity_score_case`: مقدار `float("inf")` → `ValueError`.
- `test_negative_infinity_score_case`: مقدار `float("-inf")` →
  `ValueError`.
- `test_non_numeric_score_case`: رشته‌ای مانند `"2222"` → `TypeError`.
- `test_boolean_score_case`: مقدار `True` → `TypeError`، نه اینکه
  بی‌سروصدا به‌عنوان `1` پذیرفته شود.

</div>

### Rejecting an invalid `user_id`

- `test_missing_user_case`: the `user_id` key is absent → `ValueError`.
- `test_blank_user_case`: `""` and a whitespace-only `"   "` →
  `ValueError`.
- `test_non_string_user_case`: a non-string such as `20` → `ValueError`.

<div dir="rtl" align="right">

- `test_missing_user_case`: نبودِ کلید `user_id` → `ValueError`.
- `test_blank_user_case`: مقدار `""` و مقدار فقط-فاصله‌ی `"   "` →
  `ValueError`.
- `test_non_string_user_case`: مقدار غیررشته‌ای مانند `20` → `ValueError`.

</div>

### Contracts

- `test_input_not_mutated_case`: keep a copy of the records before the
  call and assert the original list is unchanged afterward.
- `test_float_precision_case`: compare a float average with
  `pytest.approx` — averaging `0.1` and `0.2` yields
  `0.15000000000000002`, which is **not** `== 0.15`.
- `test_error_message_index_case`: capture the exception with
  `pytest.raises(...) as exc_info` and assert the offending record's index
  appears in `str(exc_info.value)`. Put the bad record second so that a
  hard-coded `0` cannot pass by accident.

<div dir="rtl" align="right">

- `test_input_not_mutated_case`: پیش از فراخوانی یک کپی از رکوردها نگه
  دارید و پس از آن بررسی کنید که لیست اصلی تغییر نکرده است.
- `test_float_precision_case`: میانگین اعشاری را با `pytest.approx`
  مقایسه کنید — میانگین `0.1` و `0.2` برابر `0.15000000000000002` است که
  با `0.15` برابر **نیست**.
- `test_error_message_index_case`: استثنا را با
  `pytest.raises(...) as exc_info` بگیرید و بررسی کنید که ایندکس رکورد
  خطادار در `str(exc_info.value)` آمده است. رکورد خطادار را در جایگاه دوم
  قرار دهید تا یک `0` ثابت به‌طور تصادفی تست را پاس نکند.

</div>

## Notes

- Use `pytest` (`uv run pytest tests/test_hw04.py`) — see
  [`help.md`](help.md) for the full set of commands.
- Keep one test function per behavior, following the existing
  `test_<description>_case` naming.

<div dir="rtl" align="right">

## نکات

- از `pytest` استفاده کنید (`uv run pytest tests/test_hw04.py`) — برای
  مجموعه کامل دستورات به [`help.md`](help.md) مراجعه کنید.
- برای هر رفتار یک تابع تست جداگانه بنویسید و از الگوی نام‌گذاری موجود
  یعنی `test_<description>_case` پیروی کنید.

</div>
