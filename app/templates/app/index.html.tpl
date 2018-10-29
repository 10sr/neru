<p>Userinfo: {{ user.str }}</p>

{% if sleeps %}
<ul>
    {% for sleep in sleeps %}
    <li>{{ sleep.time_of_sleep }}</li>
    {% endfor %}
</ul>
{% else %}
<p>No sleep record found.</p>
{% endif %}

<a href="{% url 'app:user' user.username %}">This page</a>
<a href="{% url 'app:index' %}">Top</a>
