# UAWA Rule Engine

## Evaluation order
1. Check applicable platform constraints and law.
2. Filter internal rules by task scope and effective/approved status.
3. Sort applicable rules by hierarchy, highest first.
4. Reject or narrow lower-level instructions that conflict with higher-level rules.
5. Pause on same-level conflicts, unclear status, or missing authority; request owner resolution.
6. Check permissions separately. Instructions do not grant access.

## Pseudocode

    evaluate(instruction, rules, platform_constraints):
      if violates(platform_constraints, instruction): return REJECTED
      for rule in sort_high_to_low(applicable(rules)):
        if conflicts(instruction, rule): return CONFLICT(rule.reference)
      if same_level_conflict(rules): return NEEDS_OWNER_APPROVAL
      if permission_missing(instruction): return BLOCKED
      return VALID

This is a decision procedure for participating agents, not a technical sandbox.