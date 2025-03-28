---
x-trestle-comp-def-rules:
  Ubuntu_Linux_24.04_LTS:
    - name: accounts_passwords_pam_faillock_deny
      description: accounts_passwords_pam_faillock_deny
    - name: accounts_passwords_pam_faillock_enabled
      description: accounts_passwords_pam_faillock_enabled
    - name: accounts_passwords_pam_faillock_root_unlock_time
      description: accounts_passwords_pam_faillock_root_unlock_time
    - name: accounts_passwords_pam_faillock_unlock_time
      description: accounts_passwords_pam_faillock_unlock_time
x-trestle-param-values:
  ac-02.01_odp:
x-trestle-global:
  profile:
    title: NIST SP 800-53 Rev 5 Controls, selected
    href: profiles/NIST_800-53_rev5_selected/profile.json
  sort-id: ac-02.01
---

# ac-2.1 - \[\] Automated System Account Management

## Control Statement

Support the management of system accounts using {{ insert: param, ac-02.01_odp }}.

## Control guidance

Automated system account management includes using automated mechanisms to create, enable, modify, disable, and remove accounts; notify account managers when an account is created, enabled, modified, disabled, or removed, or when users are terminated or transferred; monitor system account usage; and report atypical system account usage. Automated mechanisms can include internal system functions and email, telephonic, and text messaging notifications.

## Control assessment_objective

the management of system accounts is supported using {{ insert: param, ac-02.01_odp }}.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: ac-2.1 -->

### Rules:

  - accounts_passwords_pam_faillock_deny
  - accounts_passwords_pam_faillock_enabled
  - accounts_passwords_pam_faillock_root_unlock_time
  - accounts_passwords_pam_faillock_unlock_time

### Implementation Status: planned

______________________________________________________________________
