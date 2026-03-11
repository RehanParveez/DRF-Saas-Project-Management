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


## Addition of Transaction.atomic:

# What is the use of @transaction.atomic?

. The transaction.atomic used in the form of a decorator is a simple is a django logic feature which helps makeing the group of database operations very clear like if all the steps are successful than -> everything is saved in the database, but if any of the group of steps fails -> then nothing is saved in the database.

# Its use in the taskviewset:

In the taskviewset first i simply imported the transaction and then by using the transaction.atomic decorator added a method of create which simply saves a new task, then its related subtasks and then also handles the activity of creating all of this as well. 
. so this create method basically validates the data first and then it creates the task and any subtasks related to it and finally it validates the the record of any activity which happened.

-- Outside this create method used the @transaction.atomic decorator over the already existing actions in the taskviewset like task, comment, status, and completed.

-- So this transaction.atomic logic is helping in all these related multiple operations like creating a task with its subtasks or updating the status, methods like these they work togetherr and as per the defination of the transaction.atomic decorator:

. Like if any step fails, then no half progress is saved this thing mainly it is preventing in the taskviewset.


## Addition of the Signals Logic:
In this project i added two signals in the tasks app, which are:

# creating_task:
. This creating task signal first creating task signal has the logic of running automatically like whenever a new task is created/updated,
. Furhter tt is about checking like whether the specific task is new or any previous task is just been updated,
. Next it has the logic of createing a simple record in the table of Activity, which is a model in the notifications app, and this record will show the user and the work performed, means which user performed which specific work.

# comment_notification:
. Next this comment_notification signal has the logic of running automatically similar to last signal but in this the difference is it will run whenever a new comment is added inside the given task,
. Furhter it will give a simple notification for showing like who is the creator of the task and then next it gives the notification which has the information related to like which specific person added the comment and which task it was in which he added the comment.

## Addition of the Middleware Logic:
-- Next i did the addition of the middleware logic in the project level folder by creating a middleware class:

# ApiRequestMiddleware:
. This middleware class of ApiRequestMiddleware has the logic like it will run on the every API request which is made by an authenticated user,
. Further it records some specific details like about the user, HTTP methods like GET, POST, etc, and also about the requested path of the API, and the each request it gives it is going to be saved in the apirequest table present in the database, which was generated after i added hte apirequest model in the notifications app.


## Use of Caching logic:
. In this project for practice the addition of the caching logic is about the addition of the caching through redis for the frequently called on endpoints like for the taskviewset and the projectviewset.

. Firstly i have added simple list methods in both these viewsets which according to the logic first check whether the data for the user is in the cache or not,

. Then if the cached data is present then it is directly returned like without writing the extra queries to get the data from the database,

. And in case if this not the reality like the cached data is not present then the data is extracted from the database, it is serialized and after doing this it is stored in the redis refernce database so that in the future requests can be made to get the data from here which,

. then next after this the automatic clearing of the cache is also done in the create methods of these both viewsets, like whenever a new task or a project is added, then the old cached data is cleared.


## Use of reporting APIs:

. In this project the addition of the reporting apis is related to creating the endpoints which are providing the important statistics related to tasks, projects, and work of a team and which shows the progress and the productivity of a team.

- the following are the added actions in the reportviewset:

# 1. completed_task:
. This first action which is completed task it helps in calculating the count like how many tasks have been completed by the each user. in it the use of filter and the annotate methods is done in order to count the tasks with their status which is done for the every assignee in project, and after doing this it simply returns the result.

# 2. progress:
. Then the second action which is progress, now it gives the output related to the progress of a specific project. in this method the logic of counting the total tasks and completed tasks of this project is present, further it also calculates the percentage of the completed tasks.

# 3. work:
. Next the third action which is work it simply shows the performance of the team like how much work is done by the given team and in it the logic of giving all the users alongside their number of total tasks and completed the tasks is present.

# 4. project_tasks:
. Now the fourth action which is project tasks it calculates and shows the total number of tasks related to specific project. In this action with the use of raw sql the logic of joining the task and the project tables is done, also it counts the number of the tasks which are grouped by a given project and after doing this it gives the output of showing the each project with its related number of total tasks.

