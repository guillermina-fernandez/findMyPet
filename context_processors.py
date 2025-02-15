from django.contrib.auth.models import Group


def user_profile_data(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = f'{request.user.username}'
    
    user_groups = Group.objects.filter(user=request.user.id)
    is_administrator = False
    for group in user_groups:
        if group.name == 'administration':
            is_administrator = True
    
    return {
        'is_administrator': is_administrator,
        'user_profile': user_profile,
    }