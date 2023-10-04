// Copyright (c) 2023, Jide Olayinka and all Ardentpros contributors and contributors
// For license information, please see license.txt

frappe.ui.form.on('Idea Concept', {
	refresh: function(frm) {
		if(!frm.is_new()) {
			// Quotation or [Request for Quote]
			frm.add_custom_button(__('Meeting'),
				function() {
					frm.trigger("make_meeting")
				}, __('Create'));	
			frm.add_custom_button(__('Request For Quotation[WIP]'),
				function() {
					frm.trigger("make_request_for_quotation")
				}, __('Create'));
			
				// project
			//frm.add_custom_button(__('Project'), () => make_project(), __('Create'));
			frm.add_custom_button(__('Project [WIP]'), function(){
				frm.trigger("make_project")
			}, __('Create'));
			
		}

	},

	make_request_for_quotation: function(frm) {
		frappe.model.open_mapped_doc({
			method: "jpsage_projects_idea.jpsage_projects_idea.doctype.idea_concept.idea_concept.make_request_for_quotation",
			frm: frm
		})
	},
	make_project: function(frm) {
		frappe.model.open_mapped_doc({
			method: "jpsage_projects_idea.jpsage_projects_idea.doctype.idea_concept.idea_concept.make_project",
			frm: frm
		})
	},
	make_meeting: function(frm) {
		frappe.model.open_mapped_doc({
			method: "jpsage_projects_idea.jpsage_projects_idea.doctype.idea_concept.idea_concept.make_meeting",
			frm: frm
		})
	},
});
 
