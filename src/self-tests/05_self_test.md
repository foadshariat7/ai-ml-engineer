# Self-Test 05: Time Complexity

This document explains the six exercises in
[`05_self_test.py`](05_self_test.py): constant time, a single loop, nested
loops, sequential loops and dropped constants, repeated halving, and the
difference between best case and worst case.

<div dir="rtl" align="right">

## خودآزمون ۵: پیچیدگی زمانی (Time Complexity)

این سند شش تمرین موجود در فایل [`05_self_test.py`](05_self_test.py) را توضیح
می‌دهد: زمان ثابت، یک حلقه‌ی ساده، حلقه‌های تودرتو، حلقه‌های پشت‌سرهم و حذف
ضرایب ثابت، نصف‌کردن پیاپی، و تفاوت بهترین حالت با بدترین حالت.

</div>

## 1: Constant time

`first` does exactly one thing: index into the list. A Python list stores its
elements in a contiguous block, so `items[0]` jumps straight to the element
without scanning anything. The number of operations is the same whether
`items` has 10 elements or 10 million, so the size of the input does **not**
change the work done. The complexity is **O(1)** — constant time.

<div dir="rtl" align="right">

### ۱: زمان ثابت

تابع `first` دقیقاً یک کار انجام می‌دهد: دسترسی به یک ایندکس از لیست. لیست در
پایتون عناصر خود را در یک بلوک پیوسته نگه می‌دارد، پس `items[0]` مستقیماً به
آن عنصر می‌پرد و چیزی را پیمایش نمی‌کند. تعداد عملیات چه لیست ۱۰ عنصر داشته
باشد و چه ۱۰ میلیون عنصر یکسان است، پس اندازه‌ی ورودی کارِ انجام‌شده را
**تغییر نمی‌دهد**. پیچیدگی برابر **O(1)** است — زمان ثابت.

</div>

## 2: A single loop

The loop body runs once per element, so for a list of `n` elements it runs
`n` times. If `items` becomes twice as long, the work doubles: the growth is
directly proportional to the input size. The complexity is **O(n)** — linear
time.

<div dir="rtl" align="right">

### ۲: یک حلقه‌ی ساده

بدنه‌ی حلقه به‌ازای هر عنصر یک‌بار اجرا می‌شود، پس برای لیستی با `n` عنصر،
`n` بار اجرا می‌شود. اگر طول `items` دو برابر شود، کار هم دو برابر می‌شود:
رشد مستقیماً متناسب با اندازه‌ی ورودی است. پیچیدگی برابر **O(n)** است — زمان
خطی.

</div>

## 3: Nested loops

For **each** of the `n` outer iterations, the inner loop runs a full `n`
times, so the counts multiply: `n × n = n²` pairs are printed. Nesting is
multiplication — that is the key signal to look for. The complexity is
**O(n²)** — quadratic time. With `n = 1,000` that is a million prints; with
`n = 10,000` it is a hundred million.

<div dir="rtl" align="right">

### ۳: حلقه‌های تودرتو

به‌ازای **هر یک** از `n` تکرار حلقه‌ی بیرونی، حلقه‌ی درونی کامل `n` بار اجرا
می‌شود، پس تعدادها در هم ضرب می‌شوند: `n × n = n²` جفت چاپ می‌شود. تودرتویی
یعنی ضرب — و این همان نشانه‌ی کلیدی است که باید دنبالش بگردید. پیچیدگی برابر
**O(n²)** است — زمان درجه‌دو. با `n = 1000` یعنی یک میلیون چاپ، و با
`n = 10000` یعنی صد میلیون چاپ.

</div>

## 4: Two sequential loops

No — this is **not** O(n²). The two loops are **sequential**, not nested: the
second loop starts only after the first one has finished. Sequential work
**adds** (`n + n = 2n`) while nested work **multiplies** (`n × n = n²`). Big-O
describes how the cost *grows*, not its exact value, so constant factors are
dropped: `2n` becomes **O(n)**. The function really is twice as slow as
exercise 2, but it belongs to the same growth class — doubling the input still
only doubles the work.

<div dir="rtl" align="right">

