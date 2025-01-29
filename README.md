# Odoo-CRM_extension_01
Define a Boolean field named mani_contact for crm.lead Module / make limit for CRM-LEADS Tag creating by all users

# Custom CRM Lead Extension

این ماژول یک افزونه برای ماژول `crm` در Odoo است که قابلیت‌های جدیدی را برای مدیریت سرنخ‌ها و برچسب‌های CRM اضافه می‌کند.

## ویژگی‌ها

- **افزودن فیلد `Main Contact`**: 
  - این فیلد به مدل `crm.lead` اضافه شده و به کاربران اجازه می‌دهد مشخص کنند که یک سرنخ، مخاطب اصلی است.
- **کنترل دسترسی برای ایجاد برچسب‌های CRM**:
  - تنها کاربران دارای گروه `CRM Tag Manager` می‌توانند برچسب‌های جدید ایجاد کنند.
  
## نحوه نصب

1. این ماژول را در مسیر `addons` مربوط به Odoo خود قرار دهید.
2. از طریق **Apps** در Odoo، ماژول را فعال کنید یا دستور زیر را در ترمینال اجرا کنید:

   ```bash
   odoo -c /etc/odoo.conf -u custom_crm_lead_extension

