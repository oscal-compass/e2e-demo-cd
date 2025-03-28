---
x-trestle-comp-def-rules:
  Ubuntu_Linux_24.04_LTS:
    - name: package_sudo_installed
      description: package_sudo_installed
    - name: sshd_disable_root_login
      description: sshd_disable_root_login
    - name: sudo_add_use_pty
      description: sudo_add_use_pty
    - name: sudo_remove_no_authenticate
      description: sudo_remove_no_authenticate
    - name: sudo_require_authentication
      description: sudo_require_authentication
    - name: sudo_require_reauthentication
      description: sudo_require_reauthentication
x-trestle-param-values:
  ac-06.05_odp:
x-trestle-global:
  profile:
    title: NIST SP 800-53 Rev 5 Controls, selected
    href: profiles/NIST_800-53_rev5_selected/profile.json
  sort-id: ac-06.05
---

# ac-6.5 - \[\] Privileged Accounts

## Control Statement

Restrict privileged accounts on the system to {{ insert: param, ac-06.05_odp }}.

## Control guidance

Privileged accounts, including super user accounts, are typically described as system administrator for various types of commercial off-the-shelf operating systems. Restricting privileged accounts to specific personnel or roles prevents day-to-day users from accessing privileged information or privileged functions. Organizations may differentiate in the application of restricting privileged accounts between allowed privileges for local accounts and for domain accounts provided that they retain the ability to control system configurations for key parameters and as otherwise necessary to sufficiently mitigate risk.

## Control assessment_objective

privileged accounts on the system are restricted to {{ insert: param, ac-06.05_odp }}.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: ac-6.5 -->

### Rules:

  - package_sudo_installed
  - sshd_disable_root_login
  - sudo_add_use_pty
  - sudo_remove_no_authenticate
  - sudo_require_authentication
  - sudo_require_reauthentication

### Implementation Status: planned

______________________________________________________________________
