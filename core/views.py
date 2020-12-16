from django.shortcuts import render


def home(request):
    """
    This is a starting, dummy view pointing to the base template.
    Please modify it to your own needs and return your extending
    template instead, currently inexistent.
    """

    return render(request, "base.html")
