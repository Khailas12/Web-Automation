from using_oops import Secondary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Final(Secondary):
        def driver_wait(self):
            try:   # Explicit Wait is code you define to wait for a certain condition to occur before proceeding further in the code
                WebDriverWait(self, 5).until(
                    EC.text_to_be_present_in_element(
                        (By.CLASS_NAME, "progress-label"),   # Element filteration
                        'Complete!'     # The expected text
                    )
                )
                print("Four")
            except:
                AttributeError
                print("\nPassed the AttributeError Succesfully")

        def __exit__(self, exc_type, exc_val, exc_to):
            if self.teardown:
                self.quit()
                print("Exit")


if __name__ == "__main__":
    with Final() as fin:
        fin.first_page()
        fin.popup_skip()
        fin.message()
        fin.text_btn()
        fin.sum()
        fin.sum_button()
        fin.driver_wait()
        fin.quit()
        
        print("Done")