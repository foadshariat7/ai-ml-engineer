# Interview 06

### Question 1

Rewrite the following code using a comprehension. Then explain the conceptual execution order.

```python
result: list[int] = []

for value in values:
    if value > 0:
        result.append(value * value)
```

<div dir="rtl" align="right">

کد بالا را با یک comprehension بازنویسی کنید. سپس ترتیب مفهومی اجرای آن را توضیح دهید.

</div>

### Question 2

Explain the difference between:

```python
[
    value
    for value in values
    if value > 0
]
```

and:

```python
[
    value if value > 0 else 0
    for value in values
]
```

Give a concrete input where they produce different output lengths.

<div dir="rtl" align="right">

تفاوت دو کد بالا را توضیح دهید. یک ورودی مشخص ارائه دهید که در آن این دو کد طول خروجی متفاوتی تولید کنند.

</div>

### Question 3

Why is this potentially incorrect?

```python
valid_scores = [
    score
    for score in scores
    if score
]
```

Assume zero is a valid score. Fix it when `None` represents missing data.

<div dir="rtl" align="right">

چرا کد بالا ممکن است نادرست باشد؟ فرض کنید صفر یک امتیاز معتبر است. آن را برای حالتی که `None` نشان‌دهنده‌ی داده‌ی گمشده است اصلاح کنید.

</div>

### Question 4

Compare:

```python
result = []

for item in items:
    result.append(transform(item))
```

with:

```python
result = [
    transform(item)
    for item in items
]
```

Discuss:

- semantics
- readability
- Big-O complexity
- when you would prefer one over the other

<div dir="rtl" align="right">

دو کد بالا را با هم مقایسه کنید. موارد زیر را بحث کنید:

- معناشناسی (semantics)
- خوانایی (readability)
- پیچیدگی Big-O
- اینکه در چه شرایطی هرکدام را ترجیح می‌دهید

</div>

### Question 5

What are the expected time and output-space complexities of:

```python
{
    token.lower()
    for token in tokens
}
```

where `n` = number of tokens and `k` = number of unique lowercase tokens. Explain the dictionary/set hashing assumption behind your answer.

<div dir="rtl" align="right">

پیچیدگی زمانی و پیچیدگی فضای خروجیِ موردانتظار برای کد بالا چقدر است، جایی که `n` تعداد token‌ها و `k` تعداد token‌های یکتای حروف‌کوچک‌شده است؟ فرض هش‌کردنِ dictionary/set را که پشت این پاسخ است توضیح دهید.

</div>

### Question 6

An interviewer shows:

```python
[
    log(record)
    for record in records
]
```

and asks whether you approve it. Explain your answer.

<div dir="rtl" align="right">

یک مصاحبه‌کننده کد بالا را نشان می‌دهد و می‌پرسد آیا آن را تأیید می‌کنید؟ پاسخ خود را توضیح دهید.

</div>
