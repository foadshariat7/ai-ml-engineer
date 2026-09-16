# Interview 04

## Question 1

Implement a function that returns the frequency of every word in a list.

Explain the expected time and space complexity.

<div dir="rtl" align="right">

تابعی بنویسید که فراوانی (frequency) هر کلمه در یک لیست را برمی‌گرداند. پیچیدگی زمانی و مکانی (time and space complexity) موردانتظار را توضیح دهید.

</div>

## Question 2

Why is this incorrect for calculating per-user averages?

```python
result[user_id] = score
```

Describe the state that must be maintained instead.

<div dir="rtl" align="right">

چرا کد بالا برای محاسبه‌ی میانگین به‌ازای هر کاربر نادرست است؟ وضعیتی (state) را که در عوض باید نگه‌داری شود شرح دهید.

</div>

## Question 3

What is the difference among:

```python
dictionary[key]
dictionary.get(key)
key in dictionary
```

When would you use each?

<div dir="rtl" align="right">

تفاوت بین سه کد بالا چیست؟ هرکدام را در چه شرایطی استفاده می‌کنید؟

</div>

## Question 4

A candidate writes:

```python
if not score:
    continue
```

The score may legally be zero.

Explain the defect and provide the correct condition.

<div dir="rtl" align="right">

یک داوطلب کد بالا را می‌نویسد. مقدار `score` ممکن است به‌طور قانونی صفر باشد. نقص این کد را توضیح داده و شرط صحیح را ارائه دهید.

</div>

## Question 5

Why does this check accept a Boolean?

```python
isinstance(value, (int, float))
```

How would you correct it?

<div dir="rtl" align="right">

چرا بررسی بالا یک مقدار Boolean را هم می‌پذیرد؟ چگونه آن را اصلاح می‌کنید؟

</div>

## Question 6

You must compute averages for 100 million records that arrive as a stream.

Would you store every score in a list by user? Explain:

- memory tradeoffs
- required running state
- complexity
- what changes if you also need the median

<div dir="rtl" align="right">

باید میانگین‌ها را برای ۱۰۰ میلیون رکورد که به‌صورت stream می‌رسند محاسبه کنید. آیا هر امتیاز را در لیستی به‌ازای هر کاربر ذخیره می‌کنید؟ موارد زیر را توضیح دهید:

- مصالحه‌های حافظه (memory tradeoffs)
- وضعیت در حال اجرای (running state) موردنیاز
- پیچیدگی (complexity)
- اینکه اگر به میانه (median) هم نیاز داشته باشید چه چیزی تغییر می‌کند

</div>

## Question 7

What is the expected complexity of dictionary lookup?

What assumption is hidden inside that answer?

<div dir="rtl" align="right">

پیچیدگی موردانتظار برای جست‌وجو (lookup) در دیکشنری چقدر است؟ چه فرضی درون آن پاسخ پنهان شده است؟

</div>

## Question 8

A test for an average fails because the result is:

```python
0.15000000000000002
```

instead of:

```python
0.15
```

Explain why and describe an appropriate test strategy.

<div dir="rtl" align="right">

یک تست برای میانگین شکست می‌خورد، زیرا نتیجه به‌جای `0.15` برابر `0.15000000000000002` است. دلیل آن را توضیح داده و یک استراتژی تست مناسب شرح دهید.

</div>
