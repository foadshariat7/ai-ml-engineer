# Self-Test 06: Comprehensions

This document explains the seven exercises in
[`06_self_test.py`](06_self_test.py): list comprehensions as transformation,
filtering with `if`, the difference between a filter clause and a conditional
expression, set and dictionary comprehensions, and the truthiness trap in a
comprehension filter.

<div dir="rtl" align="right">

## خودآزمون ۶: Comprehensionها

این سند هفت تمرین موجود در فایل [`06_self_test.py`](06_self_test.py) را توضیح
می‌دهد: comprehension لیستی به‌عنوان تبدیل (transformation)، فیلتر کردن با
`if`، تفاوت بند فیلتر با عبارت شرطی (conditional expression)، comprehension
مجموعه‌ای و دیکشنری، و تله‌ی truthiness در فیلتر یک comprehension.

</div>

## 1: Basic transformation

The comprehension prints `[2, 4, 6, 8]`. Every input value produces exactly
one output value, so **four** output values are created — a comprehension
without an `if` clause is a pure one-to-one transformation. It does **not**
change `values`: `value * 2` builds new integers and the comprehension
collects them in a brand-new list, leaving the original `[1, 2, 3, 4]`
untouched.

<div dir="rtl" align="right">

### ۱: تبدیل پایه

این comprehension مقدار `[2, 4, 6, 8]` را چاپ می‌کند. هر مقدار ورودی دقیقاً یک
مقدار خروجی تولید می‌کند، پس **چهار** مقدار خروجی ساخته می‌شود — یک
comprehension بدون بند `if` صرفاً یک تبدیل یک‌به‌یک است. این کار `values` را
**تغییر نمی‌دهد**: عبارت `value * 2` اعداد جدیدی می‌سازد و comprehension آن‌ها
را در یک لیست کاملاً تازه جمع می‌کند، و لیست اصلی `[1, 2, 3, 4]` دست‌نخورده
باقی می‌ماند.

</div>

## 2: Filtering

The result is `[1, 2, 3]`. Zero is **not** included, because `0 > 0` is
`False`. Here not every input value produces an output: `if value > 0` is a
**filter**, not a transformation — it decides which items survive, so the
output list can be shorter than the input (seven inputs, three outputs). The
expression part (`value`) is what transforms; the `if` clause only selects.

<div dir="rtl" align="right">

### ۲: فیلتر کردن

نتیجه `[1, 2, 3]` است. صفر **گنجانده نمی‌شود**، چون `0 > 0` برابر `False` است.
اینجا هر مقدار ورودی یک خروجی تولید نمی‌کند: `if value > 0` یک **فیلتر** است،
نه یک تبدیل — تعیین می‌کند کدام عناصر باقی بمانند، پس لیست خروجی می‌تواند
کوتاه‌تر از ورودی باشد (هفت ورودی، سه خروجی). بخش عبارت (`value`) کار تبدیل را
انجام می‌دهد؛ بند `if` فقط انتخاب می‌کند.

</div>

## 3: Transformation + filtering

The result is `[1, 4, 9]`. Python does **not** square the negative numbers and
then discard them — the condition is evaluated **first**, and only the items
that pass it ever reach the expression. The evaluation order is: take
`value` from `values` → test `if value > 0` → if it passes, evaluate
`value * value` and append. So `-3`, `-2`, `-1` and `0` are rejected before
any multiplication happens, and only `1`, `2`, `3` are squared.

<div dir="rtl" align="right">

### ۳: تبدیل به‌همراه فیلتر

نتیجه `[1, 4, 9]` است. پایتون اعداد منفی را مجذور **نمی‌کند** تا بعد دور
بریزد — شرط **اول** ارزیابی می‌شود و تنها عناصری که از آن عبور کنند به عبارت
می‌رسند. ترتیب ارزیابی چنین است: گرفتن `value` از `values` ← بررسی
`if value > 0` ← در صورت عبور، ارزیابی `value * value` و افزودن آن. پس `-3`،
`-2`، `-1` و `0` پیش از هر ضربی رد می‌شوند و فقط `1`، `2` و `3` مجذور
می‌شوند.

</div>

## 4: Filter versus conditional expression

`a` is `[3]` and `b` is `[0, 0, 3]`. The lengths differ because the two `if`s
sit in different places and do different jobs. In `a`, the `if value > 0`
comes **after** the `for` and is a filter clause: it **removes** elements, so
`a` has fewer entries than the input. In `b`, `value if value > 0 else 0` is a
**conditional expression** in the expression slot: it runs for every element
and only chooses what that element maps to, so `b` always has exactly as many
entries as the input (three). Rule of thumb: an `if` before the `for` picks a
value; an `if` after the `for` picks which items stay.

<div dir="rtl" align="right">

### ۴: فیلتر در برابر عبارت شرطی

