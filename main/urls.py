from django.urls import path
from main.views import buy_product_ajax, delete_product_ajax, login_ajax, register_ajax, show_main, show_xml, show_xml_by_id, show_json, show_json_by_id, create_product, show_product, register, login_user, logout_user, edit_product, delete_product, buy_product, add_product_entry_ajax, update_product_ajax, create_product_flutter, my_products

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path("buy/<uuid:id>/", buy_product, name="buy_product"),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('ajax/product/<uuid:id>/update/', update_product_ajax, name='update_product_ajax'),
    path('ajax/product/<uuid:id>/delete/', delete_product_ajax, name='delete_product_ajax'),
    path('ajax/register/', register_ajax, name='register_ajax'),
    path('ajax/login/', login_ajax, name='login_ajax'),
    path('ajax/product/<uuid:id>/buy/', buy_product_ajax, name='buy_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('my-products/', my_products, name='my_products'),
]