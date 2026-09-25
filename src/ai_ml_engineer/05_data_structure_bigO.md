# 05: Big O Notation

This document is the written explanation for the code examples in
[`05_data_structure_bigO.py`](05_data_structure_bigO.py). The section numbers
and the letters inside each section match that file, so the two can be read
side by side.

<div dir="rtl" align="right">

# ۰۵: نماد Big O

این سند توضیح نوشتاریِ نمونه‌کدهای فایل
[`05_data_structure_bigO.py`](05_data_structure_bigO.py) است. شماره‌ی بخش‌ها و
حروف داخل هر بخش با آن فایل یکی است، پس می‌توان این دو را کنار هم خواند.

</div>

---

## 1: Big O fundamentals

<div dir="rtl" align="right">

## ۱: مبانی Big O

</div>

### A: What is Big O?

Big O notation describes how the resource requirements of an algorithm grow
as its input grows. Usually we analyze **time** or **memory**.

Suppose an algorithm performs approximately `3n + 10` operations:

- `n = 10` → `3(10) + 10` = `40`
- `n = 1,000,000` → `3,000,010`

As `n` becomes very large, the `+10` matters very little. The dominant
behavior is proportional to `n`, so we describe the algorithm as **O(n)**.

<div dir="rtl" align="right">

### الف: Big O چیست؟

نماد Big O توصیف می‌کند که نیازهای منابع یک الگوریتم با بزرگ‌شدن ورودی چگونه
رشد می‌کنند. معمولاً **زمان** یا **حافظه** را تحلیل می‌کنیم.

فرض کنید الگوریتمی تقریباً `3n + 10` عملیات انجام می‌دهد:

- `n = 10` ← `3(10) + 10` برابر `40`
- `n = 1,000,000` ← `3,000,010`

هرچه `n` بسیار بزرگ‌تر شود، مقدار `10+` اهمیت بسیار کمی پیدا می‌کند. رفتار
غالب متناسب با `n` است، پس الگوریتم را **O(n)** می‌نامیم.

</div>

### B: Big O is about growth, not seconds

This distinction is extremely important. Big O does **not** mean "this
function takes 2 seconds." It describes **how runtime grows as input size
grows**.

- **O(n)** means doubling the input may roughly double the amount of work.
- **O(n²)** means doubling the input may roughly quadruple the amount of work.

At `n = 1,000`, O(n) is about 1,000 operations while O(n²) is about 1,000,000.
At `n = 1,000,000` the difference becomes enormous.

<div dir="rtl" align="right">

### ب: Big O درباره‌ی رشد است، نه ثانیه

این تمایز بسیار مهم است. Big O به این معنا **نیست** که «این تابع ۲ ثانیه طول
می‌کشد». Big O توصیف می‌کند که **زمان اجرا با بزرگ‌شدن ورودی چگونه رشد
می‌کند**.

- **O(n)** یعنی دو برابر شدن ورودی تقریباً کار را دو برابر می‌کند.
- **O(n²)** یعنی دو برابر شدن ورودی تقریباً کار را چهار برابر می‌کند.

در `n = 1000`، مقدار O(n) حدود ۱۰۰۰ عملیات است در حالی که O(n²) حدود
۱٬۰۰۰٬۰۰۰ عملیات. در `n = 1,000,000` این تفاوت عظیم می‌شود.

</div>

### C: What does n mean?

Usually `n` is the **input size**. In `print_names(names)`, `n` is the number
of names: for `["Ali", "Sara"]` it is `2`, and for a list of one million names
it is `1,000,000`.

<div dir="rtl" align="right">

### پ: `n` یعنی چه؟

معمولاً `n` همان **اندازه‌ی ورودی** است. در `print_names(names)`، مقدار `n`
تعداد نام‌هاست: برای `["Ali", "Sara"]` برابر `2` است و برای فهرستی با یک
میلیون نام برابر `1,000,000`.

</div>

---

## 2: Reading complexity from loops

<div dir="rtl" align="right">

## ۲: خواندن پیچیدگی از روی حلقه‌ها

</div>

### A: O(1) — constant time

Whether `get_first(items)` receives a list of 10 elements or 10,000,000
elements, we still perform approximately one lookup. That is **O(1)**, called
constant time. Typical list indexing, dictionary lookup, and set membership
are all O(1) (the last two on average).

<div dir="rtl" align="right">

### الف: O(1) — زمان ثابت

چه `get_first(items)` فهرستی با ۱۰ عنصر بگیرد و چه با ۱۰٬۰۰۰٬۰۰۰ عنصر، باز هم
تقریباً یک دسترسی انجام می‌دهیم. این یعنی **O(1)** که به آن زمان ثابت می‌گویند.
ایندکس‌گذاری معمول لیست، جست‌وجوی کلید در دیکشنری و عضویت در مجموعه همگی O(1)
هستند (دو مورد آخر در حالت میانگین).

</div>

### B: O(n) — linear time

In `print_all(items)`, 10 items means the loop executes 10 times and 1,000
items means 1,000 times. So `T(n) ≈ n`, which is **O(n)**.

<div dir="rtl" align="right">

### ب: O(n) — زمان خطی

در `print_all(items)`، با ۱۰ عنصر حلقه ۱۰ بار اجرا می‌شود و با ۱۰۰۰ عنصر،
۱۰۰۰ بار. پس `T(n) ≈ n` است، یعنی **O(n)**.

</div>

### C: Multiple sequential operations

The first loop costs `n` and the second costs `n`, so the total is `n + n`, or
`2n`. Big O ignores constant multipliers, so O(2n) becomes **O(n)**. This is
**not** O(n²) — two sequential loops do not multiply, they add.

<div dir="rtl" align="right">

### پ: چند عملیات پشت‌سرهم

حلقه‌ی اول `n` هزینه دارد و حلقه‌ی دوم هم `n`، پس مجموع برابر `n + n` یا `2n`
است. Big O ضرایب ثابت را نادیده می‌گیرد، پس O(2n) تبدیل به **O(n)** می‌شود.
این **O(n²) نیست** — دو حلقه‌ی پشت‌سرهم در هم ضرب نمی‌شوند، بلکه جمع می‌شوند.

</div>

### D: Nested loops

The outer loop runs `n` times and the inner loop runs `n` times **for every**
outer iteration, so the total is `n × n = n²` → **O(n²)**.

<div dir="rtl" align="right">

### ت: حلقه‌های تودرتو

حلقه‌ی بیرونی `n` بار اجرا می‌شود و حلقه‌ی درونی **به‌ازای هر** تکرار بیرونی
`n` بار، پس مجموع برابر `n × n = n²` است ← **O(n²)**.

</div>

### E: Sequential loops add; nested loops multiply

Memorize this principle carefully:

- Sequential ≈ `n + n` → **O(n)**
- Nested ≈ `n × n` → **O(n²)**

This is one of the most important distinctions in complexity analysis.

<div dir="rtl" align="right">

### ث: حلقه‌های پشت‌سرهم جمع می‌شوند؛ حلقه‌های تودرتو ضرب

این اصل را به‌دقت به خاطر بسپارید:

- پشت‌سرهم ≈ `n + n` ← **O(n)**
- تودرتو ≈ `n × n` ← **O(n²)**

این یکی از مهم‌ترین تمایزها در تحلیل پیچیدگی است.

