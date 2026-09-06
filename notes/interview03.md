# Interview 03

## Part 1: Concepts

### Question 1

What is a variable in Python?

<div dir="rtl" align="right">

متغیر در پایتون چیست؟

</div>

A strong answer should explain that a Python variable is better thought of as a name bound to an object, rather than a typed container holding the object itself.

<div dir="rtl" align="right">

یک پاسخ خوب باید توضیح دهد که متغیر در پایتون را بهتر است به‌عنوان نامی در نظر گرفت که به یک شیء متصل (bound) شده است، نه یک ظرفِ تایپ‌شده که خودِ شیء را در خود نگه می‌دارد.

</div>

### Question 2

Is Python dynamically typed or statically typed? Explain what dynamic typing means and why the following is valid:

<div dir="rtl" align="right">

آیا پایتون dynamically typed است یا statically typed؟ توضیح دهید dynamic typing به چه معناست و چرا کد زیر معتبر است:

</div>

```python
x = 10
x = "Python"
```

### Question 3

What is scope?

<div dir="rtl" align="right">

scope چیست؟

</div>

Explain how scope determines where names are visible and accessible.

<div dir="rtl" align="right">

توضیح دهید scope چگونه تعیین می‌کند که نام‌ها کجا قابل مشاهده و قابل دسترسی هستند.

</div>

### Question 4

Explain the LEGB rule. You should be able to state:

- Local
- Enclosing
- Global
- Built-in

and explain the lookup order.

<div dir="rtl" align="right">

قانون LEGB را توضیح دهید. باید بتوانید موارد زیر را بیان کنید:

- Local (محلی)
- Enclosing (محصورکننده)
- Global (سراسری)
- Built-in (درونی)

و ترتیب جست‌وجو را توضیح دهید.

</div>

### Question 5

What is variable shadowing? Explain:

```python
x = 10

def foo():
    x = 20
```

and also why this can be problematic:

```python
list = [1, 2]
```

<div dir="rtl" align="right">

سایه‌اندازی متغیر (variable shadowing) چیست؟ کد بالا را توضیح دهید و همچنین بگویید چرا کد زیر می‌تواند مشکل‌ساز باشد:

```python
list = [1, 2]
```

</div>

### Question 6

What's the difference between `global` and `nonlocal`?

<div dir="rtl" align="right">

تفاوت بین `global` و `nonlocal` چیست؟

</div>

Expected distinction:

- `global` → module-level binding
- `nonlocal` → nearest enclosing function binding

<div dir="rtl" align="right">

تمایز موردانتظار:

- `global` → اتصال (binding) در سطح ماژول
- `nonlocal` → اتصال در نزدیک‌ترین تابع محصورکننده

</div>

### Question 7

What's the difference between `int` and `float`? Also be prepared to discuss floating-point precision.

<div dir="rtl" align="right">

تفاوت بین `int` و `float` چیست؟ همچنین آماده باشید درباره‌ی دقت اعداد اعشاری (floating-point precision) صحبت کنید.

</div>

### Question 8

Why does this return `False`?

```python
0.1 + 0.2 == 0.3
```

A strong answer mentions binary floating-point representation.

<div dir="rtl" align="right">

چرا کد بالا مقدار `False` برمی‌گرداند؟ یک پاسخ خوب به نمایش دودویی اعداد اعشاری (binary floating-point representation) اشاره می‌کند.

</div>

### Question 9

What's the difference between `/` and `//`? Explain normal division and floor division.

<div dir="rtl" align="right">

تفاوت بین `/` و `//` چیست؟ تقسیم معمولی و تقسیم صحیح (floor division) را توضیح دهید.

</div>

### Question 10

What does `%` do? Give at least two practical uses:

- even/odd detection
- cyclic/index calculations
- divisibility checks

<div dir="rtl" align="right">

عملگر `%` چه کاری انجام می‌دهد؟ حداقل دو کاربرد عملی ذکر کنید:

- تشخیص زوج/فرد
- محاسبات چرخه‌ای/ایندکس
- بررسی بخش‌پذیری

</div>

### Question 11

