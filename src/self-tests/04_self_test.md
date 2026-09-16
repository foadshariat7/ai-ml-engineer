# Self-Test 04: Dictionary Semantics

This document explains the six exercises in
[`04_self_test.py`](04_self_test.py): key collisions, truthiness, `None` vs.
missing keys, booleans as numbers, and hashable keys.

<div dir="rtl" align="right">

## خودآزمون ۴: رفتار دیکشنری‌ها (Dictionary Semantics)

این سند شش تمرین موجود در فایل [`04_self_test.py`](04_self_test.py) را توضیح
می‌دهد: برخورد کلیدهای تکراری، truthiness، تفاوت `None` با کلید غایب، بولین‌ها
به‌عنوان عدد، و کلیدهای hashable.

</div>

## 1: Counting repeated keys

`counts.get(token, 0)` returns `0` when the key is not yet present, so the
first `"red"` becomes `1`. Because `"red"` is later seen two more times, the
final dictionary has **three** entries (`red`, `blue`, `green`), and on the
third occurrence of `"red"` the `.get()` call returns `2` (the count so far),
which is then incremented to `3`.

<div dir="rtl" align="right">

### ۱: شمارش کلیدهای تکراری

وقتی کلید هنوز در دیکشنری وجود ندارد، `counts.get(token, 0)` مقدار `0` را
برمی‌گرداند؛ به همین دلیل اولین `"red"` مقدار `1` می‌گیرد. چون `"red"` دو بار
دیگر هم دیده می‌شود، دیکشنری نهایی **سه** کلید دارد (`red`، `blue`، `green`)
و در سومین باری که `"red"` دیده می‌شود، `.get()` مقدار `2` (شمارش تا آن لحظه)
را برمی‌گرداند که سپس به `3` افزایش می‌یابد.

</div>

## 2: Assignment to an existing key

A dictionary can hold only **one** value per key. Each assignment to
`scores["u1"]` overwrites the previous value, so the dictionary ends up with
a single entry, `{"u1": 1.0}`, not three. To preserve all three values you
would need a different structure — e.g. append to a list stored at that key,
or use a key that is unique per assignment.

<div dir="rtl" align="right">

### ۲: انتساب به یک کلید موجود

هر کلید در دیکشنری فقط می‌تواند **یک** مقدار داشته باشد. هر انتساب به
`scores["u1"]` مقدار قبلی را جایگزین می‌کند، پس دیکشنری نهایی تنها یک ورودی
دارد، `{"u1": 1.0}`، نه سه ورودی. برای نگه‌داشتن هر سه مقدار باید از ساختار
دیگری استفاده کرد — مثلاً افزودن به یک لیست ذخیره‌شده در آن کلید، یا استفاده
از کلیدی که برای هر انتساب یکتا باشد.

</div>

## 3: Zero and truthiness

`0.0` is not missing — the key exists and holds a real, valid score. But
`0.0` is falsy in Python, so `record["score"] is None` is `False` while
`bool(record["score"])` is also `False`. The `if not record["score"]:` check
cannot tell "no score" apart from "a score of exactly zero," so it wrongly
prints `"ignored"` for a legitimate zero score. Truthiness checks are
dangerous for validation whenever a valid value (`0`, `0.0`, `""`, `[]`) is
also falsy — the check silently conflates "missing" with "present but
falsy."

<div dir="rtl" align="right">

### ۳: صفر و truthiness

`0.0` غایب نیست — کلید وجود دارد و یک امتیاز واقعی و معتبر در خود نگه می‌دارد.
اما `0.0` در پایتون falsy (نادرست‌نما) است، پس `record["score"] is None`
مقدار `False` می‌دهد در حالی که `bool(record["score"])` هم `False` است. شرط
`if not record["score"]:` نمی‌تواند «امتیاز ندارد» را از «امتیازش دقیقاً صفر
است» تشخیص دهد، پس به‌اشتباه برای یک امتیاز صفرِ معتبر عبارت `"ignored"` را
چاپ می‌کند. بررسی truthiness هرجا که یک مقدار معتبر (`0`، `0.0`، `""`، `[]`)
هم falsy باشد برای اعتبارسنجی خطرناک است — این بررسی به‌طور نامحسوس «غایب» را
با «موجود اما falsy» یکی می‌گیرد.

