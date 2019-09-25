# Workshop day20

```python
# 1.
class Question(models.Model):
    title = models.CharField(max_length=1000)

class Choice(models.Model):
    content = models.CharField(max_length=1000)
    votes = models.IntegerField()
    choice = models.ForeignKey(Question, on_delete=models.CASCADE)
```