</div>

### F: Independent input sizes

In `process(users, products)`, let `n` be the number of users and `m` the
number of products. The complexity is **O(n + m)**. Do not automatically turn
everything into O(n) — the inputs may have different sizes. If the same two
inputs are nested instead, the complexity is **O(n × m)**, written **O(nm)**.

<div dir="rtl" align="right">

### ج: اندازه‌های ورودی مستقل

در `process(users, products)`، فرض کنید `n` تعداد کاربران و `m` تعداد
محصولات باشد. پیچیدگی برابر **O(n + m)** است. همه‌چیز را به‌طور خودکار به O(n)
تبدیل نکنید — ورودی‌ها ممکن است اندازه‌های متفاوتی داشته باشند. اگر همین دو
ورودی به‌صورت تودرتو پیمایش شوند، پیچیدگی برابر **O(n × m)** است که آن را
**O(nm)** می‌نویسند.

</div>

---

## 3: Simplification rules

<div dir="rtl" align="right">

## ۳: قواعد ساده‌سازی

</div>

### A: Drop constants

`T(n) = 5n` is **O(n)**, and `T(n) = 1000n` is still **O(n)**. Why? Because
Big O analyzes growth, and both functions grow linearly.

<div dir="rtl" align="right">

### الف: حذف ضرایب ثابت

`T(n) = 5n` برابر **O(n)** است، و `T(n) = 1000n` هم باز **O(n)** است. چرا؟
چون Big O رشد را تحلیل می‌کند و هر دو تابع به‌صورت خطی رشد می‌کنند.

</div>

### B: Drop lower-order terms

For `T(n) = n² + n + 100`, the `n²` term dominates as `n` gets large, so the
complexity is **O(n²)**. Similarly `n³ + n² + 500n + 100000` becomes
**O(n³)**.

<div dir="rtl" align="right">

### ب: حذف جمله‌های مرتبه‌پایین

در `T(n) = n² + n + 100`، با بزرگ‌شدن `n` جمله‌ی `n²` غالب می‌شود، پس پیچیدگی
برابر **O(n²)** است. به همین ترتیب `n³ + n² + 500n + 100000` تبدیل به
**O(n³)** می‌شود.

</div>

### C: Complexity is not determined by the number of code lines

Three separate index assignments are three operations and still **O(1)**. A
two-line `for` loop over `data` is **O(n)**. Code length does not determine
complexity — growth determines complexity.

<div dir="rtl" align="right">

### پ: پیچیدگی با تعداد خطوط کد تعیین نمی‌شود

سه انتساب جداگانه با ایندکس، سه عملیات است و همچنان **O(1)** باقی می‌ماند. یک
حلقه‌ی `for` دوخطی روی `data` برابر **O(n)** است. طول کد پیچیدگی را تعیین
نمی‌کند — رشد است که پیچیدگی را تعیین می‌کند.

</div>

---

## 4: Common complexity classes

<div dir="rtl" align="right">

## ۴: رده‌های رایج پیچیدگی

</div>

### A: The ladder

From generally most scalable to least scalable:

`O(1)` → `O(log n)` → `O(n)` → `O(n log n)` → `O(n²)` → `O(n³)` → `O(2ⁿ)` →
`O(n!)`

<div dir="rtl" align="right">

### الف: نردبان پیچیدگی

از مقیاس‌پذیرترین به کم‌مقیاس‌پذیرترین:

`O(1)` ← `O(log n)` ← `O(n)` ← `O(n log n)` ← `O(n²)` ← `O(n³)` ← `O(2ⁿ)` ←
`O(n!)`

</div>

### B: O(log n) — logarithmic time

Imagine searching a sorted phone book. Instead of starting from page one, you
open the middle: if the target comes earlier you discard the second half,
otherwise you discard the first half. Every operation cuts the problem
approximately in half:

`1,024 → 512 → 256 → 128 → 64 → 32 → 16 → 8 → 4 → 2 → 1`

Only about **10 steps** were needed to reduce 1,024 possibilities to 1,
because `2¹⁰ = 1024`, so `log₂(1024) = 10`. Binary search therefore has
**O(log n)** search time.

<div dir="rtl" align="right">

### ب: O(log n) — زمان لگاریتمی

جست‌وجو در یک دفترچه‌ی تلفنِ مرتب را تصور کنید. به‌جای شروع از صفحه‌ی یک، از
وسط باز می‌کنید: اگر مقدار موردنظر جلوتر باشد نیمه‌ی دوم را کنار می‌گذارید،
وگرنه نیمه‌ی اول را. هر عملیات مسئله را تقریباً نصف می‌کند:

`۱۰۲۴ ← ۵۱۲ ← ۲۵۶ ← ۱۲۸ ← ۶۴ ← ۳۲ ← ۱۶ ← ۸ ← ۴ ← ۲ ← ۱`

تنها حدود **۱۰ گام** لازم بود تا ۱۰۲۴ حالت به ۱ برسد، چون `2¹⁰ = 1024` و پس
`log₂(1024) = 10`. بنابراین جست‌وجوی دودویی زمان جست‌وجوی **O(log n)** دارد.

</div>

### C: Why logarithms are so powerful

Consider one billion items, `n = 1,000,000,000`. A linear search could require
nearly 1,000,000,000 checks, while binary search requires roughly **30**
checks, because `2³⁰ ≈ 1 billion`. That difference is enormous.

<div dir="rtl" align="right">

### پ: چرا لگاریتم‌ها این‌قدر قدرتمندند

یک میلیارد عنصر را در نظر بگیرید، `n = 1,000,000,000`. جست‌وجوی خطی ممکن است
نزدیک به ۱٬۰۰۰٬۰۰۰٬۰۰۰ بررسی لازم داشته باشد، در حالی که جست‌وجوی دودویی
تقریباً **۳۰** بررسی می‌خواهد، چون `2³⁰ ≈ 1 billion`. این تفاوت عظیم است.

</div>

### D: O(n log n)

This appears frequently in efficient sorting algorithms — merge sort, heap
sort, and well-behaved divide-and-conquer sorting. Python's built-in sorting
implementation (`numbers.sort()` and `sorted(numbers)`) has worst-case
**O(n log n)** time complexity, and that is what you should generally assume
in complexity analysis.

<div dir="rtl" align="right">

### ت: O(n log n)

این رده در الگوریتم‌های مرتب‌سازی کارآمد زیاد دیده می‌شود — merge sort،
heap sort و مرتب‌سازی‌های خوش‌رفتارِ تقسیم‌وحل. پیاده‌سازی مرتب‌سازی درونیِ
پایتون (`numbers.sort()` و `sorted(numbers)`) در بدترین حالت پیچیدگی زمانی
**O(n log n)** دارد، و در تحلیل پیچیدگی معمولاً باید همین را در نظر بگیرید.

</div>

### E: O(n²) — quadratic time

The typical source is nested loops over the same input, like `all_pairs`. For
`n = 10` that is about 100 combinations; for `n = 1,000` it is about
1,000,000. This growth becomes expensive quickly.

<div dir="rtl" align="right">

### ث: O(n²) — زمان درجه‌دو

