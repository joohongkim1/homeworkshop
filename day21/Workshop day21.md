# Workshop day21



```python
def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    choices = question.choices.all()
    context = {
        'question': question,
        'choices': choices,
    }
    return render(request, 'questions/detail.html', context)
```



```django
{% comment %} detail.html {% endcomment %}
<h1>{{ question.title }}</h1>
<ul>
  {% for choice in choices %}
    <li>
      {{ choice.content }}: {{ choice.votes }}표
    </li>
  {% endfor %}
 </ul>
```

