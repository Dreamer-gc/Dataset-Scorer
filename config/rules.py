# 1️⃣ Severity Thresholds

# All your threshold boundaries go here.

# Example (conceptually):

# Completeness thresholds
# Duplicate thresholds
# Outlier thresholds
# Validity thresholds
# Structural thresholds

# This prevents hardcoding numbers inside modules.

# 2️⃣ Spread Amplification Rules

# Your completeness logic uses:

# Spread escalation threshold

# When High + spread → Critical

# That rule belongs in config.

# Not inside completeness.py.

# 3️⃣ Weight Distribution

# Your scoring weights:

# Completeness = 0.30

# Validity = 0.25

# Outliers = 0.20

# Duplicates = 0.15

# Structural = 0.10

# These belong in config.

# So if later you change weight,
# you edit one place only.

# 4️⃣ Severity → Score Mapping

# Mapping like:

# Healthy → 95
# Low → 80
# Moderate → 65
# High → 50
# Critical → 30

# Put this in config.

# Don’t hardcode inside modules.

# 5️⃣ Risk Tier Score Mapping

# Numeric ranges for final classification:

# 85–100 → Low Risk
# 70–84 → Moderate Risk
# 50–69 → High Risk
# <50 → Critical Risk

# Keep these configurable.

# 6️⃣ Override Rule Settings

# Example:

# escalate_if_multiple_high = 2

# escalate_if_completeness_high = True

# critical_override_enabled = True

# Even these flags can go in config.

# This makes your system tunable.