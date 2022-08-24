# Raising assertion errors

Python assert is basically a debugging aid which test condition for internal self-check of your code. Assert makes debugging really easy when your code gets into impossible edge cases. Assert check those impossible cases.

```python
def discount(original_price, discount):
    new_price = price - (discount*original_price)
    assert 0 < new_price < original_price
    return new_price 
```

Here, the new_price can never be less than 0. In the case the above written condition is voilated, ```assert``` raises an assertion error, which helps to identify where the error has occurred. 

If an assert statement does not return anything it mean the condition was satisfied.