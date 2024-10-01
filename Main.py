import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium import webdriver
#import pyautogui as pg
#import pandas as pd


# Exception Handling Decorator
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    return wrapper

# Gmail Login Function
@exception_handler
def login_gmail(driver, email, password, recovery_email):

    # Enter Gmail Address
    email_field = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.ID, 'identifierId')))
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))).click()
    time.sleep(2)
    curent_url = driver.current_url
    if curent_url == "https://accounts.google.com/v3/signin/challenge/recaptcha?TL=APps6eYxS8zkBYXN0tu0JWCUApKHGuZ0bQr2aE_07TLtASHIpewjkcMuKtBEZgTi&checkConnection=youtube%3A667&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ddm=0&dsh=S-1793898101%3A1727124834497741&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ifkv=ARpgrqcvTP1sRsMZB8PccFFsDGQBsgMK9TPmvoSeWlwLMgorMf_2VjQ_CMRjlPtJjg3niJnvPnbFWA&osid=1&pstMsg=1&service=cloudconsole":
        return False

    # Enter Password
    password_field = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]')))
    password_field.send_keys(password)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))).click()
    time.sleep(2)
    try:
        time.sleep(10)#//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]/div/div/button
        passkey = driver.find_element(By.XPATH,'//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 BqKGqe eR0mzb TrZEUc lw1w4b"]')
        passkey.click()
        print("Pass key")
        time.sleep(10)
        curent_url=driver.current_url
        if curent_url=="https://myaccount.google.com/?utm_source=sign_in_no_continue" or curent_url=="https://mail.google.com/mail/u/0/#inbox" or curent_url=="https://myaccount.google.com/restrictions/47?continue=https://console.cloud.google.com/project&pli=1" or curent_url=="https://console.cloud.google.com/project" or curent_url == "https://console.cloud.google.com/cloud-resource-manager" or curent_url=="":
            return True 
        elif curent_url=="https://accounts.google.com/v3/signin/challenge/iap?TL=APps6eZZxbCvSYgRtwWkRW-cBMbnBOMvObBc8YUCpx64ey7wH8-vQ9SO8uIJYw5J&checkConnection=youtube%3A322&checkedDomains=youtube&cid=3&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&ddm=0&dsh=S302801545%3A1726825085729893&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=ARpgrqcIPkIt0UEIt_EUdmijP6YKuMdVZ8dwBVg2K2L7v8anRTfJE9nKcyd2rVeQvfUn76miPCnwsA&pstMsg=1&service=accountsettings" or curent_url=="https://accounts.google.com/v3/signin/challenge/ipp/collect?TL=APps6ebg0bQBxGrBy8VUyjjO89ns9P0yEmet9ynRknvhMwPAQLXCwxgHX0RXy0Qy&checkConnection=youtube%3A406&checkedDomains=youtube&cid=3&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&ddm=0&dsh=S302801545%3A1726825085729893&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=ARpgrqcIPkIt0UEIt_EUdmijP6YKuMdVZ8dwBVg2K2L7v8anRTfJE9nKcyd2rVeQvfUn76miPCnwsA&pstMsg=1&service=accountsettings" or curent_url=="https://accounts.google.com/v3/signin/rejected?TL=APps6eaPW7ap7qD3nwPteiFSxtYLszscPxNnXtPbZN7xuu2g47K5AMhlrWMcmYbP&checkConnection=youtube%3A472&checkedDomains=youtube&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&ddm=0&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=ARpgrqfO_YqAk_u3HJMKbU160jin6c-nojrtZeB01JdOeAbiaR30-HbVYwcrvl5dwGuJRvzRHoZCyw&pstMsg=1&rhlk=su&rrk=69" or curent_url == "https://accounts.google.com/v3/signin/challenge/ipp/collect?TL=APps6eaIZw9e9AowPVk6uL5GCJ2KIVjrKYRqa4b3XIzM7MP0MqQ9Pr6N4J49Gva8&checkConnection=youtube%3A722&checkedDomains=youtube&cid=4&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ddm=0&dsh=S-637466219%3A1727125009542780&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ifkv=ARpgrqch5LZA46wxDZh6LDJwGry6LuudaMc6s3JNySqOc5wpvVYClFYnx3K-1HaNZEvsZvhK_52m7w&osid=1&pstMsg=1&service=cloudconsole":
            return False
    except NoSuchElementException:
        time.sleep(10)
        
        curent_url = driver.current_url
        if curent_url=="https://myaccount.google.com/?utm_source=sign_in_no_continue" or curent_url=="https://mail.google.com/mail/u/0/#inbox" or curent_url=="https://myaccount.google.com/restrictions/47?continue=https://console.cloud.google.com/project&pli=1" or curent_url=="https://console.cloud.google.com/project" or curent_url == "https://console.cloud.google.com/cloud-resource-manager":
            return True
        elif curent_url=="https://accounts.google.com/v3/signin/challenge/iap?TL=APps6eZZxbCvSYgRtwWkRW-cBMbnBOMvObBc8YUCpx64ey7wH8-vQ9SO8uIJYw5J&checkConnection=youtube%3A322&checkedDomains=youtube&cid=3&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&ddm=0&dsh=S302801545%3A1726825085729893&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=ARpgrqcIPkIt0UEIt_EUdmijP6YKuMdVZ8dwBVg2K2L7v8anRTfJE9nKcyd2rVeQvfUn76miPCnwsA&pstMsg=1&service=accountsettings" or curent_url=="https://accounts.google.com/v3/signin/challenge/ipp/collect?TL=APps6ebg0bQBxGrBy8VUyjjO89ns9P0yEmet9ynRknvhMwPAQLXCwxgHX0RXy0Qy&checkConnection=youtube%3A406&checkedDomains=youtube&cid=3&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&ddm=0&dsh=S302801545%3A1726825085729893&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=ARpgrqcIPkIt0UEIt_EUdmijP6YKuMdVZ8dwBVg2K2L7v8anRTfJE9nKcyd2rVeQvfUn76miPCnwsA&pstMsg=1&service=accountsettings" or curent_url=="https://accounts.google.com/v3/signin/rejected?TL=APps6eaPW7ap7qD3nwPteiFSxtYLszscPxNnXtPbZN7xuu2g47K5AMhlrWMcmYbP&checkConnection=youtube%3A472&checkedDomains=youtube&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&ddm=0&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=ARpgrqfO_YqAk_u3HJMKbU160jin6c-nojrtZeB01JdOeAbiaR30-HbVYwcrvl5dwGuJRvzRHoZCyw&pstMsg=1&rhlk=su&rrk=69" or curent_url == "https://accounts.google.com/v3/signin/challenge/ipp/collect?TL=APps6eaIZw9e9AowPVk6uL5GCJ2KIVjrKYRqa4b3XIzM7MP0MqQ9Pr6N4J49Gva8&checkConnection=youtube%3A722&checkedDomains=youtube&cid=4&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ddm=0&dsh=S-637466219%3A1727125009542780&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ifkv=ARpgrqch5LZA46wxDZh6LDJwGry6LuudaMc6s3JNySqOc5wpvVYClFYnx3K-1HaNZEvsZvhK_52m7w&osid=1&pstMsg=1&service=cloudconsole":
            return False
        elif "https://gds.google.com/web/recoveryoptions" in curent_url:
                    time.sleep(100)
                    save_button = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div/div/div/div[4]/div[2]/button')))
                    save_button.click()
                    time.sleep(100)
                    return True
        else:
        #Check for Recovery Email Option
            try:
                time.sleep(10)
                option_recovery = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/section/div/div/div/ul/li[3]/div/div[2]')
                option_recovery.click()
                time.sleep(2)
                # Check for Recovery Email Verification
                recovery_prompt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')))
                recovery_prompt.send_keys(recovery_email)
                recovery_prompt.send_keys(Keys.RETURN)
                print("Recovery email verification successful.")
                try:
                    time.sleep(10)
                    curent_url = driver.current_url
                    if curent_url=="https://myaccount.google.com/?utm_source=sign_in_no_continue" or curent_url=="https://mail.google.com/mail/u/0/#inbox" or curent_url=="https://myaccount.google.com/restrictions/47?continue=https://console.cloud.google.com/project" or curent_url=="https://console.cloud.google.com/project" or curent_url == "https://console.cloud.google.com/cloud-resource-manager":
                        return True
                    elif curent_url == "https://accounts.google.com/v3/signin/challenge/recaptcha?TL=APps6ebGhWVx2JRrhAmCsfCq7cZLfsSUoEEXVHLGwKcn2Of7pR7lrChovqAQHqeg&checkConnection=youtube%3A596&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ddm=0&dsh=S-2045556081%3A1727124629604060&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ifkv=ARpgrqd3OnAYnx4s6wPInNn4GA584DffdLAJoSkhlbJUs08aDU_6_mAWYL2BLhaEHrnZ7vsXhN2nyA&osid=1&pstMsg=1&service=cloudconsole":
                        print("Confirmation You are not a Robot")
                        return False
                    elif "https://gds.google.com/web/recoveryoptions" in curent_url:
                        time.sleep(10)
                        save_button = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH,'//butto[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 k97fxb xF8ewc"]')))
                        save_button.click()
                        time.sleep(10)
                        not_now_button = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH,'//butto[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 k97fxb yu6jOd"]')))
                        not_now_button.click()
                        return True
                        
                    else:
                        time.sleep(10)
                        passkey = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 BqKGqe eR0mzb TrZEUc lw1w4b"]')))
                        passkey.click()
                        time.sleep(50)
                        curent_url = driver.current_url
                        if curent_url=="https://myaccount.google.com/?utm_source=sign_in_no_continue" or curent_url=="https://mail.google.com/mail/u/0/#inbox" or curent_url=="https://myaccount.google.com/restrictions/47?continue=https://console.cloud.google.com/project" or curent_url=="https://console.cloud.google.com/project" or curent_url == "https://console.cloud.google.com/cloud-resource-manager":
                            return True
                        elif curent_url == "https://accounts.google.com/v3/signin/challenge/recaptcha?TL=APps6ebGhWVx2JRrhAmCsfCq7cZLfsSUoEEXVHLGwKcn2Of7pR7lrChovqAQHqeg&checkConnection=youtube%3A596&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ddm=0&dsh=S-2045556081%3A1727124629604060&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fconsole.cloud.google.com%2Fproject&ifkv=ARpgrqd3OnAYnx4s6wPInNn4GA584DffdLAJoSkhlbJUs08aDU_6_mAWYL2BLhaEHrnZ7vsXhN2nyA&osid=1&pstMsg=1&service=cloudconsole":
                            print("Confirmation You are not a Robot")
                            return False
                        elif "https://gds.google.com/web/recoveryoptions" in curent_url:
                            time.sleep(100)
                            save_button = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div/div/div/div[4]/div[2]/button')))
                            save_button.click()
                            time.sleep(100)
                            return True
                    
                    
                except NoSuchElementException:
                    time.sleep(20)
                    curent_url = driver.current_url
                    if curent_url=="https://myaccount.google.com/?utm_source=sign_in_no_continue" or curent_url=="https://mail.google.com/mail/u/0/#inbox" or curent_url=="https://myaccount.google.com/restrictions/47?continue=https://console.cloud.google.com/project" or curent_url=="https://console.cloud.google.com/project" or curent_url == "https://console.cloud.google.com/cloud-resource-manager":
                        return True
                    else:
                        return False
            except NoSuchElementException:
                    return False
            
