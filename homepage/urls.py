from django.urls import path
from . import views, views_account

urlpatterns = [
    path("", views.v_index, name="index"),
    path("feedback/create", views.v_feedback_create, name="feedback_create"),
    path("feedback/gracias", views.v_feedback_gracias, name="feedback_gracias"),
    path("sign_up", views_account.v_sign_up, name="sign_up"),
    path("sign_up/create", views_account.v_sign_up_create, name="sign_up_create"),
    path("sign_up/thank_you", views_account.v_sign_up_thank_you, name="sign_up_thank_you"),
    path("sign_in", views_account.v_sign_in, name="sign_in"),
    path("sign_in/members", views_account.v_sign_in_members, name="sign_in_members"),
    path("sign_in/login", views_account.v_sign_in_login, name="sign_in_login"),
]