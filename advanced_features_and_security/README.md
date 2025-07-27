Django Groups & Permissions Setup Guide
This Django application uses custom permissions and user groups to control access to different actions on the Document model in the office app.

Model Permissions
These custom permissions are defined in the Document model:

class Document(models.Model):
    ...
    class Meta:
        permissions = [
            ("can_view", "Can view document"),
            ("can_create", "Can create document"),
            ("can_edit", "Can edit document"),
            ("can_delete", "Can delete document"),
        ]

User Groups
We use Django's built-in group system to organize users:

Group 	 Permissions
Admins	 can_view, can_create, can_edit, can_delete
Editors	 can_view, can_create, can_edit
Viewers	 can_view only

You can manage groups via the Django Admin at /admin/auth/group/.

Assigning Users to Groups
To assign a user to a group:

1. Log into Django Admin
2. Go to Users → Select a user
3. Scroll down to Groups
4. Add the user to one of: Admins, Editors, or Viewers
5. Ensure the user has Staff status so they can log in

Permission Enforcement in Views
We use Django’s @permission_required decorator to secure access to views.

Example usage:

@permission_required('office.can_edit', raise_exception=True)
def edit_document(request, pk):
    ...
can_view → Access list/detail views

can_create → Access create form

can_edit → Access edit form

can_delete → Access delete action


Manual Testing Checklist
Log in as different users and try to:

Action	Permission Needed	Should Be Allowed For
View documents	can_view	All groups
Create document	can_create	Editors, Admins
Edit document	can_edit	Editors, Admins
Delete document	can_delete	Admins only