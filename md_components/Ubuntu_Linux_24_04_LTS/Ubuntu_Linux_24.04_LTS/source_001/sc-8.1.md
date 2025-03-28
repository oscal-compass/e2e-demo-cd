---
x-trestle-comp-def-rules:
  Ubuntu_Linux_24.04_LTS:
    - name: sshd_use_strong_ciphers
      description: sshd_use_strong_ciphers
    - name: sshd_use_strong_kex
      description: sshd_use_strong_kex
    - name: sshd_use_strong_macs
      description: sshd_use_strong_macs
x-trestle-param-values:
  sc-08.01_odp:
x-trestle-global:
  profile:
    title: NIST SP 800-53 Rev 5 Controls, selected
    href: profiles/NIST_800-53_rev5_selected/profile.json
  sort-id: sc-08.01
---

# sc-8.1 - \[\] Cryptographic Protection

## Control Statement

Implement cryptographic mechanisms to {{ insert: param, sc-08.01_odp }} during transmission.

## Control guidance

Encryption protects information from unauthorized disclosure and modification during transmission. Cryptographic mechanisms that protect the confidentiality and integrity of information during transmission include TLS and IPSec. Cryptographic mechanisms used to protect information integrity include cryptographic hash functions that have applications in digital signatures, checksums, and message authentication codes.

## Control assessment_objective

cryptographic mechanisms are implemented to {{ insert: param, sc-08.01_odp }} during transmission.

______________________________________________________________________

## What is the solution and how is it implemented?

<!-- For implementation status enter one of: implemented, partial, planned, alternative, not-applicable -->

<!-- Note that the list of rules under ### Rules: is read-only and changes will not be captured after assembly to JSON -->

<!-- Add control implementation description here for control: sc-8.1 -->

### Rules:

  - sshd_use_strong_ciphers
  - sshd_use_strong_kex
  - sshd_use_strong_macs

### Implementation Status: planned

______________________________________________________________________
