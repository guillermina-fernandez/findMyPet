from django.contrib import messages


def error_message(request, message):
    return messages.error(request, message)