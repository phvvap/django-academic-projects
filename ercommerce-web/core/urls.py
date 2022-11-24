from django.urls import path
from django.contrib.auth import views
from product.views import product
from core.views import frontpage, shop, signup, profile, edit_profile
urlpatterns = [

    path("", frontpage, name="frontpage"),
    path("signup/", signup, name="signup"),
    path("login/", views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("shop/", shop, name="shop"),
    # this mean slug we want dynamic
    path("shop/<slug:slug>/", product, name="product"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),

]
