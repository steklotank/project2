from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create-listing", views.create_listing, name="create-listing"),
    path("categories", views.categories, name="categories"),
    path("filter", views.filter, name="filter")
]
