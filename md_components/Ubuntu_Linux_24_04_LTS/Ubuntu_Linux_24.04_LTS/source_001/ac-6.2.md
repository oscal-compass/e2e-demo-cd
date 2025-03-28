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
  ac-06.02_odp:
x-trestle-global:
  profile:
    title: NIST SP 800-53 Rev 5 Controls, selected
    href: profiles/NIST_800-53_rev5_selected/profile.json
  sort-id: ac-06.02
---

# ac-6.2 - \[\] Non-privileged Access for Nonsecurity Functions

## Control Statement

Require that users of system accounts (or roles) with access to {{ insert: param, ac-06.02_odp }} use non-privileged accounts or roles, when accessing nonsecurity functions.

## Control guidance

Requiring the use of non-privileged accounts when accessing nonsecurity functions limits exposure when operating from within privileged accounts or roles. The inclusion of roles addresses situations where organizations implement access control policies, such as role-based access control, and where a change of role provides the same degree of assurance in the change of access authorizations for the user and the processes acting on behalf of the user as would be provided by a change between a privileged and non-privileged account.

## Control assessment_objective

users of system accounts (or roles) with access to {{ insert: param, ac-06.02_odp }} are required to use non-privileged accounts or roles when accessing non-security functions.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: ac-6.2 -->

### Rules:

  - package_sudo_installed
  - sshd_disable_root_login
  - sudo_add_use_pty
  - sudo_remove_no_authenticate
  - sudo_require_authentication
  - sudo_require_reauthentication

### Implementation Status: planned

______________________________________________________________________