منشأ معمول آن حلقه‌های تودرتو روی یک ورودی است، مانند `all_pairs`. برای
`n = 10` حدود ۱۰۰ ترکیب و برای `n = 1000` حدود ۱٬۰۰۰٬۰۰۰ ترکیب به‌دست می‌آید.
این رشد خیلی زود پرهزینه می‌شود.

</div>

### F: Triangular loops are still O(n²)

When the inner loop starts at `i` instead of `0`, the number of executions is
`n + (n - 1) + (n - 2) + ... + 1`, which equals `n(n + 1) / 2`, approximately
`1/2 n² + 1/2 n`. Drop constants and lower-order terms and you get **O(n²)**.
A nested loop does not necessarily execute exactly `n²` times to have
quadratic growth.

<div dir="rtl" align="right">

### ج: حلقه‌های مثلثی هم O(n²) هستند

وقتی حلقه‌ی درونی به‌جای `0` از `i` شروع شود، تعداد اجراها برابر است با
`n + (n - 1) + (n - 2) + ... + 1` که مقدار آن `n(n + 1) / 2` و تقریباً
`1/2 n² + 1/2 n` است. با حذف ضرایب ثابت و جمله‌های مرتبه‌پایین به **O(n²)**
می‌رسیم. یک حلقه‌ی تودرتو لازم نیست دقیقاً `n²` بار اجرا شود تا رشد درجه‌دو
داشته باشد.

</div>

### G: O(2ⁿ) — exponential time

The naive recursive `fibonacci` repeats enormous amounts of work, and the
number of function calls grows exponentially. We often describe it
approximately as **O(2ⁿ)**. Exponential algorithms become impractical very
quickly.

<div dir="rtl" align="right">

### چ: O(2ⁿ) — زمان نمایی

پیاده‌سازی بازگشتیِ ساده‌ی `fibonacci` حجم عظیمی از کار را تکرار می‌کند و تعداد
فراخوانی‌های تابع به‌صورت نمایی رشد می‌کند. معمولاً آن را تقریباً **O(2ⁿ)**
توصیف می‌کنیم. الگوریتم‌های نمایی خیلی زود غیرعملی می‌شوند.

</div>

### H: O(n!) — factorial time

This can occur when considering every possible ordering:

- 3 elements → `3! = 6` permutations
- 10 elements → `10! = 3,628,800`
- 20 elements → approximately `2.43 × 10¹⁸`

Factorial growth is extraordinarily expensive.

<div dir="rtl" align="right">

### ح: O(n!) — زمان فاکتوریل

این حالت وقتی پیش می‌آید که همه‌ی ترتیب‌های ممکن را بررسی کنیم:

- ۳ عنصر ← `3! = 6` جایگشت
- ۱۰ عنصر ← `10! = 3,628,800`
- ۲۰ عنصر ← تقریباً `2.43 × 10¹⁸`

رشد فاکتوریل به‌طور فوق‌العاده‌ای پرهزینه است.

</div>

---

## 5: Best case, average case, worst case

Take `find(numbers, target)` with `numbers = [7, 4, 20, 99, 42]`. Searching
for `7` finds it immediately — **best case: O(1)**. Searching for `42` may
inspect all elements — **worst case: O(n)**. Searching for a value that does
not exist also requires scanning the entire list — again **O(n)**. When
engineers simply say "linear search is O(n)", they are normally describing its
asymptotic worst-case behavior.

<div dir="rtl" align="right">

## ۵: بهترین حالت، حالت میانگین، بدترین حالت

تابع `find(numbers, target)` را با `numbers = [7, 4, 20, 99, 42]` در نظر
بگیرید. جست‌وجوی `7` بی‌درنگ آن را پیدا می‌کند — **بهترین حالت: O(1)**.
جست‌وجوی `42` ممکن است همه‌ی عناصر را بررسی کند — **بدترین حالت: O(n)**.
جست‌وجوی مقداری که وجود ندارد هم نیازمند پیمایش کل لیست است — باز هم **O(n)**.
وقتی مهندسان به‌سادگی می‌گویند «جست‌وجوی خطی O(n) است»، معمولاً رفتار مجانبیِ
بدترین حالت آن را توصیف می‌کنند.

</div>

---

## 6: Time complexity vs space complexity

Big O can analyze more than time — it can also describe memory.

`duplicate(numbers)` has **time O(n)**, because we iterate through `n`
elements, and **additional memory O(n)**, because `result` stores `n`
elements.

`print_numbers(numbers)` has **time O(n)** but **extra space O(1)**, because
the function does not create storage proportional to the input size.

<div dir="rtl" align="right">

## ۶: پیچیدگی زمانی در برابر پیچیدگی فضایی

Big O فقط زمان را تحلیل نمی‌کند — می‌تواند حافظه را هم توصیف کند.

تابع `duplicate(numbers)` **زمان O(n)** دارد، چون روی `n` عنصر پیمایش
می‌کنیم، و **حافظه‌ی اضافیِ O(n)**، چون `result` تعداد `n` عنصر را نگه
می‌دارد.

تابع `print_numbers(numbers)` **زمان O(n)** دارد اما **فضای اضافیِ O(1)**، چون
تابع هیچ حافظه‌ای متناسب با اندازه‌ی ورودی نمی‌سازد.

</div>

---

## 7: Python list complexity

This is extremely important. Given `numbers = [10, 20, 30, 40]`:

| Operation | Example | Complexity |
| --- | --- | --- |
| Index access | `numbers[2]` | O(1) |
| Assignment by index | `numbers[2] = 100` | O(1) |
| Search | `30 in numbers` | O(n) — Python may need to scan the list |
| `index()` | `numbers.index(30)` | O(n) |
| Append | `numbers.append(50)` | amortized O(1) |
| Pop from end | `numbers.pop()` | usually O(1) |
| Insert at beginning | `numbers.insert(0, 5)` | O(n) |
| Remove from beginning | `numbers.pop(0)` | O(n) |

Why is inserting at the beginning O(n)? Existing elements need to move. Before
the insert the list is `[10, 20, 30, 40]`; after inserting `5` it is
`[5, 10, 20, 30, 40]` — every existing element shifted right. Removing from
the beginning is the mirror image: the remaining elements shift left.

<div dir="rtl" align="right">

## ۷: پیچیدگی لیست در پایتون

این بخش بسیار مهم است. فرض کنید `numbers = [10, 20, 30, 40]`:

| عملیات | نمونه | پیچیدگی |
| --- | --- | --- |
| دسترسی با ایندکس | `numbers[2]` | O(1) |
| انتساب با ایندکس | `numbers[2] = 100` | O(1) |
| جست‌وجو | `30 in numbers` | O(n) — پایتون ممکن است کل لیست را پیمایش کند |
| `index()` | `numbers.index(30)` | O(n) |
| افزودن به انتها | `numbers.append(50)` | O(1) سرشکن‌شده |
| برداشتن از انتها | `numbers.pop()` | معمولاً O(1) |
| درج در ابتدا | `numbers.insert(0, 5)` | O(n) |
| حذف از ابتدا | `numbers.pop(0)` | O(n) |

چرا درج در ابتدا O(n) است؟ چون عناصر موجود باید جابه‌جا شوند. پیش از درج، لیست
`[10, 20, 30, 40]` است؛ پس از درج `5` می‌شود `[5, 10, 20, 30, 40]` — یعنی همه‌ی
عناصر قبلی یک واحد به راست منتقل شدند. حذف از ابتدا هم قرینه‌ی همین است:
عناصر باقی‌مانده به چپ منتقل می‌شوند.

