# Interview 05

## Part 1: Practice Mode

Answer aloud as though I were interviewing you.

<div dir="rtl" align="right">

به‌صورت شفاهی پاسخ دهید، همان‌طور که انگار من از شما مصاحبه می‌گیرم.

</div>

### Question 1

What is Big O notation?

<div dir="rtl" align="right">

نماد Big O چیست؟

</div>

### Question 2

What is the complexity of the following code? Explain why.

```python
for item in items:
    print(item)
```

<div dir="rtl" align="right">

پیچیدگی کد بالا چقدر است؟ دلیل آن را توضیح دهید.

</div>

### Question 3

What is the complexity of the following code?

```python
for x in items:
    for y in items:
        print(x, y)
```

<div dir="rtl" align="right">

پیچیدگی کد بالا چقدر است؟

</div>

### Question 4

What is the difference between two sequential loops and two nested loops?

<div dir="rtl" align="right">

تفاوت دو حلقه‌ی پشت‌سرهم با دو حلقه‌ی تودرتو چیست؟

</div>

### Question 5

What is the average lookup complexity of a Python dictionary? What about its theoretical worst case?

<div dir="rtl" align="right">

پیچیدگی میانگین جست‌وجو (lookup) در دیکشنری پایتون چقدر است؟ بدترین حالت نظری آن چطور؟

</div>

### Question 6

Why is Python list append described as amortized O(1)?

<div dir="rtl" align="right">

چرا append در لیست پایتون به‌صورت سرشکن‌شده (amortized) O(1) توصیف می‌شود؟

</div>

### Question 7

Suppose this code is too slow, where `blocked_ids` is a list. How might you improve it?

```python
for user in users:
    if user.id in blocked_ids:
        ...
```

<div dir="rtl" align="right">

فرض کنید کد بالا بیش از حد کند است، جایی که `blocked_ids` یک لیست است. چگونه آن را بهبود می‌دهید؟

</div>

### Question 8

What is the difference between `O(n)` and `O(log n)` as input grows?

<div dir="rtl" align="right">

با بزرگ‌شدن ورودی، تفاوت `O(n)` و `O(log n)` چیست؟

</div>

### Question 9

Can an O(n²) algorithm ever outperform an O(n) algorithm? Explain carefully.

<div dir="rtl" align="right">

آیا ممکن است یک الگوریتم O(n²) هرگز از یک الگوریتم O(n) بهتر عمل کند؟ با دقت توضیح دهید.

</div>

### Question 10

What is auxiliary space complexity?

<div dir="rtl" align="right">

پیچیدگی فضای کمکی (auxiliary space complexity) چیست؟

</div>

## Part 2: Trap Questions

### Trap 1

```python
for i in range(0, n, 2):
    print(i)
```

The candidate says `O(n / 2)`. How should this be expressed?

<div dir="rtl" align="right">

داوطلب می‌گوید `O(n / 2)`. این پاسخ را چگونه باید بیان کرد؟

</div>

### Trap 2

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

The candidate says `O(n²)`. Why is that wrong?

<div dir="rtl" align="right">

داوطلب می‌گوید `O(n²)`. چرا این پاسخ نادرست است؟

</div>

### Trap 3

```python
for item in numbers:
    if item in numbers:
        ...
```

The candidate says `O(n)`. What did they miss?

<div dir="rtl" align="right">

داوطلب می‌گوید `O(n)`. چه چیزی را از قلم انداخته است؟

</div>

### Trap 4

```python
sorted(numbers)
```

The candidate says `O(1)`, because it is one function call. Explain the error.

<div dir="rtl" align="right">

داوطلب می‌گوید `O(1)`، چون فقط یک فراخوانی تابع است. این اشتباه را توضیح دهید.

</div>
