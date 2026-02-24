# Copyright (c) 2026, Henriette and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Loan(Document):
	# def before_save(self):
	# 	now = nowdate()
	# 	if not self.transaction_date:
	# 		self.transaction_date = now
	
	def before_submit(self):
		loan_book = self.book
		book = frappe.get_doc("Book", loan_book)
		book.status = "Rented"
		book.save()

	def on_cancel(self):
		loan_book = self.book
		book = frappe.get_doc("Book", loan_book)
		book.status = "Available"
		book.save()