</div>

---

## 8: Dictionary complexity

Python dictionaries are implemented using hash tables. Lookup, insertion,
deletion, and membership are all **O(1) on average**.

**Important technical detail:** O(1) here is an average-case expectation.
Pathological collision behavior can produce worse performance, and the
theoretical worst case can be **O(n)**. But for normal Python programming,
dictionary lookup is normally discussed as average O(1).

<div dir="rtl" align="right">

## ۸: پیچیدگی دیکشنری

دیکشنری‌های پایتون با جدول هش (hash table) پیاده‌سازی شده‌اند. جست‌وجو، درج،
حذف و بررسی عضویت همگی **به‌طور میانگین O(1)** هستند.

**نکته‌ی فنی مهم:** این O(1) یک انتظار در حالت میانگین است. رفتار برخوردِ
(collision) نامتعارف می‌تواند کارایی بدتری ایجاد کند و بدترین حالت نظری
می‌تواند **O(n)** باشد. اما در برنامه‌نویسی معمول پایتون، جست‌وجوی دیکشنری
معمولاً به‌عنوان میانگین O(1) مطرح می‌شود.

</div>

---

## 9: Set complexity

Sets are also hash-table-based. With `ids = {10, 20, 30, 40}`, the membership
test `30 in ids` is **O(1) on average**. With the same values in a list,
`ids = [10, 20, 30, 40]`, the identical-looking `30 in ids` is **O(n)**. This
difference can completely change an algorithm.

<div dir="rtl" align="right">

## ۹: پیچیدگی مجموعه (set)

مجموعه‌ها هم مبتنی بر جدول هش هستند. با `ids = {10, 20, 30, 40}`، بررسی عضویت
`30 in ids` به‌طور میانگین **O(1)** است. با همان مقادیر در قالب یک لیست،
`ids = [10, 20, 30, 40]`، همان عبارتِ ظاهراً یکسانِ `30 in ids` برابر **O(n)**
است. این تفاوت می‌تواند یک الگوریتم را به‌کلی دگرگون کند.

</div>

---

## 10: A very important optimization example

Suppose `users` and `blocked_users` are both lists containing roughly `n`
elements, and we check each user against the blocked list. The outer loop is
O(n) and list membership is O(n), so combined they are **O(n²)**.

Now convert the blocked users to a set first. Creating the set is O(n), the
outer loop is O(n), and set lookup is O(1) on average, so the total is
`O(n + n)` which simplifies to **O(n)**.

You just changed O(n²) into O(n) by selecting a more appropriate data
structure. That is exactly why Big O matters.

<div dir="rtl" align="right">

## ۱۰: یک مثال بسیار مهم از بهینه‌سازی

فرض کنید `users` و `blocked_users` هر دو لیست‌هایی با حدود `n` عنصر باشند و هر
کاربر را در برابر فهرست مسدودشده‌ها بررسی کنیم. حلقه‌ی بیرونی O(n) است و بررسی
عضویت در لیست هم O(n)، پس در مجموع **O(n²)** می‌شود.

حالا ابتدا کاربران مسدودشده را به یک مجموعه تبدیل کنید. ساخت مجموعه O(n) است،
حلقه‌ی بیرونی O(n) است و جست‌وجو در مجموعه به‌طور میانگین O(1)، پس مجموع برابر
`O(n + n)` است که به **O(n)** ساده می‌شود.

شما فقط با انتخاب ساختار داده‌ی مناسب‌تر، O(n²) را به O(n) تبدیل کردید. دقیقاً
به همین دلیل است که Big O اهمیت دارد.

</div>

---

## 11: Better grouping algorithm

### A: Grouping into lists

Instead of rescanning the whole collection, group words by length into a
dictionary of lists. But notice that `word not in result[length]` is **list
membership**, so it may itself be **O(m)** for the bucket size.

<div dir="rtl" align="right">

## ۱۱: الگوریتم بهتر برای گروه‌بندی

### الف: گروه‌بندی در قالب لیست

به‌جای پیمایش دوباره‌ی کل مجموعه، واژه‌ها را بر اساس طول در یک دیکشنری از
لیست‌ها گروه‌بندی می‌کنیم. اما توجه کنید که `word not in result[length]` یک
**بررسی عضویت در لیست** است، پس خودش می‌تواند به اندازه‌ی سطل (bucket) برابر
**O(m)** باشد.

</div>

### B: Grouping into sets

If we store each bucket as a set instead, adding a word is an average O(1)
operation, so the whole grouping pass becomes **O(n)** on average.

<div dir="rtl" align="right">

### ب: گروه‌بندی در قالب مجموعه

اگر هر سطل را به‌جای لیست، یک مجموعه (set) در نظر بگیریم، افزودن هر واژه
به‌طور میانگین O(1) است، پس کل مرحله‌ی گروه‌بندی به‌طور میانگین **O(n)**
می‌شود.

</div>

### C: Convert back to lists

If lists are required by the caller, convert the buckets at the end with a
dictionary comprehension. This is an excellent example of using data
structures to improve complexity.

<div dir="rtl" align="right">

### پ: تبدیل دوباره به لیست

اگر مصرف‌کننده‌ی کد به لیست نیاز دارد، در پایان سطل‌ها را با یک dictionary
comprehension تبدیل کنید. این نمونه‌ی بسیار خوبی است از استفاده از ساختار
داده برای بهبود پیچیدگی.

</div>

---

## 12: Hidden costs in everyday operations

<div dir="rtl" align="right">

## ۱۲: هزینه‌های پنهان در عملیات روزمره

</div>

### A: String complexity

Strings are immutable, so `text = text + "a"` must create a new string by
copying characters. If the string currently contains `n` characters, that is
**O(n)**. This becomes important in loops: `result += character` inside a loop
repeatedly copies increasingly large strings, and the total work can approach
**O(n²)**. A better pattern is often `"".join(characters)`, which operates
approximately linearly — **O(n)** with respect to the total number of
characters.

<div dir="rtl" align="right">

### الف: پیچیدگی رشته

رشته‌ها تغییرناپذیرند، پس `text = text + "a"` باید با کپی‌کردن کاراکترها یک
رشته‌ی جدید بسازد. اگر رشته در آن لحظه `n` کاراکتر داشته باشد، این کار
**O(n)** است. این موضوع در حلقه‌ها اهمیت پیدا می‌کند: عبارت
`result += character` داخل حلقه، رشته‌هایی با اندازه‌ی روبه‌رشد را پیاپی کپی
می‌کند و مجموع کار می‌تواند به **O(n²)** نزدیک شود. الگوی بهتر معمولاً
`"".join(characters)` است که تقریباً خطی عمل می‌کند — یعنی **O(n)** نسبت به
تعداد کل کاراکترها.

</div>

### B: Sorting complexity

Do not treat `numbers.sort()` or `sorted(numbers)` as **O(1)** just because
you wrote one line of code — sorting itself performs substantial work. For
general analysis, think **O(n log n)**. In `for number in sorted(numbers)`,
the sort is O(n log n) and the loop is O(n), giving `O(n log n + n)` whose
dominant term is **O(n log n)**.

<div dir="rtl" align="right">

### ب: پیچیدگی مرتب‌سازی

