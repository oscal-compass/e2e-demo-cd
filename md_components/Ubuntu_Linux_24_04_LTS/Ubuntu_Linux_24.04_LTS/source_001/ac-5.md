---
x-trestle-comp-def-rules:
  Ubuntu_Linux_24.04_LTS:
    - name: accounts_password_pam_unix_enabled
      description: accounts_password_pam_unix_enabled
    - name: accounts_root_gid_zero
      description: accounts_root_gid_zero
    - name: accounts_umask_etc_bashrc
      description: accounts_umask_etc_bashrc
    - name: accounts_umask_etc_login_defs
      description: accounts_umask_etc_login_defs
    - name: accounts_umask_etc_profile
      description: accounts_umask_etc_profile
    - name: accounts_umask_root
      description: accounts_umask_root
    - name: ensure_pam_wheel_group_empty
      description: ensure_pam_wheel_group_empty
    - name: ensure_root_access_controlled
      description: ensure_root_access_controlled
    - name: file_groupowner_sshd_config
      description: file_groupowner_sshd_config
    - name: file_owner_sshd_config
      description: file_owner_sshd_config
    - name: file_permissions_sshd_config
      description: file_permissions_sshd_config
    - name: file_permissions_sshd_private_key
      description: file_permissions_sshd_private_key
    - name: file_permissions_sshd_pub_key
      description: file_permissions_sshd_pub_key
    - name: groups_no_zero_gid_except_root
      description: groups_no_zero_gid_except_root
    - name: no_invalid_shell_accounts_unlocked
      description: no_invalid_shell_accounts_unlocked
    - name: no_shelllogin_for_systemaccounts
      description: no_shelllogin_for_systemaccounts
    - name: sshd_limit_user_access
      description: sshd_limit_user_access
    - name: use_pam_wheel_group_for_su
      description: use_pam_wheel_group_for_su
x-trestle-param-values:
  ac-05_odp:
x-trestle-global:
  profile:
    title: NIST SP 800-53 Rev 5 Controls, selected
    href: profiles/NIST_800-53_rev5_selected/profile.json
  sort-id: ac-05
---

# ac-5 - \[\] Separation of Duties

## Control Statement

- \[a.\] Identify and document {{ insert: param, ac-05_odp }} ; and

- \[b.\] Define system access authorizations to support separation of duties.

## Control guidance

Separation of duties addresses the potential for abuse of authorized privileges and helps to reduce the risk of malevolent activity without collusion. Separation of duties includes dividing mission or business functions and support functions among different individuals or roles, conducting system support functions with different individuals, and ensuring that security personnel who administer access control functions do not also administer audit functions. Because separation of duty violations can span systems and application domains, organizations consider the entirety of systems and system components when developing policy on separation of duties. Separation of duties is enforced through the account management activities in [AC-2](#ac-2) , access control mechanisms in [AC-3](#ac-3) , and identity management activities in [IA-2](#ia-2), [IA-4](#ia-4) , and [IA-12](#ia-12).

## Control assessment_objective

- \[AC-05a.\]  {{ insert: param, ac-05_odp }} are identified and documented;

- \[AC-05b.\] system access authorizations to support separation of duties are defined.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: ac-5 -->

### Rules:

  - accounts_password_pam_unix_enabled
  - accounts_root_gid_zero
  - accounts_umask_etc_bashrc
  - accounts_umask_etc_login_defs
  - accounts_umask_etc_profile
  - accounts_umask_root
  - ensure_pam_wheel_group_empty
  - ensure_root_access_controlled
  - file_groupowner_sshd_config
  - file_owner_sshd_config
  - file_permissions_sshd_config
  - file_permissions_sshd_private_key
  - file_permissions_sshd_pub_key
  - groups_no_zero_gid_except_root
  - no_invalid_shell_accounts_unlocked
  - no_shelllogin_for_systemaccounts
  - sshd_limit_user_access
  - use_pam_wheel_group_for_su

### Implementation Status: planned

______________________________________________________________________
