# Interview 02

## Question 1

Why is this function dangerous?

<div dir="rtl" align="right">

چرا این تابع خطرناک است؟

</div>

```python
def add(value, values=[]):
    values.append(value)
    return values
```

## Question 2

Explain the difference between:

```python
x == y
```

and:

```python
x is y
```

Give one appropriate use for each.

<div dir="rtl" align="right">

تفاوت بین `x == y` و `x is y` را توضیح دهید. برای هر‌کدام یک کاربرد مناسب ذکر کنید.

</div>

## Question 3

Predict and explain:

<div dir="rtl" align="right">

خروجی کد زیر را پیش‌بینی کرده و توضیح دهید:

</div>

```python
a = [1, 2]
b = a
c = a.copy()

a.append(3)

print(b)
print(c)
print(a is b)
print(a is c)
```

## Question 4

A data-preprocessing function receives a list of examples. Should it mutate the list or return a new list? Explain the tradeoff and the API contract you would choose.

<div dir="rtl" align="right">

یک تابع پیش‌پردازش داده، لیستی از نمونه‌ها را دریافت می‌کند. آیا باید لیست را تغییر دهد (mutate) یا یک لیست جدید برگرداند؟ مصالحه‌ی (tradeoff) بین این دو رویکرد و قراردادی (API contract) که خودتان انتخاب می‌کنید را توضیح دهید.

</div>

## Question 5

A test passes when run alone but fails when the full test suite runs. The function under test has a dictionary default parameter. Describe your investigation.

<div dir="rtl" align="right">

یک تست هنگام اجرای تنها موفق است، اما هنگام اجرای کل مجموعه‌ی تست‌ها شکست می‌خورد. تابع موردِ تست، یک پارامتر پیش‌فرض از نوع دیکشنری دارد. روند بررسی خود را شرح دهید.

</div>

## Question 6

You make a shallow copy of an experiment configuration, modify a nested list, and discover that the original configuration changed. Explain precisely why.

<div dir="rtl" align="right">

شما یک کپی سطحی (shallow copy) از تنظیمات یک آزمایش می‌سازید، یک لیست تودرتو (nested list) را تغییر می‌دهید و متوجه می‌شوید که تنظیمات اصلی نیز تغییر کرده است. دقیقاً توضیح دهید چرا.

</div>
