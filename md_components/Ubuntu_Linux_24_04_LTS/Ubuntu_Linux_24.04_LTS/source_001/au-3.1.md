---
x-trestle-comp-def-rules:
  Ubuntu_Linux_24.04_LTS:
    - name: sshd_set_max_auth_tries
      description: sshd_set_max_auth_tries
    - name: sudo_custom_logfile
      description: sudo_custom_logfile
x-trestle-param-values:
  au-03.01_odp:
x-trestle-global:
  profile:
    title: NIST SP 800-53 Rev 5 Controls, selected
    href: profiles/NIST_800-53_rev5_selected/profile.json
  sort-id: au-03.01
---

# au-3.1 - \[\] Additional Audit Information

## Control Statement

Generate audit records containing the following additional information: {{ insert: param, au-03.01_odp }}.

## Control guidance

The ability to add information generated in audit records is dependent on system functionality to configure the audit record content. Organizations may consider additional information in audit records including, but not limited to, access control or flow control rules invoked and individual identities of group account users. Organizations may also consider limiting additional audit record information to only information that is explicitly needed for audit requirements. This facilitates the use of audit trails and audit logs by not including information in audit records that could potentially be misleading, make it more difficult to locate information of interest, or increase the risk to individuals' privacy.

## Control assessment_objective

generated audit records contain the following {{ insert: param, au-03.01_odp }}.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: au-3.1 -->

### Rules:

  - sshd_set_max_auth_tries
  - sudo_custom_logfile

### Implementation Status: planned

______________________________________________________________________