`numbers.sort()` یا `sorted(numbers)` را صرفاً به این دلیل که یک خط کد
نوشته‌اید **O(1)** فرض نکنید — خودِ مرتب‌سازی کار قابل‌توجهی انجام می‌دهد. برای
تحلیل کلی، **O(n log n)** را در نظر بگیرید. در
`for number in sorted(numbers)`، مرتب‌سازی O(n log n) و حلقه O(n) است که
مجموعاً `O(n log n + n)` می‌شود و جمله‌ی غالب آن **O(n log n)** است.

</div>

### C: Function calls can hide complexity

Someone may look at `process(numbers)` and say "there is only one loop, so
this is O(n)." Wrong: inside the loop, `number in numbers` is itself **O(n)**,
so the real cost is `n × n` — **O(n²)**. When analyzing complexity, inspect
what each operation actually does.

<div dir="rtl" align="right">

### پ: فراخوانی توابع می‌تواند پیچیدگی را پنهان کند

ممکن است کسی با دیدن `process(numbers)` بگوید «فقط یک حلقه هست، پس O(n)
است». اشتباه است: داخل حلقه، `number in numbers` خودش **O(n)** است، پس هزینه‌ی
واقعی `n × n` یعنی **O(n²)** است. هنگام تحلیل پیچیدگی، بررسی کنید که هر
عملیات واقعاً چه کاری انجام می‌دهد.

</div>

### D: len() in Python

For built-in Python lists, `len(numbers)` is **O(1)** — Python stores the
collection's length internally and does not count every element each time. So
`for _ in range(len(numbers))` does not make `len(numbers)` an O(n)
operation.

<div dir="rtl" align="right">

### ت: تابع len() در پایتون

برای لیست‌های درونیِ پایتون، `len(numbers)` برابر **O(1)** است — پایتون طول
مجموعه را به‌صورت داخلی نگه می‌دارد و هر بار همه‌ی عناصر را نمی‌شمارد. پس
`for _ in range(len(numbers))` باعث نمی‌شود `len(numbers)` یک عملیات O(n)
شود.

</div>

### E: Slicing

`subset = numbers[2:8]` creates a new list containing the selected references.
If the slice contains `k` elements, that is **time O(k)** and **space O(k)**.
This can hide significant costs: in `while numbers: numbers = numbers[1:]`
each iteration copies most of the list, leading to **O(n²)** overall
behavior.

<div dir="rtl" align="right">

### ث: برش (slicing)

`subset = numbers[2:8]` یک لیست جدید می‌سازد که ارجاع‌های انتخاب‌شده را در خود
دارد. اگر برش `k` عنصر داشته باشد، این کار **زمان O(k)** و **فضای O(k)** است.
این موضوع می‌تواند هزینه‌های مهمی را پنهان کند: در
`while numbers: numbers = numbers[1:]` هر تکرار بخش بزرگی از لیست را کپی
می‌کند و رفتار کلی به **O(n²)** می‌رسد.

</div>

---

## 13: Amortized complexity

Earlier we said `numbers.append(value)` is **O(1) amortized**. Why not simply
O(1)? Python lists are dynamic arrays. When the underlying array becomes full,
Python may need to allocate a larger block of memory, copy references from the
old array, and then insert the new item. That particular append can cost
**O(n)**. But resizing does not happen every time — most appends are cheap.
When averaged across many appends, the average cost per append is O(1), and
that is what **amortized O(1)** means.

<div dir="rtl" align="right">

## ۱۳: پیچیدگی سرشکن‌شده (Amortized)

پیش‌تر گفتیم `numbers.append(value)` برابر **O(1) سرشکن‌شده** است. چرا به‌سادگی
O(1) نیست؟ لیست‌های پایتون آرایه‌های پویا (dynamic array) هستند. وقتی آرایه‌ی
زیرین پر می‌شود، پایتون ممکن است ناچار شود بلوک بزرگ‌تری از حافظه بگیرد،
ارجاع‌ها را از آرایه‌ی قبلی کپی کند و سپس عنصر جدید را درج کند. آن append خاص
می‌تواند **O(n)** هزینه داشته باشد. اما تغییر اندازه هر بار رخ نمی‌دهد — بیشتر
appendها ارزان‌اند. وقتی روی تعداد زیادی append میانگین بگیریم، هزینه‌ی
میانگین هر append برابر O(1) است، و معنای **O(1) سرشکن‌شده** همین است.

</div>

---

## 14: Reading loops carefully

<div dir="rtl" align="right">

## ۱۴: خواندن دقیق حلقه‌ها

</div>

### A: Early exit does not automatically change Big O

Yes, the function might return immediately. But in the worst case the target
could be the last item, or not present at all, so the worst-case complexity
remains **O(n)**.

<div dir="rtl" align="right">

### الف: خروج زودهنگام به‌خودی‌خود Big O را تغییر نمی‌دهد

بله، ممکن است تابع بی‌درنگ بازگردد. اما در بدترین حالت، مقدار موردنظر می‌تواند
آخرین عنصر باشد یا اصلاً وجود نداشته باشد، پس پیچیدگی بدترین حالت همان
**O(n)** باقی می‌ماند.

</div>

### B: Conditions inside loops

The condition `number % 2 == 0` is constant-time work and the loop still runs
`n` times, so the complexity is **O(n)**. An `if` statement does not
automatically create another factor of `n`.

<div dir="rtl" align="right">

### ب: شرط‌ها داخل حلقه

شرط `number % 2 == 0` کاری با زمان ثابت است و حلقه همچنان `n` بار اجرا
می‌شود، پس پیچیدگی **O(n)** است. یک دستور `if` به‌طور خودکار ضریب `n` دیگری
اضافه نمی‌کند.

</div>

### C: Loop that runs half of n

`for i in range(n // 2)` performs roughly `n / 2` operations. Big O drops
constants, so it is **O(n)**.

<div dir="rtl" align="right">

### پ: حلقه‌ای که نصف n اجرا می‌شود

`for i in range(n // 2)` تقریباً `n / 2` عملیات انجام می‌دهد. Big O ضرایب ثابت
را حذف می‌کند، پس برابر **O(n)** است.

</div>

### D: Loop that jumps by 2

`for i in range(0, n, 2)` runs approximately `n / 2` iterations, so it is
**O(n)** — not `O(n / 2)`, which is not written in standard simplified Big O
notation.

<div dir="rtl" align="right">

### ت: حلقه‌ای که دوتا دوتا جلو می‌رود

`for i in range(0, n, 2)` تقریباً `n / 2` تکرار دارد، پس **O(n)** است — نه
`O(n / 2)` که در نماد ساده‌شده‌ی استاندارد Big O نوشته نمی‌شود.

</div>

### E: Loop that doubles each time

With `i = 1` and `i *= 2`, the values are 1, 2, 4, 8, 16, 32, 64 … How many
times can we double before reaching `n`? Approximately `log₂(n)`, so the
complexity is **O(log n)**.

<div dir="rtl" align="right">

### ث: حلقه‌ای که هر بار دو برابر می‌شود

با `i = 1` و `i *= 2`، مقادیر عبارت‌اند از ۱، ۲، ۴، ۸، ۱۶، ۳۲، ۶۴ … چند بار
می‌توان دو برابر کرد تا به `n` رسید؟ تقریباً `log₂(n)` بار، پس پیچیدگی
**O(log n)** است.

