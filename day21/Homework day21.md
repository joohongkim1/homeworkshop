# Homework day21



```django
# 1.

{% for comment in comments %}
<h3>{{ comment.content }}}</h3>
{% endfor %}
```



```django
# 2. 

"{% url 'questions:comments_create' question.pk %}"
```

