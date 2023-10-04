frappe.listview_settings['Idea Concept'] = {

	get_indicator: function(doc) {
		if(doc.status==="Pending") {
			return [__("Pending"), "yellow", "status,=,Pending"];
		}
	}
};