</div>

### F: Loop that halves each time

`while n > 1: n //= 2` follows the same principle — each step removes half the
remaining problem, so the complexity is **O(log n)**.

<div dir="rtl" align="right">

### ج: حلقه‌ای که هر بار نصف می‌شود

`while n > 1: n //= 2` از همان اصل پیروی می‌کند — هر گام نیمی از مسئله‌ی
باقی‌مانده را حذف می‌کند، پس پیچیدگی **O(log n)** است.

</div>

### G: Nested loop with logarithmic inner loop

The outer loop is O(n) and the inner doubling loop is O(log n). Nested work
multiplies, so the total is **O(n log n)**.

<div dir="rtl" align="right">

### چ: حلقه‌ی تودرتو با حلقه‌ی درونیِ لگاریتمی

حلقه‌ی بیرونی O(n) است و حلقه‌ی درونیِ دوبرابرشونده O(log n). کار تودرتو در هم
ضرب می‌شود، پس مجموع برابر **O(n log n)** است.

</div>

---

## 15: Recursive complexity

Recursion itself does not determine complexity. In `countdown(n)` there are
approximately `n` calls, so the time is **O(n)** and the call-stack space is
also **O(n)**, because each recursive call consumes stack-frame space until
the base case is reached.

<div dir="rtl" align="right">

## ۱۵: پیچیدگی بازگشتی (Recursive)

خودِ بازگشت (recursion) پیچیدگی را تعیین نمی‌کند. در `countdown(n)` تقریباً
`n` فراخوانی وجود دارد، پس زمان **O(n)** است و فضای پشته‌ی فراخوانی هم
**O(n)**، چون هر فراخوانی بازگشتی تا رسیدن به حالت پایه یک قاب پشته (stack
frame) اشغال می‌کند.

</div>

---

## 16: Big O and machine learning

You are studying Big O because it becomes extremely important later in your
AI/ML path. Suppose the sequence length is `n`. In standard self-attention,
every token interacts with every other token, so the attention matrix has
dimensions approximately `n × n`. A major part of standard attention therefore
has quadratic dependence on sequence length — **O(n²)**. This is one reason
long-context models can become computationally expensive.

Later, when we study transformers, attention, KV cache, FlashAttention,
grouped-query attention, batching, matrix multiplication, and inference
optimization, Big O reasoning will become extremely important.

<div dir="rtl" align="right">

## ۱۶: Big O و یادگیری ماشین

شما Big O را می‌آموزید چون در ادامه‌ی مسیر AI/ML بسیار مهم می‌شود. فرض کنید
طول دنباله برابر `n` باشد. در self-attention استاندارد، هر توکن با همه‌ی
توکن‌های دیگر تعامل دارد، پس ماتریس attention ابعادی تقریباً `n × n` دارد.
بنابراین بخش عمده‌ای از attention استاندارد وابستگی درجه‌دو به طول دنباله
دارد — **O(n²)**. این یکی از دلایلی است که مدل‌های با زمینه‌ی طولانی می‌توانند
از نظر محاسباتی پرهزینه شوند.

بعدها که transformerها، attention، KV cache، FlashAttention،
grouped-query attention، batching، ضرب ماتریسی و بهینه‌سازی استنتاج را
بخوانیم، استدلال بر پایه‌ی Big O بسیار مهم خواهد شد.

</div>

---

## 17: Complexity is not the same as performance

This distinction is critical. Suppose Algorithm A costs `1000n` and Algorithm
B costs `n²`. For very small `n`, Algorithm B might actually run faster. Big O
describes **asymptotic scaling**; it does not tell you every detail of
real-world performance.

Actual runtime also depends on CPU architecture, caching, memory access,
interpreter overhead, implementation language, vectorization, constants,
network latency, disk access, parallelism, and GPU hardware.

- Big O answers: *how does the resource requirement grow?*
- Benchmarking answers: *how fast is this particular implementation on this
  particular system?*

They are related but not identical questions.

<div dir="rtl" align="right">

## ۱۷: پیچیدگی با کارایی یکی نیست

این تمایز حیاتی است. فرض کنید الگوریتم A هزینه‌ی `1000n` و الگوریتم B هزینه‌ی
`n²` داشته باشد. برای `n` های بسیار کوچک، ممکن است الگوریتم B واقعاً سریع‌تر
اجرا شود. Big O **مقیاس‌پذیری مجانبی** را توصیف می‌کند؛ همه‌ی جزئیات کارایی در
دنیای واقعی را به شما نمی‌گوید.

زمان اجرای واقعی به معماری CPU، کش، دسترسی به حافظه، سربار مفسر، زبان
پیاده‌سازی، برداری‌سازی (vectorization)، ضرایب ثابت، تأخیر شبکه، دسترسی به
دیسک، موازی‌سازی و سخت‌افزار GPU هم بستگی دارد.

- Big O به این پرسش پاسخ می‌دهد: *نیاز به منابع چگونه رشد می‌کند؟*
- بنچمارک به این پرسش پاسخ می‌دهد: *این پیاده‌سازیِ خاص روی این سیستمِ خاص چقدر
  سریع است؟*

این دو به هم مرتبط‌اند اما یکسان نیستند.

</div>

---

## 18: Big O vs Big Ω vs Big Θ

You will most often use Big O, but there are related mathematical concepts:

- **Big O** — upper asymptotic bound: the algorithm grows no faster than this
  class asymptotically.
- **Big Omega (Ω)** — lower asymptotic bound.
- **Big Theta (Θ)** — tight asymptotic bound.

For example, a loop that always visits every element has tightly linear
growth: **Θ(n)**. In normal programming discussion, engineers often casually
say O(n) even when Θ(n) would be mathematically more precise. You should
understand the distinction, but `O(...)` dominates everyday
software-engineering conversation.

<div dir="rtl" align="right">

## ۱۸: Big O در برابر Big Ω و Big Θ

بیشتر اوقات از Big O استفاده می‌کنید، اما مفاهیم ریاضیِ مرتبط دیگری هم وجود
دارد:

- **Big O** — کران بالای مجانبی: الگوریتم به‌صورت مجانبی سریع‌تر از این رده رشد
  نمی‌کند.
- **Big Omega (Ω)** — کران پایین مجانبی.
- **Big Theta (Θ)** — کران دقیق (tight) مجانبی.

برای نمونه، حلقه‌ای که همیشه همه‌ی عناصر را می‌پیماید رشد دقیقاً خطی دارد:
**Θ(n)**. در گفت‌وگوی معمول برنامه‌نویسی، مهندسان اغلب به‌سادگی O(n) می‌گویند،
حتی جایی که Θ(n) از نظر ریاضی دقیق‌تر است. باید این تمایز را بدانید، اما در
گفت‌وگوی روزمره‌ی مهندسی نرم‌افزار `O(...)` غالب است.

</div>

---

## 19: Practical Big O analysis method

When you encounter unfamiliar code, use this process:

1. **Identify the inputs.** Ask what grows — maybe `n` = number of users and
   `m` = number of products.
2. **Find loops.** A single loop is possibly O(n); nested loops are possibly
   multiplied. But analyze carefully.
3. **Inspect operations inside loops.** Ask: is this operation really O(1)?
   `x in list` is O(n), while `x in set` is O(1) on average.