@exception_handler
def create_api(driver,email,api_type,password,recovery_email,used):
    # Logging into google
    driver.get("https://console.developers.google.com/project")
    driver.maximize_window()
    if(login_gmail(driver,email,password,recovery_email)):
    # Navigate to Google API Console
        print("I'm creation api")
        time.sleep(10)
        if used==0:
            agree_checkbox = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mat-mdc-checkbox-1-input"]')))
            agree_checkbox.click()
            time.sleep(10)
            agree_button = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mat-mdc-dialog-0"]/div/div/xap-deferred-loader-outlet/ng-component/mat-dialog-actions/cfc-progress-button/div[1]/button')))
            agree_button.click()
            time.sleep(10)
        
        create_project_button = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-project-button"]')))
        create_project_button.click()
        print("Step 1")
        time.sleep(10)
    
        # project_name_input = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="p6ntest-name-input"]')))
        # project_name_input.send_keys("My App")
        # print("Step 2")
        # time.sleep(5)
    
        create_button = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="p6ntest-project-create-page"]/cfc-panel-body/cfc-virtual-viewport/div[1]/div/proj-creation-form/form/button[1]'))) 
        create_button.click()
        print("Step 3")
        time.sleep(10)
    
        notification_select_button = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cfc-notification-item-0"]/div[2]/button')))
        notification_select_button.click()
        print("Step 4")
        time.sleep(10)
        
        navigation_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pcc-console-nav-container"]/pcc-platform-bar-console-nav-button/pcc-platform-bar-button/button')))
        navigation_button.click()
        print("One step")
        #time.sleep(10)
        
        api_service = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cdk-drop-list-0"]/div[1]/cfc-console-nav-flyout/a')))
        api_service.click()
        print("Two Step")
        time.sleep(10)
        
        library_link = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cfctest-section-nav-item-marketplace_api_library"]')))
        library_link.click()
        print("Three Step")
        time.sleep(10)
        
        search_input = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//input[@name="searchInput"]')))
        search_input.send_keys("Gmail Api")
        search_input.send_keys(Keys.RETURN)
        print("Four Step")
        time.sleep(10)
        
        gmail_api = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//a[contains(@href, "/apis/library/gmail.googleapis.com?")]')))
        gmail_api.click()
        print("Fifth Step")
        time.sleep(10)
                                                                                                                                          
        enable_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//button[@class = "mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base gmat-mdc-button cm-button cfc-tooltip cfc-tooltip-disable-user-select-on-touch-device ng-star-inserted"]')))
        enable_button.click()
        print("Sixth Step")
        time.sleep(10)

        #api_service = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cdk-drop-list-0"]/div[1]/cfc-console-nav-flyout/a')))
        #api_service.click()
        #print("Step 5")
        #time.sleep(10)

        credentials_button = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cfctest-section-nav-item-metropolis_api_credentials"]')))
        credentials_button.click()
        print("Step 6")
        time.sleep(10)

        create_credentials_button = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_3rif_action-bar-create-button"]')))
        create_credentials_button.click()
        print("Step 7")
        time.sleep(10)

        api_key_create_link = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//cfc-menu-item[contains(@label,"API key")]')))
        api_key_create_link.click()
        print("Step 8")
        time.sleep(10)

        api_key_created_close_button = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//button[@matdialogclose]')))
        api_key_created_close_button.click()
        print("Step 9")
        time.sleep(10)

        create_credentials_button = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_3rif_action-bar-create-button"]')))
        create_credentials_button.click()
        print("Step 10")
        time.sleep(10)

        client_id_credentials_link = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//cfc-menu-item[contains(@label,"OAuth client ID")]')))
        client_id_credentials_link.click()
        print("Step 11")
        time.sleep(10)

        configure_consent_screen = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//a[@class="mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base gmat-mdc-button cm-button"]')))
        configure_consent_screen.click()
        print("Step 12")
        time.sleep(10)

        external_radio_button = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//input[@value="external"]')))
        external_radio_button.click()
        print("Step 13")
        time.sleep(30)

        print("Push the Create button manually")
        create_external_radio_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base gmat-mdc-button cm-button" or @mat-raised-button]')))
        #loc = create_external_radio_button.location
        #pg.moveTo(loc['x'],loc['y'])
        #time.sleep(10)
        #pg.click(loc['x'],loc['y'],duration=2)
        create_external_radio_button.click()
        print("Step 14")
        time.sleep(10)
        
        curent_url = driver.current_url
        
        if "https://console.cloud.google.com/freetrial/signup" in curent_url:
           driver.back()
           external_radio_button = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//input[@value="external"]')))
           external_radio_button.click()
           print("Step 13")
           time.sleep(10)

           print("Press Create button manually")
           #create_external_radio_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base gmat-mdc-button cm-button" or @mat-raised-button]')))
           #create_external_radio_button.click()
           #print("Step 14")
           time.sleep(20)

        consent_screen_app_name = WebDriverWait(driver,200).until(EC.presence_of_element_located((By.XPATH,'//input[@matinput and @required="" and @class="cm-input mat-mdc-input-element gmat-mdc-input mat-mdc-form-field-input-control mdc-text-field__input cdk-text-field-autofill-monitored ng-touched"]')))
        consent_screen_app_name.send_keys("My App")
        print("Step 15")
        time.sleep(10)
        

        consent_screen_email_user_support = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//mat-option[@role="option" and @class="mat-mdc-option mdc-list-item ng-star-inserted"]')))
        consent_screen_email_user_support.click()
        print("Step 16")
        time.sleep(10)

        consent_screen_developer_contact_email = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@aria-label="Text field for emails"]')))
        consent_screen_developer_contact_email.send_keys(email)
        print("Step 17")
        time.sleep(10)

        save_and_continue_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_13rif_cfc-stepper-step-content-and-continue-0"]/div[2]/button[1]')))
        save_and_continue_button.click()
        print("Step 18")
        time.sleep(10)

        save_and_continue_button2 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_13rif_cfc-stepper-step-content-and-continue-1"]/div[2]/button[1]')))
        save_and_continue_button2.click()
        print("Step 19")
        time.sleep(10)

        save_and_continue_button3 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_13rif_cfc-stepper-step-content-and-continue-3"]/div[2]/button[1]')))
        save_and_continue_button3.click()
        print("Step 20")
        time.sleep(10)

        credentials_button_again = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cfctest-section-nav-item-metropolis_api_credentials"]')))
        credentials_button_again.click()
        print("Step 21")
        time.sleep(10)

        create_credentials_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_3rif_action-bar-create-button"]')))
        create_credentials_button.click()
        print("Step 22")
        time.sleep(10)

        client_id_credentials_link = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_3rif_cdk-overlay-15"]/div/div/div/cfc-menu-section[1]/div/cfc-menu-item[2]/a')))
        client_id_credentials_link.click()
        print("Step 23")
        time.sleep(10)

        api_type_dropdown = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_13rif_cfc-select-1"]')))
        print("Step 24")
        time.sleep(10)

        dropdown_selection = Select(api_type_dropdown)
        dropdown_selection.select_by_visible_text(api_type)
        print("Step 25")
        time.sleep(10)

        create_api_type_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_13rif_panelgoog_1847418012"]/cfc-panel-body/cfc-virtual-viewport/div[1]/div/form/services-oauth-client-form/form/cfc-progress-button/div[1]/button')))
        create_api_type_button.click()
        print("Step 26")
        time.sleep(10)

        ok_button_after_credentials_created = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_16rif_mat-mdc-dialog-1"]/div/div/highlight-client-dialog-oauth-clients-gql/div[2]/button')))
        ok_button_after_credentials_created.click()
        print("Step 27")
        time.sleep( 10)

        download_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_16rif_cfc-labelledby-message-goog_1200291473"]')))
        download_button.click()
        print("Step 28")
        time.sleep(10)

        download_json_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="_16rif_oauth-secrets-download-dialog"]/div/div/button')))
        download_json_button.click()
        print("Step 29")
        time.sleep(10)
        print("API created successfully.")
    else:
        print("Login Failed")
# Main Script Logic
@exception_handler
def main():
    # Setup Chrome options to 
    # Disable the "enable-automation" flag.
    # Add the "no-sandbox" argument.
    # Add the "disable-infobars" argument.
    # Add the "disable-dev-shm-usage" argument.

    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # exclude the collection of enable-automation switches 
    #chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
    # turn-off userAutomationExtension 
    #chrome_options.add_experimental_option("use-automation-extension",False)
    #chrome_options.add_experimental_option('prefs', {"download.default_directory":r"D:\API-AUTOMATION-TOOL", "download.prompt_for_download": False, "download.directory_upgrade": True})

    # User credentials
    email = "jueidelfonso@gmail.com"
    password = "dd8lltsdcrc2be"
    recovery_email = "zbslifscarpootd@xtra.co.nz"
    api_type = "Web application"


    # Use the ChromeDriver version that matches the Chrome browser version
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    create_api(driver,email,api_type,password,recovery_email,1)

    # Close Browser
    driver.quit()
    print("Browser closed.")

if __name__ == "__main__":
    main()