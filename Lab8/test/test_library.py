# Panyawut Saengdaeng 653380138-3 Sec.1

import unittest
import os, sys

# ปรับเปลี่ยนพาธให้ถูกต้อง
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from source.library.main import app  # นำเข้าแอปพลิเคชัน FastAPI 
from fastapi.testclient import TestClient

client = TestClient(app)

class TestLibrary(unittest.TestCase):
    def setUp(self):
        """เตรียมข้อมูลสำหรับการทดสอบ"""
        # สามารถเตรียมข้อมูลที่ต้องใช้ได้ เช่น การสร้างผู้ใช้
        client.post("/users/", json={"username": "testuser", "fullname": "Test User"})

    def tearDown(self):
        """ทำความสะอาดหลังจากการทดสอบ"""
        print('\nEnd of test', self.shortDescription())

    def test_create_user(self):
        """ทดสอบการสร้างผู้ใช้ใหม่"""
        response = client.post("/users/", json={"username": "newuser", "fullname": "New User"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], "newuser")

    def test_create_book(self):
        """ทดสอบการเพิ่มหนังสือใหม่"""
        response = client.post("/books/", json={"title": "New Book", "firstauthor": "Author One", "isbn": "1234567890"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "New Book")

    def make_suite(self):
        """สร้าง Test Suite สำหรับการทดสอบ"""
        suite = unittest.TestSuite()
        suite.addTest(TestLibrary("test_create_user"))
        suite.addTest(TestLibrary("test_create_book"))
        return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = TestLibrary().make_suite()
    runner.run(test_suite)
