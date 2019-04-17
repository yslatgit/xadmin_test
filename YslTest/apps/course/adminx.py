#coding:utf-8
import xadmin
from xadmin import views
from course.models import *


# class GlobalSettings(object):
#     """此方法不会用"""
#     def get_site_menu(self):
#         return [
#             {
#                 'title':'课程信息',
#                 'perm':self.get_model_perm(Course,'view'),
#                 'icon':'',
#                 'menus':{
#                     {'title':'视频信息','url':self.get_model_url(Course,'videosource')},
#                     {'title':'章节信息','url':self.get_model_url(Course,'section')},
#                     {'title':'讲师信息','url':self.get_model_url(Course,'teacher')},
#                     {'title':'课程信息','url':self.get_model_url(Course,'course')},
#                 }
#             }
#         ]

class VideoSourceAdmin(object):
    list_display = ['name','time','create_time','update_time']
    #展示的列表中的链接
    list_display_links = ['name','time']
    #搜索框--支持输入名称
    search_fields = ['name']
    #过滤器
    list_filter = ['name']
    #页面上可以编辑的字段
    list_editable = ['name']
    #排序
    ordering = ['update_time']
    #只读字段
    readonly_fields = ['time']
    # fieldsets = ['视频666',{'fields':('name','create_time','update_time')}] #不知道怎样使用

class SectionAdmin(object):
    list_display = ['name','create_time','update_time','video']
    search_fields = ['name','video']
    list_filter = ['name','video']
    # inlines = [VideoSourceAdmin]

class TeacherAdmin(object):
    list_display = ['name','email','introduction', 'create_time', 'update_time']
    search_fields = ['name','email','introduction']
    list_filter = ['name','email']

class CourseAdmin(object):
    list_display = ['name','time','type','level','introduction','studey_num','create_time','update_time','section','teacher']
    search_fields = ['name','time','type','level']
    list_filter = ['name','time','type','level']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Section,SectionAdmin)
xadmin.site.register(VideoSource,VideoSourceAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
# xadmin.site.register(views.CommAdminView,GlobalSettings)