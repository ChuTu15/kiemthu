def tinh_dien_tich_chu_nhat(chieu_rong, chieu_dai):
    if chieu_dai <= 0 or chieu_rong <= 0:
        return "Lỗi: Chiều dài và chiều rộng phải lớn hơn 0"
    return chieu_dai * chieu_rong
import unittest

class TestHinhChuNhat(unittest.TestCase):
    def test_dien_tich_hop_le(self):
        self.assertEqual(tinh_dien_tich_chu_nhat(4, 5), 20)

    def test_chieu_rong_am(self):
        self.assertEqual(tinh_dien_tich_chu_nhat(-3, 5), "Lỗi: Chiều dài và chiều rộng phải lớn hơn 0")

    def test_chieu_dai_am(self):
        self.assertEqual(tinh_dien_tich_chu_nhat(6, -8), "Lỗi: Chiều dài và chiều rộng phải lớn hơn 0")

    def test_chieu_dai_va_chieu_rong_bang_0(self):
        self.assertEqual(tinh_dien_tich_chu_nhat(0, 0), "Lỗi: Chiều dài và chiều rộng phải lớn hơn 0")
    
    def test_chieu_dai_va_chieu_rong_am(self):
        self.assertEqual(tinh_dien_tich_chu_nhat(-5, -2), "Lỗi: Chiều dài và chiều rộng phải lớn hơn 0")

    def test_chieu_dai_bang_0(self):
        self.assertEqual(tinh_dien_tich_chu_nhat(8, 0), "Lỗi: Chiều dài và chiều rộng phải lớn hơn 0")

    def test_chieu_rong_bang_0(self):
        self.assertEqual(tinh_dien_tich_chu_nhat(0, 7), "Lỗi: Chiều dài và chiều rộng phải lớn hơn 0")

if __name__ == '__main__':
    unittest.main()