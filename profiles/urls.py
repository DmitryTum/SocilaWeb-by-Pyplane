from django.urls import path
from .views import (my_profile_view,
                    invites_receiver_view,
                    profiles_list_view,
                    invite_profiles_list_view,
                    send_invitation,
                    remove_from_friends,
                    accept_invitation,
                    reject_invitation,)
from .views import ProfileListView, ProfileDetailView

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('my-invites/', invites_receiver_view, name='my-invites-view'),

    # вызов на основе функиции
    # path('all-profiles/', profiles_list_view, name='all-profiles-view'),
    # на основе класса ListView
    path('', ProfileListView.as_view(), name='all-profiles-view'),

    path('/<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('to-invite/', invite_profiles_list_view, name='invite-profiles-view'),
    path('send-invite/', send_invitation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('my-invites/acctept/', accept_invitation, name='accept-invite'),
    path('my-invites/reject/', reject_invitation, name='reject-invite'),
]
