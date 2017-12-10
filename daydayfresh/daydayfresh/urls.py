
from django.conf.urls import url, include

import xadmin

from daydayfresh.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

# 用户Token
from rest_framework.authtoken import views

from goods.views import GoodsListViewSet, CategoryViewSet
from user.views import SmsCodeViewset

router = DefaultRouter()

# 商品
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 商品分类
router.register(r'categorys', CategoryViewSet, base_name='categorys')
router.register(r'codes', SmsCodeViewset, base_name='codes')

urlpatterns = [

    # 基础路由
    url(r'^admin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^', include(router.urls)),

    # 用户token
    url(r'^api-token-auth/', views.obtain_auth_token),

    # jwt认证模式
    url(r'^login/', obtain_jwt_token),

    # 文档
    url(r'docs/', include_docs_urls(title='天天生鲜'))
]