مقدار `a` برابر `[3]` و مقدار `b` برابر `[0, 0, 3]` است. طول‌ها متفاوت‌اند چون
این دو `if` در جای متفاوتی قرار دارند و کار متفاوتی انجام می‌دهند. در `a`،
عبارت `if value > 0` **پس از** `for` آمده و یک بند فیلتر است: عناصر را **حذف
می‌کند**، پس `a` ورودی‌های کمتری از ورودی دارد. در `b`، عبارت
`value if value > 0 else 0` یک **عبارت شرطی** در جایگاه عبارت است: برای هر
عنصر اجرا می‌شود و فقط تعیین می‌کند آن عنصر به چه چیزی نگاشت شود، پس `b` همیشه
دقیقاً به تعداد ورودی (سه) عنصر دارد. قاعده‌ی سرانگشتی: `if` پیش از `for` یک
مقدار را انتخاب می‌کند؛ `if` پس از `for` انتخاب می‌کند چه عناصری بمانند.

</div>

## 5: Set comprehension

The lengths are `2, 2, 2, 6, 2`, so there are only **two** unique lengths and
the result is `{2, 6}`. The result can contain fewer entries than the input
because a set stores each distinct value only once — duplicates collapse
silently (five words in, two lengths out). A set comprehension is **not**
guaranteed to preserve the original order: a set is unordered, so the printed
order comes from the internal hash layout, not from `words`. If order matters,
use a list comprehension (and de-duplicate explicitly) or
`dict.fromkeys(...)`.

<div dir="rtl" align="right">

### ۵: Comprehension مجموعه‌ای

طول‌ها برابر `2, 2, 2, 6, 2` هستند، پس تنها **دو** طول یکتا وجود دارد و نتیجه
`{2, 6}` است. نتیجه می‌تواند ورودی‌های کمتری از ورودی داشته باشد چون مجموعه
(set) هر مقدار متمایز را فقط یک‌بار نگه می‌دارد — مقادیر تکراری بی‌سروصدا در هم
ادغام می‌شوند (پنج واژه وارد، دو طول خارج). یک comprehension مجموعه‌ای تضمینی
برای حفظ ترتیب اصلی **نمی‌دهد**: مجموعه بدون ترتیب است، پس ترتیب چاپ‌شده از
چیدمان داخلی hash می‌آید، نه از `words`. اگر ترتیب مهم است، از comprehension
لیستی (به‌همراه حذف صریح تکراری‌ها) یا از `dict.fromkeys(...)` استفاده کنید.

</div>

## 6: Dictionary comprehension

The result is `{"Foad": 4, "Rezvan": 6, "Alice": 5}`. The keys are the names
themselves and the values are their lengths. The part **before** the colon
(`name`) is the key expression, and the part after it (`len(name)`) is the
value expression — `{key: value for item in iterable}`. Because the keys come
from an expression, duplicate keys would silently overwrite each other, just
as with ordinary dictionary assignment.

<div dir="rtl" align="right">

### ۶: Comprehension دیکشنری

نتیجه `{"Foad": 4, "Rezvan": 6, "Alice": 5}` است. کلیدها خودِ نام‌ها هستند و
مقدارها طول آن‌ها. بخشی که **پیش از** دونقطه می‌آید (`name`) عبارت کلید است و
بخش پس از آن (`len(name)`) عبارت مقدار — یعنی
`{key: value for item in iterable}`. چون کلیدها از یک عبارت به‌دست می‌آیند،
کلیدهای تکراری بی‌سروصدا روی هم بازنویسی می‌شوند، دقیقاً مانند انتساب معمولی در
دیکشنری.

</div>

## 7: The truthiness trap

The result is `{"charlie": 0.7}`. `"alice"` is **not** present even though her
score `0.0` is a real, valid score — `0.0` is falsy, so `if score` rejects it.
`"bob"` is **not** present either, but for a different reason: his score is
genuinely missing (`None`, which is also falsy). So `if score` does **not**
mean the same thing as `if score is not None`: the first filters out every
falsy value (`None`, `0`, `0.0`, `""`, `[]`, `{}`), while the second filters
out only `None` and would have kept `"alice"` with her zero score. When the
valid range of a value includes something falsy, always test for `None`
explicitly.

<div dir="rtl" align="right">

### ۷: تله‌ی truthiness

نتیجه `{"charlie": 0.7}` است. `"alice"` **حاضر نیست**، هرچند امتیاز `0.0` او یک
امتیاز واقعی و معتبر است — `0.0` مقدار falsy دارد، پس `if score` آن را رد
می‌کند. `"bob"` هم **حاضر نیست**، اما به دلیلی متفاوت: امتیاز او واقعاً وجود
ندارد (`None` که آن هم falsy است). پس `if score` با `if score is not None`
یکی **نیست**: اولی هر مقدار falsy را حذف می‌کند (`None`، `0`، `0.0`، `""`،
`[]`، `{}`)، در حالی که دومی فقط `None` را حذف می‌کرد و `"alice"` را با امتیاز
صفرش نگه می‌داشت. هرگاه بازه‌ی معتبر یک مقدار شامل چیزی falsy باشد، همیشه
به‌صراحت `None` را بررسی کنید.

</div>
