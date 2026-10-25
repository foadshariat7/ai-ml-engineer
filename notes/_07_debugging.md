# Debugging 07: Functions

This document explains the five deliberate bugs in
[`_07_debugging.py`](_07_debugging.py): the mutable-default trap, a missing
`return`, a callback that is called instead of passed, closure late binding,
and recursion without a base case.

<div dir="rtl" align="right">

## دیباگ ۷: توابع (Functions)

این سند پنج باگ عمدی موجود در فایل [`_07_debugging.py`](_07_debugging.py) را
توضیح می‌دهد: تله‌ی پیش‌فرض تغییرپذیر (mutable default)، نبودِ `return`،
callbackی که به‌جای ارسال‌شدن فراخوانی می‌شود، اتصال دیرهنگام (late binding)
در closureها، و بازگشت (recursion) بدون حالت پایه.

</div>

## Part A: Mutable default

```python
def record_loss(loss, history=[]):
    history.append(loss)
    return history
```

1. **Root cause.** The default `[]` is a single list object shared by every
   call that omits `history`. `append` mutates that shared list, so values
   accumulate across calls.
2. **When the list is created.** Default values are evaluated **once**, when
   the `def` statement runs (at import time), not on each call. The list is
   stored on the function object (`record_loss.__defaults__`).
3. **Why test ordering reveals the bug.** Run alone, a test sees a fresh,
   empty default and `record_loss(0.5)` returns `[0.5]`. If another test ran
   first, the shared list already holds its values, so the same call returns
   e.g. `[0.9, 0.5]`. The function carries hidden state between calls, and
   only the order of calls exposes it.
4. **Safe fix.** Use `None` as a sentinel and create a new list inside the
   function:

```python
def record_loss(loss, history=None):
    if history is None:
        history = []
    history.append(loss)
    return history
```

<div dir="rtl" align="right">

### بخش A: پیش‌فرض تغییرپذیر

۱. **علت اصلی.** مقدار پیش‌فرض `[]` یک شیء لیستِ واحد است که بین همه‌ی
فراخوانی‌هایی که `history` را ارسال نمی‌کنند مشترک است. `append` همین لیست
مشترک را تغییر می‌دهد، پس مقادیر در طول فراخوانی‌ها انباشته می‌شوند.

۲. **لیست چه زمانی ساخته می‌شود.** مقادیر پیش‌فرض فقط **یک بار** ارزیابی
می‌شوند، یعنی هنگام اجرای دستور `def` (در زمان import)، نه در هر فراخوانی.
این لیست روی خودِ شیء تابع ذخیره می‌شود (`record_loss.__defaults__`).

۳. **چرا ترتیب تست‌ها باگ را آشکار می‌کند.** وقتی یک تست به‌تنهایی اجرا شود،
پیش‌فرضِ تازه و خالی را می‌بیند و `record_loss(0.5)` مقدار `[0.5]` را
برمی‌گرداند. اگر تست دیگری قبل از آن اجرا شده باشد، لیست مشترک از قبل
مقادیر آن تست را دارد و همان فراخوانی مثلاً `[0.9, 0.5]` را برمی‌گرداند. تابع
بین فراخوانی‌ها حالت پنهان (hidden state) نگه می‌دارد و فقط ترتیب
فراخوانی‌هاست که آن را آشکار می‌کند.

۴. **راه‌حل امن.** از `None` به‌عنوان نگهبان (sentinel) استفاده کنید و لیست
جدید را درون تابع بسازید (کد بالا).

</div>

## Part B: Missing return

```python
def normalize(value):
    result = value / 100
    print(result)

score = normalize(50)
print(score * 2)
```

What happens, step by step:

1. `normalize(50)` computes `0.5` and **prints** `0.5`.
2. The function has no `return`, so it returns `None`. Therefore
   `score = None`.
3. `score * 2` evaluates `None * 2`, which raises
   `TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'`.

The output is `0.5` followed by the traceback. The misleading part is that
`0.5` appears on screen, so the function *looks* like it worked, but printing
shows a value without handing it back to the caller. The crash also happens
one line after the real bug. The fix is to `return result` instead of (or as
well as) printing it.

