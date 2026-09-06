# Tests for Homework 02

This document explains what [`test_hw02.py`](test_hw02.py) needs to
verify. The file is currently empty — write `pytest` test functions that
import each function from `notes/hw02.py` and check both its return
value and its mutation contract (whether it changes its input or not).

<div dir="rtl" align="right">

## تست‌های تمرین ۱

این سند توضیح می‌دهد که فایل [`test_hw02.py`](test_hw02.py) باید چه چیزی
را بررسی کند. این فایل در حال حاضر خالی است — توابع تست `pytest` بنویسید
که هر تابع را از `notes/hw02.py` وارد (import) کرده و هم مقدار
بازگشتی و هم قرارداد تغییرپذیری (mutation contract) آن (اینکه آیا ورودی
را تغییر می‌دهد یا نه) را بررسی کنند.

</div>

## What each test should check

### `add_loss`

- Calling `add_loss(3.0, [1.0, 2.0])` returns `[1.0, 2.0, 3.0]`.
- The original `history` list passed in is **unchanged** afterward.
- Calling `add_loss(1.0)` with no `history` returns `[1.0]`.

<div dir="rtl" align="right">

- فراخوانی `add_loss(3.0, [1.0, 2.0])` باید `[1.0, 2.0, 3.0]` برگرداند.
- لیست اصلی `history` که ارسال شده باید بعد از فراخوانی **بدون تغییر**
  باقی بماند.
- فراخوانی `add_loss(1.0)` بدون `history` باید `[1.0]` برگرداند.

</div>

### `add_loss_in_place`

- Calling `add_loss_in_place(3.0, history)` returns `None`.
- After the call, the **same** `history` object has `3.0` appended
  (check with `is` that it's the same list, and check its new contents).

<div dir="rtl" align="right">

- فراخوانی `add_loss_in_place(3.0, history)` باید `None` برگرداند.
- بعد از فراخوانی، همان شیء `history` باید `3.0` را ضافه‌شده داشته باشد
  (با `is` بررسی کنید که همان لیست است، و محتوای جدید آن را نیز بررسی
  کنید).

</div>

### `clone_folds`

- With `deep=False` (default): the result is a new outer list
  (`result is not folds`), but each inner list is the same object as in
  `folds` (`result[i] is folds[i]`).
- With `deep=True`: the outer list is new **and** every inner list is a
  new object (`result[i] is not folds[i]`), though equal in value.
- `folds` itself is never mutated by either call.
- Confirm `deep` must be passed as a keyword (e.g. that
  `clone_folds(folds, True)` is a `TypeError`).

<div dir="rtl" align="right">

- با `deep=False` (پیش‌فرض): نتیجه یک لیست بیرونی جدید است
  (`result is not folds`)، اما هر لیست داخلی همان شیء موجود در `folds`
  است (`result[i] is folds[i]`).
- با `deep=True`: هم لیست بیرونی و هم تمام لیست‌های داخلی، اشیائی جدید
  هستند (`result[i] is not folds[i]`)، هرچند از نظر مقدار برابرند.
- `folds` در هیچ‌کدام از دو حالت نباید تغییر کند.
- بررسی کنید که `deep` باید به‌صورت کلیدواژه‌ای ارسال شود (مثلاً
  `clone_folds(folds, True)` باید `TypeError` ایجاد کند).

</div>

### `same_object` and `same_value`

- Two equal but distinct lists (`[1, 2]` and `[1, 2]`, created
  separately) should give `same_object(...) == False` and
  `same_value(...) == True`.
- The same list assigned to two names (`a = [1, 2]; b = a`) should give
  `same_object(a, b) == True` and `same_value(a, b) == True`.

<div dir="rtl" align="right">

- دو لیست برابر اما متفاوت (`[1, 2]` و `[1, 2]`، ساخته‌شده به‌صورت جداگانه)
  باید `same_object(...) == False` و `same_value(...) == True` بدهند.
- یک لیست که به دو نام نسبت داده شده (`a = [1, 2]; b = a`) باید
  `same_object(a, b) == True` و `same_value(a, b) == True` بدهد.

</div>

### `shallow_clone_batches` and `deep_clone_batches`

- Both return a new outer list (`result is not batches`) equal in value
  to `batches`.
- For `shallow_clone_batches`: mutating an inner list of the result
  (e.g. `result[0].append(99)`) **also** changes `batches[0]`.
- For `deep_clone_batches`: the same mutation does **not** affect
  `batches`.
- `batches` itself is never mutated by the call alone (before you
  deliberately mutate the result to test sharing).

<div dir="rtl" align="right">

- هر دو باید یک لیست بیرونی جدید (`result is not batches`) و برابر با
  `batches` از نظر مقدار برگردانند.
- برای `shallow_clone_batches`: تغییر یک لیست داخلی در نتیجه (مثلاً
  `result[0].append(99)`) باید `batches[0]` را **نیز** تغییر دهد.
- برای `deep_clone_batches`: همان تغییر **نباید** روی `batches` تأثیر
  بگذارد.
- خودِ `batches` نباید صرفاً با فراخوانی تابع تغییر کند (پیش از اینکه
  عمداً نتیجه را برای تست اشتراک‌گذاری تغییر دهید).

</div>

## Notes

- Use `pytest` (`uv run pytest tests/test_hw01.py`) — see
  [`help.md`](help.md) for the full set of commands.
- Prefer one test function per behavior, with clear names like
  `test_add_loss_does_not_mutate_history`.

<div dir="rtl" align="right">

## نکات

- از `pytest` استفاده کنید (`uv run pytest tests/test_hw01.py`) — برای
  مجموعه کامل دستورات به [`help.md`](help.md) مراجعه کنید.
- ترجیحاً برای هر رفتار یک تابع تست جداگانه با نام واضح بنویسید، مثل
  `test_add_loss_does_not_mutate_history`.

</div>
