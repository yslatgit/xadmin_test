#coding:utf-8
import xadmin
from xadmin import views
from users.models import EmailVerfiy


class BaseSetting(object):
    enable_themes = True #更改页面主题
    use_bootswatch = True #主题菜单
    # show_bookmarks = False  # 不显示书签


class GlobalSettings(object):
    '''全局变量配置'''
    site_title = 'YSL后台管理'#标题
    site_footer = '技术支持@ysl.com'#底部名称
    menu_style = 'accordion'#菜单风格


class EmailVerfiyAdmin(object):
    list_display = ['email','type','send_time']
    search_fileds = ['email','type']
    list_filter = ['email','type']

xadmin.site.register(EmailVerfiy,EmailVerfiyAdmin)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(views.BaseAdminView,BaseSetting)