from datetime import datetime
import pytest
from src import UserProfile

class TestProfileAgeCalculation:
    def test_exact_birthday(self):
        profile = UserProfile(
        "Test Age", 
        "testAge@gmail.com", 
        "SecurePass2@",
        "2000-11-8",
        {
            "city": "NewYork",
            "state": "NY",
            "country": "US"
        })
        profile.dob = "2000-11-8"
        reference_date = datetime(2026, 11, 8)
        expected_age = 26
        assert profile.get_age(reference_date = reference_date) == expected_age

if __name__ == "__main__":
    pytest.main([__file__, "-v"])