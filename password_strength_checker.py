"""
password_strength_checker.py

Scores a password on length (weighted heavily), character variety,
predictability (repeated/sequential runs), and rejects known-common
passwords outright.
"""

import getpass
from string import punctuation


COMMON_PASSWORDS = {
    "password", "password1", "password123", "123456", "12345678",
    "qwerty", "qwerty123", "letmein", "admin", "welcome",
    "iloveyou", "monkey", "dragon", "111111", "abc123",
    "passw0rd", "password1!", "p@ssword", "p@ssw0rd",
}


def check_password_strength(password):
    """
    Pure logic, no I/O -- testable on its own.
    Returns (score: int, max_score: int, reasons: list[str]).
    """
    reasons = []
    score = 0
    max_score = 7  # 3 for length + 4 for digit/upper/lower/special

    # Known-common password -> instant fail, nothing else matters
    if password.lower() in COMMON_PASSWORDS:
        reasons.append(
            "This password appears on common password lists. Choose something unpredictable."
        )
        return 0, max_score, reasons

    # Length weighted more heavily than any single character class
    length = len(password)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        reasons.append("Password is too short. Aim for 12+ characters -- length beats complexity.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        reasons.append("Add at least one digit.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        reasons.append("Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        reasons.append("Add at least one lowercase letter.")

    if any(char in punctuation for char in password):
        score += 1
    else:
        reasons.append("Add at least one special character.")

    if _has_repeated_or_sequential_run(password):
        reasons.append("Avoid repeated or sequential characters (e.g. 'aaa', '123', 'abc').")
        score = max(0, score - 1)

    return score, max_score, reasons


def _has_repeated_or_sequential_run(password, run_length=3):
    """Detect runs like 'aaa', '111', or ascending sequences like 'abc', '123'."""
    for i in range(len(password) - run_length + 1):
        window = password[i:i + run_length]
        if len(set(window)) == 1:
            return True
        codes = [ord(c) for c in window]
        if all(codes[j] + 1 == codes[j + 1] for j in range(len(codes) - 1)):
            return True
    return False


def rate_strength(score, max_score):
    """Convert numeric score to a human-readable rating."""
    ratio = score / max_score
    if ratio >= 0.85:
        return "STRONG"
    elif ratio >= 0.5:
        return "MEDIUM"
    else:
        return "TOO WEAK"


def main():
    password = getpass.getpass("Enter your password: ")  # doesn't echo to screen

    score, max_score, reasons = check_password_strength(password)

    for reason in reasons:
        print(f"- {reason}")

    rating = rate_strength(score, max_score)
    print(f"\nREMARKS -- Password is {rating} ({score}/{max_score})")


if __name__ == "__main__":
    main()