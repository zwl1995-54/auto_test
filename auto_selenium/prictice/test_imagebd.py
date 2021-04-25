from time import sleep

from auto_selenium.prictice.base import Base


class TestImge(Base):
    def test_image(self):
        self.driver.get("https://image.baidu.com/")
        sleep(10)
        # Base.setup()
        # self.driver.execute_script("document.querySelector('#sttb > img.st_camera_on')").click()
        # self.driver.find_element_by_class_nam("st_camera_on").click()
        self.driver.find_element_by_xpath("//*[@id='sttb'']/img[2]").click()
        self.driver.execute_script("document.querySelector('#uploadImg')").send_keys("C:\picture/fj1.jpg")
        sleep(10)
