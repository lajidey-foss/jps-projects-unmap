from frappe import _


def get_data():
	return {
		"fieldname": "idea_concept",
		"non_standard_fieldnames": {
			"Project": "cost_center",
			"Request for Quotation": "opportunity",
			"In Meeting": "idea",
		},
		"transactions": [
			{"label": _("Shedules"), "items": ["In Meeting"]},
			{"label": _("Related (Work In Progress)"), "items": ["Request for Quotation"]},
			{"label": _("Reference (Work In Progress)"), "items": ["Project"]},
		],
	}