</div>

## 4: Missing key versus present None

No — `.get()` alone cannot distinguish them: `first.get("score")` and
`second.get("score")` both return `None`, one because the key is absent and
the other because the key is present with value `None`. The `in` operator
distinguishes them: `"score" in first` is `False` (key absent) while
`"score" in second` is `True` (key present, value `None`).

<div dir="rtl" align="right">

### ۴: کلید غایب در برابر مقدار None موجود

خیر — تنها با `.get()` نمی‌توان این دو را از هم تشخیص داد: هم
`first.get("score")` و هم `second.get("score")` مقدار `None` برمی‌گردانند،
یکی به این دلیل که کلید وجود ندارد و دیگری چون کلید با مقدار `None` وجود
دارد. عملگر `in` این دو را از هم تشخیص می‌دهد: `"score" in first` مقدار
`False` می‌دهد (کلید غایب است) در حالی که `"score" in second` مقدار `True`
می‌دهد (کلید موجود است، با مقدار `None`).

</div>

## 5: Boolean numbers

In Python, `bool` is a subclass of `int`, so `isinstance(True, bool)` and
`isinstance(True, int)` are both `True`. `True` behaves as `1` numerically:
`float(True)` is `1.0` and `True + 2` is `3`. A model score of `True` should
**not** be silently accepted as `1.0`, because a boolean usually signals a
different kind of value than a genuine numeric score. To reject booleans
while still accepting integers, check `type(x) is bool` (or
`isinstance(x, bool)`) **before** the `isinstance(x, int)` check, since
`isinstance` alone cannot separate the two.

<div dir="rtl" align="right">

### ۵: بولین‌ها به‌عنوان عدد

در پایتون، `bool` زیرکلاسی از `int` است، پس هم `isinstance(True, bool)` و هم
`isinstance(True, int)` مقدار `True` می‌دهند. `True` از نظر عددی مانند `1`
رفتار می‌کند: `float(True)` برابر `1.0` است و `True + 2` برابر `3` است. یک
امتیاز مدل با مقدار `True` **نباید** به‌سادگی به‌عنوان `1.0` پذیرفته شود،
چون بولین معمولاً نوع متفاوتی از مقدار را نسبت به یک امتیاز عددی واقعی نشان
می‌دهد. برای رد کردن بولین‌ها و در عین حال پذیرفتن عدد صحیح، باید
`type(x) is bool` (یا `isinstance(x, bool)`) را **پیش از** بررسی
`isinstance(x, int)` چک کرد، چون خودِ `isinstance` به‌تنهایی نمی‌تواند این دو
را از هم جدا کند.

</div>

## 6: Hashable keys

The third assignment, `result[[1, 2]] = "ready"`, fails with a
`TypeError: unhashable type: 'list'`. Dictionary keys must be hashable
(their hash value must never change over their lifetime), which requires
them to be immutable. Strings and tuples (of hashable elements) are
immutable and hashable, so `"model-a"` and `("model", 1)` work fine as
keys. Lists are mutable, so Python refuses to hash them — allowing a list as
a key would let its hash change after insertion, breaking the dictionary's
internal lookup structure.

<div dir="rtl" align="right">

### ۶: کلیدهای hashable

سومین انتساب، `result[[1, 2]] = "ready"`، با خطای
`TypeError: unhashable type: 'list'` شکست می‌خورد. کلیدهای دیکشنری باید
hashable باشند (مقدار hash آن‌ها هرگز در طول عمرشان نباید تغییر کند)، و این
یعنی باید تغییرناپذیر (immutable) باشند. رشته‌ها و تاپل‌ها (با عناصر
hashable) تغییرناپذیر و hashable هستند، پس `"model-a"` و `("model", 1)`
به‌خوبی به‌عنوان کلید کار می‌کنند. لیست‌ها تغییرپذیرند، پس پایتون از hash کردن
آن‌ها خودداری می‌کند — اگر لیست به‌عنوان کلید مجاز بود، hash آن می‌توانست پس
از درج تغییر کند و ساختار جست‌وجوی داخلی دیکشنری را خراب کند.

</div>
