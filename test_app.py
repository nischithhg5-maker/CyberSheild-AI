    
# @title
import unittest


def calculate_risk(text):
    text = text.lower()
    score = 0

    warning_words = [
        "otp",
        "password",
        "urgent",
        "verify your account",
        "prize",
        "bank details",
        "click here",
    ]

    for word in warning_words:
        if word in text:
            score += 10

    if "http://" in text or "https://" in text:
        score += 20

    return min(score, 100)


class TestCyberShield(unittest.TestCase):

    def test_otp_warning(self):
        self.assertGreater(
            calculate_risk("Share your OTP urgently"),
            0
        )

    def test_suspicious_link(self):
        self.assertGreater(
            calculate_risk("Verify your account https://example.com"),
            0
        )

    def test_empty_message(self):
        self.assertEqual(calculate_risk(""), 0)

    def test_risk_never_exceeds_100(self):
        self.assertLessEqual(
            calculate_risk("OTP password urgent prize " * 20),
            100
        )


if __name__ == "__main__":
    # Run the tests programmatically to avoid any interactive/notebook argv conflicts
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCyberShield)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
