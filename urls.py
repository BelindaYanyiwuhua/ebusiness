from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from  django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user.urls', namespace='user')),  # 用户模块
    url(r'^goods/', include('goods.urls', namespace='goods')),  # 商品模块
    url(r'^', include('goods.urls', namespace='goods')),  # 商品模块
    url(r'^cart/', include('cart.urls', namespace='cart')),  # 购物车模块
    url(r'^order/', include('order.urls', namespace='order')),  # 订单模块
#    url(r'^captcha', include('captcha.urls')),#图形验证
#    url(r'^tinymce/', include('tinymce.urls')),  # 富文本编辑器
#    url(r'^search', include('haystack.urls')),  # 全文检索框架
]

'''
if settings.DEBUG:      #配置静态文件路径
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''