Are Python strings mutable? No. Explain what occurs here:

```python
name = "Foad"
name = name.upper()
```

A new string object is produced and `name` is rebound.

<div dir="rtl" align="right">

آیا رشته‌های پایتون تغییرپذیرند (mutable)؟ خیر. توضیح دهید در کد بالا چه اتفاقی می‌افتد؛ یک شیء رشته‌ی جدید ساخته می‌شود و `name` به آن rebind می‌شود.

</div>

### Question 12

What's the difference between `==` and `is`?

<div dir="rtl" align="right">

تفاوت بین `==` و `is` چیست؟

</div>

Expected:

- `==` → value/equality
- `is` → identity

<div dir="rtl" align="right">

موردانتظار:

- `==` → برابری مقدار
- `is` → یکسانی هویت (identity)

</div>

### Question 13

Why should `None` normally be checked with `is`? Because `None` is a singleton object and you're checking identity:

```python
value is None
```

<div dir="rtl" align="right">

چرا معمولاً باید `None` را با `is` بررسی کرد؟ چون `None` یک شیء singleton است و شما هویت (identity) آن را بررسی می‌کنید:

</div>

### Question 14

What is truthiness? Explain why:

```python
bool("")
```

is false but:

```python
bool("False")
```

is true.

<div dir="rtl" align="right">

truthiness چیست؟ توضیح دهید چرا `bool("")` برابر `False` است اما `bool("False")` برابر `True` است.

</div>

### Question 15

Does `and` always return a Boolean? No. Explain:

```python
"" or "default"
```

and:

```python
"Python" and "AI"
```

<div dir="rtl" align="right">

آیا `and` همیشه یک Boolean برمی‌گرداند؟ خیر. کدهای بالا را توضیح دهید.

</div>

### Question 16

What is short-circuit evaluation? Explain why Python may not evaluate the second expression in:

```python
a and b
```

or:

```python
a or b
```

<div dir="rtl" align="right">

ارزیابی اتصال کوتاه (short-circuit evaluation) چیست؟ توضیح دهید چرا پایتون ممکن است عبارت دوم را در `a and b` یا `a or b` ارزیابی نکند.

</div>

### Question 17

What is the difference between `if`, `elif`, and `else`? Also explain why condition order matters.

<div dir="rtl" align="right">

تفاوت بین `if`، `elif` و `else` چیست؟ همچنین توضیح دهید چرا ترتیب شرط‌ها اهمیت دارد.

</div>

### Question 18

What's the difference between a `for` loop and a `while` loop?

<div dir="rtl" align="right">

تفاوت بین حلقه‌ی `for` و حلقه‌ی `while` چیست؟

</div>

A good answer:

- `for` → iterate over an iterable
- `while` → continue while a condition remains truthy

<div dir="rtl" align="right">

یک پاسخ خوب:

- `for` → پیمایش روی یک iterable
- `while` → ادامه تا زمانی که یک شرط truthy باقی بماند

</div>

### Question 19

What's the difference between `break`, `continue`, and `pass`?

<div dir="rtl" align="right">

تفاوت بین `break`، `continue` و `pass` چیست؟

</div>

Expected:

- `break` → terminate loop
- `continue` → skip rest of current iteration
- `pass` → perform no operation

<div dir="rtl" align="right">

موردانتظار:

- `break` → پایان دادن به حلقه
- `continue` → رد کردن باقی‌ی تکرار فعلی
- `pass` → انجام ندادن هیچ عملیاتی

</div>

### Question 20

What is `range(10)`? Explain why it represents values:

```python
0 through 9
```

rather than:

```python
1 through 10
```

<div dir="rtl" align="right">

`range(10)` چیست؟ توضیح دهید چرا مقادیر `۰ تا ۹` را نشان می‌دهد، نه `۱ تا ۱۰`.

</div>

### Question 21

What does `range(2, 10, 2)` produce?

<div dir="rtl" align="right">

`range(2, 10, 2)` چه مقادیری تولید می‌کند؟

</div>

Expected: `2, 4, 6, 8`. Explain start, stop, and step.

<div dir="rtl" align="right">