<div dir="rtl" align="right">

### بخش B: نبودِ return

مراحل اجرا:

۱. `normalize(50)` مقدار `0.5` را محاسبه و آن را **چاپ** می‌کند.

۲. تابع `return` ندارد، پس `None` برمی‌گرداند. در نتیجه `score = None`.

۳. عبارت `score * 2` در واقع `None * 2` است که خطای
`TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'` می‌دهد.

خروجی، `0.5` و سپس traceback است. نکته‌ی گمراه‌کننده این است که `0.5` روی
صفحه ظاهر می‌شود، پس تابع *به‌ظاهر* درست کار کرده است؛ اما چاپ‌کردن فقط مقدار
را نمایش می‌دهد و آن را به فراخواننده برنمی‌گرداند. همچنین خطا یک خط بعد از
باگ واقعی رخ می‌دهد. راه‌حل این است که به‌جای چاپ (یا علاوه بر آن)
`return result` بنویسید.

</div>

## Part C: Callback accidentally called

```python
result = apply(5, double())
```

1. **Why it fails.** Arguments are evaluated *before* `apply` runs. `double()`
   calls `double` immediately with no arguments, which raises
   `TypeError: double() missing 1 required positional argument: 'value'`.
   `apply` is never even entered.
2. **`double` versus `double()`.** `double` is the function object itself, a
   value that can be stored or passed around. `double()` *calls* the function
   and evaluates to whatever it returns. A higher-order function like `apply`
   needs the function, so it can call it later with the right argument.
3. **Correct call.** Pass the function without parentheses:

```python
result = apply(5, double)  # 10
```

<div dir="rtl" align="right">

### بخش C: callbackی که اشتباهاً فراخوانی شده

۱. **چرا خطا می‌دهد.** آرگومان‌ها *قبل از* اجرای `apply` ارزیابی می‌شوند.
`double()` تابع `double` را فوراً و بدون آرگومان فراخوانی می‌کند که خطای
`TypeError: double() missing 1 required positional argument: 'value'` می‌دهد.
اجرا اصلاً وارد `apply` نمی‌شود.

۲. **تفاوت `double` و `double()`.** `double` خودِ شیء تابع است، یعنی مقداری
که می‌توان آن را ذخیره یا ارسال کرد. `double()` تابع را *فراخوانی* می‌کند و
حاصلش همان مقداری است که تابع برمی‌گرداند. تابع مرتبه‌بالایی مثل `apply` به
خودِ تابع نیاز دارد تا بعداً آن را با آرگومان درست فراخوانی کند.

۳. **فراخوانی درست.** تابع را بدون پرانتز ارسال کنید:
`apply(5, double)` که حاصلش `10` است.

</div>

## Part D: Closure late binding

```python
operations = []
for factor in [2, 3, 4]:
    operations.append(lambda value: value * factor)

print([operation(10) for operation in operations])
```

**Prediction:** `[40, 40, 40]`, not `[20, 30, 40]`.

**Why.** Each lambda captures the *variable* `factor`, not its value at the
moment the lambda is created. The name is looked up only when the lambda is
called (late binding). All three lambdas share the same loop variable, and by
the time they are called the loop has finished and `factor` is `4`. So each
computes `10 * 4`.

**Fix 1: default argument.** Defaults are evaluated at definition time, so
they freeze the current value:

```python
for factor in [2, 3, 4]:
    operations.append(lambda value, factor=factor: value * factor)
```

**Fix 2: factory function.** Each call creates a new scope, so each closure
captures its own `factor`. This version cannot be overridden by a caller
passing an extra argument:

```python
def make_multiplier(factor):
    return lambda value: value * factor

operations = [make_multiplier(factor) for factor in [2, 3, 4]]
```

Both fixes print `[20, 30, 40]`.

<div dir="rtl" align="right">

### بخش D: اتصال دیرهنگام در closure

**پیش‌بینی:** `[40, 40, 40]`، نه `[20, 30, 40]`.

