"""
URL configuration for super_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from superapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('superadmin',views.signin),
    path('signin',views.signin),
    path('log_out',views.logout),
    path('Dashboard_profile_finder/<id>', views.dashboard_profile_finder),
    path('Dashboard_hiring_manager/<id>', views.dashboard_hiring_manager),
    path('Dashboard_regional_manager/<id>', views.dashboard_regional_manager),
    path('Dashboard_ad_provider/<id>', views.dashboard_ad_provider),
    path('dashboard_ad_distributor/<id>', views.dashboard_ad_distributor),
    path('dashboard_profile_manager/<id>', views.dashboard_profile_manager),
    path('dashboard_sales_person/<id>', views.dashboard_sales_person),
    path('dashboard_private_investigator/<id>', views.dashboard_private_investigator),
    path('dashboard_affiliate_marketing/<id>', views.dashboard_affiliate_marketing),
    path('revenue/<id>', views.revenue),
    path('expense/<id>', views.expense),
    path('public_user/<id>', views.public_user),
    path('view_details/<id>', views.view_details),
    
    path('hiring_manager/<id>', views.hiring_manager),
    path('hm_edit_acc/<id>/<uid>', views.hm_edit_acc),
    
    path('profile_manager/<id>', views.admin_profile_manager),
    path('pm_edit_acc/<id>/<uid>', views.pm_edit_acc),

    
    path('sales_person/<id>', views.sales_person),
    path('sm_edit_profile/<id>/<uid>', views.sm_edit_profile),
    
    path('affiliate_marketing/<id>', views.affiliate_marketing),
    path('am_editaccount/<id>/<uid>', views.am_editaccount),

    
    path('ad_provider/<id>', views.ad_provider),
    path('ad_pro_edit_account/<id>/<uid>', views.ad_pro_edit_account), 
    
    path('ad_distributor/<id>', views.ad_distributor),
    path('ad_dis_edit_account/<id>/<uid>', views.ad_dis_edit_account), 

    
    
    path('private_investigator/<id>', views.private_investigator),
    path('pi_edit_profile/<id>/<uid>', views.pi_edit_profile),
    
    
    path('pi_settings/<id>', views.pi_settings),
    path('performance_settings/<id>', views.performance_settings),
    path('emra_coin/<id>', views.emra_coin),
    path('commision_calculator/<id>', views.commision_cal),
    path('Add_Commision_1/<id>/<uid>', views.Add_Commision_1),
    path('complaint_list/<id>', views.complaint_list),
    path('dropdown_values/<id>', views.dropdown_values),
    path('third_party_users/<id>', views.third_party_users),
    path('third_party_user_Add/<id>/<uid>', views.third_party_user_Add),
    path('subscription/<id>', views.subscription),
    path('subscriptionadd/<id>', views.subscriptionadd),
    path('subedit/<id>/<sid>', views.subscriptionedit),
    path('External_expense/<id>', views.External_expense),
    path('insentives_settings/<id>', views.insentives_settings),
    path('dummy_matching_list/<id>', views.matching_list),











]
