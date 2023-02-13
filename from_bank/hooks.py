from . import __version__ as app_version

app_name = "from_bank"
app_title = "Loan From Bank Management"
app_publisher = "Ahmed Fourati"
app_description = "this App is to manage external loans from banks "
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ahmed.fourati@slnee.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/from_bank/css/from_bank.css"
# app_include_js = "/assets/from_bank/js/from_bank.js"

# include js, css files in header of web template
# web_include_css = "/assets/from_bank/css/from_bank.css"
# web_include_js = "/assets/from_bank/js/from_bank.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "from_bank/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "from_bank.install.before_install"
# after_install = "from_bank.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "from_bank.uninstall.before_uninstall"
# after_uninstall = "from_bank.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "from_bank.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"from_bank.tasks.all"
# 	],
# 	"daily": [
# 		"from_bank.tasks.daily"
# 	],
# 	"hourly": [
# 		"from_bank.tasks.hourly"
# 	],
# 	"weekly": [
# 		"from_bank.tasks.weekly"
# 	]
# 	"monthly": [
# 		"from_bank.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "from_bank.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "from_bank.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "from_bank.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"from_bank.auth.validate"
# ]

