from django.contrib import admin
from .models import User, Group, groupListNode, groupLinkedList, userTreeNode, userBinarySearchTree

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('picture', 'name', 'id', 'description', 'password', 'theme', 'language', 'groupsList')

@admin.register(groupListNode)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('data', 'next')

@admin.register(groupLinkedList)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('head', )

@admin.register(userTreeNode)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('data', 'left', 'right')

@admin.register(userBinarySearchTree)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('root', )
    
@admin.register(Group)
class userAdmin(admin.ModelAdmin):
    readonly_fields = ('picture', 'name', 'id', 'description', 'adminList', 'membersList')

# Register your models here.