موردانتظار: `2, 4, 6, 8`. پارامترهای start، stop و step را توضیح دهید.

</div>

### Question 22

What is the `else` block on a Python loop?

<div dir="rtl" align="right">

بلوک `else` در حلقه‌ی پایتون چیست؟

</div>

A strong answer should mention: it runs when the loop finishes normally and is skipped when the loop terminates through `break`.

<div dir="rtl" align="right">

یک پاسخ خوب باید اشاره کند: این بلوک زمانی اجرا می‌شود که حلقه به‌طور عادی تمام شود، و اگر حلقه با `break` پایان یابد، نادیده گرفته می‌شود.

</div>

## Part 2: Code Questions

### Code Question 1

Without running it, determine the output:

```python
x = 10

def outer():
    x = 20

    def inner():
        print(x)

    inner()

outer()
```

Then explain which LEGB scope resolves `x`.

<div dir="rtl" align="right">

بدون اجرای کد بالا، خروجی آن را تعیین کنید. سپس توضیح دهید کدام scope در LEGB مقدار `x` را resolve می‌کند.

</div>

### Code Question 2

What happens?

```python
x = 10

def change():
    print(x)
    x = 20

change()
```

Explain the `UnboundLocalError`. This is an excellent scope interview question.

<div dir="rtl" align="right">

چه اتفاقی می‌افتد؟ خطای `UnboundLocalError` را توضیح دهید. این یک سؤال مصاحبه‌ی عالی درباره‌ی scope است.

</div>

### Code Question 3

What does this print?

```python
print(bool([]))
print(bool([0]))
print(bool(""))
print(bool("0"))
print(bool(None))
```

Explain every result.

<div dir="rtl" align="right">

این کد چه چیزی چاپ می‌کند؟ هر نتیجه را توضیح دهید.

</div>

### Code Question 4

What is wrong?

```python
str = "hello"

number = str(10)
```

Explain using LEGB and built-in shadowing.

<div dir="rtl" align="right">

این کد چه مشکلی دارد؟ با استفاده از LEGB و سایه‌اندازی روی built-in توضیح دهید.

</div>

### Code Question 5

Predict:

```python
x = 5

if x:
    print("A")

if x > 10:
    print("B")
elif x > 0:
    print("C")
else:
    print("D")
```

<div dir="rtl" align="right">

پیش‌بینی کنید:

</div>

### Code Question 6

Predict:

```python
for i in range(5):
    if i == 2:
        continue

    if i == 4:
        break

    print(i)
```

Then explain execution one iteration at a time.

<div dir="rtl" align="right">

پیش‌بینی کنید. سپس اجرای کد را تکرار‌به‌تکرار توضیح دهید.

</div>

### Code Question 7

Write code that determines whether:

```python
number = 42
```

is divisible by both 3 and 7.

<div dir="rtl" align="right">

کدی بنویسید که تعیین کند آیا `number = 42` هم بر ۳ و هم بر ۷ بخش‌پذیر است.

</div>

### Code Question 8

Write code that finds the first number between 1 and 100 divisible by 7 and 11. Use `break`.

<div dir="rtl" align="right">

کدی بنویسید که اولین عدد بین ۱ تا ۱۰۰ را پیدا کند که بر ۷ و ۱۱ بخش‌پذیر باشد. از `break` استفاده کنید.

</div>

### Code Question 9

Write a loop that calculates:

```python
1 + 2 + 3 + ... + 100
```

without using `sum()`. Then explain the time complexity. Expected: `O(n)`.

<div dir="rtl" align="right">

حلقه‌ای بنویسید که مجموع `1 + 2 + 3 + ... + 100` را بدون استفاده از `sum()` محاسبه کند. سپس پیچیدگی زمانی آن را توضیح دهید. موردانتظار: `O(n)`.

</div>

### Code Question 10

Given:

```python
text = "machine learning"
```

count how many times the character `"n"` appears without using `text.count()`.

<div dir="rtl" align="right">

با داشتن `text = "machine learning"`، تعداد تکرار کاراکتر `"n"` را بدون استفاده از `text.count()` بشمارید.

</div>
