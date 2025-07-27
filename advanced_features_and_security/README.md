Django Groups & Permissions Setup Guide:

    This Django application uses custom permissions and user groups to control access to different actions on the Document model in the office app.

Model Permissions:

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

User Groups:

    We use Django's built-in group system to organize users:

    Group 	 Permissions
1. Admins	 can_view, can_create, can_edit, can_delete
2. Editors	 can_view, can_create, can_edit
3. Viewers	 can_view only

You can manage groups via the Django Admin at /admin/auth/group/.

Assigning Users to Groups:

    To assign a user to a group:

1. Log into Django Admin
2. Go to Users → Select a user
3. Scroll down to Groups
4. Add the user to one of: Admins, Editors, or Viewers
5. Ensure the user has Staff status so they can log in

Permission Enforcement in Views:

    We use Django’s @permission_required decorator to secure access to views.

Example usage:

@permission_required('office.can_edit', raise_exception=True)
def edit_document(request, pk):
    ...

1. can_view → Access list/detail views
2. can_create → Access create form
3. can_edit → Access edit form
4. can_delete → Access delete action


Manual Testing Checklist:

    Log in as different users and try to:

    Action	Permission Needed	Should Be Allowed For
1. View documents	can_view	All groups
2. Create document	can_create	Editors, Admins
3. Edit document	can_edit	Editors, Admins
4. Delete document	can_delete	Admins only