import pytest
from src import UserProfile

class TestPasswordValidation:
    def test_start_lowercase_uppercase_middle(self):
        assert UserProfile.valid_password("password1A!") is True

    def test_starts_with_digit(self):
        assert UserProfile.valid_password("1PasswordA!") is True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])