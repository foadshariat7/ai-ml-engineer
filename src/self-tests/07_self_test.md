# Self-Test 07: Functions

This document explains the fourteen exercises in
[`07_self_test.py`](07_self_test.py): parameters versus arguments, positional
and keyword arguments, default arguments and the mutable-default trap,
rebinding versus mutation, `*args`, keyword-only arguments, `**kwargs`,
`return` versus `print`, functions as objects, higher-order functions,
closures, and recursion.

<div dir="rtl" align="right">

## خودآزمون ۷: توابع (Functions)

این سند چهارده تمرین موجود در فایل [`07_self_test.py`](07_self_test.py) را
توضیح می‌دهد: پارامتر در برابر آرگومان، آرگومان‌های موقعیتی (positional) و
کلیدواژه‌ای (keyword)، آرگومان‌های پیش‌فرض و تله‌ی پیش‌فرض تغییرپذیر،
بازانتساب (rebinding) در برابر تغییر درجا (mutation)، `*args`، آرگومان‌های فقط
کلیدواژه‌ای، `**kwargs`، `return` در برابر `print`، توابع به‌عنوان شیء، توابع
مرتبه‌بالا (higher-order)، closureها، و بازگشت (recursion).

</div>

## 1: Parameter versus argument

`value` and `factor` are the **parameters** — the names written in the `def`
line, which act as local variables inside the function. `5` and `3` are the
**arguments** — the actual values passed in the call `multiply(5, 3)`. When
the call runs, `value` is bound to `5` and `factor` to `3`, and the function
returns `15`, which is stored in `result` and printed. Parameters belong to
the definition; arguments belong to the call.

<div dir="rtl" align="right">

### ۱: پارامتر در برابر آرگومان

`value` و `factor` **پارامترها** هستند — نام‌هایی که در خط `def` نوشته می‌شوند
و درون تابع مانند متغیرهای محلی عمل می‌کنند. `5` و `3` **آرگومان‌ها** هستند —
مقادیر واقعی‌ای که در فراخوانی `multiply(5, 3)` ارسال می‌شوند. هنگام اجرای
فراخوانی، `value` به `5` و `factor` به `3` متصل می‌شود و تابع مقدار `15` را
برمی‌گرداند که در `result` ذخیره و چاپ می‌شود. پارامترها متعلق به تعریف‌اند؛
آرگومان‌ها متعلق به فراخوانی.

</div>

## 2: Positional versus keyword

Both calls work and both print `alice 0.9`. The first call is
**positional**: arguments are matched to parameters by order, so `"alice"` →
`name` and `0.9` → `score`. The second call uses **keyword** arguments: each
argument names its parameter explicitly, so the order no longer matters —
Python matches by name, not by position. `describe(0.9, "alice")` would
**not** mean the same thing: positionally it binds `name = 0.9` and
`score = "alice"`, printing `0.9 alice`. Python raises no error, so the bug is
silent — one reason keyword arguments make calls safer and more readable.

<div dir="rtl" align="right">

### ۲: موقعیتی در برابر کلیدواژه‌ای

هر دو فراخوانی کار می‌کنند و هر دو `alice 0.9` را چاپ می‌کنند. فراخوانی اول
**موقعیتی** است: آرگومان‌ها بر اساس ترتیب به پارامترها نسبت داده می‌شوند، پس
`"alice"` ← `name` و `0.9` ← `score`. فراخوانی دوم از آرگومان‌های
**کلیدواژه‌ای** استفاده می‌کند: هر آرگومان صراحتاً نام پارامتر خود را ذکر
می‌کند، پس ترتیب دیگر اهمیتی ندارد — پایتون بر اساس نام تطبیق می‌دهد، نه
موقعیت. `describe(0.9, "alice")` معنای یکسانی **ندارد**: به‌صورت موقعیتی
`name = 0.9` و `score = "alice"` می‌شود و `0.9 alice` چاپ می‌شود. پایتون خطایی
نمی‌دهد، پس این باگ بی‌صدا است — یکی از دلایلی که آرگومان‌های کلیدواژه‌ای
فراخوانی‌ها را امن‌تر و خواناتر می‌کنند.

</div>

## 3: Default arguments

The outputs are `9`, `27` and `16`. `power(3)` omits `exponent`, so the
default `2` is used: `3 ** 2 = 9`. `power(3, 3)` overrides the default:
`3 ** 3 = 27`. `power(value=4)` passes `value` by keyword and again falls back
to the default exponent: `4 ** 2 = 16`. A default is only used when the caller
does not supply that argument.

<div dir="rtl" align="right">

### ۳: آرگومان‌های پیش‌فرض

