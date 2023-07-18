#!/usr/bin/python3
"""Unittest module for review()

    1. to_dict
    2. save
    3. serialization and deserialization
"""

import models
import unittest
from datetime import datetime
import time
from models.review import Review
from models.base_model import BaseModel
from unittest.mock import patch
import json
from models import storage


class TestReview_method(unittest.TestCase):
    """Implementations
    """

    def setUp(self):
        self.review = Review()

    def test_review_inherits_from_base_model(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_to_dict_returns_dictionary(self):
        result = self.review.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_contains_expected_attributes(self):
        result = self.review.to_dict()
        self.assertIn("id", result)
        self.assertIn("created_at", result)
        self.assertIn("updated_at", result)
        self.assertIn("__class__", result)

    def test_to_dict_attribute_values_are_correct(self):
        self.review.place_id = "place_id_123"
        self.review.user_id = "user_id_123"
        self.review.text = "This is a review."

        result = self.review.to_dict()
        self.assertEqual(result['place_id'], "place_id_123")
        self.assertEqual(result['user_id'], "user_id_123")
        self.assertEqual(result['text'], "This is a review.")


class TestReviewsave_method(unittest.TestCase):
    """Unittests for testing save() for the class Review
    """

    def test_review_updates_updated_at_attribute(self):
        review = Review()
        initial_updated_at = review.updated_at
        time.sleep(1)
        review.save()
        new_updated_at = review.updated_at
        self.assertGreater(new_updated_at, initial_updated_at)


class TestReviewAttributes(unittest.TestCase):
    """Checks if review public attributes are set to None
    """

    def test_attributes_are_none(self):
        review = Review()
        if review.place_id is None:
            self.assertIsNone(review.place_id)
        else:
            self.assertIsNotNone(review.place_id)
        if review.user_id is None:
            self.assertIsNone(review.user_id)
        else:
            self.assertIsNotNone(review.user_id)
        if review.text is None:
            self.assertIsNone(review.text)
        else:
            self.assertIsNotNone(review.text)


class TestReview_to_dict_method(unittest.TestCase):
    """Unittests for testing to_dict() for the class Review
    """

    def setUp(self):
        self.review = Review()
        self.review.place_id = "456789"
        self.review.user_id = "fce12f8a"
        self.review.text = "proper"

    def test_to_dict_returns_dictionary(self):
        result = self.review.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_contains_expected_attributes(self):
        result = self.review.to_dict()

        self.assertIn('id', result)
        self.assertIn('created_at', result)
        self.assertIn('updated_at', result)
        self.assertIn('place_id', result)
        self.assertIn('user_id', result)
        self.assertIn('text', result)

    def test_to_dict_attribute_values_are_correct(self):
        result = self.review.to_dict()
        self.assertEqual(result['place_id'], "456789")
        self.assertEqual(result['user_id'], "fce12f8a")
        self.assertEqual(result['text'], "proper")

    def test_serialization_and_deserialization(self):
        self.review.place_id = "place_id_123"
        self.review.user_id = "user_id_123"
        self.review.text = "This is a review."
        serialized_review = json.dumps(self.review.to_dict())
        deserialized_review_dict = json.loads(serialized_review)
        deserialized_review = Review(**deserialized_review_dict)
        self.assertEqual(deserialized_review.place_id, self.review.place_id)
        self.assertEqual(deserialized_review.user_id, self.review.user_id)
        self.assertEqual(deserialized_review.text, self.review.text)


if __name__ == '__main__':
    unittest.main()
