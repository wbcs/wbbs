from django.db import models

class User(models.Model):
  class Meta:
    db_table = 'table_user'
    ordering = ('-create_time',)

  phone_number = models.CharField(max_length=11, primary_key=True)
  name = models.CharField(max_length=50)
  avatar = models.CharField(max_length=200)

  create_time = models.DateTimeField(
    auto_now_add=True,
    verbose_name='创建时间'
  )
  modify_time = models.DateTimeField(
    auto_now=True,
    verbose_name='最后修改时间'
  )


class Friends(models.Model):
  class Meta:
    db_table = 'table_friends'
    ordering = ('-create_time',)
    
  phone_number = models.ForeignKey(User, on_delete=models.CASCADE)
  friend_phone_number = models.CharField(max_length=11)
  note_name = models.CharField(max_length=50)

  create_time = models.DateTimeField(
    auto_now_add=True,
    verbose_name='添加时间'
  )
  modify_time = models.DateTimeField(
    auto_now=True,
    verbose_name='最后修改时间'
  )


class Group(models.Model):
  class Meta:
    db_table = 'table_group'
    
  phone_number = models.ForeignKey(User, on_delete=models.CASCADE)
  owner_id = models.CharField(max_length=11, null=False)
  group_id = models.CharField(max_length=11, null=False)


class History(models.Model):
  class Meta:
    db_table = 'table_history'
    ordering = ('-create_time',)

  phone_number = models.ForeignKey(User, on_delete=models.CASCADE)
  to_people_or_group_id = models.CharField(max_length=11)
  is_to_people = models.BooleanField(default=True)
  content = models.CharField(max_length=10000)

  create_time = models.DateTimeField(
    auto_now_add=True,
    null=False,
    verbose_name='发送时间'
  )

