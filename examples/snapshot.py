# This script uses LDLite to extract sample data from folio-snapshot.

import traceback
import ldlite
ld = ldlite.LDLite()
ld.connect_okapi(url='https://folio-snapshot-okapi.dev.folio.org',
                 tenant='diku',
                 user='diku_admin',
                 password='admin')

db = ld.connect_db(filename='ldlite.db')
# For PostgreSQL, use connect_db_postgresql() instead of connect_db():
# db = ld.connect_db_postgresql(dsn='dbname=ldlite host=localhost user=ldlite')

queries = [
        ('acquisitions_memberships', '/acquisitions-units-storage/memberships', 'cql.allRecords=1 sortby id'),
        ('acquisitions_units', '/acquisitions-units-storage/units', 'cql.allRecords=1 sortby id'),
        ('audit_circulation_logs', '/audit-data/circulation/logs', 'cql.allRecords=1 sortby id'),
        ('circulation_cancellation_reasons', '/cancellation-reason-storage/cancellation-reasons', 'cql.allRecords=1 sortby id'),
        ('circulation_check_ins', '/check-in-storage/check-ins', 'cql.allRecords=1 sortby id'),
        ('circulation_fixed_due_date_schedules', '/fixed-due-date-schedule-storage/fixed-due-date-schedules', 'cql.allRecords=1 sortby id'),
        ('circulation_loan_history', '/loan-storage/loan-history', 'cql.allRecords=1 sortby id'),
        ('circulation_loan_policies', '/loan-policy-storage/loan-policies', 'cql.allRecords=1 sortby id'),
        ('circulation_loans', '/loan-storage/loans', 'cql.allRecords=1 sortby id'),
        ('circulation_patron_action_sessions', '/patron-action-session-storage/patron-action-sessions', 'cql.allRecords=1 sortby id'),
        ('circulation_patron_notice_policies', '/patron-notice-policy-storage/patron-notice-policies', 'cql.allRecords=1 sortby id'),
        ('circulation_request_policies', '/request-policy-storage/request-policies', 'cql.allRecords=1 sortby id'),
        ('circulation_request_preference', '/request-preference-storage/request-preference', 'cql.allRecords=1 sortby id'),
        ('circulation_requests', '/request-storage/requests', 'cql.allRecords=1 sortby id'),
        ('circulation_scheduled_notices', '/scheduled-notice-storage/scheduled-notices', 'cql.allRecords=1 sortby id'),
        ('circulation_staff_slips', '/staff-slips-storage/staff-slips', 'cql.allRecords=1 sortby id'),
        ('configuration_entries', '/configurations/entries', 'cql.allRecords=1 sortby id'),
        ('course_copyrightstatuses', '/coursereserves/copyrightstatuses', 'cql.allRecords=1 sortby id'),
        ('course_courselistings', '/coursereserves/courselistings', 'cql.allRecords=1 sortby id'),
        ('course_courses', '/coursereserves/courses', 'cql.allRecords=1 sortby id'),
        ('course_coursetypes', '/coursereserves/coursetypes', 'cql.allRecords=1 sortby id'),
        ('course_departments', '/coursereserves/departments', 'cql.allRecords=1 sortby id'),
        ('course_processingstatuses', '/coursereserves/processingstatuses', 'cql.allRecords=1 sortby id'),
        ('course_reserves', '/coursereserves/reserves', 'cql.allRecords=1 sortby id'),
        ('course_roles', '/coursereserves/roles', 'cql.allRecords=1 sortby id'),
        ('course_terms', '/coursereserves/terms', 'cql.allRecords=1 sortby id'),
        ('email_email', '/email', 'cql.allRecords=1 sortby id'),
        ('erm_contacts', '/erm/contacts', 'cql.allRecords=1 sortby id'),
        ('erm_counter_reports', '/counter-reports', 'cql.allRecords=1 sortby id'),
        ('erm_entitlements', '/erm/entitlements', 'cql.allRecords=1 sortby id'),
        ('erm_files', '/erm/files', 'cql.allRecords=1 sortby id'),
        ('erm_licenses', '/licenses/licenses', 'cql.allRecords=1 sortby id'),
        ('erm_org', '/erm/org', 'cql.allRecords=1 sortby id'),
        ('erm_refdata', '/erm/refdata', 'cql.allRecords=1 sortby id'),
        ('erm_resource', '/erm/resource', 'cql.allRecords=1 sortby id'),
        ('erm_usage_data_providers', '/usage-data-providers', 'cql.allRecords=1 sortby id'),
        ('feesfines_accounts', '/accounts', 'cql.allRecords=1 sortby id'),
        ('feesfines_comments', '/comments', 'cql.allRecords=1 sortby id'),
        ('feesfines_feefineactions', '/feefineactions', 'cql.allRecords=1 sortby id'),
        ('feesfines_feefines', '/feefines', 'cql.allRecords=1 sortby id'),
        ('feesfines_lost_item_fees_policies', '/lost-item-fees-policies', 'cql.allRecords=1 sortby id'),
        ('feesfines_manualblocks', '/manualblocks', 'cql.allRecords=1 sortby id'),
        ('feesfines_overdue_fines_policies', '/overdue-fines-policies', 'cql.allRecords=1 sortby id'),
        ('feesfines_owners', '/owners', 'cql.allRecords=1 sortby id'),
        ('feesfines_payments', '/payments', 'cql.allRecords=1 sortby id'),
        ('feesfines_refunds', '/refunds', 'cql.allRecords=1 sortby id'),
        ('feesfines_transfer_criterias', '/transfer-criterias', 'cql.allRecords=1 sortby id'),
        ('feesfines_transfers', '/transfers', 'cql.allRecords=1 sortby id'),
        ('feesfines_waives', '/waives', 'cql.allRecords=1 sortby id'),
        ('finance_budgets', '/finance-storage/budgets', 'cql.allRecords=1 sortby id'),
        ('finance_expense_classes', '/finance-storage/expense-classes', 'cql.allRecords=1 sortby id'),
        ('finance_fiscal_years', '/finance-storage/fiscal-years', 'cql.allRecords=1 sortby id'),
        ('finance_funds', '/finance-storage/funds', 'cql.allRecords=1 sortby id'),
        ('finance_fund_types', '/finance-storage/fund-types', 'cql.allRecords=1 sortby id'),
        ('finance_group_fund_fiscal_years', '/finance-storage/group-fund-fiscal-years', 'cql.allRecords=1 sortby id'),
        ('finance_groups', '/finance-storage/groups', 'cql.allRecords=1 sortby id'),
        ('finance_ledgers', '/finance-storage/ledgers', 'cql.allRecords=1 sortby id'),
        ('finance_transactions', '/finance-storage/transactions', 'cql.allRecords=1 sortby id'),
        ('inventory_alternative_title_types', '/alternative-title-types', 'cql.allRecords=1 sortby id'),
        ('inventory_call_number_types', '/call-number-types', 'cql.allRecords=1 sortby id'),
        ('inventory_campuses', '/location-units/campuses', 'cql.allRecords=1 sortby id'),
        ('inventory_classification_types', '/classification-types', 'cql.allRecords=1 sortby id'),
        ('inventory_contributor_name_types', '/contributor-name-types', 'cql.allRecords=1 sortby id'),
        ('inventory_contributor_types', '/contributor-types', 'cql.allRecords=1 sortby id'),
        ('inventory_electronic_access_relationships', '/electronic-access-relationships', 'cql.allRecords=1 sortby id'),
        ('inventory_holdings', '/holdings-storage/holdings', 'cql.allRecords=1 sortby id'),
        ('inventory_holdings_note_types', '/holdings-note-types', 'cql.allRecords=1 sortby id'),
        ('inventory_holdings_sources', '/holdings-sources', 'cql.allRecords=1 sortby id'),
        ('inventory_holdings_types', '/holdings-types', 'cql.allRecords=1 sortby id'),
        ('inventory_identifier_types', '/identifier-types', 'cql.allRecords=1 sortby id'),
        ('inventory_ill_policies', '/ill-policies', 'cql.allRecords=1 sortby id'),
        ('inventory_instance_formats', '/instance-formats', 'cql.allRecords=1 sortby id'),
        ('inventory_instance_note_types', '/instance-note-types', 'cql.allRecords=1 sortby id'),
        ('inventory_instance_relationships', '/instance-storage/instance-relationships', 'cql.allRecords=1 sortby id'),
        ('inventory_instance_relationship_types', '/instance-relationship-types', 'cql.allRecords=1 sortby id'),
        ('inventory_instances', '/instance-storage/instances', 'cql.allRecords=1 sortby id'),
        ('inventory_instance_statuses', '/instance-statuses', 'cql.allRecords=1 sortby id'),
        ('inventory_instance_types', '/instance-types', 'cql.allRecords=1 sortby id'),
        ('inventory_institutions', '/location-units/institutions', 'cql.allRecords=1 sortby id'),
        ('inventory_item_damaged_statuses', '/item-damaged-statuses', 'cql.allRecords=1 sortby id'),
        ('inventory_item_note_types', '/item-note-types', 'cql.allRecords=1 sortby id'),
        ('inventory_items', '/item-storage/items', 'cql.allRecords=1 sortby id'),
        ('inventory_libraries', '/location-units/libraries', 'cql.allRecords=1 sortby id'),
        ('inventory_loan_types', '/loan-types', 'cql.allRecords=1 sortby id'),
        ('inventory_locations', '/locations', 'cql.allRecords=1 sortby id'),
        ('inventory_material_types', '/material-types', 'cql.allRecords=1 sortby id'),
        ('inventory_modes_of_issuance', '/modes-of-issuance', 'cql.allRecords=1 sortby id'),
        ('inventory_nature_of_content_terms', '/nature-of-content-terms', 'cql.allRecords=1 sortby id'),
        ('inventory_service_points', '/service-points', 'cql.allRecords=1 sortby id'),
        ('inventory_service_points_users', '/service-points-users', 'cql.allRecords=1 sortby id'),
        ('inventory_statistical_codes', '/statistical-codes', 'cql.allRecords=1 sortby id'),
        ('inventory_statistical_code_types', '/statistical-code-types', 'cql.allRecords=1 sortby id'),
        ('invoice_invoices', '/invoice-storage/invoices', 'cql.allRecords=1 sortby id'),
        ('invoice_lines', '/invoice-storage/invoice-lines', 'cql.allRecords=1 sortby id'),
        ('invoice_voucher_lines', '/voucher-storage/voucher-lines', 'cql.allRecords=1 sortby id'),
        ('invoice_vouchers', '/voucher-storage/vouchers', 'cql.allRecords=1 sortby id'),
        ('notes', '/notes', 'cql.allRecords=1 sortby id'),
        ('organization_addresses', '/organizations-storage/addresses', 'cql.allRecords=1 sortby id'),
        ('organization_categories', '/organizations-storage/categories', 'cql.allRecords=1 sortby id'),
        ('organization_contacts', '/organizations-storage/contacts', 'cql.allRecords=1 sortby id'),
        ('organization_emails', '/organizations-storage/emails', 'cql.allRecords=1 sortby id'),
        ('organization_interfaces', '/organizations-storage/interfaces', 'cql.allRecords=1 sortby id'),
        ('organization_organizations', '/organizations-storage/organizations', 'cql.allRecords=1 sortby id'),
        ('organization_phone_numbers', '/organizations-storage/phone-numbers', 'cql.allRecords=1 sortby id'),
        ('organization_urls', '/organizations-storage/urls', 'cql.allRecords=1 sortby id'),
        ('po_alerts', '/orders-storage/alerts', 'cql.allRecords=1 sortby id'),
        ('po_lines', '/orders-storage/po-lines', 'cql.allRecords=1 sortby id'),
        ('po_order_invoice_relns', '/orders-storage/order-invoice-relns', 'cql.allRecords=1 sortby id'),
        ('po_order_templates', '/orders-storage/order-templates', 'cql.allRecords=1 sortby id'),
        ('po_pieces', '/orders-storage/pieces', 'cql.allRecords=1 sortby id'),
        ('po_purchase_orders', '/orders-storage/purchase-orders', 'cql.allRecords=1 sortby id'),
        ('po_receiving_history', '/orders-storage/receiving-history', 'cql.allRecords=1 sortby id'),
        ('po_reporting_codes', '/orders-storage/reporting-codes', 'cql.allRecords=1 sortby id'),
        ('user_addresstypes', '/addresstypes', 'cql.allRecords=1 sortby id'),
        ('user_departments', '/departments', 'cql.allRecords=1 sortby id'),
        ('user_groups', '/groups', 'cql.allRecords=1 sortby id'),
        ('user_proxiesfor', '/proxiesfor', 'cql.allRecords=1 sortby id'),
        ('user_users', '/users', 'cql.allRecords=1 sortby id'),
    ]

tables = []
for q in queries:
    try:
        t = ld.query(table=q[0], path=q[1], query=q[2])
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
    tables += t
print()
print('Tables:')
for t in tables:
    print(t)
print('('+str(len(tables))+' tables)')

