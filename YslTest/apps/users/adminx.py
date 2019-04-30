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

    def get_site_menu(self):
        """自定义菜单dj44"""
        return [
            {
                'title': '课程管理',
                'icon': 'fa fa-bars',       # Font Awesome图标
                'menus':(
                    {
                        'title': '课程信息',
                        'icon': 'fa fa-bug',
                        'url':'http://127.0.0.1:8000/xadmin/course/course/'

                    },
                    {
                        'title': '章节信息',
                        'icon': 'fa fa-envelope-o',
                        'url':'http://127.0.0.1:8000/xadmin/course/section/'
                    },
                    {
                        'title': '视频信息',
                        'icon': 'fa fa-envelope-o',
                        'url':'http://127.0.0.1:8000/xadmin/course/videosource/'
                    },
                    {
                        'title': '讲师信息',
                        'icon': 'fa fa-envelope-o',
                        'url':'http://127.0.0.1:8000/xadmin/course/teacher/'
                    }
                )
            },
            {
                'title': 'Bug统计',
                'icon': 'fa fa-bug',
                'menus':(
                    {
                        'title': 'Bug表',
                        'icon': 'fa fa-bug',
                        'url': "https://www.cnblogs.com/yoyoketang/"  # 自定义跳转列表

                    },)
            }

        ]


class EmailVerfiyAdmin(object):
    list_display = ['email','type','send_time']
    search_fields = ['email','type']
    list_filter = ['email','type']

xadmin.site.register(EmailVerfiy,EmailVerfiyAdmin)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(views.BaseAdminView,BaseSetting)