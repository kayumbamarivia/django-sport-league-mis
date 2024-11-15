from django.contrib.auth.models import Permission, AbstractUser
from django.db import models
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coach', 'Coach'),
        ('player', 'Player'),
        ('fan', 'Fan'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_image = models.ImageField(upload_to='profile_images/', default='logo.jpg',blank=True, null=True)

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        db_table = "users"
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if self.role == 'admin':
            self._assign_permissions('admin_permissions')
        elif self.role == 'coach':
            self._assign_permissions('coach_permissions')
        elif self.role == 'player':
            self._assign_permissions('player_permissions')
        elif self.role == 'fan':
            self._assign_permissions('fan_permissions')

    def _assign_permissions(self, role_permissions):
        permissions_map = {
            'admin_permissions': ['can_edit_team', 'can_add_match', 'can_manage_users'],
            'coach_permissions': ['can_add_match', 'can_view_team'],
            'player_permissions': ['can_view_team'],
            'fan_permissions': ['can_view_match']
        }

        self.user_permissions.clear()
        for permission_codename in permissions_map.get(role_permissions, []):
            permission = Permission.objects.get(codename=permission_codename)
            self.user_permissions.add(permission)