خروجی‌ها `9`، `27` و `16` هستند. `power(3)` مقدار `exponent` را ارسال نمی‌کند،
پس مقدار پیش‌فرض `2` استفاده می‌شود: `3 ** 2 = 9`. `power(3, 3)` مقدار پیش‌فرض
را بازنویسی می‌کند: `3 ** 3 = 27`. `power(value=4)` مقدار `value` را به‌صورت
کلیدواژه‌ای ارسال می‌کند و باز هم از توان پیش‌فرض استفاده می‌شود:
`4 ** 2 = 16`. مقدار پیش‌فرض فقط زمانی به کار می‌رود که فراخواننده آن آرگومان
را ارسال نکند.

</div>

## 4: Mutable default

The outputs are `[1]`, `[1, 2]`, `[3]` and `[1, 2, 4]`. A default value is
evaluated **once**, when the `def` statement runs — not on every call. So the
default `[]` is a single list object that lives on the function itself.
`add(1)`, `add(2)` and `add(4)` all omit `values`, so they all **share** that
same list, which keeps growing across calls. `add(3, [])` passes its own
fresh list, so it is unaffected and returns `[3]` — and it does not touch the
shared default either. The standard fix is a `None` sentinel:

```python
def add(value, values=None):
    if values is None:
        values = []
    values.append(value)
    return values
```

<div dir="rtl" align="right">

### ۴: پیش‌فرض تغییرپذیر

خروجی‌ها `[1]`، `[1, 2]`، `[3]` و `[1, 2, 4]` هستند. مقدار پیش‌فرض فقط **یک‌بار**
ارزیابی می‌شود، یعنی زمانی که دستور `def` اجرا می‌شود — نه در هر فراخوانی. پس
پیش‌فرض `[]` یک شیء لیست واحد است که روی خودِ تابع نگه داشته می‌شود.
`add(1)`، `add(2)` و `add(4)` همگی `values` را ارسال نمی‌کنند، پس همگی **در
همان لیست شریک‌اند** و آن لیست در طول فراخوانی‌ها مدام بزرگ‌تر می‌شود.
`add(3, [])` لیست تازه‌ی خودش را ارسال می‌کند، پس تحت تأثیر قرار نمی‌گیرد و
`[3]` را برمی‌گرداند — و به لیست پیش‌فرض مشترک هم دست نمی‌زند. راه‌حل استاندارد
استفاده از `None` به‌عنوان نگهبان (sentinel) است (کد بالا).

</div>

## 5: Local rebinding

The caller's list does **not** become `[99]`; `data` is still `[1, 2, 3]`.
Python passes a reference to the object, so at first the parameter `values`
and the caller's `data` point at the same list. But `values = [99]` is an
**assignment**: it creates a new list and rebinds only the local name
`values` to it. The caller's name `data` is a separate name that still points
at the original list, and the new list is discarded when the function
returns. Assigning to a parameter never changes the caller's variable.

<div dir="rtl" align="right">

### ۵: بازانتساب محلی

لیست فراخواننده به `[99]` تبدیل **نمی‌شود**؛ `data` همچنان `[1, 2, 3]` است.
پایتون ارجاعی به شیء ارسال می‌کند، پس در ابتدا پارامتر `values` و `data`ی
فراخواننده به یک لیست اشاره می‌کنند. اما `values = [99]` یک **انتساب** است:
لیست جدیدی می‌سازد و فقط نام محلی `values` را به آن متصل می‌کند. نام `data` در
فراخواننده نامی جداگانه است که همچنان به لیست اصلی اشاره می‌کند، و لیست جدید
هنگام بازگشت تابع دور ریخته می‌شود. انتساب به یک پارامتر هرگز متغیر
فراخواننده را تغییر نمی‌دهد.

</div>

## 6: Mutation

This time the output is `[1, 2, 3, 99]`. The difference from exercise 5 is
**mutation versus rebinding**. `values.append(99)` does not rebind the name
`values` — it modifies the list object that `values` points to. Since `data`
points at that very same object, the caller sees the change. Rule of thumb:
`name = ...` changes what a name refers to (local only); `name.method(...)` or
`name[i] = ...` changes the object itself (visible to everyone holding a
reference).

<div dir="rtl" align="right">

### ۶: تغییر درجا (Mutation)

این بار خروجی `[1, 2, 3, 99]` است. تفاوت با تمرین ۵، **تغییر درجا در برابر
بازانتساب** است. `values.append(99)` نام `values` را دوباره متصل نمی‌کند — بلکه
خودِ شیء لیستی را که `values` به آن اشاره می‌کند تغییر می‌دهد. چون `data` به
همان شیء اشاره می‌کند، فراخواننده تغییر را می‌بیند. قاعده‌ی سرانگشتی:
`name = ...` تغییر می‌دهد که یک نام به چه چیزی اشاره کند (فقط محلی)؛
`name.method(...)` یا `name[i] = ...` خودِ شیء را تغییر می‌دهد (برای هر کسی که
ارجاعی به آن دارد قابل مشاهده است).

