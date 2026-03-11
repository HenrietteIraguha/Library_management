import frappe

def new_user(doc, method):
    frappe.log_error(title="Library Hook", message=f"New user created:{doc.name}")