# Tests for Homework 07

This document explains what [`test_hw07.py`](test_hw07.py) needs to verify.
That file currently holds one stub per case — replace each `...` with real
assertions against the seven functions imported from `notes/hw07.py`.

Write at least 28 meaningful executed test cases.

<div dir="rtl" align="right">

## تست‌های تمرین 7

این سند توضیح می‌دهد که فایل [`test_hw07.py`](test_hw07.py) باید چه چیزی را
بررسی کند. آن فایل در حال حاضر برای هر حالت یک تابع خالی (stub) دارد —
به‌جای هر `...` تست واقعی بنویسید که هفت تابعِ وارد‌شده (import) از
`notes/hw07.py` را بررسی می‌کند.

حداقل ۲۸ تست معنادار و اجراشده بنویسید.

</div>

## What each test should check

### `clamp_score`

- `test_clamp_score_below_default_minimum_case`: `clamp_score(-0.3)`
  returns `0.0`.
- `test_clamp_score_inside_range_case`: `clamp_score(0.6)` returns `0.6`.
- `test_clamp_score_above_default_maximum_case`: `clamp_score(1.8)` returns
  `1.0`.
- `test_clamp_score_custom_minimum_case`: `clamp_score(0.1, minimum=0.2)`
  returns `0.2`.
- `test_clamp_score_custom_maximum_case`: `clamp_score(0.9, maximum=0.5)`
  returns `0.5`.
- `test_clamp_score_invalid_range_raises_case`:
  `clamp_score(0.5, minimum=1.0, maximum=0.0)` raises `ValueError` — use
  `pytest.raises`.

<div dir="rtl" align="right">

- `test_clamp_score_below_default_minimum_case`: `clamp_score(-0.3)` باید
  `0.0` برگرداند.
- `test_clamp_score_inside_range_case`: `clamp_score(0.6)` باید `0.6`
  برگرداند.
- `test_clamp_score_above_default_maximum_case`: `clamp_score(1.8)` باید
  `1.0` برگرداند.
- `test_clamp_score_custom_minimum_case`: `clamp_score(0.1, minimum=0.2)`
  باید `0.2` برگرداند.
- `test_clamp_score_custom_maximum_case`: `clamp_score(0.9, maximum=0.5)`
  باید `0.5` برگرداند.
- `test_clamp_score_invalid_range_raises_case`:
  `clamp_score(0.5, minimum=1.0, maximum=0.0)` باید `ValueError` ایجاد کند
  — از `pytest.raises` استفاده کنید.

</div>

### `metric_report`

- `test_metric_report_one_score_case`: `metric_report("train", 0.7)`
  returns `{"name": "train", "scores": (0.7,), "average": 0.7}`.
- `test_metric_report_multiple_scores_case`:
  `metric_report("validation", 0.8, 0.9, 1.0)` has `"average"` equal to
  `0.9`.
- `test_metric_report_no_scores_case`: `metric_report("empty")` returns
  `{"name": "empty", "scores": (), "average": None}` — no division by zero.
- `test_metric_report_custom_precision_case`:
  `metric_report("validation", 0.8, 0.9, precision=2)` has `"average"`
  equal to `0.85`; with `0.1, 0.2, 0.2` and `precision=1` the average is
  `0.2`.
- `test_metric_report_scores_is_tuple_case`: `isinstance(report["scores"],
  tuple)` is `True`.
- `test_metric_report_positional_precision_is_a_score_case`:
  `metric_report("x", 0.8, 0.9, 2)` treats `2` as a **score**, so
  `"scores"` is `(0.8, 0.9, 2)` — `precision` can only be set by keyword.

<div dir="rtl" align="right">

- `test_metric_report_one_score_case`: `metric_report("train", 0.7)` باید
  `{"name": "train", "scores": (0.7,), "average": 0.7}` برگرداند.
- `test_metric_report_multiple_scores_case`:
  `metric_report("validation", 0.8, 0.9, 1.0)` باید `"average"` برابر
  `0.9` داشته باشد.
- `test_metric_report_no_scores_case`: `metric_report("empty")` باید
  `{"name": "empty", "scores": (), "average": None}` برگرداند — بدون
  تقسیم بر صفر.
- `test_metric_report_custom_precision_case`:
  `metric_report("validation", 0.8, 0.9, precision=2)` باید `"average"`
  برابر `0.85` داشته باشد؛ با `0.1, 0.2, 0.2` و `precision=1` میانگین
  `0.2` است.
- `test_metric_report_scores_is_tuple_case`:
  `isinstance(report["scores"], tuple)` باید `True` باشد.
- `test_metric_report_positional_precision_is_a_score_case`:
  `metric_report("x", 0.8, 0.9, 2)` عدد `2` را یک **امتیاز** در نظر
  می‌گیرد، پس `"scores"` برابر `(0.8, 0.9, 2)` است — `precision` فقط با
  کلید (keyword) قابل تنظیم است.

