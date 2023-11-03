// Copyright (c) 2023, Jide Olayinka and all Ardentpros contributors and contributors
// For license information, please see license.txt

frappe.ui.form.on('In Meeting', {
	refresh: function(frm) {
		//set value of project
		if(frm.is_new()){ 
			//frappe.datetime.get_day_diff(frm.doc.due_date,frm.doc.posting_date)

			/* frm.set_value("idea","0c799dd441");
			cur_frm.refresh_fields("idear");
			console.log('operated here'); */
		}
		else {
			//
			/* cur_frm.set_query("idea", () => {
				return {
					filters: [
						["Idea Concept", "name", "=", "0c799dd441"]
					]
				}
			});
			console.log('happened here'); */
		}
		

	},
	date: function(frm) {
		//dif
		let diff = frappe.datetime.get_day_diff(frm.doc.posting_date, get_today());
		console.log('time dif is  :', diff);
	}
	
});