**چرا.** هر lambda خودِ *متغیر* `factor` را نگه می‌دارد، نه مقدار آن در لحظه‌ی
ساخته‌شدن lambda را. این نام فقط هنگام فراخوانی lambda جست‌وجو می‌شود (اتصال
دیرهنگام). هر سه lambda متغیر حلقه‌ی یکسانی را به اشتراک می‌گذارند و وقتی
فراخوانی می‌شوند، حلقه تمام شده و `factor` برابر `4` است. پس هر کدام `10 * 4`
را محاسبه می‌کنند.

**راه‌حل ۱: آرگومان پیش‌فرض.** مقادیر پیش‌فرض در زمان تعریف ارزیابی می‌شوند،
پس مقدار فعلی را ثابت نگه می‌دارند.

**راه‌حل ۲: تابع سازنده (factory).** هر فراخوانی یک scope جدید می‌سازد، پس هر
closure متغیر `factor` مخصوص خودش را نگه می‌دارد. در این روش، فراخواننده
نمی‌تواند با ارسال آرگومان اضافه مقدار را تغییر دهد.

هر دو راه‌حل `[20, 30, 40]` را چاپ می‌کنند.

</div>

## Part E: Recursive failure

```python
def factorial(value):
    return value * factorial(value - 1)
```

- **Missing base case.** Every call unconditionally makes another call. There
  is no condition, such as `if value <= 1: return 1`, under which the
  function returns without recursing, so no call can ever finish.
- **What eventually happens.** Each call adds a frame to the call stack:
  `factorial(5)` → `factorial(4)` → … → `factorial(0)` → `factorial(-1)` → …
  When the depth reaches Python's limit (about 1000 by default), Python
  raises `RecursionError: maximum recursion depth exceeded`. No
  multiplication is ever performed, because each `value * ...` waits for a
  result that never arrives.
- **Why decreasing numbers do not terminate it.** The argument getting
  smaller is not the same as stopping. Recursion ends only when the code
  reaches a branch that *returns without calling itself*. Python has no idea
  that `0` or `1` is special for factorial. Without an explicit check, the
  argument passes `0` and continues into negative numbers forever. Even
  `factorial(0)` would be computed as `0 * factorial(-1)` and never return.

**Fix:**

```python
def factorial(value):
    if value <= 1:
        return 1
    return value * factorial(value - 1)
```

<div dir="rtl" align="right">

### بخش E: شکست بازگشتی

- **نبودِ حالت پایه (base case).** هر فراخوانی بدون هیچ شرطی یک فراخوانی دیگر
انجام می‌دهد. هیچ شرطی مانند `if value <= 1: return 1` وجود ندارد که تابع در
آن بدون بازگشت مقدار برگرداند، پس هیچ فراخوانی هرگز تمام نمی‌شود.

- **در نهایت چه اتفاقی می‌افتد.** هر فراخوانی یک frame به پشته‌ی فراخوانی
(call stack) اضافه می‌کند: `factorial(5)` ← `factorial(4)` ← … ← `factorial(0)`
← `factorial(-1)` ← … وقتی عمق به حد مجاز پایتون (به‌طور پیش‌فرض حدود ۱۰۰۰)
برسد، پایتون خطای `RecursionError: maximum recursion depth exceeded` می‌دهد.
هیچ ضربی هرگز انجام نمی‌شود، چون هر `value * ...` منتظر نتیجه‌ای است که هرگز
نمی‌رسد.

- **چرا کاهش اعداد بازگشت را متوقف نمی‌کند.** کوچک‌شدن آرگومان به معنای توقف
نیست. بازگشت فقط وقتی تمام می‌شود که کد به شاخه‌ای برسد که *بدون فراخوانی
خودش مقدار برگرداند*. پایتون نمی‌داند که `0` یا `1` برای فاکتوریل خاص است.
بدون یک بررسی صریح، آرگومان از `0` عبور می‌کند و تا بی‌نهایت به اعداد منفی
ادامه می‌دهد. حتی `factorial(0)` به‌صورت `0 * factorial(-1)` محاسبه می‌شود و
هرگز برنمی‌گردد.

**راه‌حل:** حالت پایه‌ی `if value <= 1: return 1` را اضافه کنید (کد بالا).

</div>
