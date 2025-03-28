---
x-trestle-comp-def-rules:
  Ubuntu_Linux_24.04_LTS:
    - name: accounts_tmout
      description: accounts_tmout
x-trestle-param-values:
  ac-02.05_odp:
x-trestle-global:
  profile:
    title: NIST SP 800-53 Rev 5 Controls, selected
    href: profiles/NIST_800-53_rev5_selected/profile.json
  sort-id: ac-02.05
---

# ac-2.5 - \[\] Inactivity Logout

## Control Statement

Require that users log out when {{ insert: param, ac-02.05_odp }}.

## Control guidance

Inactivity logout is behavior- or policy-based and requires users to take physical action to log out when they are expecting inactivity longer than the defined period. Automatic enforcement of inactivity logout is addressed by [AC-11](#ac-11).

## Control assessment_objective

users are required to log out when {{ insert: param, ac-02.05_odp }}.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: ac-2.5 -->

### Rules:

  - accounts_tmout

### Implementation Status: planned

______________________________________________________________________