### ۴: دو حلقه‌ی پشت‌سرهم

خیر — این **O(n²) نیست**. دو حلقه **پشت‌سرهم** هستند، نه تودرتو: حلقه‌ی دوم
تنها پس از پایان حلقه‌ی اول شروع می‌شود. کارِ پشت‌سرهم با هم **جمع** می‌شود
(`n + n = 2n`) در حالی که کارِ تودرتو در هم **ضرب** می‌شود (`n × n = n²`).
Big-O نحوه‌ی *رشد* هزینه را توصیف می‌کند، نه مقدار دقیق آن را، پس ضرایب ثابت
حذف می‌شوند: `2n` تبدیل به **O(n)** می‌شود. این تابع واقعاً دو برابر تمرین ۲
کند است، اما در همان رده‌ی رشد قرار دارد — دو برابر شدن ورودی باز هم کار را
فقط دو برابر می‌کند.

</div>

## 5: Repeated halving

Each iteration replaces `n` with `n // 2`, so the value shrinks by a factor
of two every time instead of by one. The question "how many halvings reach
1?" is exactly the definition of the base-2 logarithm, so the loop runs about
**log₂(n)** times. For `n = 1024` that is **10** iterations (1024 → 512 → 256
→ 128 → 64 → 32 → 16 → 8 → 4 → 2 → 1). The complexity is **O(log n)** —
logarithmic time, the growth class of binary search. Dividing (or
multiplying) the loop variable is the signal for `log n`; adding or
subtracting a constant is the signal for `n`.

<div dir="rtl" align="right">

### ۵: نصف‌کردن پیاپی

هر تکرار مقدار `n` را با `n // 2` جایگزین می‌کند، پس مقدار در هر گام به‌جای
کم‌شدن یک واحد، بر ۲ تقسیم می‌شود. پرسشِ «چند بار نصف‌کردن به ۱ می‌رسد؟»
دقیقاً همان تعریف لگاریتم در پایه‌ی ۲ است، پس حلقه تقریباً **log₂(n)** بار
اجرا می‌شود. برای `n = 1024` یعنی **۱۰** تکرار
(۱۰۲۴ ← ۵۱۲ ← ۲۵۶ ← ۱۲۸ ← ۶۴ ← ۳۲ ← ۱۶ ← ۸ ← ۴ ← ۲ ← ۱). پیچیدگی برابر
**O(log n)** است — زمان لگاریتمی، همان رده‌ی رشدِ جست‌وجوی دودویی. تقسیم (یا
ضرب) متغیر حلقه نشانه‌ی `log n` است؛ جمع یا تفریق یک مقدار ثابت نشانه‌ی `n`.

</div>

## 6: Linear search

The **best case** is **O(1)**: `target` is the very first element, the `if`
matches immediately and the function returns after one comparison. The
**worst case** is **O(n)**: `target` is the last element, or is not in
`items` at all, so the loop compares every element before returning. The
average case is also **O(n)**, since on random data the match is found around
the middle — `n / 2` comparisons, and the constant is dropped. Big-O normally
describes the **worst case**, because that is the guarantee you can rely on,
so linear search is called an **O(n)** algorithm.

<div dir="rtl" align="right">

### ۶: جست‌وجوی خطی

**بهترین حالت** برابر **O(1)** است: `target` همان عنصر اول است، شرط `if`
بی‌درنگ برقرار می‌شود و تابع پس از یک مقایسه بازمی‌گردد. **بدترین حالت**
برابر **O(n)** است: `target` آخرین عنصر است، یا اصلاً در `items` وجود ندارد،
پس حلقه پیش از بازگشت همه‌ی عناصر را مقایسه می‌کند. حالت میانگین هم **O(n)**
است، چون روی داده‌ی تصادفی مقدار موردنظر حدوداً در میانه پیدا می‌شود —
`n / 2` مقایسه، که ضریب ثابتش حذف می‌شود. Big-O معمولاً **بدترین حالت** را
توصیف می‌کند، چون همان چیزی است که می‌توان به آن تکیه کرد، پس جست‌وجوی خطی را
الگوریتمی **O(n)** می‌نامند.

</div>
