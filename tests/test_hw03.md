# Tests for Homework 03

This document explains what a `test_hw03.py` needs to verify. No such
file exists yet — [`hw03.py`](../notes/hw02.py) is a **script** that
prints its answers rather than a module of functions, so testing it
means running it and capturing its printed output (with pytest's
`capsys` fixture), then asserting on what was printed.

<div dir="rtl" align="right">

## تست‌های تمرین ۲

این سند توضیح می‌دهد که یک فایل `test_hw03.py` باید چه چیزی را بررسی
کند. چنین فایلی هنوز وجود ندارد — [`hw03.py`](../notes/hw03.py) یک
**اسکریپت** است که پاسخ‌های خود را چاپ می‌کند، نه ماژولی از توابع؛ پس
تست کردن آن یعنی اجرای آن و گرفتن خروجی چاپ‌شده (با fixture مربوط به
`capsys` در pytest)، و سپس بررسی آنچه چاپ شده است.

</div>

## Suggested approach

Because the exercises are plain script code (not functions), a test
file has two reasonable strategies:

1. **Run the whole file and check stdout.** Use
   `runpy.run_path("notes/hw03.py")` inside a test, capture stdout with
   `capsys.readouterr()`, and assert that expected substrings (e.g. the
   FizzBuzz values, or the analyzed `text` results) appear in the
   output.
2. **Refactor into testable functions first** (a larger step, and only
   worth it if the instructor wants this). Each exercise's logic moves
   into a small function (e.g. `describe_number(n)`,
   `analyze_string(text)`, `fizzbuzz(n)` returning `"Fizz"` etc.), and
   the script calls those functions and prints their results. Then
   `test_hw03.py` can import and call the functions directly instead of
   parsing printed text.

Pick whichever approach the instructor asks for; the checklist below
lists what to verify either way.

<div dir="rtl" align="right">

## رویکرد پیشنهادی

از آنجا که تمرین‌ها کدِ اسکریپتی ساده هستند (نه تابع)، یک فایل تست دو
راهبرد معقول دارد:

۱. **اجرای کل فایل و بررسی stdout.** در یک تست، از
`runpy.run_path("notes/hw03.py")` استفاده کنید، خروجی stdout را با
`capsys.readouterr()` بگیرید، و بررسی کنید که رشته‌های موردانتظار
(مثلاً مقادیر FizzBuzz، یا نتایج تحلیل `text`) در خروجی وجود دارند.

۲. **بازنویسی به‌صورت توابع قابل‌تست** (گام بزرگ‌تری است، فقط در صورتی
ارزش دارد که مدرس این را بخواهد). منطق هر تمرین به یک تابع کوچک منتقل
می‌شود (مثلاً `describe_number(n)`، `analyze_string(text)`،
`fizzbuzz(n)` که مقادیری مثل `"Fizz"` برمی‌گرداند)، و اسکریپت این
توابع را فراخوانی کرده و نتیجه‌شان را چاپ می‌کند. سپس `test_hw03.py`
می‌تواند به‌طور مستقیم توابع را import و فراخوانی کند، به‌جای تجزیه‌ی
متن چاپ‌شده.

هرکدام از این دو رویکرد را که مدرس بخواهد انتخاب کنید؛ فهرست زیر
موضوعاتی است که در هر دو حالت باید بررسی شوند.

</div>

## What each test should check

### Exercise 1: Variables and types

- Each of the five variables (name, age, lesson number, completed flag,
  optional value) has the expected type (`str`, `int`, `int`, `bool`,
  `NoneType`).
- The printed output includes each variable's value and `type(...)`.

<div dir="rtl" align="right">

- هر یک از پنج متغیر (نام، سن، شماره درس، وضعیت تکمیل، مقدار اختیاری)
  type مورد انتظار خود را دارد (`str`، `int`، `int`، `bool`،
  `NoneType`).
- خروجی چاپ‌شده شامل مقدار و `type(...)` هر متغیر است.

</div>

### Exercise 2: Rebinding and identity

- After each rebind (`float`, `str`, `bool`, `None`), the printed
  `type(value)` matches the new type.
- The printed `id(value)` differs across the rebinds (a new object each
  time), which is the point of the exercise.

<div dir="rtl" align="right">

- بعد از هر rebind (`float`، `str`، `bool`، `None`)، مقدار چاپ‌شده‌ی
  `type(value)` با نوع جدید مطابقت دارد.
- مقدار چاپ‌شده‌ی `id(value)` در هر rebind متفاوت است (هر بار یک شیء
  جدید)، که هدف اصلی این تمرین همین است.

</div>

### Exercise 3: Scope

- With both `x` variables present: output is `inner: local`,
  `outer: enclosing`, `global: global`.
