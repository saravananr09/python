select
    ACD.dealer_name,
    AC.legal_name,
    ACD.dealer_tekion_id,
    ACD.account_dealer_id,
    ACD.dealer_tenant_id,
    DOEM.dealer_oem_id,
    ADG.dealer_group_name,
    ACM.campaign_name,
    concat(AO.email_id, ' ', AO.role) as Account_owner,
    AC.created_by,
    AC.created_at,
    ACD.first_signed_on,
    ACD.dealer_first_sell_implementation_status as first_sell_status,
    case
        when CA.influencer_level = "decision_maker" then CA.created_by
        else null
    end as auth_signers,
    ACP.dms_provider_name,
    ACP.dms_expiry,
    sum(DSC.count) over(partition by DSC.account_id) as staff_count,
    AC.account_size,
    DOEM.oem_name,
    DOEM.makes_name as makes,
    ACD.bill_to,
    concat(C.contact_first_name, ' ', C.contact_last_name) as contact_person,
    ACD.dealer_region,
    ACCOM.country,
    ACCOM.state,
    ACCOM.city
from
    account AC
    join account_dealer ACD on AC.account_id = ACD.account_id

    JOIN dealer_oem DOEM on ACD.account_id = DOEM.account_id

    JOIN account_communication ACCOM on ACD.account_id = ACCOM.account_id
    join account_provider ACP on AC.account_id = ACP.account_id
    join contact_account CA on AC.account_id = CA.account_id
    join contact C on C.contact_id = CA.contact_id
    JOIN dealer_staff_count DSC on AC.account_id = DSC.account_id
   
   /* poor condition */
    join account_dealer_group ADG
    join account_owner AO
    join account_campaign_map ACM
LIMIT
    1001


select account_id from account_dealer group by account_id having count(*) > 1;