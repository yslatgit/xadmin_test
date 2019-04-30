#coding:utf-8
import xadmin
from xadmin import views
from course.models import *
from xadmin.layout import Main,TabHolder,Tab,Fieldset,Row,Col,AppendedText,Side,Field #dj39


# class GlobalSettings(object):
#     """此方法不会用"""
#     # def get_site_menu(self):
#     #     return [
#     #         {
#     #             'title':'课程信息',
#     #             'perm':self.get_model_perm(Course,'view'),
#     #             'icon':'',
#     #             'menus':{
#     #                 {'title':'视频信息','url':self.get_model_url(Course,'videosource')},
#     #                 {'title':'章节信息','url':self.get_model_url(Course,'section')},
#     #                 {'title':'讲师信息','url':self.get_model_url(Course,'teacher')},
#     #                 {'title':'课程信息','url':self.get_model_url(Course,'course')},
#     #             }
#     #         }
#     #     ]
#     def get_site_menu(self):
#         return [
#             {
#                 'title': '自定义菜单',
#                 'icon': 'fa fa-bars',       # Font Awesome图标
#                 'menus':(
#                     {
#                         'title': 'Card表',
#                         'icon': 'fa fa-bug',
#
#                     },
#                     {
#                         'title': 'a发邮件',
#                         'icon': 'fa fa-envelope-o',
#
#                     }
#                 )
#             },
#             {
#                 'title': 'Bug统计',
#                 'icon': 'fa fa-bug',
#                 'menus':(
#                     {
#                         'title': 'Bug表',
#                         'icon': 'fa fa-bug',
#                         'url': "https://www.cnblogs.com/yoyoketang/"  # 自定义跳转列表
#
#                     },)
#             }
#
#         ]


class VideoSourceAdmin(object):
    list_display = ['name','create_time','update_time']
    search_fileds = ['name']
    list_filter = ['name']

class SectionAdmin(object):
    list_display = ['name','create_time','update_time','video']
    search_fileds = ['name','video']
    list_filter = ['name','video']

class TeacherAdmin(object):
    list_display = ['name','email','photo','introduction', 'create_time', 'update_time']
    search_fileds = ['name','email','introduction']
    list_filter = ['name','email']

class CourseAdmin(object):
    list_display = ['name','time','type','level','introduction','studey_num','create_time','update_time','section','teacher']
    search_fileds = ['name','time','type','level']
    list_filter = ['name','time','type','level']

    #dj39
    form_layout = (
        Fieldset(u'',
             Row('name','time','type'),
             Row('level','studey_num','teacher'),
             #模块不可以拖动
             css_class='unsort'
         ),
        Fieldset(('描述'),
             Row('introduction'),
        ),
        Fieldset(('章节'),
             Row('section'),
             #不显示区块的title名
             css_class='unsort no_title'
        ),
        #dj41
        TabHolder(
            Tab('标签1',
                Field('name',css_class="extra"),#输入框可以占一整行
                Field('time'),
                css_class='unsort'),
            Tab('标签2',
                Field('type','level'),
                Field('teacher'),
                )
        ),
    )


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Section,SectionAdmin)
xadmin.site.register(VideoSource,VideoSourceAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
# xadmin.site.register(views.CommAdminView,GlobalSettings)