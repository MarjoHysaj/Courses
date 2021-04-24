from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if 'name' not in postData or len(postData['name']) < 2:
            errors["name"] = "Title should be at least 2 characters."
        if 'desc' not in postData or len(postData['desc']) < 2:
            errors["desc"] = "Network should be at least 2 characters."
        return errors

class Desc(models.Model):
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.OneToOneField(Desc, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    text = models.TextField()
    course = models.ForeignKey(Course, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)