</div>

## 7: *args

The outputs are `(10, 20, 30)` and `<class 'tuple'>`. The `*` in `*values`
collects **all extra positional arguments** into a single **tuple**, however
many there are — zero, three, or a hundred. It is a tuple (not a list), so it
is immutable. The name `args` is only a convention; the `*` is what does the
work.

<div dir="rtl" align="right">

### ۷: *args

خروجی‌ها `(10, 20, 30)` و `<class 'tuple'>` هستند. علامت `*` در `*values`
**همه‌ی آرگومان‌های موقعیتی اضافی** را در یک **تاپل (tuple)** جمع می‌کند، به
هر تعداد که باشند — صفر، سه یا صد. این یک تاپل است (نه لیست)، پس تغییرناپذیر
است. نام `args` فقط یک قرارداد است؛ کار اصلی را `*` انجام می‌دهد.

</div>

## 8: Keyword-only argument

The first call prints `('hello', 0.2)`. The second call, `predict("hello",
0.2)`, **fails** with:

```
TypeError: predict() takes 1 positional argument but 2 were given
```

The bare `*` in the signature means every parameter after it is
**keyword-only**: `temperature` can only be passed as `temperature=...`, never
by position. This forces callers to write self-documenting calls and prevents
a stray number from silently landing in the wrong parameter.

> Note: because this error is not caught, running the script stops here, and
> exercises 9–14 never execute. Comment out the failing line to see the rest.

<div dir="rtl" align="right">

### ۸: آرگومان فقط کلیدواژه‌ای

فراخوانی اول `('hello', 0.2)` را چاپ می‌کند. فراخوانی دوم،
`predict("hello", 0.2)`، با خطای `TypeError` بالا **شکست می‌خورد**. علامت `*`
تنها در امضای تابع یعنی هر پارامتر پس از آن **فقط کلیدواژه‌ای** است:
`temperature` فقط به‌صورت `temperature=...` قابل ارسال است، هرگز به‌صورت
موقعیتی. این کار فراخواننده‌ها را مجبور می‌کند فراخوانی‌هایی خودتوضیح بنویسند و
مانع می‌شود که یک عدد سرگردان بی‌صدا در پارامتر اشتباه قرار گیرد.

> توجه: چون این خطا گرفته نمی‌شود، اجرای اسکریپت همین‌جا متوقف می‌شود و
> تمرین‌های ۹ تا ۱۴ اجرا نمی‌شوند. برای دیدن بقیه، خط خطادار را کامنت کنید.

</div>

## 9: **kwargs

`options` is a **dict**, and it contains
`{'device': 'cuda', 'batch_size': 32}`. The `**` collects **all extra keyword
arguments** into a dictionary, mapping each argument name (as a string key)
to its value. It is the keyword counterpart of `*args`, and is commonly used
to forward configuration options to another function.

<div dir="rtl" align="right">

### ۹: **kwargs

`options` یک **دیکشنری (dict)** است و شامل `{'device': 'cuda', 'batch_size': 32}`
است. علامت `**` **همه‌ی آرگومان‌های کلیدواژه‌ای اضافی** را در یک دیکشنری جمع
می‌کند و نام هر آرگومان (به‌صورت کلید رشته‌ای) را به مقدارش نگاشت می‌کند. این
همتای کلیدواژه‌ای `*args` است و معمولاً برای انتقال گزینه‌های پیکربندی به تابعی
دیگر استفاده می‌شود.

</div>

## 10: return versus print

The printed lines are `10`, `None`, `10`. Calling `first()` prints `10` as a
side effect — but it has no `return` statement, so it returns `None`, and `a`
is `None`. Calling `second()` prints nothing; it returns `10`, so `b` is `10`.
Then `print(a)` shows `None` and `print(b)` shows `10`. `print` sends text to
the screen; `return` hands a value back to the caller. Only a returned value
can be stored and used later.

<div dir="rtl" align="right">

### ۱۰: return در برابر print

خطوط چاپ‌شده `10`، `None` و `10` هستند. فراخوانی `first()` مقدار `10` را به‌عنوان
اثر جانبی چاپ می‌کند — اما دستور `return` ندارد، پس `None` برمی‌گرداند و `a`
برابر `None` می‌شود. فراخوانی `second()` چیزی چاپ نمی‌کند؛ مقدار `10` را
برمی‌گرداند، پس `b` برابر `10` است. سپس `print(a)` مقدار `None` و `print(b)`
مقدار `10` را نشان می‌دهد. `print` متن را روی صفحه می‌فرستد؛ `return` مقداری را
به فراخواننده تحویل می‌دهد. فقط مقدار بازگشتی را می‌توان ذخیره کرد و بعداً
استفاده کرد.