- After removing the local `x`: `inner` now prints the enclosing value
  (`inner: enclosing`), while `outer` and `global` are unchanged.
- After also removing the enclosing `x`: both `inner` and `outer` now
  print the global value (`inner: global`, `outer: global`).

<div dir="rtl" align="right">

- وقتی هر دو `x` وجود دارند: خروجی برابر است با `inner: local`،
  `outer: enclosing`، `global: global`.
- بعد از حذف `x` محلی: `inner` اکنون مقدار enclosing را چاپ می‌کند
  (`inner: enclosing`)، در حالی که `outer` و `global` بدون تغییر
  می‌مانند.
- بعد از حذف `x` محصورکننده نیز: هم `inner` و هم `outer` اکنون مقدار
  global را چاپ می‌کنند (`inner: global`, `outer: global`).

</div>

### Exercise 4: Number properties

- For `number = 17`: positive, odd, not divisible by 3, not divisible
  by 5, and between 10 and 20 inclusive (true). Verify each of the five
  properties against the actual value of `number`, not a hard-coded
  assumption.
- Test with at least one other value (e.g. a negative number, an even
  number, zero) to make sure the logic isn't hard-coded to `17`.

<div dir="rtl" align="right">

- برای `number = 17`: مثبت است، فرد است، بر ۳ بخش‌پذیر نیست، بر ۵
  بخش‌پذیر نیست، اما بین ۱۰ و ۲۰ **هست** (شامل خودشان). هر پنج ویژگی را
  بر اساس مقدار واقعی `number` بررسی کنید، نه یک فرض ثابت‌شده.
- حداقل با یک مقدار دیگر نیز تست کنید (مثلاً یک عدد منفی، یک عدد زوج، یا
  صفر) تا مطمئن شوید منطق کد صرفاً برای `17` نوشته نشده است.

</div>

### Exercise 5: String analyzer

- For `text = "Artificial Intelligence"`: first character `"A"`, last
  character `"e"`, first 10 characters `"Artificial"`, length `24`,
  uppercase and lowercase versions match `text.upper()` /
  `text.lower()`, reversed string matches `text[::-1]`, and `"Intel"`
  is found in the string (`True`).

<div dir="rtl" align="right">

- برای `text = "Artificial Intelligence"`: اولین کاراکتر `"A"`، آخرین
  کاراکتر `"e"`، ۱۰ کاراکتر اول `"Artificial"`، طول `24`، نسخه‌های
  uppercase و lowercase با `text.upper()` / `text.lower()` مطابقت
  دارند، رشته‌ی معکوس‌شده با `text[::-1]` مطابقت دارد، و `"Intel"` در
  رشته پیدا می‌شود (`True`).

</div>

### Exercise 6: FizzBuzz

- For numbers 1 through 100: multiples of 3 (not 5) print `"Fizz"`,
  multiples of 5 (not 3) print `"Buzz"`, multiples of both 3 and 5
  (e.g. 15, 30, 45) print `"FizzBuzz"`, and every other number prints
  itself.
- Check at least one example of each of the four cases (e.g. 3, 5, 15,
  7).

<div dir="rtl" align="right">

- برای اعداد ۱ تا ۱۰۰: مضرب‌های ۳ (و نه ۵) باید `"Fizz"` چاپ کنند،
  مضرب‌های ۵ (و نه ۳) باید `"Buzz"` چاپ کنند، مضرب‌های مشترک ۳ و ۵
  (مثل ۱۵، ۳۰، ۴۵) باید `"FizzBuzz"` چاپ کنند، و بقیه‌ی اعداد باید خودِ
  عدد را چاپ کنند.
- حداقل یک نمونه از هر یک از این چهار حالت را بررسی کنید (مثلاً ۳، ۵،
  ۱۵، ۷).

</div>

## Notes

- Use `pytest` (`uv run pytest tests/test_hw02.py`) — see
  [`help.md`](help.md) for the full set of commands.
- If testing via captured stdout, keep assertions loose enough to
  survive minor formatting differences (e.g. check for a substring
  rather than an exact full-line match), since the exact print format
  is up to the student.

<div dir="rtl" align="right">

## نکات

- از `pytest` استفاده کنید (`uv run pytest tests/test_hw02.py`) — برای
  مجموعه کامل دستورات به [`help.md`](help.md) مراجعه کنید.
- اگر از طریق گرفتن خروجی stdout تست می‌کنید، assertion‌ها را به‌اندازه‌ی
  کافی انعطاف‌پذیر نگه دارید تا تفاوت‌های جزئی در قالب‌بندی را تحمل کنند
  (مثلاً بررسی یک substring به‌جای تطابق دقیق کل خط)، چون قالب دقیق چاپ
  به انتخاب دانشجو بستگی دارد.

</div>
