# Self-Test 02: Scope, Operators, and Loops

This document explains the twelve exercises in
[`02_self_test.py`](02_self_test.py): variable scope and LEGB, shadowing a
built-in name, the three division/modulo operators, operator
associativity, string indexing and immutability, short-circuiting
`and`/`or`, chained comparisons, `if`/`elif` ordering, and loop
constructs.

<div dir="rtl" align="right">

## خودآزمون ۲: دامنه (Scope)، عملگرها و حلقه‌ها

این سند دوازده تمرین موجود در فایل [`02_self_test.py`](02_self_test.py) را
توضیح می‌دهد: دامنه‌ی متغیرها و قانون LEGB، سایه انداختن روی یک نام درونی
(built-in)، سه عملگر تقسیم/باقی‌مانده، شرکت‌پذیری (associativity) عملگرها،
ایندکس‌گذاری و تغییرناپذیری رشته، اتصال کوتاه (short-circuit) در `and`/`or`،
مقایسه‌های زنجیره‌ای، ترتیب `if`/`elif`، و ساختارهای حلقه.

</div>

## 1: Scope

`show()` prints `20`, and the `print(x)` after it prints `10`. Assigning
to `x` anywhere inside a function body (`x = 20`) makes Python treat `x`
as a **local** variable for the entire function, even on lines before
the assignment. That local `x` shadows the global `x` only inside
`show`; it is a separate variable that disappears once the function
returns, leaving the global `x` (`10`) untouched.

<div dir="rtl" align="right">

### ۱: دامنه (Scope)

`show()` مقدار `20` را چاپ می‌کند، و `print(x)` بعد از آن مقدار `10` را
چاپ می‌کند. انتساب به `x` در هر جای بدنه‌ی تابع (`x = 20`) باعث می‌شود
پایتون `x` را در کل آن تابع به‌عنوان یک متغیر **محلی (local)** در نظر
بگیرد، حتی در خطوطی که پیش از آن انتساب قرار دارند. این `x` محلی فقط
داخل `show` روی `x` سراسری سایه می‌اندازد؛ متغیری جداگانه است که با پایان
تابع از بین می‌رود و `x` سراسری (`10`) دست‌نخورده باقی می‌ماند.

</div>

## 2: LEGB (Local, Enclosing, Global, Built-in)

