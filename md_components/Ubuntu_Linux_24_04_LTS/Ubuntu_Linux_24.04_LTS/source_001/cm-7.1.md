---
x-trestle-comp-def-rules:
  Ubuntu_Linux_24.04_LTS:
    - name: accounts_password_warn_age_login_defs
      description: accounts_password_warn_age_login_defs
x-trestle-param-values:
  cm-7.1_prm_2:
  cm-07.01_odp.01:
  cm-07.01_odp.02:
  cm-07.01_odp.03:
  cm-07.01_odp.04:
  cm-07.01_odp.05:
  cm-07.01_odp.06:
x-trestle-global:
  profile:
    title: NIST SP 800-53 Rev 5 Controls, selected
    href: profiles/NIST_800-53_rev5_selected/profile.json
  sort-id: cm-07.01
---

# cm-7.1 - \[\] Periodic Review

## Control Statement

- \[(a)\] Review the system {{ insert: param, cm-07.01_odp.01 }} to identify unnecessary and/or nonsecure functions, ports, protocols, software, and services; and

- \[(b)\] Disable or remove {{ insert: param, cm-7.1_prm_2 }}.

## Control guidance

Organizations review functions, ports, protocols, and services provided by systems or system components to determine the functions and services that are candidates for elimination. Such reviews are especially important during transition periods from older technologies to newer technologies (e.g., transition from IPv4 to IPv6). These technology transitions may require implementing the older and newer technologies simultaneously during the transition period and returning to minimum essential functions, ports, protocols, and services at the earliest opportunity. Organizations can either decide the relative security of the function, port, protocol, and/or service or base the security decision on the assessment of other entities. Unsecure protocols include Bluetooth, FTP, and peer-to-peer networking.

## Control assessment_objective

- \[CM-07(01)(a)\] the system is reviewed {{ insert: param, cm-07.01_odp.01 }} to identify unnecessary and/or non-secure functions, ports, protocols, software, and services:

- \[CM-07(01)(b)\]

- \[CM-07(01)(b)[01]\]  {{ insert: param, cm-07.01_odp.02 }} deemed to be unnecessary and/or non-secure are disabled or removed;
- \[CM-07(01)(b)[02]\]  {{ insert: param, cm-07.01_odp.03 }} deemed to be unnecessary and/or non-secure are disabled or removed;
- \[CM-07(01)(b)[03]\]  {{ insert: param, cm-07.01_odp.04 }} deemed to be unnecessary and/or non-secure are disabled or removed;
- \[CM-07(01)(b)[04]\]  {{ insert: param, cm-07.01_odp.05 }} deemed to be unnecessary and/or non-secure is disabled or removed;
- \[CM-07(01)(b)[05]\]  {{ insert: param, cm-07.01_odp.06 }} deemed to be unnecessary and/or non-secure are disabled or removed.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: cm-7.1 -->

### Rules:

  - accounts_password_warn_age_login_defs

### Implementation Status: planned

______________________________________________________________________