</div>

### `build_config`

- `test_build_config_model_only_case`: `build_config("gpt")` returns
  `{"model": "gpt"}`.
- `test_build_config_several_options_case`:
  `build_config("gpt", temperature=0.2, max_tokens=100)` returns
  `{"model": "gpt", "temperature": 0.2, "max_tokens": 100}`.
- `test_build_config_independent_from_caller_dict_case`: build
  `options = {"temperature": 0.2}`, call `build_config("gpt", **options)`,
  then mutate the result (e.g. `result["temperature"] = 0.9`) and assert
  `options` is still `{"temperature": 0.2}` — and that `options` gained no
  `"model"` key.

<div dir="rtl" align="right">

- `test_build_config_model_only_case`: `build_config("gpt")` باید
  `{"model": "gpt"}` برگرداند.
- `test_build_config_several_options_case`:
  `build_config("gpt", temperature=0.2, max_tokens=100)` باید
  `{"model": "gpt", "temperature": 0.2, "max_tokens": 100}` برگرداند.
- `test_build_config_independent_from_caller_dict_case`: دیکشنری
  `options = {"temperature": 0.2}` را بسازید، `build_config("gpt", **options)`
  را صدا بزنید، سپس نتیجه را تغییر دهید (مثلاً
  `result["temperature"] = 0.9`) و بررسی کنید که `options` همچنان
  `{"temperature": 0.2}` است — و کلید `"model"` به آن اضافه نشده است.

</div>

### `apply_transform`

- `test_apply_transform_ordinary_function_case`: with a named `double`
  function, `[1.0, 2.0, 3.0]` returns `[2.0, 4.0, 6.0]`.
- `test_apply_transform_lambda_case`: `lambda value: value + 1` on
  `[1.0, 2.0]` returns `[2.0, 3.0]`.
- `test_apply_transform_empty_input_case`: `apply_transform([], double)`
  returns `[]`.
- `test_apply_transform_preserves_order_case`: `[3.0, 1.0, 2.0]` doubled
  returns `[6.0, 2.0, 4.0]` — not sorted.
- `test_apply_transform_does_not_mutate_input_case`: keep a copy of the
  input list before the call, assert the original is unchanged afterward,
  and that the result `is not` the input.
- `test_apply_transform_calls_transform_once_per_item_case`: use a transform
  that appends each value it receives to a `calls` list; after
  `apply_transform([1.0, 2.0, 3.0], spy)`, assert
  `calls == [1.0, 2.0, 3.0]` — one call per item, in order.

<div dir="rtl" align="right">

- `test_apply_transform_ordinary_function_case`: با یک تابع نام‌دار
  `double`، ورودی `[1.0, 2.0, 3.0]` باید `[2.0, 4.0, 6.0]` برگرداند.
- `test_apply_transform_lambda_case`: `lambda value: value + 1` روی
  `[1.0, 2.0]` باید `[2.0, 3.0]` برگرداند.
- `test_apply_transform_empty_input_case`: `apply_transform([], double)`
  باید `[]` برگرداند.
- `test_apply_transform_preserves_order_case`: دو برابر کردن
  `[3.0, 1.0, 2.0]` باید `[6.0, 2.0, 4.0]` برگرداند — نه مرتب‌شده.
- `test_apply_transform_does_not_mutate_input_case`: پیش از فراخوانی یک کپی
  از لیست ورودی نگه دارید، بررسی کنید که لیست اصلی بعد از آن تغییر نکرده و
  نتیجه همان شیء ورودی نیست (`is not`).
- `test_apply_transform_calls_transform_once_per_item_case`: از یک transform
  استفاده کنید که هر مقدار دریافتی را به لیست `calls` اضافه کند؛ پس از
  `apply_transform([1.0, 2.0, 3.0], spy)` بررسی کنید که
  `calls == [1.0, 2.0, 3.0]` — یک فراخوانی برای هر آیتم، به ترتیب.

</div>

### `make_threshold_checker`

- `test_threshold_checker_below_threshold_case`:
  `make_threshold_checker(0.8)(0.7)` is `False`.
- `test_threshold_checker_equal_threshold_case`:
  `make_threshold_checker(0.8)(0.8)` is `True` — the comparison is `>=`.
- `test_threshold_checker_above_threshold_case`:
  `make_threshold_checker(0.8)(0.9)` is `True`.
- `test_threshold_checker_independent_closures_case`: create
  `is_high = make_threshold_checker(0.8)` and
  `is_passing = make_threshold_checker(0.5)`; `is_passing(0.6)` is `True`
  while `is_high(0.6)` is `False` — creating the second did not overwrite
  the first one's threshold.

<div dir="rtl" align="right">

- `test_threshold_checker_below_threshold_case`:
  `make_threshold_checker(0.8)(0.7)` باید `False` باشد.
- `test_threshold_checker_equal_threshold_case`:
  `make_threshold_checker(0.8)(0.8)` باید `True` باشد — مقایسه `>=` است.