`inner()` prints `"enclosing"`. `inner` has no local `x` of its own, so
Python looks outward following **LEGB**: Local (none in `inner`) →
Enclosing (`outer`'s `x = "enclosing"` — found here, search stops) →
Global → Built-in. Because the enclosing scope already has a match, the
global `x = "global"` is never reached.

<div dir="rtl" align="right">

### ۲: LEGB (محلی، محصورکننده، سراسری، درونی)

`inner()` مقدار `"enclosing"` را چاپ می‌کند. `inner` هیچ `x` محلی خاص خود
را ندارد، پس پایتون طبق قانون **LEGB** به بیرون نگاه می‌کند: محلی (چیزی در
`inner` نیست) → محصورکننده (`x = "enclosing"` در `outer` — اینجا پیدا
می‌شود و جست‌وجو متوقف می‌شود) → سراسری → درونی (Built-in). چون در
scope محصورکننده مقدار پیدا شده، هرگز به `x = "global"` سراسری نمی‌رسد.

</div>

## 3: Built-in shadowing

`list = [1, 2, 3]` rebinds the name `list` in this scope to a plain list
object, shadowing the built-in `list` type. If the commented-out line
`numbers = list("123")` were uncommented, it would raise
`TypeError: 'list' object is not callable`, because `list` no longer
refers to the built-in constructor — it refers to `[1, 2, 3]`, which
isn't callable. This is why naming a variable after a built-in
(`list`, `dict`, `str`, `id`, `type`, ...) is risky: it hides the
built-in for the rest of that scope.

<div dir="rtl" align="right">

### ۳: سایه انداختن روی نام‌های درونی (Built-in shadowing)

`list = [1, 2, 3]` نام `list` را در این scope به یک شیء لیست ساده تغییر
می‌دهد و روی نوع درونی (built-in) `list` سایه می‌اندازد. اگر خط
کامنت‌شده‌ی `numbers = list("123")` از حالت کامنت خارج شود، خطای
`TypeError: 'list' object is not callable` رخ می‌دهد، چون `list` دیگر به
سازنده‌ی درونی اشاره نمی‌کند — بلکه به `[1, 2, 3]` اشاره می‌کند که
callable نیست. به همین دلیل نام‌گذاری یک متغیر با نام یک built-in
(`list`، `dict`، `str`، `id`، `type` و...) خطرناک است: آن built-in را در
باقی‌ی آن scope پنهان می‌کند.

</div>

## 4: Integer division

- `7 / 2` → `3.5` — **true division**, always returns a `float`.
- `7 // 2` → `3` — **floor division**, discards the remainder and rounds
  toward negative infinity (returns an `int` when both operands are
  `int`).
- `7 % 2` → `1` — **modulo**, the remainder left over after floor
  division; it satisfies `a == (a // b) * b + (a % b)`.

<div dir="rtl" align="right">

### ۴: تقسیم اعداد صحیح

- `7 / 2` → `3.5` — **تقسیم واقعی (true division)**، همیشه یک `float`
  برمی‌گرداند.
- `7 // 2` → `3` — **تقسیم صحیح (floor division)**، باقی‌مانده را کنار
  می‌گذارد و به سمت منفی بی‌نهایت گرد می‌کند (وقتی هر دو عملوند `int`
  باشند، یک `int` برمی‌گرداند).
- `7 % 2` → `1` — **باقی‌مانده (modulo)**، باقی‌مانده‌ی پس از تقسیم صحیح؛
  در رابطه‌ی `a == (a // b) * b + (a % b)` صدق می‌کند.

</div>

## 5: Exponentiation

`result` is `512`, not `64`. The `**` operator is **right-associative**,
so `2 ** 3 ** 2` groups as `2 ** (3 ** 2)` = `2 ** 9` = `512` — not
`(2 ** 3) ** 2` = `64`. This is the opposite of most other binary
operators (like `-` or `/`), which are left-associative.

<div dir="rtl" align="right">

### ۵: توان‌رسانی (Exponentiation)

مقدار `result` برابر `512` است، نه `64`. عملگر `**` **راست‌شرکت‌پذیر
(right-associative)** است، پس `2 ** 3 ** 2` به‌صورت `2 ** (3 ** 2)` یعنی
`2 ** 9` یعنی `512` گروه‌بندی می‌شود — نه `(2 ** 3) ** 2` که `64` می‌شود.
این رفتار برخلاف بیشتر عملگرهای دوتایی دیگر (مثل `-` یا `/`) است که
چپ‌شرکت‌پذیر (left-associative) هستند.

</div>

## 6: String indexing

- `language[0]` → `"P"` — indexing is 0-based, so index `0` is the first
  character.
- `language[-1]` → `"n"` — negative indices count from the end;
  `-1` is the last character.
- `language[1:4]` → `"yth"` — a slice `[start:stop]` includes `start`
  and excludes `stop`, so it takes indices `1`, `2`, `3`.

<div dir="rtl" align="right">

### ۶: ایندکس‌گذاری رشته

- `language[0]` → `"P"` — ایندکس‌گذاری از ۰ شروع می‌شود، پس ایندکس `0`
  اولین کاراکتر است.
- `language[-1]` → `"n"` — ایندکس‌های منفی از انتها شمرده می‌شوند؛
  `-1` آخرین کاراکتر است.
- `language[1:4]` → `"yth"` — یک برش (slice) با فرم `[start:stop]`
  شامل `start` است و `stop` را شامل نمی‌شود، پس ایندکس‌های `1`، `2`، `3`
  را برمی‌دارد.

</div>

## 7: String immutability

No — `name[0] = "T"` would raise
`TypeError: 'str' object does not support item assignment`. Strings in
Python are **immutable**: none of their characters can be changed after
creation. To get a modified string you must build a new one, e.g.
`name = "T" + name[1:]`.

<div dir="rtl" align="right">

### ۷: تغییرناپذیری رشته

خیر — `name[0] = "T"` خطای
`TypeError: 'str' object does not support item assignment` می‌دهد.
رشته‌ها در پایتون **تغییرناپذیر (immutable)** هستند: هیچ‌کدام از
کاراکترهای آن‌ها پس از ساخته‌شدن قابل تغییر نیست. برای گرفتن یک رشته‌ی
تغییریافته باید رشته‌ای جدید بسازید، مثلاً `name = "T" + name[1:]`.

</div>

## 8: and

No. `result` is `""` (the empty string), not `False`. Python's `and`
does not coerce its result to a `bool` — it **short-circuits**: if the
left operand is falsy, `and` returns the left operand immediately
without evaluating the right one at all. Since `""` is falsy, `"" and
"Python"` evaluates to `""`.

<div dir="rtl" align="right">

### ۸: عملگر and

خیر. مقدار `result` برابر `""` (رشته‌ی خالی) است، نه `False`. عملگر
`and` در پایتون نتیجه را به `bool` تبدیل نمی‌کند — به‌صورت **اتصال کوتاه
(short-circuit)** عمل می‌کند: اگر عملوند چپ falsy باشد، `and` بلافاصله
همان عملوند چپ را برمی‌گرداند و اصلاً عملوند راست را ارزیابی نمی‌کند. چون
`""` مقدار falsy است، `"" and "Python"` به `""` می‌رسد.

</div>

## 9: or

Prints `Anonymous`. `or` returns the first **truthy** operand, or the
last operand if every operand is falsy. `name` is `""` (falsy), so
Python evaluates and returns the right-hand operand, `"Anonymous"`.
This is a common idiom for defaults — but like `if not value:` checks,
it can't distinguish "empty/falsy" from "genuinely absent."

<div dir="rtl" align="right">

### ۹: عملگر or

مقدار `Anonymous` چاپ می‌شود. `or` اولین عملوند **truthy** را برمی‌گرداند،
یا اگر همه‌ی عملوندها falsy باشند، آخرین عملوند را برمی‌گرداند. `name`
برابر `""` (falsy) است، پس پایتون عملوند سمت راست، یعنی `"Anonymous"`،
را ارزیابی و برمی‌گرداند. این یک الگوی رایج برای مقدار پیش‌فرض است — اما
مانند بررسی `if not value:`، نمی‌تواند «خالی/falsy» را از «واقعاً غایب»
تشخیص دهد.

</div>

## 10: Chained comparisons

`0 <= score <= 100` is equivalent to `0 <= score and score <= 100`
(equivalently `score >= 0 and score <= 100`). A chained comparison is
syntactic sugar for combining both comparisons with `and`, with one
extra benefit: the middle expression (`score`) is evaluated only
**once**, whereas the manual `and` version evaluates it twice — which
matters if that expression has side effects.

<div dir="rtl" align="right">

### ۱۰: مقایسه‌های زنجیره‌ای

`0 <= score <= 100` معادل `0 <= score and score <= 100` است (یا به‌طور
مشابه `score >= 0 and score <= 100`). یک مقایسه‌ی زنجیره‌ای در واقع
میان‌بری نحوی (syntactic sugar) برای ترکیب دو مقایسه با `and` است، با
یک مزیت اضافه: عبارت میانی (`score`) فقط **یک‌بار** ارزیابی می‌شود، در
حالی که نسخه‌ی دستی با `and` آن را دو بار ارزیابی می‌کند — که اگر آن
عبارت اثر جانبی (side effect) داشته باشد، اهمیت پیدا می‌کند.

</div>

## 11: Condition order

Prints `Passed`, not `Excellent` — and this is the bug. `score >= 60`
is `True` for `score = 95`, so that branch runs and the chain stops
there; `elif score >= 90` is never even checked, even though it's also
true. An `if`/`elif`/`else` chain runs only the **first** branch whose
condition is true. To get the intended behavior, the more specific
(higher threshold) condition must come first:

```python
if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Passed")
else:
    print("Failed")
```

<div dir="rtl" align="right">

### ۱۱: ترتیب شرط‌ها

خروجی `Passed` است، نه `Excellent` — و این همان باگ است. برای
`score = 95`، شرط `score >= 60` برابر `True` است، پس همان شاخه اجرا
می‌شود و زنجیره همان‌جا متوقف می‌شود؛ حتی `elif score >= 90` هم بررسی
نمی‌شود، با اینکه آن هم درست است. یک زنجیره‌ی `if`/`elif`/`else` فقط
**اولین** شاخه‌ای را اجرا می‌کند که شرطش درست باشد. برای رسیدن به رفتار
موردنظر، باید شرط خاص‌تر (آستانه‌ی بالاتر) اول بیاید:

```python
if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Passed")
else:
    print("Failed")
```

</div>

## 12: Loops (for, break, continue, while, else)

1. `range(2, 8, 2)` → `2, 4, 6` (the `stop` value, `8`, is excluded).
2. Prints `0, 1, 2`, then `break` exits the loop as soon as
   `number == 3` — **before** `3` is printed.
3. Prints `0, 1, 3, 4`; `continue` skips only the rest of that one
   iteration (`number == 2`), so `2` is never printed but the loop
   keeps going.
4. **This is a bug, and it hangs the program.** `count` is never
   incremented inside the `while` body, so `count < 5` is always true —
   this is an infinite loop that prints `0` forever. It needs
   `count += 1` inside the loop to terminate.
5. Prints `0, 1, 2`, then `Done`. A `for...else` block's `else` runs
   when the loop finishes normally (without hitting a `break`) — here
   there's no `break`, so `"Done"` always prints after the loop.

<div dir="rtl" align="right">

### ۱۲: حلقه‌ها (for، break، continue، while، else)

۱. `range(2, 8, 2)` → `2, 4, 6` (مقدار `stop` یعنی `8` شامل نمی‌شود).
۲. مقادیر `0, 1, 2` چاپ می‌شوند، سپس `break` به‌محض `number == 3` از
حلقه خارج می‌شود — **پیش از** چاپ `3`.
۳. مقادیر `0, 1, 3, 4` چاپ می‌شوند؛ `continue` فقط باقی‌ی همان یک تکرار
را رد می‌کند (`number == 2`)، پس `2` هرگز چاپ نمی‌شود اما حلقه ادامه
پیدا می‌کند.
۴. **این یک باگ است و برنامه را متوقف (hang) می‌کند.** `count` هرگز در
بدنه‌ی حلقه‌ی `while` افزایش پیدا نمی‌کند، پس `count < 5` همیشه درست
است — این یک حلقه‌ی بی‌نهایت است که `0` را برای همیشه چاپ می‌کند. برای
پایان یافتن، باید `count += 1` داخل حلقه اضافه شود.
۵. مقادیر `0, 1, 2` و سپس `Done` چاپ می‌شوند. بخش `else` در ساختار
`for...else` زمانی اجرا می‌شود که حلقه به‌طور عادی (بدون رسیدن به
`break`) تمام شود — اینجا `break`ای وجود ندارد، پس `"Done"` همیشه بعد
از حلقه چاپ می‌شود.

</div>
