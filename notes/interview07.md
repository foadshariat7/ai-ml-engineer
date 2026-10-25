# Interview 07

### Question 1

Explain Python's argument passing model. Use these two examples:

```python
def mutate(values):
    values.append(1)
```

and:

```python
def replace(values):
    values = [1]
```

Why does one affect the caller and the other not?

<div dir="rtl" align="right">

مدل ارسال آرگومان در پایتون را توضیح دهید. از دو مثال بالا استفاده کنید. چرا یکی روی فراخواننده اثر می‌گذارد و دیگری نه؟

</div>

### Question 2

What is wrong with:

```python
def add_item(
    item,
    items=[],
):
    items.append(item)
    return items
```

Explain when the default is created and how you'd fix it.

<div dir="rtl" align="right">

کد بالا چه مشکلی دارد؟ توضیح دهید مقدار پیش‌فرض چه زمانی ساخته می‌شود و چگونه آن را اصلاح می‌کنید.

</div>

### Question 3

Explain:

```python
*args
```

and:

```python
**kwargs
```

Include:

- what each captures
- resulting container type
- appropriate use case

<div dir="rtl" align="right">

`*args` و `**kwargs` را توضیح دهید. موارد زیر را شامل کنید:

- هرکدام چه چیزی را جمع‌آوری می‌کند
- نوع ظرف (container) حاصل
- مورد استفاده‌ی مناسب

</div>

### Question 4

What is the difference between:

```python
transform
```

and:

```python
transform()
```

Why does that matter for callbacks?

<div dir="rtl" align="right">

تفاوت بین `transform` و `transform()` چیست؟ چرا این تفاوت برای callbackها اهمیت دارد؟

</div>

### Question 5

Define a higher-order function. Give an AI/ML-oriented example of why passing behavior as an argument is useful.

<div dir="rtl" align="right">

تابع مرتبه‌بالا (higher-order function) را تعریف کنید. یک مثال مرتبط با هوش مصنوعی/یادگیری ماشین بیاورید که نشان دهد چرا ارسال رفتار به‌عنوان آرگومان مفید است.

</div>

### Question 6

What is a closure? Explain:

```python
def make_threshold(threshold):
    def check(score):
        return score >= threshold

    return check
```

Why does `check()` still know `threshold`?

<div dir="rtl" align="right">

closure چیست؟ کد بالا را توضیح دهید. چرا `check()` همچنان `threshold` را می‌شناسد؟

</div>

### Question 7

Explain the late-binding problem in:

```python
functions = [
    lambda: value
    for value in range(3)
]
```

What might the functions return later and why?

<div dir="rtl" align="right">

مشکل اتصال دیرهنگام (late binding) را در کد بالا توضیح دهید. این توابع بعداً چه مقداری ممکن است برگردانند و چرا؟

</div>

### Question 8

When would you choose a `lambda` versus a named `def`? Give one appropriate `lambda` example and one inappropriate example.

<div dir="rtl" align="right">

چه زمانی `lambda` را و چه زمانی یک `def` نام‌دار را انتخاب می‌کنید؟ یک مثال مناسب و یک مثال نامناسب برای `lambda` بیاورید.

</div>

### Question 9

Trace:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

for `n = 4`. Explain both:

- call expansion
- return unwinding

<div dir="rtl" align="right">

اجرای کد بالا را برای `n = 4` دنبال کنید. هر دو مورد زیر را توضیح دهید:

- گسترش فراخوانی‌ها (call expansion)
- بازگشت مقادیر (return unwinding)

</div>

### Question 10

Compare recursive and iterative factorial in terms of:

- time
- auxiliary memory
- readability
- Python-specific practical considerations

<div dir="rtl" align="right">

فاکتوریل بازگشتی و تکراری را از نظر موارد زیر مقایسه کنید:

- زمان
- حافظه‌ی کمکی (auxiliary memory)
- خوانایی
- ملاحظات عملی مخصوص پایتون

</div>
