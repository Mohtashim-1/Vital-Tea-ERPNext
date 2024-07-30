// Copyright (c) 2024, mohtashim and contributors
// For license information, please see license.txt


frappe.ui.form.on('Item', {
	refresh(frm) {
        frappe.msgprint("testing")
        console.log('testing')
        const text = cur_frm.doc.item_code;
        const text1 = cur_frm.doc.item_group;
        const words = text.split(/[\s]+/);
        console.log(words)
        const words1 = text1.split(/[\s-]+/);
        const firstLetters = words.map(word => word.charAt(0).toUpperCase()).slice(2);
        const firstLetters1 = words1.map(word => word.charAt(0).toUpperCase());
       
        const result = firstLetters.join('');
        const result1 = firstLetters1.join("");
        console.log(result);
        console.log(result1);
        console.log("M-"+result1+"-"+result)
        var product_code = "M-" + result1 + "-" + result;
        frm.set_value('custom_product_code', product_code)
        // frm.save()

	}
})