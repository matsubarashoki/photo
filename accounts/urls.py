from django.urls import path, include

from . import views
# viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    #サインアップページのビューの呼び出し
    #「http://<host>/signup」へのアクセスに対して、viewモジュールのSignUpViewをインスタンス化する
    path('signup/',views.SignUpView.as_view(),name='signup'),

    #サインアップ完了ページのビューの呼び出し
    #「http://<host>/signup_success」へのアクセスに対して、viewモジュールのSignUpSuccessViewをインスタンス化する
    path('signup_success/',views.SignUpSuccessView.as_view(),name='signup_success'),
        # ログインページの表示
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    # django.contrib.auth.views.LoginViewをインスタンス化して
    # ログインページを表示する
    path('login/',
         # ログイン用のテンプレート(フォーム)をレンダリング
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'
         ),
    
    # ログアウトを実行
    # 「http(s)://<ホスト名>/logout/」へのアクセスに対して、
    # django.contrib.auth.views.logoutViewをインスタンス化して
    # ログアウトさせる
    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'
         ),
]
