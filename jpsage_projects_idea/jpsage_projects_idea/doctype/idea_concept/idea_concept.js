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

/*
project: function(frm) {
		//apply filter to task field on project field selected
		cur_frm.set_query("task", () => {
            return {
                filters: [
                    ["Task", "project", "=", cur_frm.doc.project]
                ]
            }
        })
		cur_frm.refresh_fields(["project", "task"])
	},
	},



	task: function(frm) {
		//set project if task is clicked first
		if(cur_frm.doc.project == null){
			frappe.db.get_value('Task', cur_frm.doc.task, 'project')
				.then(r => {
					cur_frm.set_value("project",r.message.project);

					cur_frm.refresh_fields(["task","project"])
				})

        }

	},
*/
/**
 * py mark complete : give error coming back to click it after over 30min
 * self.db_set("project", project.name)
		self.db_set("boarding_status", "Pending")
		self.reload()
	//
	//here
			
			frm.call("set_kras_and_rating_criteria", () => {
				frm.refresh_field("appraisal_kra");
				frm.refresh_field("feedback_ratings");
			});
 */
 
