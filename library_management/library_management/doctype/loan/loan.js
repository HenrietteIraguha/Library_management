// Copyright (c) 2026, Henriette and contributors
// For license information, please see license.txt

//frappe.ui.form.on("Loan", {
	//refresh(frm) {
       // frm,set_query("book", function() {
           // return{
                //filters:{status:"Available"}
        //    }
   //     })

//	},
 //});

 frappe.ui.form.on("loan", {
    validate(frm) {
        if(frm.doc.return_date < frm.doc.transaction_date ){
        frappe.throw("return date cannot be before transaction date");
        
    }
 }} )