</div>

## 11: Function objects

The results are `25` and `True`. In Python a function is an ordinary
**object**, and `def square` simply binds that object to the name `square`.
`operation = square` (no parentheses) binds a second name to the **same**
function object — nothing is called or copied. So `operation(5)` runs
`square` and returns `25`, and `operation is square` is `True` because both
names refer to the identical object.

<div dir="rtl" align="right">

### ۱۱: توابع به‌عنوان شیء

نتایج `25` و `True` هستند. در پایتون یک تابع یک **شیء** معمولی است و
`def square` صرفاً آن شیء را به نام `square` متصل می‌کند. `operation = square`
(بدون پرانتز) نام دومی را به **همان** شیء تابع متصل می‌کند — چیزی فراخوانی یا
کپی نمی‌شود. پس `operation(5)` تابع `square` را اجرا کرده و `25` را برمی‌گرداند،
و `operation is square` برابر `True` است چون هر دو نام به یک شیء یکسان اشاره
می‌کنند.

</div>

## 12: Higher-order function

The output is `20`. `apply` is a **higher-order function**: it takes another
function as an argument. We pass `double` — the function object itself — not
`double()`. Writing `double()` would call `double` immediately (with no
argument, which would raise a `TypeError`) and pass its result instead of the
function. Passing `double` lets `apply` decide **when** and with **what** to
call it: inside, `operation(value)` becomes `double(10)`, which returns `20`.

<div dir="rtl" align="right">

### ۱۲: تابع مرتبه‌بالا

خروجی `20` است. `apply` یک **تابع مرتبه‌بالا** است: تابع دیگری را به‌عنوان
آرگومان می‌گیرد. ما `double` را ارسال می‌کنیم — یعنی خودِ شیء تابع — نه
`double()`. نوشتن `double()` تابع `double` را فوراً فراخوانی می‌کند (بدون
آرگومان، که منجر به `TypeError` می‌شود) و به‌جای خودِ تابع، نتیجه‌ی آن را ارسال
می‌کند. ارسال `double` به `apply` اجازه می‌دهد تصمیم بگیرد **کی** و با **چه
مقداری** آن را فراخوانی کند: درون آن، `operation(value)` به `double(10)` تبدیل
می‌شود که `20` را برمی‌گرداند.

</div>

## 13: Closure

The outputs are `10` and `15`. Each call to `make_multiplier` creates a new
inner function `multiply` that refers to `factor`. Normally a function's local
variables disappear when it returns, but because the inner function still
needs `factor`, Python keeps it alive in a **closure** — a captured
environment attached to the inner function. `double` remembers `factor = 2`
and `triple` remembers `factor = 3`; they are independent, so
`double(5) = 10` and `triple(5) = 15`.

<div dir="rtl" align="right">

### ۱۳: Closure

خروجی‌ها `10` و `15` هستند. هر فراخوانی `make_multiplier` یک تابع درونی جدید
`multiply` می‌سازد که به `factor` ارجاع می‌دهد. معمولاً متغیرهای محلی یک تابع
پس از بازگشت آن از بین می‌روند، اما چون تابع درونی هنوز به `factor` نیاز دارد،
پایتون آن را در یک **closure** زنده نگه می‌دارد — محیطی ضبط‌شده که به تابع
درونی پیوست شده است. `double` مقدار `factor = 2` و `triple` مقدار `factor = 3`
را به یاد دارد؛ این دو مستقل‌اند، پس `double(5) = 10` و `triple(5) = 15`.

</div>

## 14: Recursion

The output is `3`, `2`, `1`, each on its own line. The **base case** is
`if value == 0: return` — the condition under which the function stops
calling itself. The **recursive case** is `print(value)` followed by
`countdown(value - 1)` — it does one step of work and then calls itself on a
smaller problem. Each call moves `value` one step closer to `0`, which
guarantees the recursion terminates. Without the base case, the calls would
continue until Python raises `RecursionError`.

<div dir="rtl" align="right">

### ۱۴: بازگشت (Recursion)

خروجی `3`، `2`، `1` است، هر کدام در یک خط. **حالت پایه (base case)**
`if value == 0: return` است — شرطی که در آن تابع دیگر خودش را فراخوانی نمی‌کند.
**حالت بازگشتی (recursive case)** `print(value)` و سپس `countdown(value - 1)`
است — یک گام کار انجام می‌دهد و سپس خودش را روی مسئله‌ای کوچک‌تر فراخوانی
می‌کند. هر فراخوانی `value` را یک گام به `0` نزدیک‌تر می‌کند، که پایان یافتن
بازگشت را تضمین می‌کند. بدون حالت پایه، فراخوانی‌ها ادامه می‌یابند تا پایتون
خطای `RecursionError` بدهد.

</div>