4. **Analyze function calls.** Do not assume `sorted(data)` is constant time
   because it appears on one line.
5. **Combine sequential sections by addition:** `O(n) + O(n²)` → `O(n²)`.
6. **Combine nested work by multiplication:** `O(n) × O(n)` → `O(n²)`.
7. **Drop constants:** `O(5n)` → `O(n)`.
8. **Drop dominated terms:** `O(n² + n + 1)` → `O(n²)`.

<div dir="rtl" align="right">

## ۱۹: روش عملی تحلیل Big O

وقتی به کدی ناآشنا برخوردید، این فرایند را به کار ببرید:

۱. **ورودی‌ها را مشخص کنید.** بپرسید چه چیزی رشد می‌کند — شاید `n` تعداد
   کاربران و `m` تعداد محصولات باشد.
۲. **حلقه‌ها را پیدا کنید.** یک حلقه‌ی ساده احتمالاً O(n) است؛ حلقه‌های تودرتو
   احتمالاً در هم ضرب می‌شوند. اما با دقت تحلیل کنید.
۳. **عملیات داخل حلقه‌ها را بررسی کنید.** بپرسید: آیا این عملیات واقعاً O(1)
   است؟ `x in list` برابر O(n) است، در حالی که `x in set` به‌طور میانگین O(1)
   است.
۴. **فراخوانی توابع را تحلیل کنید.** فرض نکنید `sorted(data)` چون در یک خط
   آمده، زمان ثابت دارد.
۵. **بخش‌های پشت‌سرهم را با جمع ترکیب کنید:** `O(n) + O(n²)` ← `O(n²)`.
۶. **کار تودرتو را با ضرب ترکیب کنید:** `O(n) × O(n)` ← `O(n²)`.
۷. **ضرایب ثابت را حذف کنید:** `O(5n)` ← `O(n)`.
۸. **جمله‌های مغلوب را حذف کنید:** `O(n² + n + 1)` ← `O(n²)`.

</div>

---

## 20: Worked examples

| Example | What it does | Complexity |
| --- | --- | --- |
| A | one indexed lookup | time O(1) |
| B | sums every element | time O(n), extra space O(1) |
| C | builds a doubled list | time O(n), space O(n) |
| D | nested loops over the same input | time O(n²) |
| E | two sequential loops | O(n + n) → O(n) |
| F | sort then loop | O(n log n + n) → O(n log n) |
| G | build a set, then loop with O(1) lookups | O(n + n) → O(n) |

<div dir="rtl" align="right">

## ۲۰: مثال‌های حل‌شده

| مثال | چه می‌کند | پیچیدگی |
| --- | --- | --- |
| A | یک دسترسی با ایندکس | زمان O(1) |
| B | جمع‌زدن همه‌ی عناصر | زمان O(n)، فضای اضافی O(1) |
| C | ساخت لیست دوبرابرشده | زمان O(n)، فضای O(n) |
| D | حلقه‌های تودرتو روی یک ورودی | زمان O(n²) |
| E | دو حلقه‌ی پشت‌سرهم | `O(n + n)` ← `O(n)` |
| F | مرتب‌سازی و سپس حلقه | `O(n log n + n)` ← `O(n log n)` |
| G | ساخت مجموعه و حلقه با جست‌وجوی O(1) | `O(n + n)` ← `O(n)` |

</div>

---

## 21: Review questions

**1. What does Big O measure?** How the resource requirements of an algorithm
— time or memory — grow as its input grows. It is a statement about the rate
of growth, not about an absolute cost.

**2. Does O(n) mean an algorithm takes n seconds?** No. Big O says nothing
about seconds. O(n) means that doubling the input roughly doubles the amount
of work, whatever that work costs on a given machine.

**3. What does n normally represent?** The input size — usually the number of
elements being processed. When there are two independent inputs, they get
separate names, such as `n` users and `m` products.

**4. Why is list indexing O(1)?** A Python list stores its element references
in one contiguous block, so `numbers[5]` computes an address arithmetically
and jumps straight there. The length of the list never enters into it.

**5. Why is searching a list O(n)?** A list is not organized by value, so
`30 in numbers` has to compare elements one at a time until it finds a match.
In the worst case — the last element, or no match at all — it compares every
element.

**6. Why is dictionary lookup usually O(1)?** A dictionary is a hash table:
hashing the key computes the bucket directly, with no scanning. This is an
average-case expectation; pathological collisions can degrade it to O(n).

**7. Why do nested loops often produce O(n²)?** The inner loop runs its full
`n` iterations for **every** one of the outer loop's `n` iterations, so the
counts multiply: `n × n = n²`.

**8. Why do two sequential loops usually remain O(n)?** They run one after the
other rather than inside each other, so their costs add: `n + n = 2n`. Big O
drops the constant multiplier, leaving O(n).

**9. What is the difference between O(n + m) and O(nm)?** O(n + m) comes from
traversing two independent inputs **separately** — the costs add. O(nm) comes
from **nesting** one inside the other — the costs multiply. With
`n = m = 1,000` that is the difference between about 2,000 operations and
1,000,000.

**10. Why do we drop constants?** Because Big O classifies growth, and `5n`
and `1000n` both grow linearly. The constant reflects machine and
implementation details, not the shape of the curve.

**11. Simplify O(5n + 200).** → **O(n)**. Drop the constant multiplier `5` and
the constant term `200`.

**12. Simplify O(n² + 50n + 1000).** → **O(n²)**. As `n` grows, `n²` dominates
the lower-order terms completely.

**13. What makes an algorithm O(log n)?** Every step discards a constant
fraction — usually half — of what remains. Binary search and a loop variable
that doubles or halves each iteration are the standard examples.

**14. What is a common example of O(n log n)?** Efficient sorting: merge sort,
heap sort, and Python's own `sorted()` / `list.sort()`, whose worst case is
O(n log n).

**15. What is amortized complexity?** The average cost per operation measured
across a long sequence of operations, where a rare expensive step is spread
over many cheap ones.

**16. Why is list append amortized O(1)?** A Python list is a dynamic array.
Most appends just write into spare capacity, which is O(1). When the array
fills up, Python allocates a bigger block and copies the references — that one
append costs O(n) — but because capacity grows geometrically, the cost
averages out to O(1) per append.

**17. What is the difference between time and space complexity?** Time
complexity describes how the number of operations grows; space complexity
describes how much **additional** memory the algorithm allocates, not counting
the input it was given.

**18. Why can `x in some_list` be expensive inside a loop?** Because that
membership test is itself O(n). Placed inside a loop that already runs `n`
times, the real cost is `n × n` — O(n²) — even though only one loop is
visible.

**19. How can converting a list to a set improve an algorithm?** Set
membership is O(1) on average instead of O(n). Building the set costs O(n)
once, and that one-time cost turns the O(n²) pattern above into O(n).

**20. Why can a one-line Python expression still have high complexity?** Line
count is not work. `sorted(data)` is O(n log n), `x in data` is O(n) for a
list, a slice copies O(k) elements, and `"".join(...)` walks every character.
You have to look at what the operation does, not at how much you typed.

<div dir="rtl" align="right">

## ۲۱: پرسش‌های مرور

