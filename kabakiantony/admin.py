from django.contrib import admin


class KabakiAntonyAdmin(admin.AdminSite):
    site_header = 'Kabaki Antony Administration'
    site_title = 'Kabaki Antony Admin'
    index_title = 'Kabaki Antony Admin'
    site_url = None


ka_admin_site = KabakiAntonyAdmin(name='admin')