- `test_threshold_checker_above_threshold_case`:
  `make_threshold_checker(0.8)(0.9)` باید `True` باشد.
- `test_threshold_checker_independent_closures_case`:
  `is_high = make_threshold_checker(0.8)` و
  `is_passing = make_threshold_checker(0.5)` را بسازید؛ `is_passing(0.6)`
  باید `True` و `is_high(0.6)` باید `False` باشد — ساختن دومی آستانه‌ی اولی
  را بازنویسی نکرده است.

</div>

### `make_running_total`

- `test_running_total_first_update_case`: `make_running_total()(2.0)`
  returns `2.0`.
- `test_running_total_multiple_updates_case`: calling `total(2.0)` then
  `total(3.0)` returns `2.0` then `5.0`.
- `test_running_total_negative_update_case`: after `2.0` and `3.0`,
  `total(-1.0)` returns `4.0`.
- `test_running_total_independent_instances_case`: two totals `a` and `b`;
  after `a(10.0)`, `b(1.0)` returns `1.0` and `a(1.0)` returns `11.0`.
- `test_running_total_non_zero_start_case`:
  `make_running_total(start=10.0)(5.0)` returns `15.0`.

<div dir="rtl" align="right">

- `test_running_total_first_update_case`: `make_running_total()(2.0)` باید
  `2.0` برگرداند.
- `test_running_total_multiple_updates_case`: فراخوانی `total(2.0)` و سپس
  `total(3.0)` باید به ترتیب `2.0` و `5.0` برگرداند.
- `test_running_total_negative_update_case`: پس از `2.0` و `3.0`،
  `total(-1.0)` باید `4.0` برگرداند.
- `test_running_total_independent_instances_case`: دو مجموع `a` و `b`؛ پس
  از `a(10.0)`، `b(1.0)` باید `1.0` و `a(1.0)` باید `11.0` برگرداند.
- `test_running_total_non_zero_start_case`:
  `make_running_total(start=10.0)(5.0)` باید `15.0` برگرداند.

</div>

### `factorial`

- `test_factorial_zero_case`: `factorial(0)` returns `1`.
- `test_factorial_one_case`: `factorial(1)` returns `1`.
- `test_factorial_positive_integer_case`: `factorial(5)` returns `120`.
- `test_factorial_another_positive_integer_case`: `factorial(10)` returns
  `3628800`.
- `test_factorial_negative_raises_case`: `factorial(-1)` raises
  `ValueError`.
- `test_factorial_bool_raises_case`: parametrize over `True` and `False` —
  each raises `TypeError`, even though `bool` is a subclass of `int`.
- `test_factorial_float_raises_case`: parametrize over `3.0` and `2.5` —
  each raises `TypeError`, even when the float is a whole number.

<div dir="rtl" align="right">

- `test_factorial_zero_case`: `factorial(0)` باید `1` برگرداند.
- `test_factorial_one_case`: `factorial(1)` باید `1` برگرداند.
- `test_factorial_positive_integer_case`: `factorial(5)` باید `120`
  برگرداند.
- `test_factorial_another_positive_integer_case`: `factorial(10)` باید
  `3628800` برگرداند.
- `test_factorial_negative_raises_case`: `factorial(-1)` باید
  `ValueError` ایجاد کند.
- `test_factorial_bool_raises_case`: با پارامترهای `True` و `False` —
  هرکدام باید `TypeError` ایجاد کنند، با اینکه `bool` زیرکلاسی از `int`
  است.
- `test_factorial_float_raises_case`: با پارامترهای `3.0` و `2.5` —
  هرکدام باید `TypeError` ایجاد کنند، حتی وقتی float یک عدد صحیح است.

</div>

## Notes

- Use `pytest` (`uv run pytest tests/test_hw07.py`) — see
  [`help.md`](help.md) for the full set of commands.
- Keep one test function per behavior, following the existing
  `test_<description>_case` naming.
- Use `pytest.raises(...)` for every error case, and
  `@pytest.mark.parametrize` where one behavior has several inputs.
- Compare floats that come from arithmetic (like averages) with
  `pytest.approx` when exact equality would be fragile.

<div dir="rtl" align="right">

## نکات

- از `pytest` استفاده کنید (`uv run pytest tests/test_hw07.py`) — برای
  مجموعه کامل دستورات به [`help.md`](help.md) مراجعه کنید.
- برای هر رفتار یک تابع تست جداگانه بنویسید و از الگوی نام‌گذاری موجود
  یعنی `test_<description>_case` پیروی کنید.
- برای هر حالت خطا از `pytest.raises(...)` و در جایی که یک رفتار چند ورودی
  دارد از `@pytest.mark.parametrize` استفاده کنید.
- floatهایی را که از محاسبه به دست می‌آیند (مثل میانگین) با
  `pytest.approx` مقایسه کنید، وقتی برابری دقیق شکننده است.

</div>