**۱. Big O چه چیزی را اندازه می‌گیرد؟** اینکه نیازهای منابع یک الگوریتم —
زمان یا حافظه — با بزرگ‌شدن ورودی چگونه رشد می‌کنند. این گزاره‌ای درباره‌ی
نرخ رشد است، نه درباره‌ی هزینه‌ی مطلق.

**۲. آیا O(n) یعنی الگوریتم `n` ثانیه طول می‌کشد؟** خیر. Big O چیزی درباره‌ی
ثانیه نمی‌گوید. O(n) یعنی دو برابر شدن ورودی تقریباً کار را دو برابر می‌کند،
هر اندازه که آن کار روی یک ماشین مشخص هزینه داشته باشد.

**۳. `n` معمولاً به چه چیزی اشاره دارد؟** به اندازه‌ی ورودی — معمولاً تعداد
عناصری که پردازش می‌شوند. وقتی دو ورودی مستقل داریم، نام‌های جداگانه
می‌گیرند، مثلاً `n` کاربر و `m` محصول.

**۴. چرا ایندکس‌گذاری لیست O(1) است؟** لیست پایتون ارجاع‌های عناصرش را در یک
بلوک پیوسته نگه می‌دارد، پس `numbers[5]` آدرس را با یک محاسبه‌ی حسابی به‌دست
می‌آورد و مستقیماً به آنجا می‌رود. طول لیست اصلاً در این کار دخیل نیست.

**۵. چرا جست‌وجو در لیست O(n) است؟** لیست بر اساس مقدار سازمان‌دهی نشده است،
پس `30 in numbers` باید عناصر را یکی‌یکی مقایسه کند تا مورد مطابق را پیدا
کند. در بدترین حالت — آخرین عنصر یا نبودن مقدار — همه‌ی عناصر مقایسه
می‌شوند.

**۶. چرا جست‌وجوی دیکشنری معمولاً O(1) است؟** دیکشنری یک جدول هش است: هش‌کردن
کلید مستقیماً سطل (bucket) را مشخص می‌کند و پیمایشی در کار نیست. این انتظارِ
حالت میانگین است؛ برخوردهای نامتعارف می‌توانند آن را تا O(n) بدتر کنند.

**۷. چرا حلقه‌های تودرتو اغلب O(n²) می‌سازند؟** حلقه‌ی درونی **به‌ازای هر یک**
از `n` تکرار حلقه‌ی بیرونی، کل `n` تکرار خود را انجام می‌دهد، پس تعدادها در هم
ضرب می‌شوند: `n × n = n²`.

**۸. چرا دو حلقه‌ی پشت‌سرهم معمولاً O(n) می‌مانند؟** این دو پشت سر هم اجرا
می‌شوند نه داخل یکدیگر، پس هزینه‌هایشان جمع می‌شود: `n + n = 2n`. Big O ضریب
ثابت را حذف می‌کند و O(n) باقی می‌ماند.

**۹. تفاوت O(n + m) با O(nm) چیست؟** مقدار O(n + m) از پیمایش **جداگانه‌ی** دو
ورودی مستقل می‌آید — هزینه‌ها جمع می‌شوند. مقدار O(nm) از **تودرتو** کردن یکی
داخل دیگری می‌آید — هزینه‌ها ضرب می‌شوند. با `n = m = 1000` این یعنی تفاوت
میان حدود ۲۰۰۰ عملیات و ۱٬۰۰۰٬۰۰۰ عملیات.

**۱۰. چرا ضرایب ثابت را حذف می‌کنیم؟** چون Big O رشد را دسته‌بندی می‌کند و
`5n` و `1000n` هر دو خطی رشد می‌کنند. ضریب ثابت بازتاب جزئیات ماشین و
پیاده‌سازی است، نه شکل منحنی.

**۱۱. ساده‌سازی O(5n + 200).** ← **O(n)**. ضریب ثابت `5` و جمله‌ی ثابت `200`
حذف می‌شوند.

**۱۲. ساده‌سازی O(n² + 50n + 1000).** ← **O(n²)**. با بزرگ‌شدن `n`، جمله‌ی `n²`
کاملاً بر جمله‌های مرتبه‌پایین غالب می‌شود.

**۱۳. چه چیزی یک الگوریتم را O(log n) می‌کند؟** اینکه هر گام کسری ثابت —
معمولاً نصف — از باقی‌مانده را کنار بگذارد. جست‌وجوی دودویی و حلقه‌ای که متغیرش
در هر تکرار دو برابر یا نصف می‌شود نمونه‌های استاندارد آن هستند.

**۱۴. یک نمونه‌ی رایج از O(n log n) چیست؟** مرتب‌سازی کارآمد: merge sort،
heap sort و خودِ `sorted()` / `list.sort()` در پایتون که بدترین حالتشان
O(n log n) است.

**۱۵. پیچیدگی سرشکن‌شده (amortized) چیست؟** هزینه‌ی میانگین هر عملیات در طول
یک دنباله‌ی طولانی از عملیات، جایی که یک گام گران‌قیمتِ نادر روی تعداد زیادی
گام ارزان پخش می‌شود.

**۱۶. چرا append روی لیست سرشکن‌شده O(1) است؟** لیست پایتون یک آرایه‌ی پویا
است. بیشتر appendها فقط در ظرفیت خالی می‌نویسند که O(1) است. وقتی آرایه پر
می‌شود، پایتون بلوک بزرگ‌تری می‌گیرد و ارجاع‌ها را کپی می‌کند — آن یک append
هزینه‌ی O(n) دارد — اما چون ظرفیت به‌صورت هندسی رشد می‌کند، میانگین هزینه به
O(1) به‌ازای هر append می‌رسد.

**۱۷. تفاوت پیچیدگی زمانی و فضایی چیست؟** پیچیدگی زمانی توصیف می‌کند که تعداد
عملیات چگونه رشد می‌کند؛ پیچیدگی فضایی توصیف می‌کند که الگوریتم چقدر حافظه‌ی
**اضافی** تخصیص می‌دهد، بدون حساب‌کردن ورودی‌ای که به آن داده شده است.

**۱۸. چرا `x in some_list` داخل یک حلقه می‌تواند گران باشد؟** چون خودِ این
بررسی عضویت O(n) است. وقتی داخل حلقه‌ای قرار بگیرد که پیشاپیش `n` بار اجرا
می‌شود، هزینه‌ی واقعی `n × n` یعنی O(n²) است، هرچند تنها یک حلقه دیده
می‌شود.

**۱۹. تبدیل لیست به مجموعه چگونه الگوریتم را بهتر می‌کند؟** عضویت در مجموعه
به‌طور میانگین O(1) است به‌جای O(n). ساخت مجموعه یک‌بار O(n) هزینه دارد و همان
هزینه‌ی یک‌باره، الگوی O(n²) بالا را به O(n) تبدیل می‌کند.

**۲۰. چرا یک عبارت یک‌خطی در پایتون می‌تواند پیچیدگی بالایی داشته باشد؟**
تعداد خط‌ها معیار کار نیست. `sorted(data)` برابر O(n log n) است، `x in data`
برای لیست O(n) است، یک برش `k` عنصر را کپی می‌کند و `"".join(...)` همه‌ی
کاراکترها را می‌پیماید. باید دید عملیات چه می‌کند، نه اینکه چقدر تایپ
کرده‌اید.

</div>
