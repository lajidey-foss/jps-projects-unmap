from . import __version__ as app_version

app_name = "jpsage_projects_idea"
app_title = "Jpsage Projects Idea"
app_publisher = "Jide Olayinka and all Ardentpros contributors"
app_description = "Simple idea tracker to enable project ideas are follow through foretter "
app_email = "spryngmanaged@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jpsage_projects_idea/css/jpsage_projects_idea.css"
# app_include_js = "/assets/jpsage_projects_idea/js/jpsage_projects_idea.js"

# include js, css files in header of web template
# web_include_css = "/assets/jpsage_projects_idea/css/jpsage_projects_idea.css"
# web_include_js = "/assets/jpsage_projects_idea/js/jpsage_projects_idea.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "jpsage_projects_idea/public/scss/website"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "jpsage_projects_idea.utils.jinja_methods",
#	"filters": "jpsage_projects_idea.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "jpsage_projects_idea.install.before_install"
# after_install = "jpsage_projects_idea.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "jpsage_projects_idea.uninstall.before_uninstall"
# after_uninstall = "jpsage_projects_idea.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "jpsage_projects_idea.utils.before_app_install"
# after_app_install = "jpsage_projects_idea.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "jpsage_projects_idea.utils.before_app_uninstall"
# after_app_uninstall = "jpsage_projects_idea.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jpsage_projects_idea.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"jpsage_projects_idea.tasks.all"
#	],
#	"daily": [
#		"jpsage_projects_idea.tasks.daily"
#	],
#	"hourly": [
#		"jpsage_projects_idea.tasks.hourly"
#	],
#	"weekly": [
#		"jpsage_projects_idea.tasks.weekly"
#	],
#	"monthly": [
#		"jpsage_projects_idea.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "jpsage_projects_idea.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "jpsage_projects_idea.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "jpsage_projects_idea.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["jpsage_projects_idea.utils.before_request"]
# after_request = ["jpsage_projects_idea.utils.after_request"]

# Job Events
# ----------
# before_job = ["jpsage_projects_idea.utils.before_job"]
# after_job = ["jpsage_projects_idea.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"jpsage_projects_idea.auth.validate"
# ]
