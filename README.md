## SaaS Project Management System (Django + DRF)

## Logic of Permissions:
The logic of permissions in this project is according to the role based permissions which is related to making sure that the users can only perform actions on which they have the control like based on the role they have in the organization. Now there are multiple permission classes in order to control the logic of accessing and changing the data.

1. SupAdmPermission:

. This permission class has the logic of checking like if the user has the control of a super admin in the given scenario.
. Now super admins are those who can do everything like creating the organizations, managing all the projects, then also controlling the teams and the tasks, etc.

2. OrgAdmPermission:

. This permission class has the logic of checking like if a user has the control of the admin of an organization for instance.
. Now the admins of organization are those who can manage everything happening inside their organization, and that can be related to the users, projects and teams, etc.

-- One point here is important the user of one organization should not be able to disturb the data of other organization.

3. TeamAdmPermission:

. This permission class has the logic of checking like if a user is the lead of the team.
. Now the team lead is the one who can manage/control the project and tasks of their teams like they can assign the tasks for example. 
. But one thing is important here which is they cannot control or affect the operations happenign at the top of an organization.

4. MemberAdmPermission:

. This permission has the logic of checking like if a given user is the member of a team or a project going on in the organization.
. Now the members has the permission to view the data and offcourse they also have the permission to work on the tasks which are assigned to them.
. And again like the team lead they also cant control or change whats hapenning at the top level of the organization, in reality they have even lesser power than the team leads.

5. ViewerAdmPermission:

. This permission has the logic of checking like if a given user has the ability to view the data only, like a manager for example who can only view the data as a viewer.
. So now the viewers are the ones who can only read the data, like the tasks, projects, etc, and they cannot make any changes, thats a important thing here.

6. TaskPermission:

. Now talking about the taskpermission then its a special one like a one which controls the permission logic for the tasks and subtasks.
. Further in this permission class the logic of control related permissions and the object related permissions is used together.

- For example:

# control	    authority
supadm	        has the authority on everyhting like create, view, delete, or update the data. 
orgadm	        has the authority on everything happening in their given organization.
teamadm	        has the authority on everything hapenning inside a time like managing the tasks in their team for instance.
memberadm	    has the authority on selected things like only working on the tasks which are given to them.
vieweradm	    has the authority on even more selected things like they can only view the data from the outside.

# The use of has_permission() and the has_object_permission() methods:
Now the use of these methods like:
. has_permission method is about -> allowing the general level access means using the permission logic even before entering the view.
. has_object_permission method is about -> allowing the access of object/instance like for example if a member is allowed to create or delete a task which is given to them.

