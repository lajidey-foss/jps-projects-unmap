# Copyright (c) 2023, Jide Olayinka and all Ardentpros contributors and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class IdeaConcept(Document):
    #def make_appointment(source_name, target_doc=None):
    pass


@frappe.whitelist()
def make_request_for_quotation(source_name, target_doc=None):
	def update_item(obj, target, source_parent):
		target.conversion_factor = 1.0

	doclist = get_mapped_doc(
		"Idea Concept",
		source_name,
		{
			"Idea Concept": {"doctype": "Request for Quotation"},
			"Idea Concept Item": {
				"doctype": "Request for Quotation Item",
				"field_map": [["name", "idea_concept_detail"], ["parent", "idea_concept"], ["uom", "uom"]],
				"postprocess": update_item,
			},
		},
		target_doc,
	)

	return doclist

@frappe.whitelist()
def make_project(source_name, target_doc=None):
	def postprocess(source, doc):
		doc.project_type = "Internal"
		doc.project_name = source.name
		doc.department = source.assign_department
	""" def update_item(source_doc, target, source_parent):
		target.t_warehouse = ""
  

	doc = get_mapped_doc(
		"Idea Concept",
		source_name,
		{
			"Idea Concept": {
				"doctype": "Project",
				"field_map": {
					"name": "idea_concept",
				},
			},
			"Idea Concept Item": {
				"doctype": "Project Item",
				"field_map": [["name", "idea_concept_detail"], ["parent", "idea_concept"], ["uom", "uom"]],
				"postprocess": update_item,
			},
		},
		target_doc,
	) """
	doc = get_mapped_doc(
		"Idea Concept",
		source_name,
		{
			"Idea Concept": {
				"doctype": "Project",
				"field_map": {
					"name": "idea_concept",
					
				},
			},
		},
		target_doc,
		postprocess,
	)

	return doc

@frappe.whitelist()
def make_meeting(source_name, target_doc=None):
	def postprocess(source, doc):
		doc.idea = source.name
		doc.title = source.title
  
	doc = get_mapped_doc(
		"Idea Concept",
		source_name,
		{
			"Idea Concept": {
				"doctype": "In Meeting",
				"field_map": {
					"name": "idea_concept",
					
				},
			},
		},
		target_doc,
		postprocess,
	)

	return doc
